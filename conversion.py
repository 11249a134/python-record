def binary_to_decimal(binary):
    decimal = int(binary, 2)
    return decimal

def octal_to_hexadecimal(octal):
    hexadecimal = hex(int(octal, 8))
    return hexadecimal.upper()

binary_num = input("Enter a binary number: ")
octal_num = input("Enter an octal number: ")
decimal_result = binary_to_decimal(binary_num)
hexadecimal_result = octal_to_hexadecimal(octal_num)

print("\n--- Conversion Results ---")
print(f"Binary to Decimal: {binary_num} → {decimal_result}")
print(f"Octal to Hexadecimal: {octal_num} → {hexadecimal_result}")
