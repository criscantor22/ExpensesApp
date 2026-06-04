import streamlit as st

st.set_page_config(
    page_title="TravelAI Expense Assistant",
    layout="wide"
)

st.title("✈️ TravelAI Expense Assistant")

st.write(
    "Upload receipts and generate AI-powered expense reports."
)

receipts = st.file_uploader(
    "Upload Receipts",
    accept_multiple_files=True
)

itinerary = st.file_uploader(
    "Upload Travel Itinerary"
)

if st.button("Generate Report"):

    st.success("Report generated successfully!")

    st.metric(
        "Total Expenses",
        "$5,570"
    )

    st.metric(
        "Compliance",
        "92%"
    )

    st.dataframe({
        "Category": ["Hotel", "Meal", "Uber"],
        "Amount": [3500, 780, 1290]
    })
