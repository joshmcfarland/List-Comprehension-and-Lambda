# numbers 0-9
x = [i for i in range(10)]
print(x)


# adding an expression - square of each number
squares = [i**2 for i in range(10)]
print(squares)


# multiply each element by 3
list1 = [3, 4, 5]
multiplied = [item * 3 for item in list1]
print(multiplied)


# word manipulation
listOfWords = ["this", "is", "a", "list", "of", "words"]
firstLetter = [word[0] for word in listOfWords]
print(firstLetter)


list2 = ["A", "B", "C"]
lowercase = [x.lower() for x in list2]
print(lowercase)


# adding in an IF condition
# all even numbers from 0-4 (squared)
new_range = [i * i for i in range(5) if i % 2 == 0]
print(new_range)

string = "Hello 12345 World"
letters = [x for x in string if x.isalpha()]
numbers = [x for x in string if x.isdigit()]
print(letters)
print(numbers)


# using a file
myfile = open("test.txt", "r")
result = [i.rstrip("\n") for i in myfile if "line3" in i]
print(result)


# using functions
def double(x):
    return x * 2


print(double(10))

mynumbers = [double(x) for x in range(10)]
print(mynumbers)

# for even numbers only
myevennumbers = [double(x) for x in range(10) if x % 2 == 0]
print(myevennumbers)


# you can add more arguments
result = [x + y for x in [10, 30, 50] for y in [20, 40, 60]]
print(result)
