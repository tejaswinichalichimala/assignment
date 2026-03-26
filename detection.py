from utils.regex import patterns

def detect(lines):
    findings = []

    for i, line in enumerate(lines):
        for key, pattern in patterns.items():
            if pattern.search(line):
                findings.append({
                    "type": key,
                    "line": i+1,
                    "risk": risk_map(key)
                })
    return findings

def risk_map(k):
    return {
        "password": "critical",
        "api_key": "high",
        "email": "low"
    }.get(k, "low")