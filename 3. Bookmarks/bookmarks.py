import webbrowser
import os

abspath = os.path.abspath(__file__)
currentDirectory = os.path.dirname(abspath)
os.chdir(currentDirectory)

with open('links.txt') as file:
    links = file.readlines()
    for link in links:
        webbrowser.open(link)