import os
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
# Title
# -----------------------------
st.title("✈️ AI Travel Planner")
st.write("Plan your trip using Artificial Intelligence")

# -----------------------------
# User Inputs
# -----------------------------
destination = st.text_input("Enter Destination")

days = st.number_input(
    "Number of Days",
    min_value=1,
    max_value=30,
    value=5
)

budget = st.text_input(
    "Budget",
    placeholder="Example: ₹20000"
)

interests = st.text_area(
    "Your Interests",
    placeholder="Adventure, Food, Beaches, Culture..."
)

# -----------------------------
# Generate Plan
# -----------------------------
if st.button("Generate Travel Plan"):

    if destination and budget and interests:

        with st.spinner("Creating your plan..."):

            result = generate_plan(
                destination,
                days,
                budget,
                interests
            )

        st.success("✅ Travel Plan Generated")

        # Display Travel Plan
        st.markdown(result)

        # -----------------------------
        # Show Destination Image
        # -----------------------------
        destination_name = destination.lower().strip()

        image_path = f"images/{destination_name}.jpg"

        if os.path.exists(image_path):
            st.subheader(f"📍 Explore {destination.title()}")
            st.image(
                image_path,
                caption=destination.title(),
                use_container_width=True
            )
        else:
            st.info(f"No image found for {destination.title()}.")

    else:
        st.warning("Please fill all details.")
