# Solution for Project Euler problem #4:
# https://projecteuler.net/problem=4
# A palindromic number reads the same both ways. The largest palindrone
# made from the product of two 2-digit numbers is 9009 = 9 * 91
# Find the largest palindrome made from the product of two 3-digit numbers

from typing import List
import time


def products(digits=3):
    start = 10 ** (digits - 1)
    end = 10 ** digits
    products = []
    for i in range(start, end):
        for j in range(start, end):
            products.append(i * j)
    return products


def palindromes_from(possibles: List[int]):
    palindromes = []
    for num in possibles:
        test = str(num)
        for i in range(len(test) // 2):
            if test[i] == test[-(i + 1)]:
                continue
            else:
                # print(f"{test} is not a palindrome")
                break
        else:
            palindromes.append(num)
    return palindromes


def is_palindrome(test_num):
    return len(palindromes_from([test_num])) > 0


def largest_palindrome_1():
    all_products = products(3)
    palindromes = palindromes_from(all_products)
    largest_palindrome = sorted(palindromes)[-1]
    print(largest_palindrome)


def largest_palindrome_2():
    palindromes = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            if is_palindrome(i * j):
                palindromes.append(i * j)
    print(sorted(palindromes)[-1])


def largest_palindrome_3():
    palindromes = []
    for i in range(1000, 100, -1):
        for j in range(1000, 100, -1):
            if is_palindrome(i * j):
                palindromes.append(i * j)
    print(sorted(palindromes)[-1])


def largest_palindrome_4():
    largest = 1
    for i in range(100, 1000):
        for j in range(100, 1000):
            prod = i * j
            if is_palindrome(prod) and prod > largest:
                largest = prod
    print(largest)


def largest_palindrome_5():
    largest = 1
    for i in range(1000, 900, -1):
        for j in range(1000, 900, -1):
            prod = i * j
            if is_palindrome(prod) and prod > largest:
                largest = prod
    print(largest)


def main():
    methods = [
        largest_palindrome_1,
        largest_palindrome_2,
        largest_palindrome_3,
        largest_palindrome_4,
        largest_palindrome_5,
    ]
    for i, m in enumerate(methods):

        start = time.perf_counter()
        m()
        end = time.perf_counter()
        print(f"{i}: ", end - start)


if __name__ == "__main__":
    main()
