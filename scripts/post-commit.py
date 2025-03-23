import os
import pylint.lint

repo_path = os.path.dirname(os.path.abspath(__file__))
checks = ["C0301", "C0302", "C0303", "E0602", "W0611"]

files = [f for f in os.listdir(repo_path) if f.endswith(".py")]

for file in files:
    print(f"Running pylint on {file}...")
    pylint.lint.Run([file, f"--disable=all", f"--enable={','.join(checks)}"])
