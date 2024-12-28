#!/usr/bin/python3
import shodan
import sys

shodan_key = ""

if shodan_key == "":
    print("Error!! Enter API key")
    shodan_key = input("Enter API Key here>> ")
    if shodan_key == "":
        sys.exit()

# Create a Shodan object with the API key
api = shodan.Shodan(shodan_key)

# Function for saving output to a file
def save_output(received):
    with open("output.txt", "at") as f:
        f.write(received)
        f.write("\n")

print("------Shodan CLI 0_T_N----------")
item = input("Enter Search Query>> ")
print("-----------------------------")

myfind = []  # Create an empty list to save the output

try:
    # Use the user input to perform the search
    results = api.search(item)
    # Display the number of results discovered
    print("Total matched = {}".format(results['total']))
    # Add the filtered results to the list
    for result in results['matches']:
        myfind.append(f"{result['ip_str']} {result['hostnames']} {result['os']}")

except Exception as e:
    print(f"[-] Error Occurred: {e}")
    sys.exit()

print("[+] Search Successful")

# Provide the user options
try:
    output = int(input("Print to Screen select [1] or save to file [2]>> "))
    print("--------------------------------------------")
    if output == 1:
        for val in myfind:
            print(val)
    elif output == 2:
        for val in myfind:
            save_output(val)
        print("[+] Results saved to 'output.txt'")
    else:
        print("[-] Incorrect input")
except ValueError:
    print("[-] Invalid input. Please enter 1 or 2.")
