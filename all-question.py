"""
1. Simple Message
Task: Assign a message to a variable and then print that message.
"""
message:str = ('kia haal ha')
print(message)


"""
2. Simple Messages
Task:
● Assign a message to a variable and print that message.
● Change the value of the variable to a new message, and print the new message.
"""
message:str = 'who are you'
print(message)
message = 'i am ali raza'
print(message)

"""
3. Personal Message
Task:
● Use a variable to represent a person’s name.
● Print a message to that person, such as, “Hello Eric, would you like to learn some
Python today?”
"""
person_name:str = "sir irfan malik"
print(f'kia haal ha {person_name} ap ka')

"""
4. Name Cases
Task:
● Use a variable to represent a person’s name.
● Print the person’s name in lowercase, uppercase, and title case.
"""
person_name:str = 'irfan malik'
print(person_name.title())
print(person_name.upper())
print(person_name.lower())

"""
5. Famous Quote
Task:
● Find a quote from a famous person you admire.
● Print the quote and the name of its author.
"""
quote:str = "\"When you stop learning, you stop growing.\""
writer_name: str = '— Eleanor Roosevelt'
print(f'once {writer_name} said: {quote}')

"""
6. Famous Quote 2
Task:
● Use a variable called famous_person to represent the famous person’s name.
● Compose the message and represent it with a variable called message.
● Print the message.
"""
famous_person:str = 'irfan malik'
message:str  = 'can you will meet with me'
print(f'sir {famous_person} {message}')


"""
7. Stripping Names
Task:
● Use a variable to represent a person’s name, and include some whitespace characters
at the beginning and end of the name.
● Make sure you use each character combination, \t and \n, at least once.
● Print the name once, so the whitespace around the name is displayed.
● Print the name using each of the three stripping functions: lstrip(), rstrip(), and
strip().
"""
person_name:str = "\t\n    muhammad ali jinnah   \t\n"
print(person_name)
print(person_name.strip())
print(person_name.lstrip())
print(person_name.rstrip())

"""
8. Variable Sum
Task: Assign the values 5, 10, and 15 to three variables x, y, and z. Print their sum.
"""
x:int = 5
y:int = 6
z:int = 7
print(x+y+z) 

"""
9. Variable Swap
Task: Swap the values of two variables a and b. Print the values before and after the swap.
"""
a:int = 5
b:int = 9
print(f'value of a before swaping is {a} and the value of b is {b}')
temp = a
a=b
b=temp 
print(f'value of a before swaping is {a} and the value of b is {b}')


"""
10. Favorite Color
Task: Create a variable with your favorite color and print it. Then change the variable name to
something else and print the color again.
"""
favorite_color:str = 'red'
print(favorite_color)
#change the variable name 
color:str = 'red'
print(color)


"""
11. Changing Pet Name
Task: Create a variable pet_name and set it to "Buddy". Change the value of pet_name to
"Max" and print the new value.
"""
pet_name:str = 'Buddy'
print(f"pet name {pet_name}")
pet_name:str = 'Max'
print(f"new pet name {pet_name}")

"""
12. Observing Name Error
Task: Assign the value "Sunshine" to a variable and print it. Then, mistakenly try to print a
variable with a different name (like sunsine) and observe the error.
"""
sunshine:str = 'ali'
# print(Sunshine) //error

"""
13. Reassigning Score
Task: Assign the value 100 to a variable score and print it. Then assign a new value to score
and print it again.
"""
int = 20
print(int)
int = 100 
print(int)


"""
14. City Name
Task: Create a string variable city and assign it the name of a city you like. Print the city
name.
"""
city_name:str = "lhr"
print(f'i live in {city_name}')


"""
15. Title Case Text
Task: Create a variable text with the value "python programming" and print it in title case.
"""
variable:str = 'ali raza'
print(variable.title())


"""
16. Lowercase Conversion
Task: Assign a string with mixed cases to a variable and print it in all lowercase letters.
"""
variable:str = 'KIA HAAL A'
print(variable.lower())


"""
17. Uppercase Conversion
Task: Assign a string with mixed cases to a variable and print it in all uppercase letters.
"""
variable:str = 'kia haal a'
print(variable.upper())


"""
18. Current Temperature
Task: Create a variable temperature with the value 25. Print "The current temperature is
[temperature] degrees." using the variable.
"""
temperature:int = '20'
print(f'lahore temperature is {temperature} degree')


"""
19. Printing a Poem
Task: Create a variable poem with a short poem that has multiple lines. Print the poem with
each line starting on a new line.
"""
poem:str = 'In a world so vast and wide,\nWe find our dreams, our hearts abide.\nThrough joy and sorrow, we will stride,\nWith hope and love, our constant guide.\n'
print(poem) 