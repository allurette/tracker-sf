#User inputs, basic information
name = input("What is your name? ") 
age = int(input("How old are you? "))
current_day = int(input("What is your current cycle day? "))
if age <= 38: #default means standard cycle days
    default = 28
else: 
    default = 26

#Ask for user's cycle history list
cycle_history = []
print("Enter your past cycle lengths, type done when finished, or unsure of your cycle.")
while True:
    user_input = input("Enter cycle length: ")
    if user_input.lower() == "done":
        break
    cycle_length = int(user_input)
    cycle_history.append(cycle_length)

#Calculate the average cycle days based on user's input
if cycle_history:
    cycle_avg = sum(cycle_history)/ len(cycle_history)
else:
    cycle_avg = default
    
print(cycle_avg)

#random mssg
import random
menstrual = [
    "Embrace your womanly body",
    "It is so lady-like to shed",
    "Leaders bleed."
]
 
follicular = ["It's a new beginning",
              "You are a ball of energy",
              "The rainbow after rain"
    ]
    
ovulation = ["You are the source of abundance",
             "You are the sweetest nectar"
             "Your feminity is thriving"
    ]
    
luteal = ["Trust your intuition",
          "Your resolve is firm",
          "Have faith in yourself"
          
    ]

#print the mssg depends on cycle 
if current_day <= 5:
    print("You are now bleeding! cycle day: " + current_day)
    daily_mssg = random.choice(menstrual)
elif current_day <= 12:
    print("You are now in follicular phase! cycle day: " + current_day)
    daily_mssg = random.choice(follicular)
elif current_day <= 17:
    print("You are now ovulating! cycle day: " + current_day)
    daily_mssg = random.choice(ovulation)
else: 
    daily_mssg = random.choice(luteal)