import os
import sys
import subprocess
import pyperclip

def get_directory_structure(path, git_only=False):
    if git_only:
        git_files = subprocess.check_output(["git", "ls-files"], cwd=path).decode("utf-8").splitlines()
        git_files = [os.path.join(path, f) for f in git_files]

    tree = {}
    for root, dirs, files in os.walk(path):
        if git_only:
            dirs[:] = [d for d in dirs if os.path.join(root, d) in git_files]
            files = [f for f in files if os.path.join(root, f) in git_files]

        branch = tree
        for part in root.split(os.sep)[1:]:
            branch = branch.setdefault(part, {})
        for file in files:
            branch.setdefault(file, None)

    return tree

def tree_to_string(tree, level=0, indent="    "):
    result = ""
    items = sorted(tree.items())
    for i, (name, subtree) in enumerate(items):
        is_last = i == len(items) - 1
        prefix = "└── " if is_last else "├── "
        result += f"{indent * level}{prefix}{name}\n"
        if subtree is not None:
            connector = "" if is_last else "│"
            result += tree_to_string(subtree, level + 1, indent + connector + "   ")

    return result

def main():
    if len(sys.argv) < 2:
        print("Usage: python directory_copier.py [--git-only] [path]")
        sys.exit(1)

    git_only = "--git-only" in sys.argv
    path = [arg for arg in sys.argv[1:] if arg != "--git-only"]
    path = path[0] if path else "."

    tree = get_directory_structure(path, git_only)
    tree_string = tree_to_string(tree)
    pyperclip.copy(tree_string)
    print("Directory structure copied to clipboard.")

if __name__ == "__main__":
    main()
