import streamlit as st
import pandas as pd
from PIL import Image
from openai import OpenAI
from dotenv import load_dotenv
import os

# ==================================
# OPENAI CONFIGURATION
# ==================================

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = None

if api_key:
    client = OpenAI(api_key=api_key)

# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="TravelAI Expense Assistant",
    page_icon="✈️",
    layout="wide"
)

# ==================================
# HEADER
# ==================================

st.title("✈️ TravelAI Expense Assistant")

st.subheader(
    "AI-Powered Travel Expense Report Generator"
)

# ==================================
# SIDEBAR
# ==================================

st.sidebar.header("Company Policy")

meal_limit = st.sidebar.number_input(
    "Meal Limit (MXN)",
    value=500
)

hotel_limit = st.sidebar.number_input(
    "Hotel Limit Per Night (MXN)",
    value=2500
)

# ==================================
# FILE UPLOADS
# ==================================

col1, col2 = st.columns(2)

with col1:

    st.header("📄 Upload Receipts")

    receipts = st.file_uploader(
        "Upload Receipt Images",
        type=["jpg", "jpeg", "png", "pdf"],
        accept_multiple_files=True
    )

with col2:

    st.header("🛫 Upload Travel Itinerary")

    itinerary = st.file_uploader(
        "Upload Itinerary",
        type=["pdf", "csv"]
    )

# ==================================
# RECEIPT PREVIEW
# ==================================

if receipts:

    st.success(
        f"{len(receipts)} receipt(s) uploaded"
    )

    st.subheader("Receipt Preview")

    preview_cols = st.columns(3)

    for idx, receipt in enumerate(receipts[:3]):

        if receipt.type.startswith("image"):

            image = Image.open(receipt)

            with preview_cols[idx % 3]:
                st.image(
                    image,
                    caption=receipt.name,
                    use_container_width=True
                )

# ==================================
# GENERATE REPORT
# ==================================

if st.button(
    "🚀 Generate AI Report",
    use_container_width=True
):

    st.success(
        "Expense Report Generated Successfully!"
    )

    # DEMO DATA
    data = [
        ["Hotel", "Marriott", 3500, "Approved"],
        ["Meal", "Restaurant XYZ", 780, "Violation"],
        ["Transportation", "Uber", 1290, "Approved"]
    ]

    df = pd.DataFrame(
        data,
        columns=[
            "Category",
            "Vendor",
            "Amount",
            "Status"
        ]
    )

    total = df["Amount"].sum()

    # ==================================
    # METRICS
    # ==================================

    st.header("📊 Expense Dashboard")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Total Expenses",
            f"MXN {total:,.0f}"
        )

    with c2:
        st.metric(
            "Compliance Score",
            "92%"
        )

    with c3:
        st.metric(
            "Receipts Processed",
            len(receipts) if receipts else 0
        )

    with c4:
        st.metric(
            "Time Saved",
            "27 min"
        )

    # ==================================
    # TABLE
    # ==================================

    st.header("📋 Expense Details")

    st.dataframe(
        df,
        use_container_width=True
    )

    # ==================================
    # POLICY CHECKER
    # ==================================

    st.header("⚠ Policy Compliance")

    violations = []

    meal_rows = df[
        df["Category"] == "Meal"
    ]

    for _, row in meal_rows.iterrows():

        if row["Amount"] > meal_limit:

            violations.append(
                f"""
                Meal expense at {row['Vendor']}
                exceeded company policy by
                MXN {row['Amount'] - meal_limit:.0f}
                """
            )

    hotel_rows = df[
        df["Category"] == "Hotel"
    ]

    for _, row in hotel_rows.iterrows():

        if row["Amount"] > hotel_limit:

            violations.append(
                f"""
                Hotel expense at {row['Vendor']}
                exceeded company policy by
                MXN {row['Amount'] - hotel_limit:.0f}
                """
            )

    if violations:

        for violation in violations:
            st.error(violation)

    else:
        st.success(
            "No policy violations detected"
        )

    # ==================================
    # AI SUMMARY
    # ==================================

    st.header("🤖 AI Summary")

    st.info(
        f"""
Travel expense report generated successfully.

Total Expenses:
MXN {total:,.0f}

Policy Compliance:
92%

Estimated Savings:
90% reduction in manual processing effort.

Recommendation:
Review expenses flagged by compliance policies.
"""
    )

    # ==================================
    # DOWNLOAD CSV
    # ==================================

    st.download_button(
        label="📥 Download Report",
        data=df.to_csv(index=False),
        file_name="expense_report.csv",
        mime="text/csv"
    )

    # ==================================
    # CHATBOT
    # ==================================

    st.divider()

    st.header("💬 Expense Copilot")

    st.write(
        "Ask questions about your expense report."
    )

    question = st.text_input(
        "Example: Why was my meal expense rejected?"
    )

    if question:

        report_context = df.to_string(
            index=False
        )

        policy_context = f"""
Meal Limit: {meal_limit} MXN
Hotel Limit: {hotel_limit} MXN
"""

        if client:

            with st.spinner(
                "Analyzing your expenses..."
            ):

                try:

                    response = client.responses.create(
                        model="gpt-5",
                        input=f"""
You are TravelAI.

You help employees understand
their travel expense reports.

Company Policy:

{policy_context}

Expense Report:

{report_context}

User Question:

{question}

Provide a concise and professional answer.
"""
                    )

                    st.success(
                        response.output_text
                    )

                except Exception as e:

                    st.error(
                        f"OpenAI Error: {e}"
                    )

        else:

            st.warning(
                "OPENAI_API_KEY not configured."
            )
