print("--------- Activity 1 ---------")
print("===============================")
print("Welcome here!")
print("My first post!")
print("===============================")

# activity 2 - update profile
print("\n--------- Activity 2 ---------")
username = "cool_creator"
bio = "Fun Blogger"
followers = 100

print("Username:", username)
print("Bio:", bio)
print("Followers:", followers)

# activity 3 - add follower growth tracker
print("\n--------- Activity 3 ---------")
followers = 100

followers += 50
print ("Day 1: ", followers)

followers += 20
print("Day 2: ", followers)

followers += 10
print("Day 3: ", followers)

# activity 4 = interactive profile creator
print("\n--------- Activity 4 ---------")
username = input("Enter Username: ")
age = input("Enter Age: ")
category = input("Enter Content Category: ")

print("\nInstagram Profile")
print("================================")
print("Username: ", username)
print("Age: ", age)
print("Content Category: ", category)

# activity 5 - added if statement
print("\n--------- Activity 5 ---------")
username = input("Enter Username: ")
age = int(input("Enter Age: "))
category = input("Enter Content Category: ")

print("\nInstagram Profile")
print("================================")
print("Username: ", username)
print("Age: ", age)
print("Content Category: ", category)

if age > 40 and category == "fun":
    print("You are old what is fun for you??")

