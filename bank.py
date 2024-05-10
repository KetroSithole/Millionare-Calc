import streamlit as st

def calculate_savings_needed(interest_rate, years, target_amount):
    monthly_interest_rate = interest_rate / 12 / 100
    months = years * 12
    savings_needed = target_amount / ((1 + monthly_interest_rate) ** months - 1) / monthly_interest_rate
    return savings_needed

def main():
    st.title("Millionaire Calculator")

    st.sidebar.header("Parameters")
    interest_rate = st.sidebar.slider("Annual Interest Rate (%)", 0.1, 20.0, 5.0, 0.1)
    years = st.sidebar.slider("Number of Years", 1, 30, 10)
    target_amount = 1000000  # Target amount in ZAR

    savings_needed = calculate_savings_needed(interest_rate, years, target_amount)

    st.write(f"To become a millionaire in {years} years, you need to save approximately ZAR {savings_needed:.2f} per month, with an annual interest rate of {interest_rate}% compounded monthly.")

if __name__ == "__main__":
    main()
