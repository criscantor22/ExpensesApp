import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="TravelAI Expense Assistant    V2",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ TravelAI Expense Assistant")

st.markdown("""
### AI-Powered Travel Expense Report Generator

Upload receipts and travel itineraries to automatically generate
expense reports and validate compliance with company policies.
""")

# Upload Section
col1, col2 = st.columns(2)

with col1:
    receipts = st.file_uploader(
        "📄 Upload Receipts",
        type=["jpg", "jpeg", "png", "pdf"],
        accept_multiple_files=True
    )

with col2:
    itinerary = st.file_uploader(
        "🛫 Upload Travel Itinerary",
        type=["pdf", "csv"]
    )

st.divider()

if st.button("🚀 Generate Report", use_container_width=True):

    st.success("Expense Report Generated Successfully!")

    # Demo Data
    df = pd.DataFrame({
        "Category": [
            "Hotel",
            "Meal",
            "Transportation",
            "Transportation"
        ],
        "Vendor": [
            "Marriott Hotel",
            "Restaurant XYZ",
            "Uber",
            "Airport Taxi"
        ],
        "Amount (MXN)": [
            3500,
            780,
            230,
            410
        ],
        "Status": [
            "Approved",
            "Policy Violation",
            "Approved",
            "Approved"
        ]
    })

    total = df["Amount (MXN)"].sum()

    st.subheader("📊 Expense Summary")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Total Expenses",
            f"${total:,.0f}"
        )

    with c2:
        st.metric(
            "Receipts Processed",
            len(receipts) if receipts else 0
        )

    with c3:
        st.metric(
            "Compliance Score",
            "92%"
        )

    with c4:
        st.metric(
            "Time Saved",
            "27 min"
        )

    st.divider()

    st.subheader("📋 Expense Details")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.divider()

    st.subheader("⚠ Policy Compliance")

    st.error(
        "Meal expense at Restaurant XYZ exceeded company limit by MXN 280."
    )

    st.success(
        "Hotel and transportation expenses comply with company policy."
    )

    st.divider()

    st.subheader("🤖 AI Summary")

    st.info(f"""
Travel expense report generated successfully.

Employee Trip Status: Completed

Total Expenses: MXN {total:,.0f}

Key Findings:
• 1 policy violation detected
• Hotel expenses approved
• Transportation expenses approved
• Estimated 90% reduction in manual reporting effort

Recommendation:
Review the meal expense before reimbursement approval.
""")

    st.download_button(
        label="📥 Download CSV Report",
        data=df.to_csv(index=False),
        file_name="travel_expense_report.csv",
        mime="text/csv"
    )
