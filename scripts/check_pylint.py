import os
import pylint.lint

checks = [
    "C0301",  # Line too long
    "C0303",  # Trailing whitespace
    "E0602",  # Undefined variable
    "W0611",  # Unused import
    "R0913"   # Too many arguments in function
]

def run_pylint():
    # Get all Python files in the repository
    py_files = [f for f in os.listdir() if f.endswith(".py")]

    if not py_files:
        print("No Python files found in the root directory.")
        return

    # Run Pylint with the selected checks
    for file in py_files:
        print(f"\nChecking {file}...\n")
        pylint.lint.Run([file, "--disable=all", "--enable=" + ",".join(checks)])

if __name__ == "__main__":
    run_pylint()
