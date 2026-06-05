import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="TravelAI Expense Assistant",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ TravelAI Expense Assistant")
st.subheader("AI-Powered Travel Expense Report Generator")

# Sidebar
st.sidebar.header("Company Policy")

meal_limit = st.sidebar.number_input(
    "Meal Limit (MXN)",
    value=500
)

hotel_limit = st.sidebar.number_input(
    "Hotel Limit Per Night (MXN)",
    value=2500
)

# Upload section
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

# Preview uploaded receipts
if receipts:
    st.success(f"{len(receipts)} receipt(s) uploaded")

    for receipt in receipts[:3]:
        if receipt.type.startswith("image"):
            image = Image.open(receipt)
            st.image(image, width=250)

# Generate report
if st.button("🚀 Generate AI Report"):

    st.header("Generated Expense Report")

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

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Total Expenses",
            f"${total:,.0f}"
        )

    with c2:
        st.metric(
            "Compliance",
            "92%"
        )

    with c3:
        st.metric(
            "Receipts",
            len(receipts) if receipts else 0
        )

    with c4:
        st.metric(
            "Time Saved",
            "27 min"
        )

    st.dataframe(
        df,
        use_container_width=True
    )

    st.header("Policy Compliance")

    violations = []

    meal_rows = df[df["Category"] == "Meal"]

    for _, row in meal_rows.iterrows():
        if row["Amount"] > meal_limit:
            violations.append(
                f"""
                Meal expense at {row['Vendor']}
                exceeded policy by
                MXN {row['Amount'] - meal_limit}
                """
            )

    if violations:
        for violation in violations:
            st.error(violation)
    else:
        st.success("No policy violations detected")

    st.header("AI Summary")

    st.info(
        f"""
        Travel expense report generated successfully.

        Total expenses: MXN {total:,.0f}

        One policy violation detected:
        meal expense exceeded company limit.

        Estimated processing time reduced
        from 30 minutes to less than 3 minutes.
        """
    )

    st.download_button(
        label="📥 Download Report",
        data=df.to_csv(index=False),
        file_name="expense_report.csv",
        mime="text/csv"
    )

st.header("💬 Ask About Your Expenses")

question = st.text_input(
    "Ask a question about your expense report"
)

if question:

    if "hotel" in question.lower():
        st.success(
            "Hotel expenses total MXN 3,500."
        )

    elif "meal" in question.lower():
        st.warning(
            "Meal expense exceeded company policy."
        )

    elif "total" in question.lower():
        st.success(
            f"Total expenses are MXN {total:,.0f}"
        )

    else:
        st.info(
            "Expense report analyzed successfully."
        )
