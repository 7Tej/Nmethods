import struct

def decimal_to_ieee754_32bit(decimal_number):
    # Pack the decimal number into its IEEE 754 single-precision representation
    ieee754_bytes = struct.pack('>f', decimal_number)
    
    # Convert the bytes to binary representation
    ieee754_binary = ''.join(f'{byte:08b}' for byte in ieee754_bytes)
    
    return ieee754_binary

def decimal_to_ieee754_64bit(decimal_number):
    # Pack the decimal number into its IEEE 754 double-precision representation
    ieee754_bytes = struct.pack('>d', decimal_number)
    
    # Convert the bytes to binary representation
    ieee754_binary = ''.join(f'{byte:08b}' for byte in ieee754_bytes)
    
    return ieee754_binary

# Example: Convert 3.14 to 32-bit and 64-bit IEEE 754 representations
decimal_number = 1988500*10*27 # Mass of Sun in g
ieee754_32bit_representation = decimal_to_ieee754_32bit(decimal_number)
ieee754_64bit_representation = decimal_to_ieee754_64bit(decimal_number)

print(f"The 32-bit IEEE 754 representation of {decimal_number} is: {ieee754_32bit_representation}")
print(f"The 64-bit IEEE 754 representation of {decimal_number} is: {ieee754_64bit_representation}")
