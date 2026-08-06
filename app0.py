import streamlit as st
from planner import generate_plan

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)

# -----------------------------
# Header
# -----------------------------
st.title("✈️ AI Travel Planner")
st.write("Plan your trip using Artificial Intelligence")

st.markdown("---")

# -----------------------------
# User Inputs
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    destination = st.text_input(
        "📍 Destination",
        placeholder="Example: Coorg"
    )

    days = st.number_input(
        "📅 Number of Days",
        min_value=1,
        max_value=30,
        value=5
    )

with col2:
    budget = st.text_input(
        "💰 Budget",
        placeholder="Example: ₹20000"
    )

    interests = st.text_area(
        "🎯 Interests",
        placeholder="Adventure, Food, Nature, Culture..."
    )

st.markdown("---")

# -----------------------------
# Generate Button
# -----------------------------
if st.button("🚀 Generate Travel Plan", use_container_width=True):

    if destination and budget and interests:

        with st.spinner("Generating your AI travel plan..."):

            result = generate_plan(
                destination,
                days,
                budget,
                interests
            )

        st.success("✅ Travel Plan Generated Successfully!")

        st.markdown("## 🗺️ Your Travel Plan")
        st.markdown(result)

    else:
        st.error("⚠️ Please fill in all the details before generating your travel plan.")
