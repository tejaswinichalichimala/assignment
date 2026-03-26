from utils.chunk import chunk_data
from services.detection import detect
from services.log_analyzer import analyze_logs
from services.risk import calc_risk
from services.policy import apply_policy
from services.ai import ai_insights

def process(data):
    text = data["content"]
    lines = text.split("\n")

    all_findings = []

    # 🔥 CHUNK PROCESSING
    for chunk in chunk_data(lines, size=50):
        findings = detect(chunk)
        findings += analyze_logs(chunk)
        all_findings.extend(findings)

    score, level = calc_risk(all_findings)

    action, masked = apply_policy(text, all_findings, level)

    insights = ai_insights(text)

    return {
        "findings": all_findings,
        "risk_score": score,
        "risk_level": level,
        "action": action,
        "content": masked,
        "insights": insights
    }