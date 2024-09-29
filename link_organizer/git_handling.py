import os
from git import Repo

def initialize_git_repo(repo_dir):
    """Initializes or opens an existing Git repository."""
    if not os.path.exists(repo_dir):
        os.makedirs(repo_dir)
        return Repo.init(repo_dir)
    return Repo(repo_dir)

def commit_changes(repo, message="Appended new links and updated the repository"):
    """Commits all changes to the Git repository."""
    repo.git.add(A=True)  # Stage all changes
    repo.index.commit(message)  # Commit with a message
    print(f"Changes committed with message: {message}")
