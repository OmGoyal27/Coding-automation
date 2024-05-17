import webbrowser

def visit(urls):                # Opens all of the urls
    for url in urls:
        webbrowser.open(url)