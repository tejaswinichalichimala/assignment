def apply_policy(text, findings, level):
    masked = text

    for f in findings:
        if f["type"] in ["password", "api_key"]:
            masked = masked.replace("=", "=***")

    action = "allowed"
    if level in ["high", "critical"]:
        action = "masked"

    return action, masked