"""
What is the output of the following code?
for x in range(1, 5):
    print(x * x)

answer:
0
1
4
9
16
--------------------------------------------

Write a program that reads two integer numbers
from user and then prints their difference.
Don't specify any message when reading the input, please.

a = int(input())
b = int(input())

print(a - b)

-------------------------------------------

Write a program that takes 3 integer numbers a, b and c,
calculates a times b and then subtracts c from the product.
The program should print the result.

a = int(input())
b = int(input())
c = int(input())

print((a * b) - c)

-------------------------------------------
It's time for really big numbers! Calculate the integer value of
2 ** 179 and print what you got.

print(2 ** 179)

--------------------------------------------

Write a program that takes a single integer number n and then
performs the following operations in the following order:

adds n to itself
multiplies the result by n
subtracts n from the result
exactly divides the result by n (that means, you need to carry out integer division).
Then print the result of the division. The example is given below:

8 + 8 = 16
16 * 8 = 128
128 - 8 = 120
120 // 8 = 15
The variable n is already defined => 8

n = int(input())
print((((n + n) * n) - n) // n)

-----------------------------------------------------

Write a program that prints the product
of these three numbers 1 * 2 * 3.

print(1 * 2 * 3)

------------------------------------------------------

Given a three-digit integer (i.e., an integer from 100 to 999),
find the sum of its digits and print the result.

To get the separate digits of the input integer,
make use of % and //
(for example, you can get 8 from the number 508 by taking the remainder of the division by 10).

n = int(input())
a = n // 100
b = n // 10
b %= 10
c = n % 10
print(a + b + c)

------------------------------------------------------

Any recipe starts with a list of ingredients.
Below is an extract from a cookbook with the ingredients for some dishes.
Write a program that tells you what recipe you can make
based on the ingredient you have.

The input format:

A name of some ingredient.
The output format:

A message that says "food time!"
where "food" stands for the dish that contains this ingredient.
For example, "pizza time!".
If the ingredient is featured in several recipes,
write about all of them in the order they're featured in the cook book.
pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

ingredient = input()
if ingredient in pasta:
    print("pasta time!")
if ingredient in apple_pie:
    print("apple pie time!")
if ingredient in ratatouille:
    print("ratatouille time!")
if ingredient in chocolate_cake:
    print("chocolate cake time!")
if ingredient in omelette:
    print("omelette time!")

-----------------------------------------------------

Read an integer as input and print it with the opposite sign

a = int(input())
print(-a)

-----------------------------------------------------
"""




