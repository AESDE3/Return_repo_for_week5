import argparse
import subprocess
import ipaddress
def ping_device(target):
    command = ["ping", "-c", "4", target]
    try:
    	ipaddress.ip_address(target)
    except ValueError:
    	raise ValueError("invalid ip adress")
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        print(output.decode())
    except subprocess.CalledProcessError as e:
       	print(f"Failed to ping {target}\n{e.output.decode()}")

def main():
    parser = argparse.ArgumentParser(description="Ping a device. WARNING: This tool is vulnerable to command injection.")
    parser.add_argument("target", type=str, help="IP address or DNS name of the target device")
    args = parser.parse_args()
    ping_device(args.target)

if __name__ == "__main__":
    main()
