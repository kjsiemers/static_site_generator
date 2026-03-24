def markdown_to_blocks(markdown_text):
    blocks = []
    blocks = markdown_text.split('\n\n').strip()
    
    for block in blocks:
        if block == '':
            del blocks[blocks.index(block)]
    return blocks