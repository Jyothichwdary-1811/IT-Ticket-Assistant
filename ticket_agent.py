from knowledge_base import KNOWLEDGE_BASE

CRITICAL_WORDS = [
    "production down",
    "server down",
    "database down",
    "data breach",
    "ransomware",
    "malware",
    "hacked",
    "security breach",
    "all users",
    "company-wide",
    "company wide",
]

HIGH_WORDS = [
    "cannot work",
    "can't work",
    "unable to work",
    "locked out",
    "system unavailable",
    "service unavailable",
]


def _contains_any(text, words):
    return any(word in text for word in words)


def classify_ticket(ticket):
    text = ticket.lower()

    best_category = "General IT Support"
    best_score = 0

    for category, details in KNOWLEDGE_BASE.items():
        score = sum(1 for keyword in details["keywords"] if keyword in text)
        if score > best_score:
            best_score = score
            best_category = category

    return best_category


def determine_priority(ticket):
    text = ticket.lower()

    if _contains_any(text, CRITICAL_WORDS):
        return "Critical"

    if _contains_any(text, HIGH_WORDS):
        return "High"

    return "Medium"


def analyze_ticket(ticket):
    category = classify_ticket(ticket)
    priority = determine_priority(ticket)

    details = KNOWLEDGE_BASE.get(category, KNOWLEDGE_BASE["General IT Support"])

    escalate = priority == "Critical" or details.get("always_escalate", False)

    if priority == "Critical":
        escalation_reason = (
            "The description may indicate a major outage or security incident. "
            "Contact the appropriate IT/security team immediately according to company policy."
        )
    elif details.get("always_escalate", False):
        escalation_reason = details["escalation_reason"]
    else:
        escalation_reason = (
            "Escalate to the IT service desk if the troubleshooting steps do not resolve the issue."
        )

    return {
        "category": category,
        "priority": priority,
        "possible_cause": details["possible_cause"],
        "steps": details["steps"],
        "escalate": escalate,
        "escalation_reason": escalation_reason,
    }
