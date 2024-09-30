import os
from urllib.parse import quote
from .common_utils import iterate_topics

def create_or_append_markdown(directory, topic, link, title, description):
    """Creates or appends the link and description to a markdown file."""
    first_letter = topic[0].upper() if topic else 'G'
    folder_path = os.path.join(directory, first_letter)
    
    # Sanitize topic for valid folder names
    topic_folder_name = ''.join(c for c in topic if c.isalnum() or c in [' ', '-']).strip().capitalize()
    topic_folder_path = os.path.join(folder_path, topic_folder_name)  # Capitalize the topic name
    
    # Create the letter-based and topic-specific folder if they don't exist
    os.makedirs(topic_folder_path, exist_ok=True)
    
    markdown_file = os.path.join(topic_folder_path, f"{topic_folder_name.lower()}.md")
    
    # Check if the link already exists in the markdown file
    link_exists = False
    if os.path.exists(markdown_file):
        with open(markdown_file, 'r') as md:
            content = md.read()
            if link in content:
                link_exists = True
    
    if not link_exists:
        # Append the link if it doesn't exist
        with open(markdown_file, 'a') as md:
            md.write(f"### {title}\n")
            md.write(f"- [Link]({link})\n")
            md.write(f"- Description: {description}\n\n")

def update_readme(directory):
    """Updates the root README.md with links to each topic markdown file."""
    readme_path = os.path.join(directory, "README.md")
    readme_content = "# Topic Index\n\n"
    
    current_letter = None
    for letter_folder, _, topic_info in iterate_topics(directory):
        if letter_folder != current_letter:
            readme_content += f"\n## {letter_folder}\n"
            current_letter = letter_folder
        
        encoded_path = quote(topic_info['encoded_path'])
        readme_content += f"- [{topic_info['topic']}]({encoded_path})\n"
    
    with open(readme_path, 'w') as readme:
        readme.write(readme_content)
