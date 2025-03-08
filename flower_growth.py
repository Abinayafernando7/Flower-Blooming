import streamlit as st

def will_plant_grow(moisture, ph, par):
    # Define conditions
    ph_good = 6 <= ph <= 8
    moist_good = 4 <= moisture <= 7
    par_good = 400 <= par <= 700

    # Check the status of each condition
    ph_status = "Good" if ph_good else "Bad (Too acidic or too alkaline)"
    moist_status = "Good" if moist_good else "Too dry" if moisture < 4 else "Too moist (Might rot)"
    par_status = "Good" if par_good else "Insufficient light" if par < 400 else "Too intense (Might burn)"

    # Calculate growth probability
    growth_factors = [ph_good, moist_good, par_good]
    growth_percentage = (sum(growth_factors) / len(growth_factors)) * 100

    # Determine overall growth possibility
    if ph_good and moist_good and par_good:
        return f"The plant will grow well. Probability: {growth_percentage:.2f}%", ph_status, moist_status, par_status
    else:
        return f"The plant might not grow properly due to unfavorable conditions. Probability: {growth_percentage:.2f}%", ph_status, moist_status, par_status

# Streamlit UI
st.title("Flower Blooming Prediction App")

# User input fields
moisture = st.number_input("Enter Moisture level (1-10):", min_value=1.0, max_value=10.0, step=0.1)
ph = st.number_input("Enter pH level:", min_value=0.0, max_value=14.0, step=0.1)
par = st.number_input("Enter PAR value (nm):", min_value=0.0, max_value=1000.0, step=1.0)

if st.button("Predict Growth"):
    result, ph_reason, moist_reason, par_reason = will_plant_grow(moisture, ph, par)
    
    # Display results
    st.subheader("🌿🌺🌸 Flower Blooming Prediction:")
    st.write(result)
    st.write(f"**pH Condition:** {ph_reason}")
    st.write(f"**Moisture Condition:** {moist_reason}")
    st.write(f"**PAR Condition:** {par_reason}")
    
    # Display project credit
    # Display project credit in the middle of the page
st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; height: 100px;">
        <h4>Made by Jessie Wiselin</h4>
    </div>
    """, unsafe_allow_html=True)