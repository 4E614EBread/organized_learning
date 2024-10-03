import os

def get_sorted_folders(directory, ignore_folders=['.vitepress', '.git', 'node_modules']):
    """Returns a sorted list of folders in the given directory, excluding ignored folders."""
    return [
        folder for folder in sorted(os.listdir(directory))
        if folder not in ignore_folders and os.path.isdir(os.path.join(directory, folder))
    ]

def get_topic_info(letter_folder, topic_folder):
    """Returns information about a topic folder."""
    markdown_file = f"{topic_folder.lower()}.md"
    topic = os.path.splitext(topic_folder)[0]
    return {
        'markdown_file': markdown_file,
        'topic': topic,
        'encoded_path': f"{letter_folder}/{topic_folder}/{markdown_file}"
    }

def iterate_topics(directory):
    """Iterates through all topics in the directory structure."""
    for letter_folder in get_sorted_folders(directory):
        folder_path = os.path.join(directory, letter_folder)
        for topic_folder in get_sorted_folders(folder_path):
            topic_path = os.path.join(folder_path, topic_folder)
            if os.path.isdir(topic_path):
                yield letter_folder, topic_folder, get_topic_info(letter_folder, topic_folder)