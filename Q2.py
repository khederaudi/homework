def binary_to_decimal_alt(binary_str):
    decimal_value = 0
    for i, digit in enumerate(reversed(binary_str)):
        if digit not in '01':
            raise ValueError("Invalid binary number: Input contains non-binary digits.")

        # Convert binary digit to integer
        digit_int = int(digit)

        # Calculate decimal contribution using bitwise operations
        decimal_value += digit_int << i

    return decimal_value

if __name__ == "__main__":
    while True:
        try:
            binary_str = input("Enter a binary number (or 'kheder' to quit): ")

            if binary_str.lower() == 'q':
                break

            decimal_value = binary_to_decimal_alt(binary_str)
            print("The decimal equivalent of", binary_str, "is", decimal_value)
        except ValueError as e:
            print(e)
 
