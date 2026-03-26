from services.ip_analyzer import check_ip

def analyze_logs(lines):
    findings = []
    fails = 0

    for i, line in enumerate(lines):
        if "failed" in line.lower():
            fails += 1

        if "exception" in line.lower():
            findings.append({"type": "error", "risk": "medium", "line": i+1})

        ip = check_ip(line)
        if ip:
            findings.append(ip)

    if fails > 3:
        findings.append({"type": "brute_force", "risk": "high"})

    return findings