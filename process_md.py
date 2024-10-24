import re
import os
from pathlib import Path

def process_markdown(content):
    # Remove front matter (content between +++ or --- markers at start of file)
    content = re.sub(r'^[+-]{3}.*?[+-]{3}\s*', '', content, flags=re.DOTALL)
    
    # Remove table of contents section if it exists (assumes it's between <!-- TOC --> markers)
    content = re.sub(r'<!-- TOC -->.*?<!-- /TOC -->', '', content, flags=re.DOTALL)
    
    # Remove HTML comments
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    
    # Remove markdown links but keep the text
    content = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', content)
    
    # Remove markdown headers (#)
    content = re.sub(r'^#+\s*(.+)$', r'\1', content, flags=re.MULTILINE)
    
    # Remove emphasis marks (* and _) but keep the text
    content = re.sub(r'[*_]{1,2}([^*_]+)[*_]{1,2}', r'\1', content)
    
    # Remove images
    content = re.sub(r'!\[.*?\]\(.*?\)', '', content)
    
    # Remove TOML configuration sections
    content = re.sub(r'\[\[.*?\]\].*?(?=\n\n|\Z)', '', content, flags=re.DOTALL)
    
    # Clean up extra whitespace
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    
    return content.strip()

base_dir = '/Users/micn/Documents/code/ftl/docs/content'
output = []

# Process each markdown file
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                processed = process_markdown(content)
                if processed.strip():  # Only include non-empty content
                    output.append(f"\n\n=== {os.path.relpath(file_path, base_dir)} ===\n\n")
                    output.append(processed)

# Write the combined output
with open('ftl.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))