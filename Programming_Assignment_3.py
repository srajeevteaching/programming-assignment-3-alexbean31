# Programmer: Alex Bean
# Course: CS151, Dr. Rajeev
# Programming Assignment: 3
# Program Inputs: The desired sport and the stats that are associated with it.
# Program Outputs: The quarterback passing rating, the gymnast score including the highest and lowest execution scores, and/or the quidditch score.

# Begin by defining the inputs for football
def football_input():
    number_of_completions = input("How many completions were there? ")
    if not (number_of_completions.isdigit()):
        print("This is not a valid input.")
        number_of_completions = 0
    else:
        number_of_completions = float(number_of_completions)
    number_of_attempts = input("How many attempts were there? ")
    if not (number_of_attempts.isdigit()):
        print("This is not a valid input.")
    elif number_of_attempts == 0:
        print("This is not a valid input.")
    else:
        number_of_attempts = float(number_of_attempts)
    passing_yards = input("How many passing yards were there? ")
    if not (passing_yards.isdigit()):
        print("This is not a valid input.")
        passing_yards = 0
    else:
        passing_yards = float(passing_yards)
    touchdown_passes = input("How many touchdown passes were thrown? ")
    if not (touchdown_passes.isdigit()):
        print("This is not a valid input.")
        touchdown_passes = 0
    else:
        touchdown_passes = float(touchdown_passes)
    number_of_interceptions = input("How many interceptions were thrown? ")
    if not (number_of_interceptions.isdigit()):
        print("This is not a valid input.")
        number_of_interceptions = 0
    else:
        number_of_interceptions = float(number_of_interceptions)
#Return these stats
    return number_of_completions, number_of_attempts, passing_yards, touchdown_passes, number_of_interceptions

# Then define the inputs for quidditch
def qudditch_input():
    goals_scored = input("How many goals were scored? ")
    if not(goals_scored.isdigit()):
        print("This is not a valid input.")
        goals_scored = 0
    goals_scored = int(goals_scored)
    caught_the_snitch = input("Was the snitch caught? ")
    caught_the_snitch = caught_the_snitch.strip().lower()
# Recognize if the user does not answer with yes or no
    if not(caught_the_snitch == "yes" or caught_the_snitch == "no"):
        print("This is not a valid input.")
#Return goals and if snitch was caught
    return goals_scored, caught_the_snitch

# Then define the inputs for gymnastics
def gymnastics_input():
    execution_difficulty = input("What is the difficulty score (from 0 to 10)? ")
    if not(execution_difficulty.isdigit()):
        print("This is not a valid input.")
        execution_difficulty = 0
    else:
        execution_difficulty = float(execution_difficulty)
        if not(0 <= execution_difficulty <= 10):
            print("This is not a valid input.")
    first_execution = input("What is the first execution score (from 0 to 10)? ")
    if not(first_execution.isdigit()):
        print("This is not a valid input.")
        first_execution = 0
    else:
        first_execution = float(first_execution)
        if not(0 <= first_execution <= 10):
            print("This is not a valid input.")
    second_execution = input("What is the second execution score (from 0 to 10)? ")
    if not(second_execution.isdigit()):
        print("This is not a valid input.")
        second_execution = 0
    else:
        second_execution = float(second_execution)
        if not(0 <= second_execution <= 10):
            print("This is not a valid input.")
    third_execution = input("What is the third execution score (from 0 to 10)? ")
    if not(third_execution.isdigit()):
        print("This is not a valid input.")
        third_execution = 0
    else:
        third_execution = float(third_execution)
        if not(0 <= third_execution <= 10):
            print("This is not a valid input.")
    fourth_execution = input("What is the fourth execution score (from 0 to 10)? ")
    if not(fourth_execution.isdigit()):
        print("This is not a valid input.")
        fourth_execution = 0
    else:
        fourth_execution = float(fourth_execution)
        if not(0 <= fourth_execution <= 10):
            print("This is not a valid input.")
    fifth_execution = input("What is the fifth execution score (from 0 to 10)? ")
    if not(fifth_execution.isdigit()):
        print("This is not a valid input.")
        fifth_execution = 0
    else:
        fifth_execution = float(fifth_execution)
        if not(0 <= fifth_execution <= 10):
            print("This is not a valid input.")
#Return scores
    return execution_difficulty, first_execution, second_execution, third_execution, fourth_execution, fifth_execution

#Create function for calculating quaterback rating
def football_calculation(number_of_completions,number_of_attempts,passing_yards,number_of_interceptions,touchdown_passes):
    quarterback_rating= 100 * ((5 * ((number_of_completions/number_of_attempts) - 0.3)+(0.25 * ((passing_yards/number_of_attempts) - 3))+(20 * (touchdown_passes/number_of_attempts))+(2.375-(25*number_of_interceptions/number_of_attempts)))/6)
    print("Your quarterback rating is: ", quarterback_rating)
# Tell user that they have a perfect QB rating if it is 158.3
    if quarterback_rating == 158.3:
        print("Wow, this is perfect passing rating!")

#Create function for calculating quidditch score
def quidditch_calculation(goals_scored, caught_the_snitch):
    if caught_the_snitch == "yes":
        snitch = 30
    else:
        snitch = 0
#Calculate score
    quidditch_score = (10 * goals_scored) + snitch
#Print snitch score
    print("The quidditch score total is: ", quidditch_score)

#Create function calculating gymnastics score
def gymnastics_calculation(difficulty, first_execution, second_execution, third_execution, fourth_execution, fifth_execution):
    lowest_score = min(first_execution, second_execution, third_execution, fourth_execution, fifth_execution)
    highest_score = max(first_execution, second_execution, third_execution, fourth_execution, fifth_execution)
#Gymnastics score is equal to the middle three execution scores divided by 3 plus difficulty score
    gymnast_score = (first_execution + second_execution + third_execution + fourth_execution + fifth_execution - lowest_score - highest_score)/(3+difficulty)
#Print gymnastics score and the minimum and maximum execution scores
    print("The gymnastics score is:", gymnast_score)
    print("The lowest execution score was", lowest_score, "and the highest execution score was", highest_score)

#Create main function
def main():
    #Ask what sport they want
    chosen_sport = input("Please choose the sport you want to know the statistics of: football, gymnastics, or quidditch.")
    chosen_sport = chosen_sport.strip().lower()
#Make sure that the code recognizes that the user input a plausible option
    while chosen_sport != "football" and chosen_sport != "gymnastics" and chosen_sport != "quidditch":
        print("This is not a valid input.")
        chosen_sport = input("Please choose the sport you want to know the statistics of: football, gymnastics, or quidditch.")
        chosen_sport = chosen_sport.strip().lower()
#If user chooses football, call football function
    if chosen_sport == "football":
        number_of_completions, number_of_attempts, passing_yards, touchdown_passes, number_of_interceptions = football_input()
        football_calculation(number_of_completions, number_of_attempts, passing_yards, number_of_interceptions, touchdown_passes)
#If user chooses quidditch, call quidditch function
    elif chosen_sport == "quidditch":
        goals_scored, caught_the_snitch = qudditch_input()
        quidditch_calculation(goals_scored, caught_the_snitch)

#If user chooses gymnastics, call gymnastics function
    elif chosen_sport =="gymnastics":
        execution_difficulty, first_execution, second_execution, third_execution, fourth_execution, fifth_execution = gymnastics_input()
        gymnastics_calculation(execution_difficulty, first_execution, second_execution, third_execution, fourth_execution, fifth_execution)

main()