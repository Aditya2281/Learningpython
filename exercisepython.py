name = "Aditya"
age = 24
height = 1.75  # in meters
is_student = False

print(name)
print(age)
print(height)
print(is_student)

# ✅ Task 1: Create variables for your city (string), number of kids (int), and has_pet (boolean)
city = 'Vancouver'
hobby = 'reading books'
car = False

print(city)
print(hobby)
print(car)

# ▶️ 2. Reassigning Variables
age = 24 #happy birthday!
print("\nNew age after birthday:", age)

# ✅ Task 2: Change the value of your city variable to another city and print it
city = "Toronto"
print("New city:", city)


# ▶️ 3. Using Variables in Expressions
year_born = 2025 - age
print("\nYear born:", year_born)

##4. Data Types Check
print("\nType of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of is_student:", type(is_student))

# ▶️ 5. String Concatenation Using Variables
greeting = 'hello, my name is' + name + " and I live in " + city + "."
print("\n" + greeting)

# ✅ Task 5: Create a sentence introducing yourself using your variables and print it


my_intro = f"My name is {name}, I am {age} years old, and I live in {city}."
print(my_intro)
