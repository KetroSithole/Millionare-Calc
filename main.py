import streamlit as st

# Define app wide style
st.markdown(
    """
    <style>
    .main-title {
        font-size: 36px;
        font-weight: bold;
        color: #333333;
        margin-bottom: 30px;
    }
    .sidebar {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    .parameter-title {
        font-size: 18px;
        font-weight: bold;
        color: #333333;
        margin-bottom: 10px;
    }
    .result {
        font-size: 24px;
        color: #1e88e5;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def calculate_savings_needed(years, target_amount):
    months = years * 12
    savings_needed = target_amount / months
    return savings_needed

def main():
    st.title("Millionaire Calculator")
    st.markdown('<p class="main-title">Millionaire Calculator</p>', unsafe_allow_html=True)

    st.sidebar.header("Parameters")
    years = st.sidebar.slider("Number of Years", 1, 30, 10)
    target_amount = 1000000  # Target amount in ZAR

    savings_needed = calculate_savings_needed(years, target_amount)

    st.markdown('<p class="result">To become a millionaire in {} years, you need to save approximately ZAR {:.2f} per month.</p>'.format(years, savings_needed), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
