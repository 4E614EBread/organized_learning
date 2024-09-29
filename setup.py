from setuptools import setup, find_packages
import subprocess
import sys

def install_spacy_model():
    subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])

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
            'link-organizer=link_organizer.main:main',
        ],
    },
    description="A tool for organizing links into markdown files with Git integration.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/link-organizer",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

# Install spaCy model after setup
install_spacy_model()