def markdown_to_blocks(markdown):
    filtered_blocks = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        if block == "":
            continue
        filtered_blocks.append(block.strip())
    return filtered_blocks

def block_to_block_type(markdown):
    if markdown[0] == '#':
        first_word = markdown.split(' ',1)[0]
        if first_word == '#'*len(first_word) and len(first_word) < 7:
            return 'heading'
    if markdown[:3] == markdown[-3:] == "```":
        return 'code'
    if markdown[0] == '>':
        lines = markdown.split('\n')
        for line in lines:
            if line[0] != '>':
                return 'paragraph'
        return 'quote'
    if markdown[:2] in ['* ','- ']:
        lines = markdown.split('\n')
        for line in lines:
            if line[:2] != markdown[:2]:
                return 'paragraph'
        return 'unordered_list'
    if markdown[:3] == '1. ':
        lines = markdown.split('\n')
        for i in range(len(lines)):
            if lines[i][:3] != f"{i+1}. ":
                return 'paragraph'
        return 'ordered_list'
    return 'paragraph'

