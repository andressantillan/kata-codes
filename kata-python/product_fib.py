# Product of consecutive Fib numbers
# The Fibonacci numbers are the numbers in the following integer sequence (Fn):
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...
# such as
# F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.
# Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying
# F(n) * F(n+1) = prod.
# Your function productFib takes an integer (prod) and returns an array:
# [F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
# depending on the language if F(n) * F(n+1) = prod.
# If you don't find two consecutive F(m) verifying F(m) * F(m+1) = prodyou will return
# [F(m), F(m+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
# F(m) being the smallest one such as F(m) * F(m+1) > prod.
# Examples
# productFib(714) # should return [21, 34, true], 
#                 # since F(8) = 21, F(9) = 34 and 714 = 21 * 34
# productFib(800) # should return [34, 55, false], 
#                 # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55

from math import sqrt

def product_fibonacci(prod):
    a = 0 # prev
    b = 1 # curr
    mult = a*b
    while mult < prod:
        temp = b
        b += a
        a = temp
        mult = a*b

    if prod == mult:
        return [a, b, True]

    return [a, b, False]

# [354224848179263111168, 573147844013818970112, False] should equal 
# [354224848179261915075, 573147844013817084101, True]

print(product_fibonacci(0))
print(product_fibonacci(203023208030065646654504166904697594722575))