import streamlit as st

def calculate_savings_needed(initial_balance, monthly_contribution, annual_interest_rate, years, target_amount):
    total_months = years * 12
    monthly_interest_rate = annual_interest_rate / 12 / 100
    future_value = initial_balance
    for month in range(total_months):
        future_value = (future_value + monthly_contribution) * (1 + monthly_interest_rate)
        if month % 12 == 0 and month > 0:
            annual_interest_rate *= 0.95  #  5% decrease in interest rate every year
            monthly_interest_rate = annual_interest_rate / 12 / 100
    return future_value

def main():
    st.title("Millionaire Calculator")

    st.sidebar.header("Parameters")
    initial_balance = st.sidebar.number_input("Initial Balance (ZAR)", min_value=0, step=10000, value=0)
    monthly_contribution = st.sidebar.number_input("Monthly Contribution (ZAR)", min_value=0, step=100, value=1000)
    annual_interest_rate = st.sidebar.slider("Initial Annual Interest Rate (%)", 0.1, 20.0, 5.0, 0.1)
    years = st.sidebar.slider("Number of Years", 1, 30, 10)
    target_amount = 1000000  # Target amount in ZAR

    if st.sidebar.button("Calculate"):
        if initial_balance >= target_amount:
            st.error("Your initial balance is already greater than or equal to the target amount!")
        else:
            savings_needed = calculate_savings_needed(initial_balance, monthly_contribution, annual_interest_rate, years, target_amount)
            if savings_needed < 0:
                st.error("Sorry, it seems impossible to reach the target amount with the given parameters.")
            else:
                st.success(f"To reach a target of ZAR {target_amount:,} in {years} years, you need to start with an initial balance of ZAR {initial_balance:,} and save ZAR {monthly_contribution:,} every month.")
                st.write(f"Total savings needed (including interest adjustments): ZAR {savings_needed:,.2f}")

if __name__ == "__main__":
    main()
