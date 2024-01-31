def create_2d_list(rows, cols):
    return [[None] * cols for _ in range(rows)]

# Example usage
rows = 3
cols = 4
my_list = create_2d_list(rows, cols)
print(my_list)
