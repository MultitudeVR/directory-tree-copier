# Directory Tree Copier

Directory Tree Copier is a Python tool that allows you to copy the directory structure of any given directory to your clipboard, either including all files, or only those tracked by Git.

## Structure

The project has the following structure:

```
directory-tree-copier/
├── LICENSE
├── README.md
├── directory_copier.py
├── example-registries/
│   ├── directory-copier-create.reg
│   ├── directory-copier-git-only.reg
│   └── directory-copier.reg
└── requirements.txt
```
The above is an example of Directory Tree Copier's output.

# Purpose

The Directory Tree Copier is designed to serve a dual-purpose, making it a robust and versatile tool for developers.

Firstly, it empowers developers to provide ChatGPT with comprehensive context regarding a project they are currently working on. By showing the AI model the entire directory structure of the project, it helps the AI understand the context better, making its suggestions and recommendations more accurate and relevant. This can be particularly useful when you're using ChatGPT for code generation or review, as it can produce responses with an understanding of your project's structure.

Secondly, Directory Tree Copier is also built to facilitate rapid creation of directories and files that ChatGPT produces when asked to provide a "directory tree" of a project it designs or edits. This means that if you're using ChatGPT to design software projects, the Directory Tree Copier can take ChatGPT's output and quickly set up the files and directories, saving you valuable time and effort.

In essence, this tool acts as a bridge between your development work and the AI model, ensuring that both the human and the machine understand each other's context and constraints, leading to a more efficient and effective development process. 

Whether you're working on a new project from scratch, restructuring an existing one, or collaborating on a large codebase, the Directory Tree Copier can help make your work easier and more streamlined.

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
