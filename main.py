"""
Unit 8
Code Your Own: Unit 8
Hex to Binary Encryptor
"""

def encrypt(code: str) -> str:
    try:
        decimal_val = int(code, 16)
    except ValueError:
        return None
    binary_str = bin(decimal_val)[2:].zfill(8)
    return binary_str

def main():
    code = input("Enter an 8-bit hex code (e.g., FF or 0xFF): ").strip()
    if code.lower().startswith("0x"):
        code = code[2:]
    if not code or any(c not in "0123456789abcdefABCDEF" for c in code):
        print("Error: Invalid hexadecimal code.")
        return
    if len(code) > 2:
        print("Error: Please enter exactly 8 bits (2 hex digits).")
        return
    binary_result = encrypt(code)
    if binary_result is None:
        print("Error: Invalid hexadecimal value.")
    else:
        print(f"\nBinary Equivalent: {binary_result}")

if __name__ == "__main__":
    main()
