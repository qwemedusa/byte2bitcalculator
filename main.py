def convert_bits_to_bytes(bits):
    bytes_value = bits // 8
    return bytes_value

def convert_bytes_to_bits(bytes_value):
    bits_value = bytes_value * 8
    return bits_value

def main():
    print("Bit-Byte Calculator")
    print("1. Convert bits to bytes")
    print("2. Convert bytes to bits")

    while True:
        user_choice = input("Enter your choice (1/2): ")
        if user_choice.isdigit() and int(user_choice) in [1, 2]:
            user_choice = int(user_choice)
            break
        else:
            print("Invalid input. Please enter a number between 1 and 2.")

    if user_choice == 1:
        while True:
            bits = input("Enter the number of bits: ")
            if bits.isdigit():
                bits = int(bits)
                break
            else:
                print("Invalid input. Please enter a valid number of bits.")
        bytes_value = convert_bits_to_bytes(bits)
        print(f"{bits} bits is equal to {bytes_value} bytes.")
    elif user_choice == 2:
        while True:
            bytes_value = input("Enter the number of bytes: ")
            if bytes_value.isdigit():
                bytes_value = int(bytes_value)
                break
            else:
                print("Invalid input. Please enter a valid number of bytes.")
        bits = convert_bytes_to_bits(bytes_value)
        print(f"{bytes_value} bytes is equal to {bits} bits.")

    while True:
        another_question = input("Do you have another question? (yes/no or y/n): ").lower()
        if another_question in ["yes", "y", "no", "n"]:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    if another_question in ["no", "n"]:
        print("Goodbye!")
    else:
        main()

if __name__ == "__main__":
    main()
