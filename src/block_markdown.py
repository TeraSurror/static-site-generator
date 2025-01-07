block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):
    markdown = markdown.split('\n\n')
    blocks = []

    for block in markdown:
        if block == '':
            continue
        blocks.append(block.strip())

    return blocks

def block_to_block_type(markdown_block):
    lines = markdown_block.split('\n')

    if markdown_block.startswith(('#', '##', '###', '####', '#####', '######')):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith('```') and lines[-1].endswith('```'):
        return block_type_code
    if markdown_block.startswith(">"):
        for line in lines:
            if not line.startswith('>'):
                return block_type_paragraph
        return block_type_quote
    if markdown_block.startswith('* '):
        for line in lines:
            if not line.startswith('* '):
                return block_type_paragraph
        return block_type_ulist
    if markdown_block.startswith('- '):
        for line in lines:
            if not line.startswith('- '):
                return block_type_paragraph
        return block_type_ulist
    if markdown_block.startswith('1. '):
        i = 1
        for line in lines:
            if not line.startswith(f'{i}. '):
                return block_type_paragraph
            i += 1
        return block_type_olist

    return block_type_paragraph
    