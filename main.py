import os
from dotenv import load_dotenv
from agents.analyzer import AnalyzerAgent
from agents.coder import CoderAgent
from utils.github_client import GitHubClient

# Memuat environment variables dari file .env
load_dotenv()

def main():
    print("=== Memulai MiMo Refactor Agent ===")
    
    # 1. Inisialisasi Agen & Tools
    analyzer = AnalyzerAgent()
    coder = CoderAgent()
    github = GitHubClient()
    
    # 2. Jalankan Proses Scanning
    issues = analyzer.scan_codebase("./target_repo")
    
    # 3. Proses perbaikan dengan MiMo dan kirim ke GitHub
    for issue in issues:
        fixed_code = coder.generate_refactor(issue)
        github.create_pull_request(issue['file'], fixed_code)
        
    print("=== Proses Otomatisasi Selesai ===")

if __name__ == "__main__":
    main()
