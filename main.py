import socket
from IPy import IP

def scan(target, port_num, timeout):
    converted_ip = check_ip(target)
    print('\n' + '[-_0 Scanning Target] ' + str(target))

    for port in range(1,port_num):
        scan_port(converted_ip, port, timeout)

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def get_baner(s):
    return s.recv(1024)

def scan_port(ipadress, port, timeout):
    try:
        sock = socket.socket()
        sock.settimeout(timeout)
        sock.connect((ipadress, port))
        try:
            banner = get_baner(sock)
            print('[+] Open port ' + str(port) + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('[+] Open port ' + str(port))

    except:
        pass

if __name__ == "__main__":
    targets = input('[+] Enter target/s to scan (split multiple targets using ,): ')
    port_num = int(input('Enter the number of ports that you want to scan: '))
    timeout = int(input('Enter the time of scanning one port in seconds: '))

    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '), port_num, timeout)

    else:
        scan(targets, port_num, timeout)
