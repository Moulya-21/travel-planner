import streamlit as st
from planner import generate_plan


st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️"
)


st.title("✈️ AI Travel Planner")

st.write(
    "Plan your trip using Artificial Intelligence"
)


destination = st.text_input(
    "Enter Destination"
)

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


if st.button("Generate Travel Plan"):

    if destination and budget and interests:

        with st.spinner("Creating your plan..."):

            result = generate_plan(
                destination,
                days,
                budget,
                interests
            )

        st.success("Travel Plan Generated")

        st.markdown(result)


    else:

        st.warning(
            "Please fill all details"
        )