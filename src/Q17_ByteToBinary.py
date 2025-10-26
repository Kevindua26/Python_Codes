# Write a program to perform byte → binary type data type
print('Q17_ByteToBinary.py')

print("===BYTE EXAMPLE===")
b = bytes([65, 66, 67, 68, 69])
print(b)

# assessing elements ina bite object
print(b[0])
print(b[1])

for byte in b:
    print(byte, end = "")

print("\n===BYTE EXAMPLE===")

#creating byte array

ba = bytearray([65, 66, 67, 68, 69])
print(ba)

# modifying elements
ba[0] = 97
print(ba)

# adding element to byte array
ba.append(70)
print(ba)

#converting byte array to bytes
b_converted = bytes(ba)
print(b_converted)

# memory view
print("\n===Memory view example===")
b_mv = bytes([65, 66, 67, 68, 69])

# creating memory view object
mv = memoryview(b_mv)
print(mv)
print("\n")

# accessing elements through memory
print(mv[0])

# slicing memory view
mv_slice = mv[1:4]
print(mv_slice.tobytes())
print("\n")

# creating byte array memory view
ba_mv = bytearray([65, 66, 67, 68, 69])
mv_ba = memoryview(ba_mv)

# modifying the original bytearray through memory
mv_ba[0] = 97
print(ba_mv)

print(ba_mv)
