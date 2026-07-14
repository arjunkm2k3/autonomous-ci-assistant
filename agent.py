from tools.log_analyzer import LogAnalyzer
from tools.git_operator import GitOperator
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from config import Config

class CICDAssistant:
    def __init__(self, auto_fix=True):
        self.auto_fix = auto_fix
        self.log_analyzer = LogAnalyzer()
        self.git_operator = GitOperator()

        # Embeddings for RAG (HuggingFace – free, local)
        self.embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2",
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': True}
        )

        # Vector store for RAG
        self.vectordb = Chroma(
            persist_directory=Config.CHROMA_PERSIST_DIR,
            embedding_function=self.embeddings
        )

        # LLM for reasoning (Ollama – free, local)
        self.llm = Ollama(model=Config.OLLAMA_MODEL, temperature=Config.TEMPERATURE)

        # Chain for generating fixes (LCEL)
        self.prompt = PromptTemplate(
            input_variables=["error", "context"],
            template="""
            You are a senior DevOps engineer.
            Error: {error}
            Similar past failures (context): {context}
            Provide a clear, step‑by‑step fix plan.
            Fix plan:
            """
        )
        self.fix_chain = self.prompt | self.llm

    def process_failure(self, log_content):
        # 1. Analyse logs
        analysis = self.log_analyzer.analyze(log_content)
        error = analysis.get('error', 'Unknown error')

        # 2. Retrieve similar past failures from RAG
        docs = self.vectordb.similarity_search(error, k=2)
        context = "\n".join([d.page_content for d in docs])

        # 3. Generate a fix plan using the LLM
        fix = self.fix_chain.invoke({"error": error, "context": context})

        # 4. Apply the fix if auto_fix is enabled
        pr_result = None
        if self.auto_fix:
            # Simple heuristic: if error mentions Python, fix requirements.txt
            file_to_fix = "requirements.txt" if "python" in error.lower() else None
            pr_result = self.git_operator.apply_fix(error, fix, file_to_fix)

        return {
            "analysis": analysis,
            "fix": fix,
            "pr": pr_result
        }