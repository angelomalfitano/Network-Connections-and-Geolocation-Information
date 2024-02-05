# Network Connections and Geolocation Information
This Python script is designed to monitor network connections and retrieve geolocation information for each connection. Using the requests library, it fetches data from ipinfo.io for given IP addresses. It leverages psutil to list active network connections, including local and remote addresses, connection status, process IDs, and process names. Additionally, it enriches this data with geographical information (latitude, longitude, and organization details) based on the remote address's IP.

Requirements
Python 3.x
requests library
psutil library
Installation
First, ensure that Python 3 is installed on your system. Then, install the required libraries using pip:  pip install requests psutil
Usage
To run the script, navigate to the directory containing the script and execute it with Python: python network_geo_info.py

The script will create a file named result.txt in the same directory, listing all active network connections along with the following details:

Local Address
Remote Address
Connection Status
Process ID (PID)
Process Name
Geographical Coordinates (latitude and longitude)
Location Details (organization name)

Contributions
Contributions are welcome! If you'd like to improve the script or add new features, please feel free to fork the repository, make your changes, and submit a pull request.

