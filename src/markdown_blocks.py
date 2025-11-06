from enum import Enum

from htmlnode import HTMLNode
from textnode import TextNode, TextType, text_node_to_html_node
#    blocks = markdown.split("\n\n")
#    filtered_blocks = []
#    for block in blocks:
#        if block == "":
#            continue
#        block = block.strip()
#        filtered_blocks.append(block)
#    return filtered_blocks

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks = list(map(lambda x: x.strip(), blocks))
    while "" in blocks:
        blocks.remove("")
    return blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        html_node = block_to_html(block, block_type)

        if block_type == BlockType.CODE:
            text_node_code = TextNode(block, TextType.CODE)
            text_node_to_html_node(text_node_code)
        else:


def block_to_html(block, block_type):
    if block_type == BlockType.PARAGRAPH:
        return HTMLNode("p", block)
    if block_type == BlockType.HEADING:
        i = 0
        while block[i] == "#":
            i += 1
        return HTMLNode(f"h{i}", block)
    if block_type == BlockType.CODE:
        return HTMLNode("```", block)
    if block_type == BlockType.QUOTE:
        return HTMLNode("blockquote", block)
    if block_type == BlockType.ULIST:
        return HTMLNode("ul", block)
    if block_type == BlockType.OLIST:
        return HTMLNode("ol", block)
    
def text_to_children(text):
    pass

            
    
        
#
#Based on the type of block, create a new HTMLNode with the proper data
        
#Assign the proper child HTMLNode objects to the block node. I created a shared text_to_children(text) 
# function that works for all block types. It takes a string of text and returns a list of HTMLNodes 
# that represent the inline markdown using previously created functions (think TextNode -> HTMLNode).

#The "code" block is a bit of a special case: it should not do any inline markdown parsing of its children. 
# I didn't use my text_to_children function for this block type, I manually made a TextNode and used text_node_to_html_node.

'''
This is **bolded** paragraph
text in a p
tag here
        
This is another paragraph with _italic_ text and `code` here
'''
#"<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"