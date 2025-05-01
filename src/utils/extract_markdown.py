from re import findall


def extract_markdown_images(text) -> list[tuple[str,str]]:
    """takes raw text(markdown), and returns a list of tuples(alt text and the URL for the image)"""
    images = findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return images

def extract_markdown_links(text) -> list[tuple[str,str]]:
    """takes raw text(markdown), and returns a list of tuples(alt text and the URL)"""
    
    links = findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return links