# Problem 4
# 16 November 2001

# Find the largest palindrome made from the product of two 3-digit numbers.


def is_pal(num):
    if list(str(num)) == list(reversed(list(str(num)))):
        return True
max_pal = 0
for a in range(999, 100, -1):
    for b in range(999, 100, -1):
        prod = a * b
        if prod < max_pal:
            continue
        if is_pal(prod):
            max_pal = prod
print(max_pal)
