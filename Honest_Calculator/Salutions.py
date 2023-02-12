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
-----------------------------------------------------

Write a program that reads two integer numbers
from user and then prints their difference.
Don't specify any message when reading the input, please.

a = int(input())
b = int(input())

print(a - b)

-----------------------------------------------------

Write a program that takes 3 integer numbers a, b and c,
calculates a times b and then subtracts c from the product.
The program should print the result.

a = int(input())
b = int(input())
c = int(input())

print((a * b) - c)

-----------------------------------------------------
It's time for really big numbers! Calculate the integer value of
2 ** 179 and print what you got.

print(2 ** 179)

-----------------------------------------------------

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
Read three angles given on separate input lines and check
whether they form a triangle.
Print the answer in the following format:
"The triangle is valid!" or "The triangle is not valid!".

a = int(input())
b = int(input())
c = int(input())

if (a + b + c) == 180:
    print("The triangle is valid!")
else:
    print("The triangle is not valid!")

-----------------------------------------------------

Whoa! This problem requires knowledge of list collection type. If you're feeling up to the challenge, brace yourself,
and good luck! Otherwise, you can skip it for now and return any time later.
Write a simple spellchecker that tells you if the word is spelled correctly.
Use the dictionary in the code below: it contains the list of all correctly written words.

The input format:

A single line with the "word".

The output format:

If the word is spelled correctly write Correct, otherwise, Incorrect.

dictionary = ["aa", "abab", "aac", "ba", "bac", "baba", "cac", "caac"]
word = input()

if word in dictionary:
    print("Correct")
else:
    print("Incorrect")

-----------------------------------------------------

When a bank has financial problems the government can return
a client's deposit if it is less than 700,000.
The interest rate for a particular deposit is 7.1% a year.
The percentages are paid to the same deposit at the end of the year
and a new value of the interest is calculated.

Find out how many years it will take for the sum of the deposit
to exceed the value protected by the government.

The input format:
The initial sum of the deposit.
It is guaranteed that the value will be between 50,000 and 700,000.
The output format:
The number of years.

years = 0
amount = int(input())
target = 700_000
year_interest = 1.071
while amount < target:
    years += 1
    amount *= year_interest

print(years)

------------------------------------------------------

Kitty wants to visit a cat café! Help her find the one with
the largest number of cats.
It is guaranteed that all cafés have a different number of cats.

Input format

Each string contains a café's name followed by a space and the number of cats in it,
e.g. Paws 11, Kittens 9.

The names would be one-word only. Read input lines until you get
a string MEOW (without any number).

Output format

The café with the maximum number of cats.

name = ""
max_count = 0
while True:
    command = input()
    if command == "MEOW":
        break
    info = command.split()
    cafe_name = info[0]
    cat_count = int(info[1])
    if cat_count > max_count:
        max_count = cat_count
        name = cafe_name

print(name)

-----------------------------------------------------
Write a program that will print the following multi-line string:

' '' '''
' '' '''
' '' '''

print("""
' '' '''
' '' '''
' '' '''
""")
"""





