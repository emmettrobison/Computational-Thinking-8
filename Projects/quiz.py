# This is a quiz to determine if you are a fan of Trae Young or Jalen Johnson.

# Beginning: Create variables
jalen_johnson = 0
trae_young = 0


# Middle: Ask questions
# Question 1
answer = input("Do you prefer watching A) guards or B) forwards? ")
if answer.lower() == "a":
    trae_young += 1
elif answer.lower() == "b":
    jalen_johnson += 1
else:
    print("Invalid answer. Please enter A or B.")
    # Re-ask the question
    answer = input("Do you prefer watching A) guards or B) forwards? ")
    if answer.lower() == "a":
        trae_young += 1
    elif answer.lower() == "b":
        jalen_johnson += 1


# Question 2
answer = input("Do you prefer watching A) players who finish by using floaters and fakes or B) players who finish by dunking? ")
if answer.lower() == "a":
    trae_young += 1
elif answer.lower() == "b":
    jalen_johnson += 1
else:
    print("Invalid answer. Please enter A or B.")
    # Re-ask the question
    answer = input("Do you prefer watching A) players who finish by using floaters and fakes or B) players who finish by dunking? ")
    if answer.lower() == "a":
        trae_young += 1
    elif answer.lower() == "b":
        jalen_johnson += 1


# Question 3
answer = input("Do you prefer watching A) players who mostly shoot from deep or B) players who mostly shoot from close to the rim? ")
if answer.lower() == "a":
    trae_young += 1
elif answer.lower() == "b":
    jalen_johnson += 1
else:
    print("Invalid answer. Please enter A or B.")
    # Re-ask the question
    answer = input("Do you prefer watching A) players who mostly shoot from deep or B) players who mostly shoot from close to the rim? ")
    if answer.lower() == "a":
        trae_young += 1
    elif answer.lower() == "b":
        jalen_johnson += 1


# Question 4
answer = input("Do you prefer watching A) players who are quick and agile or B) players who are strong and powerful? ")
if answer.lower() == "a":
    trae_young += 1
elif answer.lower() == "b":
    jalen_johnson += 1 
else:
    print("Invalid answer. Please enter A or B.")
    # Re-ask the question
    answer = input("Do you prefer watching A) players who are quick and agile or B) players who are strong and powerful? ")
    if answer.lower() == "a":
        trae_young += 1
    elif answer.lower() == "b":
        jalen_johnson += 1


# Question 5
answer = input("Do you prefer watching A) players who are flashy and showy or B) players who are more reserved? ")
if answer.lower() == "a":
    trae_young += 1
elif answer.lower() == "b":
    jalen_johnson += 1
else:
    print("Invalid answer. Please enter A or B.")
    # Re-ask the question
    answer = input("Do you prefer watching A) players who are flashy and showy or B) players who are more reserved? ")
    if answer.lower() == "a":
        trae_young += 1
    elif answer.lower() == "b":
        jalen_johnson += 1


# End: Determine final results
if trae_young > jalen_johnson:
    print("You are a Trae Young fan!")
elif jalen_johnson > trae_young:
    print("You are a Jalen Johnson fan!")

# The quiz is over, and the results are printed based on the user's answers.