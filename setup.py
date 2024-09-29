from setuptools import setup, find_packages

setup(
    name="link-organizer",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "httpx",
        "beautifulsoup4",
        "spacy",
        "pandas",
        "gitpython",
        "openpyxl",
    ],
    entry_points={
        'console_scripts': [
            'link-organizer=main:main',  # Command to run the program
        ],
    },
    description="A tool for organizing links into markdown files with Git integration.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/link-organizer",  # Optional GitHub repo link
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
