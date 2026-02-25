
# # 🟢 Level 1 – Very Basic (Warm-Up)

# 1. Print "Hello Data Science" 10 times using a loop.
# 2. Take a number from user and print whether it is even or odd.
# 3. Take two numbers and print the larger one.
# 4. Print all numbers from 1 to 100 that are divisible by 3.
# 5. Find the sum of numbers from 1 to N (N from user).

# q1:- Print "Hello Data Science" 10 times using a loop.

for i in range(10):
    print("Hello Data Science")

a = 1
while a <= 10:
    print("Hello Data Science")
    a+=1


# q2:- Take a number from user and print whether it is even or odd.

number = int(input("Enter the value of number: "))

if number == 0:
    print(f"number: {number} is zero ")
elif (number%2) == 0:
    print(f"number: {number} is even")
else:
    print(f"number: {number} is odd")


# q3:- Take two numbers and print the larger one.

numOne = 59
numbTwo = 83
print(f"larone one is: {max(numOne, numbTwo)}")

# q4:- Print all numbers from 1 to 100 that are divisible by 3.

for i in range(1, 101):
    if (i%3) == 0:
        print(i)


# q5:- Find the sum of numbers from 1 to N (N from user).
N = int(input("Enter the value of N: "))
sum = 0
for i in range(N+1):
    sum = sum+i
print(f"sum of 1 to {N} is: {sum}")