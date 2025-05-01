
def markdown_to_blocks(markdown):
    parts = map(lambda x: x.strip(), markdown.split("\n\n"))
    parts = list(filter( lambda x: x != "", parts))
    return parts
