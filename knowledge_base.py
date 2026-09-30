KNOWLEDGE_BASE = {
    "Network / VPN": {
        "keywords": [
            "vpn", "network", "internet", "wifi", "wi-fi",
            "connection", "connect", "remote access"
        ],
        "possible_cause": (
            "The issue may be related to connectivity, cached credentials, "
            "VPN configuration, or an authentication session."
        ),
        "steps": [
            "Confirm that the device has a working internet connection.",
            "Disconnect and restart the VPN client.",
            "If your password recently changed, sign out and enter the new credentials.",
            "Restart the computer and try the connection again.",
            "If the problem continues, capture the error message and contact IT support.",
        ],
    },

    "Password / Account": {
        "keywords": [
            "password", "login", "log in", "sign in",
            "account", "locked", "credentials", "authentication"
        ],
        "possible_cause": (
            "The password may be incorrect or expired, the account may be locked, "
            "or cached credentials may be out of date."
        ),
        "steps": [
            "Confirm that the correct username/account is being used.",
            "Check Caps Lock and keyboard layout.",
            "Use the organization's approved password-reset process if necessary.",
            "After a password change, sign out of affected applications and sign in again.",
            "Contact the service desk if the account remains locked.",
        ],
    },

    "Email / Outlook": {
        "keywords": [
            "email", "outlook", "mail", "inbox",
            "send email", "receive email"
        ],
        "possible_cause": (
            "The mail client may have a connectivity, authentication, synchronization, "
            "or mailbox configuration problem."
        ),
        "steps": [
            "Check whether the internet connection is working.",
            "Close and reopen the mail application.",
            "Confirm that the account is signed in.",
            "Check whether webmail works, if your organization provides it.",
            "Record any error message and contact IT if synchronization still fails.",
        ],
    },

    "Printer": {
        "keywords": [
            "printer", "printing", "print", "paper jam",
            "toner", "offline"
        ],
        "possible_cause": (
            "The printer may be offline, disconnected, out of paper/toner, "
            "or have a print-queue problem."
        ),
        "steps": [
            "Check that the printer is powered on and shows no hardware error.",
            "Confirm paper and toner/ink status.",
            "Verify that the correct printer is selected.",
            "Clear stuck jobs from the print queue if permitted.",
            "Restart the printer and try again.",
        ],
    },

    "Application / Software": {
        "keywords": [
            "application", "software", "app", "crash",
            "freezing", "freeze", "not opening", "error"
        ],
        "possible_cause": (
            "The application may have a temporary process, configuration, "
            "permission, update, or dependency problem."
        ),
        "steps": [
            "Save other work and restart the affected application.",
            "Capture the exact error message or screenshot.",
            "Restart the computer if the application remains unresponsive.",
            "Check whether the issue affects only you or multiple users.",
            "Contact application support if the issue continues.",
        ],
    },

    "Security Incident": {
        "keywords": [
            "phishing", "malware", "ransomware", "virus",
            "hacked", "data breach", "security breach",
            "suspicious email", "compromised"
        ],
        "possible_cause": (
            "The report may indicate a security event that requires review by "
            "the organization's security team."
        ),
        "steps": [
            "Do not enter credentials into suspicious prompts or links.",
            "Do not forward suspicious files or links to coworkers.",
            "Preserve the suspicious message or relevant details for the security team.",
            "Follow your organization's incident-reporting procedure immediately.",
        ],
        "always_escalate": True,
        "escalation_reason": (
            "Potential security incidents should be reviewed by the organization's "
            "authorized security team."
        ),
    },

    "General IT Support": {
        "keywords": [],
        "possible_cause": (
            "The problem does not closely match one of the prototype's known categories."
        ),
        "steps": [
            "Restart the affected application or device when safe to do so.",
            "Record the exact error message and when the issue started.",
            "Check whether other users are experiencing the same problem.",
            "Contact the IT service desk with these details if the issue continues.",
        ],
    },
}
