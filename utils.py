# Function to find the largest number among three numbers
    
def largest_number(num1, num2, num3):
    """
    Finds the largest number among three given numbers.

    Args:
        num1 (int): First number
        num2 (int): Second number
        num3 (int): Third number

    Returns:
        int: The largest number among the three numbers
    """
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3