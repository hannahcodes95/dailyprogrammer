#create a program that will ask the users name, age, and reddit username. have it tell them the information back,
# in the format: your name is (blank), you are (blank) years old, and your username is (blank)

name,age,username = input(f"Hello, please tell me your name, age and reddit username: ").split()
print(f"your name is {name}, you are {age} years old, and your username is {username}")
