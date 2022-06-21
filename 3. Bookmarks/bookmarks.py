import webbrowser

with open('links.txt') as file:
    links = file.readlines()
    for link in links:
        webbrowser.open(link)