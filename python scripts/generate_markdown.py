import bibtexparser

def clean_bibtex_title(title):
    """Clean and convert BibTeX special characters to plain text."""
    # Replace BibTeX special characters with equivalent plain text characters
    replacements = {
        r'{\c{S}}': 'Ş', 
        r'{\c{t}}': 'ţ',
        # Add other special character replacements as needed
        r'{\'a}': 'á',
        r'{\'e}': 'é',
        r'{\'i}': 'í',
        r'{\'o}': 'ó',
        r'{\'u}': 'ú',
        r'{\"u}': 'ü',
        r'{\~n}': 'ñ',
        r'{\~a}': 'ã',
        r'{\^o}': 'ô',
        r'{\~o}': 'õ',
        r'{\`e}': 'è',
        # Continue adding replacements for other special characters...
    }
    
    for pattern, replacement in replacements.items():
        title = title.replace(pattern, replacement)
    
    # Remove any remaining braces
    return title.replace('{', '').replace('}', '')

def bibtex_to_markdown_with_links(bib_file):
    # Load the BibTeX database
    with open(bib_file, 'r') as file:
        bib_database = bibtexparser.load(file)

    # Custom header layout
    markdown_entries = [
        '---\n',
        'layout: home\n',
        '---\n',
        '<img src="assets/img/portfolio/publications.png" alt="books" width="200" align="left" style="margin-right:10px; border-radius:80px" />\n',
        '# Publications\n'
    ]

    # Create a numbered list
    for i, entry in enumerate(bib_database.entries, start=1):
        author = entry.get('author', 'Unknown Author')
        title = clean_bibtex_title(entry.get('title', 'Untitled'))
        journal = entry.get('journal', '')
        year = entry.get('year', 'Year Unknown')
        volume = entry.get('volume', '')
        pages = entry.get('pages', '')
        url = entry.get('url', None)  # Get URL if available
        
        # Start the markdown entry for the numbered list
        markdown_entry = f"{i}. {author} ({year}). **{title}.** "
        
        if journal:
            markdown_entry += f"*{journal}*, "
        if volume:
            markdown_entry += f"{volume} "
        if pages:
            markdown_entry += f"{pages}. "
        
        # Add the link if it exists
        if url:
            markdown_entry += f"[Link]({url})"
        
        markdown_entries.append(markdown_entry + "\n")
    
    return "".join(markdown_entries)

def save_markdown_to_file(markdown_content, output_file):
    # Write the Markdown content to a file
    with open(output_file, 'w') as file:
        file.write(markdown_content)

# Replace 'references.bib' with the path to your BibTeX file
bib_file = 'references.bib'
# Define the output Markdown file name
output_file = 'publications.markdown'

# Generate Markdown content
markdown_output = bibtex_to_markdown_with_links(bib_file)

# Save the content to a Markdown file
save_markdown_to_file(markdown_output, output_file)

print(f"Markdown file '{output_file}' has been created.")
