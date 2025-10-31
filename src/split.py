from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        if node.text.count(delimiter) == 0:
            new_nodes.append(node)
            continue
        
        if node.text.count(delimiter) % 2 != 0:
            raise Exception(f"not found closing delimiter: {delimiter}")

        splited = node.text.split(delimiter)
        if node.text.find(delimiter) == 0:
            deli = True
        else: deli = False

        while len(splited) != 0:
            if deli:
                new_node = TextNode(splited.pop(0), text_type)
                deli = False
            else: 
                new_node = TextNode(splited.pop(0), TextType.TEXT)
                deli = True
            new_nodes.append(new_node)

    return new_nodes