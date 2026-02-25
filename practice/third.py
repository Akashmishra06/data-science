# # 🟡 Level 3 – Strings

# 11. Count vowels in a string.
# 12. Reverse a string.
# 13. Check if a string is palindrome.
# 14. Count frequency of each character in a string.
# 15. Remove all spaces from a string.

# 11. Count vowels in a string.
# getString = input("Enter the value of getString: ")
# vowels = ["a", "e", "i", "o", "u"]
# totalVewelsInGetStrings = 0
# for i in getString:
#     if i.lower() in vowels:
#         totalVewelsInGetStrings += 1

# print(totalVewelsInGetStrings)

# 12. Reverse a string.
# getString = input("Enter the value of getString: ")
# reverString = getString[::-1]
# print(reverString)

# 13. Check if a string is palindrome.
# getString = input("Enter the value of getString: ")
# clean = getString.lower()

# if clean == clean[::-1]:
#     print(f"Yes, {getString} is a palindrome")
# else:
#     print(f"No, {getString} is not a palindrome")

# # 14. Count frequency of each character in a string.
# getString = input("Enter the value of getString: ")
# leOfgetString = len(getString)
# valOfI = 0
# charIsCount = []
# for i in getString:
#     for j in getString:
#         if i == j:
#             valOfI += 1
#     if i in charIsCount:
#         valOfI = 0
#         continue
#     print(f"in this {getString}:- {i} = {valOfI}")
#     valOfI = 0
#     charIsCount.append(i)

# 15. Remove all spaces from a string.
getString = input("Enter the value of getString: ")

print(getString.replace(" ", ""))