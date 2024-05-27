from textnode import TextNode, text_type_text


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