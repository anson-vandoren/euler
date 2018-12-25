# Find the sum of all multiples of 3 or 5 below 1000
# https://projecteuler.net/problem=1


def multiples_of(multiplier, max):
    return list(range(multiplier, max + 1, multiplier))


def main():
    print("Sum of multiples of 3 or 5 < 1000:")
    of_three = multiples_of(3, 1000)
    of_five = multiples_of(5, 1000)
    of_both = of_three + of_five
    print(sum(of_both))


if __name__ == "__main__":
    main()
