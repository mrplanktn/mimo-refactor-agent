class GitHubClient:
    def __init__(self):
        print("[GitHub Client] Menginisialisasi koneksi dengan GitHub API...")

    def create_pull_request(self, file_name, new_code):
        print(f"[GitHub Client] Sukses membuat Pull Request otomatis untuk file: {file_name}")
        return "https://github.com/user/repo/pull/1"
