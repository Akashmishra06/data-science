
# # 🟢 Level 2 – Loops + Logic

# 6. Print multiplication table of a number (up to 10).
# 7. Count how many digits are in a given number.
# 8. Reverse a number (e.g., 1234 → 4321).
# 9. Check if a number is a palindrome (121 → Yes).
# 10. Print all prime numbers between 1 and 100.

# q6:- Print multiplication table of a number (up to 10).

# multiplication_number = int(input("Enter the value of multiplication number: "))

# for i in range(1, 11):
#     print(f"{multiplication_number} * {i} = {i*multiplication_number}")

# 7. Count how many digits are in a given number.
# valOne = int(input("Enter the value of valOne: "))
# print(len(str(abs(valOne))))

# 8. Reverse a number (e.g., 1234 → 4321).
# valOne = int(input("Enter the value of valOne: "))
# neg = False
# if valOne < 0:
#     neg = True
# emList = ""
# for i in range(len(str(valOne))):
#     if valOne > 0:
#         storeValue = valOne % 10
#         emList = emList + str(storeValue)
#         valOne = valOne // 10
# if neg:
#     print(-(int(emList)))
# else:
#     print(int(emList))

# if valOne > 0:
#     valOne = str(valOne)
#     reverseValOne = valOne[::-1]
#     print(int(reverseValOne))
# elif valOne < 0:
#     valOne = str(abs(valOne))
#     reverseValOne = valOne[::-1]
#     print(-(int(reverseValOne)))
# else:
#     print(0)



# 9. Check if a number is a palindrome (121 → Yes).

# palNumber = input("Enter the value of Number: ")
# reversePalNumber = palNumber[::-1]
# if palNumber == reversePalNumber:
#     print(f'yes, the Number {palNumber} is palindrome')
# else:
#     print(f"No, the number {palNumber} is not a palindrome")


# 10. Print all prime numbers between 1 and 100.
n = 100
prime = [True] * (n + 1)

prime[0] = prime[1] = False

for i in range(2, int(n ** 0.5) + 1):
    if prime[i]:
        for j in range(i * i, n + 1, i):
            prime[j] = False

for i in range(2, n + 1):
    if prime[i]:
        print(i)
