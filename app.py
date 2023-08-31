# A streamlit application to find the largest number among three numbers

# import required libraries
import streamlit as st

# import supporting functions from utils.py
from utils import largest_number

def main():
    """
    The main function of the application.
    """

    # Inputs
    num1 = st.number_input("Enter the first number: ")
    num2 = st.number_input("Enter the second number: ")
    num3 = st.number_input("Enter the third number: ")

    # Find the largest number among the three numbers
    largest_num = largest_number(num1, num2, num3)

    # Display the largest number
    st.write(f"The largest number among given three numbers is {largest_num}")
    
if __name__ == "__main__":
    main()
