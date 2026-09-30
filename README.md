# IT Ticket Assistant

A beginner-friendly Streamlit prototype that demonstrates a simple agent-like IT support workflow.

## What it does

The app accepts an IT support problem and:

1. Classifies the ticket.
2. Assigns a priority.
3. Identifies a possible cause.
4. Retrieves troubleshooting steps from a local knowledge base.
5. Decides whether immediate escalation is recommended.

This first version is intentionally local and rule-based, so it requires no API key.

## Project structure

```text
it_ticket_assistant/
├── app.py
├── ticket_agent.py
├── knowledge_base.py
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10 or newer
- pip

## Setup

Open a terminal in this project folder.

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run

```bash
python -m streamlit run app.py
```

Streamlit will normally open the app in your browser. If it does not, copy the local URL printed in the terminal (usually `http://localhost:8501`).

## Example tickets

```text
I cannot connect to VPN after changing my password.
```

```text
Outlook is not receiving new emails.
```

```text
The production database is down for all users.
```

```text
I clicked a suspicious email and think my account may be compromised.
```

## How the prototype works

`app.py` provides the user interface.

`ticket_agent.py` acts as the decision layer. It classifies the issue, determines priority, retrieves the appropriate troubleshooting information, and decides whether escalation is required.

`knowledge_base.py` contains common IT issue categories, keywords, possible causes, and troubleshooting steps.

## Why this is only the first version

The prototype uses deterministic rules instead of an LLM. This makes it easy to understand and test.

A later Agentic AI version can add:

- An LLM for understanding tickets written in natural language
- Tool/function calling
- RAG over internal IT documentation
- Conversation memory
- Jira or ServiceNow ticket creation
- Human approval before sensitive actions
- Feedback such as "Did this solve the problem?"
- Logging and evaluation

## Safety note

Do not connect this learning prototype directly to production systems or give it privileged credentials. Security incidents and critical infrastructure problems should follow your organization's approved incident-response procedures.
