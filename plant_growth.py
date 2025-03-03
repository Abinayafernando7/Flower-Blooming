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
