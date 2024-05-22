def print_formatted(number):
    width = len(bin(number)[2:])  # Calculate the width required for binary representation
    
    for i in range(1, number + 1):
        dec = str(i).rjust(width)  # Decimal representation
        octal = oct(i)[2:].rjust(width)  # Octal representation
        hexa = hex(i)[2:].upper().rjust(width)  # Hexadecimal representation
        binary = bin(i)[2:].rjust(width)  # Binary representation
        
        # Print all representations in the specified format
        print(dec, octal, hexa, binary)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)