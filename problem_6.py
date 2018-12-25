# Find the difference between the sum of the squares, and the square
# of the sum of first 100 natural numbers


# def square_of_sum(high_num):
#     s = sum(range(1, high_num + 1))
#     print(f"Sum to {high_num} is {s}")
#     print(f"Square of sum to {high_num} is {s**2}")
#     return s ** 2


# def sum_of_squares(high_num):
#     s = [x ** 2 for x in range(1, high_num + 1)]
#     print(f"Sum of squares is {sum(s)}")
#     return sum(s)


# print(square_of_sum(100) - sum_of_squares(100))

print(sum(range(1, 101)) ** 2 - sum([x ** 2 for x in range(1, 101)]))

