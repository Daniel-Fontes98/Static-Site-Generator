from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
            return (
                self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url
            )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    

def text_nodes_to_html_nodes(text_nodes):
    html_nodes = []
    for text_node in text_nodes:
        if text_node.text_type == text_type_text:
            html_nodes.append(LeafNode(None, text_node.text))
        elif text_node.text_type == text_type_bold:
            html_nodes.append(LeafNode("b", text_node.text))
        elif text_node.text_type == text_type_italic:
            html_nodes.append(LeafNode("i", text_node.text))
        elif text_node.text_type == text_type_code:
            html_nodes.append(LeafNode("code", text_node.text))
        elif text_node.text_type == text_type_link:
            html_nodes.append(LeafNode("a", text_node.text, {"href": text_node.url}))
        elif text_node.text_type == text_type_image:
            html_nodes.append(LeafNode("img", "", {"src": text_node.url, "alt": text_node.text}))
        else:
            raise ValueError(f"Invalid text type: {text_node.text_type}")
    return html_nodes




        

