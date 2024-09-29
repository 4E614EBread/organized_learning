import os
import argparse
import asyncio
from file_handling import parse_file_input, process_directory
from link_processing import fetch_link_preview, classify_topic
from markdown_handling import create_or_append_markdown, update_readme
from git_handling import initialize_git_repo, commit_changes

def load_processed_links(repo_path):
    """Load the list of processed links from a log file."""
    log_file = os.path.join(repo_path, 'processed_links.log')
    if os.path.exists(log_file):
        with open(log_file, 'r') as log:
            processed_links = set(log.read().splitlines())
            return processed_links
    return set()

def log_processed_link(link, repo_path):
    """Log a processed link in the repository."""
    log_file = os.path.join(repo_path, 'processed_links.log')
    with open(log_file, 'a') as log:
        log.write(f"{link}\n")

async def add_link_manually(link, topic=None, description=None, processed_links=set(), repo_path=None):
    """Handles adding a link manually, with automatic topic/description if needed, asynchronously."""
    if link in processed_links:
        print(f"Link '{link}' has already been processed. Skipping...")
        return {}

    if not topic or not description:
        title, description = await fetch_link_preview(link)
        if not topic:
            topic_keywords = classify_topic(title + " " + description)
            topic = topic_keywords[0].lower() if topic_keywords else 'general'
    else:
        title, _ = await fetch_link_preview(link)

    # Log the processed link
    if repo_path:
        log_processed_link(link, repo_path)

    return {link: (topic.lower(), title, description)}

async def process_links(links_data, repo_path, processed_links):
    """Processes the links data and creates markdown files, skipping already processed links."""
    for link, (topic, title, description) in links_data.items():
        if link in processed_links:
            print(f"Link '{link}' has already been processed. Skipping...")
            continue
        create_or_append_markdown(repo_path, topic, link, title, description)
        # Log the processed link
        log_processed_link(link, repo_path)
    
    # Update README.md
    update_readme(repo_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Organize links by topic and save them in a git repository.')
    parser.add_argument('--file', type=str, help='Path to the input text or CSV file containing links')
    parser.add_argument('--directory', type=str, help='Directory containing text, CSV, or spreadsheet files')
    parser.add_argument('--link', type=str, help='Link to be added manually')
    parser.add_argument('--topic', type=str, help='Topic of the manually added link (optional)')
    parser.add_argument('--description', type=str, help='Description of the manually added link (optional)')
    parser.add_argument('--delimiter', type=str, default=',', help='Delimiter used in the input text or CSV file')
    parser.add_argument('--repo', type=str, required=True, help='Path to the git repository where links will be saved')
    
    args = parser.parse_args()

    links_data = {}

    # Initialize Git repo
    repo = initialize_git_repo(args.repo)

    # Load already processed links
    processed_links = load_processed_links(args.repo)

    if args.file:
        links_data = asyncio.run(parse_file_input(args.file, args.delimiter))

    elif args.directory:
        links_data = asyncio.run(process_directory(args.directory, args.delimiter))

    elif args.link:
        links_data = asyncio.run(add_link_manually(args.link, args.topic, args.description, processed_links, args.repo))
    
    if links_data:
        # Process the links asynchronously and create markdown files
        asyncio.run(process_links(links_data, args.repo, processed_links))

        # Commit changes to Git
        commit_changes(repo, message="Appended new links and updated the repository.")
    else:
        print("No links were processed. Please check the input.")
