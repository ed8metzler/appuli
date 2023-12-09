import socket
import os
import time

# Get the computer name
computer_name = socket.gethostname()

# Function to create scrolling effect
def scroll_text(text, width):
    extended_text = text + ' ' * width
    for i in range(len(extended_text) - width):
        print('\r' + extended_text[i:i+width], end='')
        time.sleep(0.5)

# Clear the screen and scroll the text
os.system('cls' if os.name == 'nt' else 'clear')
scroll_text(computer_name, 20)