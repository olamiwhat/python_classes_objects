# write a function that tells if a number is a prime number or not.
# if number passed is a prime number , it should return "number is a prime number"
# if number is not a prime number, it should return "Not a prime"
# e.g isPrime(2) => "2 is a prime number"
# e.g isPrime(8) => "Not a prime"


# is 1 a prime number?

# is 2 a prime number?
# can 2 be divided by 1? yes
# can it divided by 2, itself? yes

# 3 => 1, 3 yes
# 4 => 1, 2, 4 No
# 5 => 1, 5 Yes
# 6 => 1, 2, 3, 6 No

# solution

# def isPrime(n):
#     if n == 1:
#         return f"{str(n)} Not a prime"
#     if n == 2:
#         return f"{str(n)} is a prime number"
#     for i in range(2, (n//2)):
#         if n % i == 0:
#             return f"{str(n)} Not a prime"

#     return f"{str(n)} is a prime number "


# def isPrime2(n):
#     if n == 1:
#         return f"{str(n)} Not a prime"
#     if n == 2 or n == 3 or n == 5:
#         return f"{str(n)} is a prime number"
#     if n % 2 == 0:
#         return f"{str(n)} Not a prime"
#     elif n % 3 == 0:
#         return f"{str(n)} Not a prime"
#     elif n % 5 == 0:
#         return f"{str(n)} Not a prime"
#     else:
#         return f"{str(n)} is a prime number "


# list_num = [15, 14, 3, 5, 22, 43, 79, 87, 154, 90, 31, 37]

# for num in list_num:
#     print((isPrime(num)))


# print(isPrime(3))
# print(isPrime(5))
# print(isPrime(210))
# print(isPrime(1))
# print(isPrime(2))
# print(isPrime(79))
