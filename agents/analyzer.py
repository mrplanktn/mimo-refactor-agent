import os

class AnalyzerAgent:
    def __init__(self):
        pass

    def scan_codebase(self, repo_path):
        print(f"[Analyzer] Memindai repositori di: {repo_path}...")
        # Simulasi membaca file dan mendeteksi technical debt
        sample_issue = {
            "file": "legacy_code.py",
            "line": 12,
            "issue": "Menggunakan library usang dan loop tidak efisien",
            "context": "def fetch_data():\n    for i in range(len(data)):\n        print(data[i])"
        }
        return [sample_issue]
