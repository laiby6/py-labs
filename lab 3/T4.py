# Function to print the pattern
def print_pattern(rows):
    # Print the upper half of the pattern
    for i in range(1, rows + 1):
        print('* ' * i)
    # Print the lower half of the pattern
    for i in range(rows - 1, 0, -1):
        print('* ' * i)

# Number of rows for the pattern
num_rows = 5
print_pattern(num_rows)

#Alternative of Pattern
print("\n")

def print_half_diamond(n):
    # Print the upper half of the diamond
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print()
    
    # Print the lower half of the diamond
    for i in range(n - 1, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()


n = 5
print_half_diamond(n)
