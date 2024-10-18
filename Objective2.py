# Double Scoop with Nested Loops

# Task 1: Your Mood Tracker Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) for each day of the week. Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over the times of the day. For each time, randomly select a mood from a predefined list and print it. Use the random module again to randomly select the mood.

# Build the outer loop for the days, and the inner loop for the time.

# 1. Create a list of moods, days, and times
# 2. Build the if loop iterating over days
# 3. Build the nested loop
# 4. Print Statment

#Wow, I tred to run this code for an absurd amount of time before realizing I failed to import the random module. Teehee!

import random

# I'll just grab the lists from the last objective
mood_list = ["Happy", "Sad", "Energetic", "Spooky"]

day_list = ["Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

time_list = ["morning", "afternoon", "evening"]

for day in range(6):
    curr_day = day_list[day] #calling this as an indexed list later didnt work so ill just create a variable that changes every time the day iterates
    for time in range(3): #IDK why this doesnt work when I set the range to 2, but, it works when I put 3! :/
        curr_mood = random.choice(mood_list)
        curr_time = time_list[time]
        print(f"On {curr_day} {curr_time} you were {curr_mood}.")