import webbrowser
import os

file_path = os.path.abspath("NAMAN DASHBOARD PROJECT.html")

webbrowser.open("file://" + file_path)

print("Dashboard opened in your browser!")
