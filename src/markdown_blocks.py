from inline_markdown import text_to_textnodes
from textnode import text_nodes_to_html_nodes
from htmlnode import ParentNode

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    final = []
    for block in blocks:
        line = block.strip()
        if line != "":
            final.append(line)
    return final

def block_to_block_type(block):
    if is_block_heading(block):
        return block_type_heading
    elif is_block_code(block):
        return block_type_code
    elif is_block_quote(block):
        return block_type_quote
    elif is_block_unordered_list(block):
        return block_type_unordered_list
    elif is_block_ordered_list(block):
        return block_type_ordered_list
    return block_type_paragraph


def is_block_heading(block):
    lines = block.split("\n")
    if len(lines) == 1:
        if lines[0].startswith("# "):
            return True
        elif lines[0].startswith("## "):
            return True
        elif lines[0].startswith("### "):
            return True
        elif lines[0].startswith("#### "):
            return True
        elif lines[0].startswith("##### "):
            return True
        elif lines[0].startswith("###### "):
            return True
        else:
            return False
    return False

def is_block_code(block):
    if block.startswith("```") and block[-3:] == "```":
        return True
    return False

def is_block_quote(block):
    lines = block.split("\n")
    for line in lines:
        if not line.startswith(">"):
            return False
    return True

def is_block_unordered_list(block):
    lines = block.split("\n")
    for line in lines:
        if not line.startswith("* ") and not line.startswith("- "):
            return False
    return True

def is_block_ordered_list(block):
    lines = block.split("\n")
    for i in range(len(lines)):
        if not lines[i].startswith(f"{i+1}. "):
            return False
    return True

def heading_to_html_node(block):
    text = block.lstrip("# ")
    text_nodes = text_to_textnodes(text)
    html_nodes = text_nodes_to_html_nodes(text_nodes)
    return ParentNode(f"h{len(block) - len(text) - 1}", html_nodes)
    