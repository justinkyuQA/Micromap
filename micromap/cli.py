import socket
import sys
from datetime import datetime

COMMON_PORTS = {
    20: "FTP-DATA",
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    587: "SMTP-SUBMISSION",
    993: "IMAPS",
    995: "POP3S",
    3306: "MYSQL",
    3389: "RDP",
    5432: "POSTGRES",
    6379: "REDIS",
    8000: "HTTP-ALT",
    8080: "HTTP-ALT",
    8443: "HTTPS-ALT",
}

def banner():
    print()
    print("MicroMap")
    print("=" * 40)

def resolve_target(target):
    try:
        return socket.gethostbyname(target)
    except socket.gaierror:
        return None

def scan_port(ip, port, timeout=0.5):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            return s.connect_ex((ip, port)) == 0
    except Exception:
        return False

def main():
    args = sys.argv[1:]

    if not args or args[0] in ["-h", "--help", "help"]:
        banner()
        print("Usage:")
        print("  python3 -m micromap <host>")
        print()
        print("Examples:")
        print("  python3 -m micromap google.com")
        print("  python3 -m micromap 127.0.0.1")
        print()
        return

    target = args[0]
    ip = resolve_target(target)

    banner()
    print("Target:", target)

    if not ip:
        print("Status: could not resolve target")
        return

    print("IP:", ip)
    print("Time:", datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"))
    print()
    print("Open Ports")
    print("-" * 40)

    found = False

    for port, service in COMMON_PORTS.items():
        if scan_port(ip, port):
            found = True
            print(f"{port:<6} {service}")

    if not found:
        print("No common open ports found.")

    print()
    print("Scan complete.")
