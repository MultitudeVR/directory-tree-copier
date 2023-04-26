import os
import sys
import subprocess
import pyperclip
import argparse

def get_directory_structure(path, git_only=False):
    tree = {}
    for root, dirs, files in os.walk(path):
        if git_only:
            git_files = subprocess.check_output(["git", "ls-files", "--recurse-submodules"], cwd=root).decode("utf-8").splitlines()
            git_files = [os.path.join(root, f) for f in git_files]
            git_dirs = set(os.path.dirname(gf) for gf in git_files)
            dirs[:] = [d for d in dirs if any(os.path.join(root, d) in gd for gd in git_dirs)]
            files = [f for f in files if os.path.join(root, f) in git_files]

        branch = tree
        for part in root.split(os.sep)[1:]:
            branch = branch.setdefault(part, {})
        for file in files:
            branch.setdefault(file, None)

    return tree

def tree_to_string(tree, level=0, indent="    ", connector=""):
    result = ""
    items = sorted(tree.items())
    for i, (name, subtree) in enumerate(items):
        is_last = i == len(items) - 1
        prefix = "└── " if is_last else "├── "
        result += f"{connector}{prefix}{name}\n"
        if subtree is not None:
            next_connector = connector + ("    " if is_last else "│   ")
            result += tree_to_string(subtree, level + 1, indent, next_connector)

    return result

def main():
    parser = argparse.ArgumentParser(description='Copy a directory, including only git-related files.')
    parser.add_argument('path', metavar='path', type=str, default='.', nargs='?', help='path to directory to copy')
    parser.add_argument('--git-only', action='store_true', help='copy only git-related files')
    args = parser.parse_args()

    git_only = args.git_only
    path = args.path.replace("\\", "/")
    tree = get_directory_structure(path, git_only)
    tree_string = tree_to_string(tree)
    pyperclip.copy(tree_string)
    print("Directory structure copied to clipboard.")

if __name__ == "__main__":
    main()
