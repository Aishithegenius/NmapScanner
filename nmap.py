import nmap

def scan_target(target, ports):
    scanner = nmap.PortScanner()
    print(f"Scanning {target} on ports {ports}...\n")
    
    scanner.scan(target, ports)
    
    for host in scanner.all_hosts():
        print(f"Host: {host} ({scanner[host].hostname()})")
        print(f"State: {scanner[host].state()}")
        
        for proto in scanner[host].all_protocols():
            print(f"Protocol: {proto}")
            ports = scanner[host][proto].keys()
            for port in ports:
                print(f"Port {port}: {scanner[host][proto][port]['state']}")

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    port_range = input("Enter port range (e.g., 20-100): ")
    
    scan_target(target_ip, port_range)
