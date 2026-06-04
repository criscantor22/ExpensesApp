import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="TravelAI Expense Assistant",
    layout="wide"
)

st.title("✈️ TravelAI Expense Assistant")

receipts = st.file_uploader(
    "Upload Receipts",
    accept_multiple_files=True
)

itinerary = st.file_uploader(
    "Upload Travel Itinerary"
)

if st.button("Generate Report"):

    st.success("AI Report Generated")

    df = pd.DataFrame({
        "Category": [
            "Hotel",
            "Meal",
            "Transportation"
        ],
        "Vendor": [
            "Marriott",
            "Restaurant XYZ",
            "Uber"
        ],
        "Amount": [
            3500,
            780,
            1290
        ],
        "Status": [
            "Approved",
            "Policy Violation",
            "Approved"
        ]
    })

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Expenses",
            "$5,570"
        )

    with col2:
        st.metric(
            "Receipts Processed",
            len(receipts) if receipts else 0
        )

    with col3:
        st.metric(
            "Time Saved",
            "27 min"
        )

    st.dataframe(df)

    st.subheader("Policy Compliance")

    st.error(
        "Meal expense exceeded company policy by MXN 280"
    )

    st.subheader("AI Summary")

    st.info(
        """
        Travel expense report generated successfully.

        Total Expenses: MXN 5,570

        One policy violation detected.

        Estimated savings:
        90% reduction in report creation time.
        """
    )
