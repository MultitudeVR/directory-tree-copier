# Directory Tree Copier

Directory Tree Copier is a Python tool that allows you to copy the directory structure of any given directory to your clipboard, either including all files, or only those tracked by Git. It also allows you to recreate directories and files from a copied tree structure.

## Example

Here is an example of Directory Tree Copier's output:

```
directory-tree-copier/
├── LICENSE
├── README.md
├── directory_copier.py
├── example-registries/
│   ├── directory-copier-git-only.reg
│   ├── directory-copier-paste.reg
│   └── directory-copier.reg
└── requirements.txt
```

# Purpose

Designed for developers who use ChatGPT, Directory Tree Copier serves two primary functions:

1. Enhances ChatGPT's understanding of your project by feeding it a complete directory structure, leading to better code generation and review.

2. Speeds up project setup by turning ChatGPT's "directory tree" output into actual directories and files.

In essence, this tool acts as a bridge between your development work and the AI model, ensuring that both the human and the machine understand each other's context and constraints, streamlining your workflow and saving you time.

## Installation

To install and run Directory Tree Copier, you need Python 3.10+ installed on your machine. You can then clone this repository and install the necessary dependencies.

```bash
git clone https://github.com/multitudevr/directory-tree-copier.git
cd directory-tree-copier
pip install -r requirements.txt
```

## Usage

The main file to run is `directory_copier.py`. It has the following usage:

```bash
python directory_copier.py [OPTIONS] [PATH]
```

The options are as follows:

- `--git-only`: Copy only git-tracked files.
- `--paste`: Creates the folders and files of a tree from your clipboard. Fails with an error if a valid tree isn't in your clipboard.
- `PATH`: The path of the directory to copy. Defaults to the current directory if not provided.

If no option is given, it copies the file structure of the current directory to your clipboard as a directory tree.

## Adding to Windows Context Menu

You can add the "Copy File Tree", "Copy File Tree (git)", and "Paste File Tree" commands to the Windows context menu with the provided .reg files. Here's how to do it:

1. Open the `directory-copier.reg` file in a text editor. 
2. Replace `C:\\Users\\yourname\\AppData\\Local\\Programs\\Python\\Python310\\python.exe` with the path to your Python executable. You can find this by running `where python` in your command prompt.
3. Replace `C:\\_git\\directory-tree-copier\\directory_copier.py` with the absolute path to your `directory_copier.py` file.
4. Save and close the file.
5. Double click on the .reg file to merge it into your Windows registry. Confirm any prompts you receive.

Repeat these steps with the `directory-copier-git-only.reg` file to add the "Copy File Tree (git)" command to your context menu, and `directory-copier-paste.reg` to add "Paste File Tree".

Please note that editing the Windows registry can have serious effects on your system. Always create a backup before making changes, and only proceed if you know what you're doing.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/yourusername/directory-tree-copier/blob/master/LICENSE) file for details.
