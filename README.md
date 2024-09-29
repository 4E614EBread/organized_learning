# Link Organizer

![PyPI version](https://img.shields.io/pypi/v/link-organizer?color=blue)
![Python versions](https://img.shields.io/pypi/pyversions/link-organizer)
![License](https://img.shields.io/github/license/yourusername/link-organizer)

Link Organizer is a Python command-line tool that organizes links into markdown files and Git repositories based on topics. It supports links from text, CSV, and Excel files, and can classify links automatically if no topic or description is provided.

## Features

- Organizes links into a Git repository based on their topic.
- Supports text files, CSV files, and Excel files.
- Automatic link preview fetching using `httpx` to retrieve titles and descriptions.
- Automatically classifies topics using NLP (`spaCy`).
- Easy command-line usage with options for file or manual input.
- Automatically updates `README.md` with topic-based navigation links.

## Installation

### Prerequisites

- Python 3.6 or higher
- Git

### Install the Package

You can install Link Organizer from PyPI:

```bash
pip install link-organizer
```

Or, if you're developing locally, clone the repository and install it using:

```bash
git clone https://github.com/yourusername/link-organizer.git
cd link-organizer
pip install .
```

### Required Dependencies

Make sure to install the necessary dependencies, which will be installed automatically when you install the package:

- `httpx` (for asynchronous HTTP requests)
- `beautifulsoup4` (for parsing HTML)
- `spaCy` (for topic classification)
- `pandas` (for processing CSV and Excel files)
- `gitpython` (for managing Git repositories)

## Usage

Once installed, you can use the `link-organizer` command-line tool to organize links into markdown files and Git repositories.

### Example Usage

#### 1. Organizing Links from a CSV File:

```bash
link-organizer --file /path/to/file.csv --repo /path/to/git/repo
```

This will parse the CSV file and organize the links into markdown files within the specified Git repository. Each link will be classified into a topic-based folder.

#### 2. Organizing Links from a Directory of Files:

```bash
link-organizer --directory /path/to/directory --repo /path/to/git/repo
```

This will process all the files in the specified directory (supporting `.txt`, `.csv`, `.xls`, and `.xlsx` files) and organize the links accordingly.

#### 3. Adding a Single Link Manually:

```bash
link-organizer --link https://example.com --repo /path/to/git/repo
```

If you don't provide a topic or description, the tool will automatically fetch the title and classify the link.

#### Additional Options:

- `--topic`: Manually specify the topic for a link.
- `--description`: Manually specify a description for the link.
- `--delimiter`: Specify a custom delimiter for CSV or text files (default is `,`).

## Folder Structure

After running the command, the project will create a folder structure like this inside your Git repository:

```
/path/to/git/repo/
├── A/
│   └── Ansible/
│       └── ansible.md
├── M/
│   └── MachineLearning/
│       └── machinelearning.md
├── README.md
```

### `README.md`

The tool automatically updates the root `README.md` with links to the markdown files categorized by topic:

```markdown
# Topic Index

## A
- [ansible](A/Ansible/ansible.md)

## M
- [machinelearning](M/MachineLearning/machinelearning.md)
```

## Development

If you want to contribute or develop the project further, follow these steps:

### Clone the Repository

```bash
git clone https://github.com/yourusername/link-organizer.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Tests

Ensure that your changes work correctly by running the tests:

```bash
python -m unittest discover
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

We welcome contributions! If you’d like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

1. Fork the repo.
2. Create your feature branch: `git checkout -b my-new-feature`.
3. Commit your changes: `git commit -am 'Add some feature'`.
4. Push to the branch: `git push origin my-new-feature`.
5. Submit a pull request.

## Acknowledgements

- [spaCy](https://spacy.io/)
- [httpx](https://www.python-httpx.org/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
- [GitPython](https://gitpython.readthedocs.io/)
- [Pandas](https://pandas.pydata.org/)
