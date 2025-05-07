def extract_title(markdown):
    for line in markdown.split("\n"):
        if line[:2] == "# ":
            return line.lstrip("#").strip(" ")
    raise Exception("no h1")