# Objective 1

# Task 1: The Range Riddle

# Task 1: Your Mood Today Write a program that prints off different moods for each day of the week. Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm". Using the range() function, loop through every day of the week and for each day, randomly select a mood from the list and print it. Ensure that your program includes the use of the random module to select the mood.

import random

mood_list = ["Happy", "Sad", "Energetic", "Spooky"]

day_list = ["Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for i in range(6):
    curr_mood = random.choice(mood_list)
    print(f"On {day_list[i]}, you were feeling {curr_mood}")
