def extract_code_blocks(content):
    """
    Extracts code blocks from given markdown content.
    Assumes code blocks are enclosed in triple backticks.
    """
    code_blocks = []
    in_code_block = False
    current_block = []

    for line in content.split("\n"):
        if line.strip().startswith("```"):
            if in_code_block:
                # Ending a code block
                in_code_block = False
                code_blocks.append("\n".join(current_block))
                current_block = []
            else:
                # Starting a code block
                in_code_block = True
        elif in_code_block:
            current_block.append(line)

    return code_blocks

def extract_code(content):
    """
    Extracts code from given markdown content.
    Assumes code blocks are enclosed in triple backticks.
    """
    code_blocks = extract_code_blocks(content)
    return "\n".join(code_blocks)

