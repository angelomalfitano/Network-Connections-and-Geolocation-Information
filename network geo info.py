"""
Title: Network Connections and Geolocation Information Script

Description:
This script lists all active network connections along with detailed information 
such as local and remote addresses, connection status, process ID, process name, 
and geolocation data (latitude, longitude, and organization details) for the remote IP address. 
It leverages the psutil library for accessing system details and the requests library for 
fetching IP geolocation information.

Author: Angelo Malfitano

Creation Date: 2024-02-05

Link: https://www.linkedin.com/in/angelo-malfitano/

Github: https://github.com/angelomalfitano

License: GNU General Public License v3.0

INFO:
result.txt --> check in this file your output

"""

import requests
import psutil

def get_geo_info(ip_address):
    #Here, you can use your personal API services for enhanced data accuracy or additional information.
    url = f"https://ipinfo.io/{ip_address}/json"  
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        location_details = data.get("org", "N/A")
        location = data.get("city", "N/A")
        coordinates = data.get("loc", "").split(",")
        
        if len(coordinates) == 2:
            lat, lon = coordinates
        else:
            lat, lon = "N/A", "N/A"
        
        return lat, lon, location_details
    else:
        return "N/A", "N/A", "Address not found"

def list_net_connections():
    with open("result.txt", "w") as file: #use your own filename and path
        file.write(f"{'Local Address':<30}|{'Remote Address':<30}|{'Status':<15}|{'PID':<10}|{'Process Name':<20}|{'Coordinates':<20}|{'Location'}\n")
        connections = psutil.net_connections(kind='inet')
        for conn in connections:
            if conn.raddr:
                laddr = f"{conn.laddr.ip}:{conn.laddr.port}"
                raddr = f"{conn.raddr.ip}:{conn.raddr.port}"
                lat, lon, location_details = get_geo_info(conn.raddr.ip)
                coordinates = f"{lat}, {lon}" if lat != "N/A" else "N/A"
            else:
                laddr, raddr, coordinates, location_details = "N/A", "N/A", "N/A", "N/A"

            status = conn.status
            pid = conn.pid or "N/A"
            process_name = "N/A"

            if pid != "N/A":
                try:
                    process = psutil.Process(pid)
                    process_name = process.name()
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    process_name = "Access Denied or No Such Process"

            line = f"{laddr:<30}|{raddr:<30}|{status:<15}|{pid:<10}|{process_name:<20}|{coordinates:<20}|{location_details}\n"
            file.write(line)

try:
    list_net_connections()

except:
    print("Error found") #place here code to handle errors
