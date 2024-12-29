#!/usr/bin/python3
import nmap

print("[+] Starting Application")
print("--------------------------------------")

# Get target IP and port range from the user
target = input("Enter Target IP: ")  # Target IP address
begin = int(input("Enter the starting Port: "))  # Start of the port range
end = int(input("Enter the end port in range: "))  # End of the port range

print("****************************************")
print(f"Scanning target {target} for open ports in range {begin}-{end}...")
print("--------------------------------------")

# Create an nmap scanner object
scanner = nmap.PortScanner()

# Loop through the specified port range
for port in range(begin, end + 1):
    try:
        # Perform the scan on the target IP and port
        result = scanner.scan(target, str(port))
        # Extract the state of the port
        state = result['scan'][target]['tcp'][port]['state']
        
        # Print only if the port is open
        if state == 'open':
            print(f"Port {port}: {state}")
    except KeyError:
        # Skip if no information is available for the port
        pass

print("--------------------------------------")
print("[+] Scan Complete")
