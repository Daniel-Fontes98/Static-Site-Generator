import unittest
from htmlnode import ParentNode, LeafNode
from markdown_blocks import (
    markdown_to_blocks, 
    block_to_block_type,
    block_type_heading,
    block_type_code,
    block_type_ordered_list,
    block_type_paragraph,
    block_type_quote,
    block_type_unordered_list,
    heading_to_html_node,
    code_to_html_node,
    quote_to_html_node,
    unordered_list_to_html_node,
    ordered_list_to_html_node,
    paragraph_to_html_node,
    markdown_to_html_node
)


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_block_to_block_type_heading(self):
        text = "# TEST"

        self.assertEqual(
            block_to_block_type(text),
            block_type_heading
        )

    def test_block_to_block_type_code(self):
        text = "```\nHello World\n```"

        self.assertEqual(
            block_to_block_type(text),
            block_type_code
        )

    def test_block_to_block_type_quote(self):
        text = ">Hello World\n>Hello Mom!"

        self.assertEqual(
            block_to_block_type(text),
            block_type_quote
        )

    def test_block_to_block_type_unordered_list(self):
        text = "* List Item 1\n- List Item 2"

        self.assertEqual(
            block_to_block_type(text),
            block_type_unordered_list
        )
    
    def test_block_to_block_type_ordered_list(self):
        text = "1. Item 1\n2. Item 2"

        self.assertEqual(
            block_to_block_type(text),
            block_type_ordered_list
        )

    def test_block_to_block_type_paragraph(self):
        text = "1- HHHAAAA\n HEEEE\nLOL"

        self.assertEqual(
            block_to_block_type(text),
            block_type_paragraph
        )
    
    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_heading_to_html_node(self):
        block1 = "# I am h1"
        self.assertEqual(
            heading_to_html_node(block1),
            ParentNode("h1", [LeafNode(None, "I am h1")])
        )
        block2 = "## I am h2"
        self.assertEqual(
            heading_to_html_node(block2),
            ParentNode("h2", [LeafNode(None, "I am h2")])
        )
        block3 = "### I am h3"
        self.assertEqual(
            heading_to_html_node(block3),
            ParentNode("h3", [LeafNode(None, "I am h3")])
        )
        block4 = "#### I am h4"
        self.assertEqual(
            heading_to_html_node(block4),
            ParentNode("h4", [LeafNode(None, "I am h4")])
        )
        block5 = "##### I am h5"
        self.assertEqual(
            heading_to_html_node(block5),
            ParentNode("h5", [LeafNode(None, "I am h5")])
        )
        block6 = "###### I am h6"
        self.assertEqual(
            heading_to_html_node(block6),
            ParentNode("h6", [LeafNode(None, "I am h6")])
        )

    def test_code_to_html_node(self):
        block = "```Hello World\nHello Dad!```"
        self.assertEqual(
            code_to_html_node(block),
            ParentNode(
                "pre",
                [ParentNode(
                    "code",
                    [LeafNode(None, "Hello World\nHello Dad!")]
                )]
            )
        )


    def test_quote_to_html_nodes(self):
        block1 = ">This is me\n>And this is me again"
        self.assertEqual(
            quote_to_html_node(block1),
            ParentNode("blockquote", [LeafNode(None, "This is me\nAnd this is me again")])
        )

        block2 = ">This is me\n>This is me but **bold**"
        self.assertEqual(
            quote_to_html_node(block2),
            ParentNode("blockquote", [LeafNode(None, "This is me\nThis is me but "), LeafNode("b", "bold")])
        )

    def test_unordered_list_to_html_nodes(self):
        block = "- This is first\n- This is second\n- **This** is last"
        self.assertEqual(
            unordered_list_to_html_node(block),
            ParentNode(
                "ul",
                [
                    ParentNode(
                        "li",
                        [LeafNode(None, "This is first")]  
                    ),
                    ParentNode(
                        "li",
                        [LeafNode(None, "This is second")]    
                    ),
                    ParentNode(
                        "li",
                        [LeafNode("b", "This"), LeafNode(None, " is last")]    
                    ),
                ]
            )
        )
    
    def test_ordered_list_to_html_nodes(self):
        block = "1. This is first\n2. This is second\n3. **This** is last"
        self.assertEqual(
            ordered_list_to_html_node(block),
            ParentNode(
                "ol",
                [
                    ParentNode(
                        "li",
                        [LeafNode(None, "This is first")]  
                    ),
                    ParentNode(
                        "li",
                        [LeafNode(None, "This is second")]    
                    ),
                    ParentNode(
                        "li",
                        [LeafNode("b", "This"), LeafNode(None, " is last")]    
                    ),
                ]
            )
        )

    def test_paragraph_to_html_nodes(self):
        block = "Hello World\nI am *Daniel* and this is **CS50**"
        self.assertEqual(
            paragraph_to_html_node(block),
            ParentNode(
                "p",
                [
                    LeafNode(None, "Hello World I am "),
                    LeafNode("i", "Daniel"),
                    LeafNode(None, " and this is "),
                    LeafNode("b", "CS50"),
                ]
            )
        )
        
    def test_markdown_to_html_node(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        self.assertEqual(
            markdown_to_html_node(md),
            ParentNode(
                "div",
                [
                    ParentNode(
                        "p",
                        [
                            LeafNode(None, "This is "),
                            LeafNode("b", "bolded"),
                            LeafNode(None, " paragraph")
                        ]
                    ),
                    ParentNode(
                        "p",
                        [
                            LeafNode(None, "This is another paragraph with "),
                            LeafNode("i", "italic"),
                            LeafNode(None, " text and "),
                            LeafNode("code", "code"),
                            LeafNode(None, " here This is the same paragraph on a new line")
                        ]
                    ),
                    ParentNode(
                        "ul",
                        [
                            ParentNode(
                                "li",
                                [LeafNode(None, "This is a list")]
                            ),
                            ParentNode(
                                "li",
                                [LeafNode(None, "with items")]
                            )
                        ]
                    )
                ]
            )
        )
    
    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote> This is a\n blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

if __name__ == "__main__":
    unittest.main()