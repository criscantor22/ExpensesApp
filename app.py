import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="TravelAI Expense Assistant",
    layout="wide"
)

st.title("✈️ TravelAI Expense Assistant")

st.markdown(
    """
    Upload travel receipts and generate
    AI-powered expense reports.
    """
)

col1, col2 = st.columns(2)

with col1:
    receipts = st.file_uploader(
        "Upload Receipts",
        accept_multiple_files=True
    )

with col2:
    itinerary = st.file_uploader(
        "Upload Travel Itinerary"
    )

if st.button("Generate Report"):

    st.success("Report Generated Successfully!")

    data = {
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
        ]
    }

    df = pd.DataFrame(data)

    st.metric(
        "Total Expenses",
        f"${df['Amount'].sum():,.0f}"
    )

    st.dataframe(df)
