import random

def utility_function(user, agent):
    if (user == 'scissors' and agent == 'rock') \
            or (user == 'paper' and agent == 'scissors') \
            or (user == 'rock' and agent == 'paper'):
        return 1
    elif user ==  agent:
        return -1
    else:
        return 0

def Internal_memory(user, choices):
    if user == 'paper':
        return choices.append('scissors')
    elif user == 'rock':
        return choices.append('paper')
    else:
        return choices.append('rock')

agent_choices = ["rock", "paper", "scissors"]
target = int(input("Enter the winning score: "))
user_score, agent_score = 0, 0
while user_score != target and agent_score != target:
    user_choice = input("Enter your choice (rock/paper/scissors): ")
    agent_choice = random.choice(agent_choices)
    print(f"Agent chose {agent_choice}")
    if utility_function(user_choice, agent_choice) == 1:
        agent_score += 1
    elif utility_function(user_choice, agent_choice) == 0:
        user_score += 1
    Internal_memory(user_choice,agent_choices)
    print('user score = ', user_score, ', agent score = ', agent_score)

if agent_score == target:
    print("Winer is agent :)")
else:
    print("User is winer :(")
print('The final agent choices based update with internal memory is ', agent_choices)
