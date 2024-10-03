import os
from urllib.parse import quote
from .common_utils import iterate_topics

def update_vitepress_config(directory):
    """Updates the VitePress config file with the current directory structure."""
    sidebar_items = []
    current_letter = None
    letter_items = []
    
    for letter_folder, _, topic_info in iterate_topics(directory):
        if letter_folder != current_letter:
            if letter_items:
                sidebar_items.append({"text": current_letter, "items": letter_items})
            current_letter = letter_folder
            letter_items = []
        
        encoded_path = f"/{quote(topic_info['encoded_path'])}"
        letter_items.append({"text": topic_info['topic'], "link": encoded_path})
    
    if letter_items:
        sidebar_items.append({"text": current_letter, "items": letter_items})
    
    config_content = f"""
import {{ defineConfig }} from 'vitepress'

export default defineConfig({{
  title: "Learnings",
  description: "Learnings Links Collection",
  themeConfig: {{
    nav: [
      {{ text: 'Home', link: '/' }},
    ],
    sidebar: {sidebar_items},
    socialLinks: [
      {{ icon: 'github', link: 'https://github.com/yourusername/yourrepository' }}
    ]
  }}
}})
"""
    
    config_path = os.path.join(directory, '.vitepress', 'config.mts')
    os.makedirs(os.path.dirname(config_path), exist_ok=True)
    with open(config_path, 'w') as config_file:
        config_file.write(config_content)