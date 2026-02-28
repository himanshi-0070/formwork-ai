import streamlit as st
from modules.part1 import find_existing_mould
from modules.part2 import calculate_moulds_required
from modules.part3 import cost_comparison
from modules.data import generate_dataset

st.set_page_config(page_title="AI Formwork Optimizer", layout="centered")

st.title("🏗 AI-Based Formwork Optimization System")

st.subheader("Enter Formwork Details")

# User Inputs
height = st.number_input("Height (mm)", min_value=100, step=10)
width = st.number_input("Width (mm)", min_value=100, step=10)

# Load materials
df, materials_data = generate_dataset()

material = st.selectbox("Material Type", list(materials_data.keys()))

usage_required = st.number_input(
    "How many times mould will be used?",
    min_value=1,
    step=1
)

if st.button("Run Optimization"):

    # ---------------- PART 1 ----------------
    match = find_existing_mould(height, width, material)

    st.subheader("🔍 Part 1: Mould Matching")

    if match["match"]:
        st.success("Existing mould can be used ✅")
        st.write(
            f"Standard Dimension: "
            f"{match['standard_height']} x {match['standard_width']}"
        )
        st.write(f"Height Difference: {match['diff_height']} mm")
        st.write(f"Width Difference: {match['diff_width']} mm")
    else:
        st.error("No existing mould within tolerance ❌")
        st.write("New mould will be created with given dimensions.")

    # ---------------- PART 2 ----------------
    moulds_required, reuse = calculate_moulds_required(
        material,
        usage_required
    )

    st.subheader("📦 Part 2: Reusability Calculation")
    st.write(f"Material Reusability: {reuse} times")
    st.write(f"Moulds Required: {moulds_required}")

    # ---------------- PART 3 ----------------
    cost_per_mould, traditional_cost, model_cost, savings = cost_comparison(
        material,
        usage_required,
        moulds_required,
        match["standard_height"],
        match["standard_width"]
    )

    st.subheader("💰 Part 3: Cost Comparison")

    st.write(f"Cost per Mould: ₹ {cost_per_mould}")
    st.write(f"Traditional Cost (Without Optimization): ₹ {traditional_cost}")
    st.write(f"Model Cost (With Optimization): ₹ {model_cost}")

    st.success(f"Total Savings Using AI Model: ₹ {savings}")