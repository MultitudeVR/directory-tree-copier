import os
import sys
import subprocess
import pyperclip
import click

@click.command()
@click.argument('path', type=click.Path(exists=True), default='.')
@click.option('--git-only', is_flag=True, help='copy only git-related files')
@click.option('--create', is_flag=True, help='read the directory structure from the clipboard and create it')
def copy_git_structure(path, git_only, create):
    if create: # create a directory into 'path' from tree string in clipboard
        path = path.replace("\\", "/")
        tree_string = pyperclip.paste().replace("\r", "")
        if "└" not in tree_string:
            click.echo("Invalid directory structure in clipboard.")
        else:
            try:
                create_directory_structure(tree_string)
                click.echo("Directory structure created from clipboard.")
            except ValueError:
                click.echo("Invalid directory structure in clipboard.")
    else: # copy tree string to clipboard based on 'path's structure
        """Copy a directory, including only git-related files."""
        path = path.replace("\\", "/")
        tree = get_directory_structure(path, git_only)
        tree_string = os.path.basename(os.path.abspath(path)) + '/\n' + tree_to_string(tree) # Add the current directory name
        pyperclip.copy(tree_string)
        click.echo("Directory structure copied to clipboard.")

def create_directory_structure(directory_tree: str):
    lines = directory_tree.split("\n")
    stack = []

    for line in lines:
        stripped_line = line.lstrip(" │├─└")
        if not stripped_line:
            continue

        # Calculate current level of indentation (i.e., depth in the directory tree)
        indent_level = (len(line) - len(stripped_line)) // 2

        # If stack is deeper than current indent level, we need to go up in the tree
        while len(stack) > indent_level:
            stack.pop()

        # If indent levels match, we're creating a sibling, so pop the last directory/file
        if len(stack) == indent_level and stack:
            stack.pop()

        path = os.path.join(*stack, stripped_line.rstrip("/"))

        # Directories end with "/", if it doesn't exist, create it and add to stack
        if stripped_line.endswith("/"):
            if not os.path.exists(path):
                os.makedirs(path)
            stack.append(stripped_line.rstrip("/"))
        else:
            # If not a directory (i.e., a file), create the file
            with open(path, "w") as file:
                pass

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
        name_with_slash = name + ('/' if subtree is not None else '') # Add a forward slash to directory names
        result += f"{connector}{prefix}{name_with_slash}\n"
        if subtree is not None:
            next_connector = connector + ("    " if is_last else "│   ")
            result += tree_to_string(subtree, level + 1, indent, next_connector)

    return result

if __name__ == "__main__":
    copy_git_structure()
