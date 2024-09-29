import os
import csv
import pandas as pd
import asyncio
from .link_processing import fetch_link_preview, classify_topic

async def parse_file_input(file_path, delimiter=','):
    """Parses a single text, CSV, or Excel file asynchronously."""
    links_data = {}
    extension = os.path.splitext(file_path)[1].lower()
    
    if extension == '.txt':
        with open(file_path, 'r') as file:
            lines = file.readlines()
            tasks = [fetch_link_preview(line.strip().split(delimiter)[0]) for line in lines if len(line.strip().split(delimiter)) >= 1]
            results = await asyncio.gather(*tasks)
            for idx, (title, description) in enumerate(results):
                link = lines[idx].strip().split(delimiter)[0]
                topic = classify_topic(f"{title or 'No Title'} {description or 'No Description'}")[0].lower()
                links_data[link] = (topic, title, description)
    
    elif extension == '.csv':
        with open(file_path, mode='r') as file:
            reader = csv.reader(file, delimiter=delimiter)
            tasks = []
            rows = []
            for row in reader:
                for url in row:  # Handle multiple URLs in one line
                    if url.strip():
                        rows.append(url.strip())  # Store the row for later reference
                        tasks.append(fetch_link_preview(url.strip()))  # Fetch preview for each link
            results = await asyncio.gather(*tasks)
            for idx, (title, description) in enumerate(results):
                link = rows[idx]
                topic = classify_topic(f"{title or 'No Title'} {description or 'No Description'}")[0].lower()
                links_data[link] = (topic, title, description)
    
    elif extension in ['.xls', '.xlsx']:
        df = pd.read_excel(file_path)
        tasks = [fetch_link_preview(row['link']) for _, row in df.iterrows() if 'link' in df.columns]
        results = await asyncio.gather(*tasks)
        for idx, (title, description) in enumerate(results):
            link = df.iloc[idx]['link']
            topic = df.iloc[idx]['topic'] if 'topic' in df.columns else classify_topic(f"{title or 'No Title'} {description or 'No Description'}")[0].lower()
            description_in_file = df.iloc[idx]['description'] if 'description' in df.columns else description
            links_data[link] = (topic.lower(), title, description_in_file)
    
    return links_data

async def process_directory(directory, delimiter=','):
    """Processes all files in a directory asynchronously."""
    links_data = {}
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            # Parse each file and add its links to the total
            new_links = await parse_file_input(file_path, delimiter)
            links_data.update(new_links)
    
    return links_data
