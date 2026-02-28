import streamlit as st
from modules.part1 import find_existing_mould
from modules.part2 import calculate_moulds_required
from modules.part3 import cost_comparison
from modules.mip_optimizer import optimize_moulds
from modules.schedule_optimizer import schedule_based_reuse
from modules.data import generate_dataset

st.set_page_config(page_title="AI Formwork Optimizer", layout="centered")

st.title("🏗 AI-Based Formwork Optimization System")

st.subheader("Enter Formwork Details")

# -------- USER INPUTS --------
height = st.number_input("Height (mm)", min_value=100, step=10)
width = st.number_input("Width (mm)", min_value=100, step=10)

df, materials_data = generate_dataset()

material = st.selectbox("Material Type", list(materials_data.keys()))

quantity = st.number_input(
    "Total Required Usage Quantity",
    min_value=1,
    step=1
)

project_duration = st.number_input(
    "Project Duration (Days)",
    min_value=1,
    value=60
)

cycle_time = st.number_input(
    "Mould Cycle Time (Days)",
    min_value=1,
    value=5
)

# -------- RUN BUTTON --------
if st.button("Run Optimization"):

    st.markdown("---")

    # ================= PART 1 =================
    st.subheader("🔍 Part 1: Mould Matching")

    match = find_existing_mould(height, width, material)

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

    # ================= PART 2 =================
    st.subheader("📦 Part 2: Optimization & Reusability")

    reuse_limit = materials_data[material][0]

    # Schedule-based calculation
    moulds_schedule, effective_capacity = schedule_based_reuse(
        quantity,
        reuse_limit,
        project_duration,
        cycle_time
    )

    # MIP optimization
    optimized_moulds = optimize_moulds(quantity, reuse_limit)

    st.write(f"Material Reusability Limit: {reuse_limit}")
    st.write(f"Effective Capacity (Schedule Based): {effective_capacity}")
    st.write(f"Moulds Required (Schedule Model): {moulds_schedule}")
    st.write(f"Moulds Required (MIP Optimized): {optimized_moulds}")

    # ================= PART 3 =================
    st.subheader("💰 Part 3: Cost Comparison")

    cost_per_mould, traditional_cost, model_cost, savings = cost_comparison(
        material,
        quantity,
        optimized_moulds,
        match["standard_height"],
        match["standard_width"]
    )

    st.write(f"Cost per Mould: ₹ {cost_per_mould}")
    st.write(f"Traditional Cost (Without Optimization): ₹ {traditional_cost}")
    st.write(f"Optimized Cost (AI Model): ₹ {model_cost}")
    st.success(f"Total Savings Using AI Model: ₹ {savings}")
