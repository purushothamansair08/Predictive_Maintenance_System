import streamlit as st
import re
from predict import predict_failure

# -----------------------------------
# PAGE TITLE
# -----------------------------------

st.title("Predictive Maintenance System")
st.markdown("Enter machine details to predict failure")

# -----------------------------------
# Inputs
# -----------------------------------

udi = st.text_input(
    "UDI (Max 2 digits)",
    max_chars=2,
    placeholder="Example: 12"
)

product_id = st.text_input(
    "Product ID",
    placeholder="Example: A12345"
).upper()

type_ = st.selectbox(
    "Type",
    ["L", "M", "H"]
)

air_temp = st.number_input(
    "Air Temperature (K)",
    min_value=0.0,
    max_value=500.0,
    value=300.0
)

process_temp = st.number_input(
    "Process Temperature (K)",
    min_value=0.0,
    max_value=500.0,
    value=310.0
)

rpm = st.number_input(
    "Rotational Speed (rpm)",
    min_value=0,
    max_value=5000,
    value=1500
)

torque = st.number_input(
    "Torque (Nm)",
    min_value=0.0,
    max_value=200.0,
    value=40.0
)

wear = st.number_input(
    "Tool Wear (min)",
    min_value=0,
    max_value=500,
    value=120
)

# -----------------------------------
# Validation
# -----------------------------------

valid = True

# Empty check
if not udi:
    st.info("Enter UDI (Example: 12)")
    valid = False

if not product_id:
    st.info("Enter Product ID (Example: A12345)")
    valid = False

# -----------------------------------
# UDI Validation
# -----------------------------------

if udi:

    if not udi.isdigit():

        st.warning(
            "UDI must contain only numbers.\n\nExample: 12"
        )

        valid = False

    elif len(udi) > 2:

        st.warning(
            "UDI must be a maximum of 2 digits.\n\nExample: 12"
        )

        valid = False

# -----------------------------------
# Product ID Validation
# -----------------------------------

if product_id:

    if not re.fullmatch(
        r"[A-Z]\d{5}",
        product_id
    ):

        st.warning(
            "Invalid Product ID format.\n\nExample: A12345"
        )

        valid = False

# -----------------------------------
# Sensor Range Validation
# -----------------------------------

if not (250 <= air_temp <= 500):

    st.warning(
        "Air Temperature must be between 250 K and 500 K."
    )

    valid = False

if not (250 <= process_temp <= 500):

    st.warning(
        "Process Temperature must be between 250 K and 500 K."
    )

    valid = False

if not (0 <= rpm <= 5000):

    st.warning(
        "Rotational Speed must be between 0 and 5000 rpm."
    )

    valid = False

if not (0 <= torque <= 200):

    st.warning(
        "Torque must be between 0 and 200 Nm."
    )

    valid = False

if not (0 <= wear <= 500):

    st.warning(
        "Tool Wear must be between 0 and 500 minutes."
    )

    valid = False# -----------------------------------
# PREDICT BUTTON
# -----------------------------------

if st.button("Predict", disabled=not valid):

    input_data = {
        "Air temperature [K]": air_temp,
        "Process temperature [K]": process_temp,
        "Rotational speed [rpm]": rpm,
        "Torque [Nm]": torque,
        "Tool wear [min]": wear,
        "Type": type_
    }

    with st.spinner("Predicting..."):

        try:
            result = predict_failure(input_data)

        except Exception as e:
            st.error(f"Error: {e}")
            st.stop()

    # -----------------------------------
    # RESULTS
    # -----------------------------------

    prediction = result["prediction"]
    probability = result["probability"]
    health_score = result["health_score"]
    risk = result["risk"]
    recommendation = result["recommendation"]

    st.info(f"UDI: {udi} | Product ID: {product_id}")

    if prediction == 1:
        st.error("⚠️ Machine Failure Likely")
    else:
        st.success("✅ Machine is Healthy")

    col1, col2, col3 = st.columns(3)

    col1.metric("Failure Probability", f"{probability}%")
    col2.metric("Health Score", f"{health_score}")
    col3.metric("Risk Level", risk)

    st.info(f"🛠 Recommendation: {recommendation}")