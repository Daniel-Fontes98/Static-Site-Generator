from textnode import TextNode, text_type_text, text_type_image, text_type_link
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        s = node.text.split(delimiter)
        if len(s) % 2 == 0:
            raise ValueError(f"Invalid markdown syntax: {node.text}")
        
        for i in range(len(s)):
            if s[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(s[i], text_type_text))
            else:
                new_nodes.append(TextNode(s[i], text_type))
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        tuples = extract_markdown_images(node.text)
        if len(tuples) == 0:
            new_nodes.append(node)
            continue

        s = node.text
        for t in tuples:
            s = s.split(f"![{t[0]}]({t[1]})", 1)
            if s[0] != "":
                new_nodes.append(TextNode(s[0], text_type_text))
            new_nodes.append(TextNode(t[0], text_type_image, t[1]))
            s = s[1]
    return new_nodes
            
def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        tuples = extract_markdown_links(node.text)
        if len(tuples) == 0:
            new_nodes.append(node)
            continue

        s = node.text
        for t in tuples:
            s = s.split(f"[{t[0]}]({t[1]})", 1)
            if s[0] != "":
                new_nodes.append(TextNode(s[0], text_type_text))
            new_nodes.append(TextNode(t[0], text_type_link, t[1]))
            s = s[1]
    return new_nodes