import webbrowser
import time
import os

# The URL to be opened
url = "https://github.com/MONUMISHRA-XD"

# Number of tabs to open
num_tabs = 90

# Open the site in multiple tabs using Brave
for _ in range(num_tabs):
    webbrowser.open_new_tab(url)
    time.sleep(0.2)  # Slight delay between each tab opening to avoid overwhelming the browser

# Wait for 10 seconds
time.sleep(10)
