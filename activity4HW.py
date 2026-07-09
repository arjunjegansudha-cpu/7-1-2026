start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

even_squares = []
odd_squares = []

for num in range(start, end + 1):
    square_val = num ** 2

    if square_val % 2 == 0:
        even_squares.append(square_val)
    else:
        odd_squares.append(square_val)

print(f"\nEven squares within range: {even_squares}")
print(f"Odd squares within range: {odd_squares}")