import streamlit as st
from ticket_agent import analyze_ticket

st.set_page_config(
    page_title="IT Ticket Assistant",
    page_icon="🛠️",
    layout="centered"
)

st.title("🛠️ IT Ticket Assistant")
st.caption("A simple rule-based Agentic AI prototype for IT support teams.")

with st.expander("Try an example"):
    st.write("I cannot connect to VPN after changing my password.")

ticket = st.text_area(
    "Describe your IT problem",
    height=150,
    placeholder="Example: I cannot connect to VPN after changing my password."
)

if st.button("Analyze Ticket", type="primary", use_container_width=True):
    if not ticket.strip():
        st.warning("Please describe the IT problem first.")
    else:
        result = analyze_ticket(ticket)

        st.subheader("Ticket Analysis")

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Category", result["category"])
        with col2:
            st.metric("Priority", result["priority"])

        st.markdown("### Possible Cause")
        st.write(result["possible_cause"])

        st.markdown("### Recommended Troubleshooting")
        for number, step in enumerate(result["steps"], start=1):
            st.write(f"{number}. {step}")

        st.markdown("### Agent Decision")
        if result["escalate"]:
            st.error(f"Escalation recommended: {result['escalation_reason']}")
        else:
            st.success("Try the recommended steps first. Escalation is not currently required.")

        st.info(
            "This prototype provides general troubleshooting suggestions. "
            "Follow your organization's security and IT support policies."
        )
