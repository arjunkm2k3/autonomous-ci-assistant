import uuid
from github import Github
from config import Config

class GitOperator:
    def __init__(self):
        self.g = Github(Config.GITHUB_TOKEN)
        self.repo = self.g.get_repo(Config.REPO_NAME)
        self.base_branch = Config.GITHUB_BASE_BRANCH
    
    def apply_fix(self, error, suggested_fix, file_to_fix=None):
        # 1. Create a new branch
        branch = f"fix/ai-{uuid.uuid4().hex[:8]}"
        base_sha = self.repo.get_branch(self.base_branch).commit.sha
        self.repo.create_git_ref(ref=f"refs/heads/{branch}", sha=base_sha)
        
        # 2. Apply fix to a file (or create a summary)
        if file_to_fix:
            try:
                contents = self.repo.get_contents(file_to_fix, ref=branch)
                updated = contents.decoded_content.decode() + f"\n# AI FIX: {suggested_fix}"
                self.repo.update_file(file_to_fix, "AI fix", updated, contents.sha, branch=branch)
            except:
                # file doesn't exist, create it
                self.repo.create_file(file_to_fix, "AI fix", f"# AI FIX: {suggested_fix}", branch=branch)
        else:
            summary = f"# AI Fix Summary\n\n**Error:** {error}\n\n**Suggested Fix:** {suggested_fix}"
            self.repo.create_file("AI_FIX_SUMMARY.md", "AI fix summary", summary, branch=branch)
        
        # 3. Open a Pull Request
        pr = self.repo.create_pull(
            title=f" AI Fix: {error[:50]}...",
            body=f"## AI Generated Fix\n\n**Error:** {error}\n\n**Fix:** {suggested_fix}",
            head=branch,
            base=self.base_branch
        )
        return {"pr_url": pr.html_url, "pr_number": pr.number}