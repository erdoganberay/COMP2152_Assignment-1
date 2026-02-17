"""
Author: Beray Erdogan>
Assignment: #1
"""

# Step b: Create 4 variables
gym_member = "Alex Alliton" #type string
preferred_weight_kg = 20.5 #type float
highest_reps = 25 #type integer
membership_active = True #type boolean

# Step c: Create a dictionary named workout_stats

#type dict  (yoga,running,weightlifting) 
workout_stats = {
        "Berhan": (30,45,20),
        "Beray": (60,61,62),
        "Gonzalo": (53,8,61)
        }


# Step d: Calculate total workout minutes using a loop and add to dictionary
# calculate total workout minutes
workout_stats.update({
    key + "_Total": sum(value) 
    for key, value in workout_stats.items()
    })


# Step e: Create a 2D nested list called workout_list
# filter workout minutes for every person (type list)
workout_list = [
        [key,value[0],value[1],value[2]] 
        for key,value in workout_stats.items()
        if "_" not in key
        ]



# Step f: Slice the workout_list
#filter yoga minutes for every person
yoga = [
        workout[0:2] 
        for workout in workout_list
        ]

#filter running minutes for every person
running = [
        workout[0:3:2]
        for workout in workout_list
        ]

#filter weightlifting minutes for last 2 person on the list
weightlifting = [
        workout[0::3] 
        for workout in workout_list[1:]
        ]

#print workout values
print(f"\n{'Yoga':^31}")
print("======================================")
for workout in yoga:
    print(f"{workout[0]:5}: worked yoga for {workout[1]} min.")


print(f"\n{'Running':^31}")
print("======================================")
for workout in running:
    print(f"{workout[0]:5}: worked running for {workout[1]} min.")


print(f"\n{'Weightlifting':^31}")
print("======================================")
for workout in weightlifting:
    print(f"{workout[0]:5}: worked weightlifting for {workout[1]} min.")


# Step g: Check if any friend's total >= 120

substring = "_"
print(f"\n{'Most Active Users':^31}")
for person, minutes in workout_stats.items():
    if "_" in person:
        if minutes > 120:
            person = person.split(substring)[0]
            print (f"Great job staying active, {person}!")

# Step i: Friend with highest and lowest total workout minutes
total_work_minutes = {
            person.split("_")[0] : total
            for person, total in workout_stats.items()
            if "_" in person
        }
min_person = min(total_work_minutes.items(), key=lambda x: x[1])
max_person = max(total_work_minutes.items(), key=lambda x: x[1])

print(f"The top worker by {max_person[1]} minutes: {max_person[0]}")  
print(f"The least worker by {min_person[1]} minutes: {min_person[0]}")

            

# Step h: User input to look up a friend
user_query = input("\nPlease enter the name for query: ")
user_query = user_query.strip().capitalize()
if user_query in workout_stats.keys():
    print(f"\n{user_query}:")
    print(f"Yoga: {workout_stats[user_query][0]}min")
    print(f"Running {workout_stats[user_query][1]}min")
    print(f"Weightlifting: {workout_stats[user_query][2]}min")
    print(f"Total: {workout_stats[user_query][0] + workout_stats[user_query][1] + workout_stats[user_query][2]}min")
else:
    print(f"Friend {user_query} not found in the records")

       

