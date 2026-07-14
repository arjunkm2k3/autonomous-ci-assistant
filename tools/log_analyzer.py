import re
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from config import Config

class LogAnalyzer:
    def __init__(self):
        self.llm = Ollama(model=Config.OLLAMA_MODEL, temperature=0.1)
        self.prompt = PromptTemplate(
            input_variables=["log_content"],
            template="""
            You are a DevOps expert. Analyze the following CI/CD log and extract:
            ERROR: the main error message
            COMPONENT: which component or file failed
            ROOT_CAUSE: why it happened
            SUGGESTED_FIX: what to change
            CONFIDENCE: a number between 0 and 1.
            Log:
            {log_content}
            """
        )
        # Use LCEL to create the chain
        self.chain = self.prompt | self.llm

    def analyze(self, log_content):
        log_content = log_content[:8000]  # trim
        try:
            response = self.chain.invoke({"log_content": log_content})
            parsed = self._parse(response)
        except Exception:
            parsed = self._regex_fallback(log_content)
        return parsed

    def _parse(self, text):
        result = {}
        for line in text.split('\n'):
            if line.startswith('ERROR:'):
                result['error'] = line.replace('ERROR:', '').strip()
            elif line.startswith('COMPONENT:'):
                result['component'] = line.replace('COMPONENT:', '').strip()
            elif line.startswith('ROOT_CAUSE:'):
                result['root_cause'] = line.replace('ROOT_CAUSE:', '').strip()
            elif line.startswith('SUGGESTED_FIX:'):
                result['suggested_fix'] = line.replace('SUGGESTED_FIX:', '').strip()
            elif line.startswith('CONFIDENCE:'):
                result['confidence'] = line.replace('CONFIDENCE:', '').strip()
        result.setdefault('error', 'Unknown error')
        result.setdefault('component', 'Unknown')
        result.setdefault('root_cause', 'Unknown')
        result.setdefault('suggested_fix', 'Manual review required')
        result.setdefault('confidence', '0.5')
        return result

    def _regex_fallback(self, log):
        patterns = [
            r'(?i)error:?\s*(.+?)(?:\n|$)',
            r'(?i)failed:?\s*(.+?)(?:\n|$)',
            r'(?i)exception:?\s*(.+?)(?:\n|$)'
        ]
        for p in patterns:
            match = re.search(p, log)
            if match:
                return {
                    'error': match.group(1).strip(),
                    'component': 'Unknown (regex fallback)',
                    'root_cause': 'Could not determine from logs',
                    'suggested_fix': 'Manual investigation needed',
                    'confidence': '0.3'
                }
        return {
            'error': 'No error pattern found',
            'component': 'Unknown',
            'root_cause': 'Unknown',
            'suggested_fix': 'Review logs manually',
            'confidence': '0.1'
        }