import bibtexparser

def bibtex_to_markdown_with_links(bib_file):
    # Load the BibTeX database
    with open(bib_file, 'r') as file:
        bib_database = bibtexparser.load(file)

        markdown_entries = [
        'layout: home\n',
        '---\n',
        '<!-- <p align="center"> -->\n',
        '<img src="assets/img/portfolio/publications.png" alt="books" width="200" align="left" style="margin-right:10px; border-radius:80px" />\n',
        '<!-- </p> -->\n\n',
        '# Publications\n'
    ]
    
    for entry in bib_database.entries:
        author = entry.get('author', 'Unknown Author')
        title = entry.get('title', 'Untitled')
        journal = entry.get('journal', '')
        year = entry.get('year', 'Year Unknown')
        volume = entry.get('volume', '')
        pages = entry.get('pages', '')
        url = entry.get('url', None)  # Get URL if available
        
        # Format title and journal
        title = title.replace('{', '').replace('}', '')
        
        # Start the markdown entry
        markdown_entry = f"### {author} ({year}).\n**{title}.** "
        
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
    
    return "\n".join(markdown_entries)

def save_markdown_to_file(markdown_content, output_file):
    # Write the Markdown content to a file
    with open(output_file, 'w') as file:
        file.write(markdown_content)

# Replace 'yourfile.bib' with the path to your BibTeX file
bib_file = 'references.bib'
# Define the output Markdown file name
output_file = 'publications.markdown'

# Generate Markdown content
markdown_output = bibtex_to_markdown_with_links(bib_file)

# Save the content to a Markdown file
save_markdown_to_file(markdown_output, output_file)

print(f"Markdown file '{output_file}' has been created.")
