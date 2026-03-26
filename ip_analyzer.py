import re
ips = {}

def check_ip(line):
    match = re.search(r"\d+\.\d+\.\d+\.\d+", line)
    if not match:
        return None

    ip = match.group()
    ips[ip] = ips.get(ip, 0) + 1

    if ips[ip] > 5:
        return {"type": "suspicious_ip", "risk": "high", "ip": ip}