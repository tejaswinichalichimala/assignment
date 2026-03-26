def calc_risk(findings):
    score = 0

    for f in findings:
        if f["risk"] == "critical":
            score += 5
        elif f["risk"] == "high":
            score += 4
        elif f["risk"] == "medium":
            score += 3
        else:
            score += 1

    if score > 12:
        level = "critical"
    elif score > 8:
        level = "high"
    elif score > 4:
        level = "medium"
    else:
        level = "low"

    return score, level