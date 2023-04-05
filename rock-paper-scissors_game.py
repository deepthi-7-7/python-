import random
def get_choices():
  players_choice=input("enter your choice:")
  options=["rock","paper","scissors"]
  computer_choice=random.choice(options)
  choices={"player":players_choice,"computer":computer_choice}
  return choices

def check_win(player,computer):
  print(f"you chose {player} and computer chose {computer}")
  if player==computer :
    return "it's a tie"
  elif player=="rock":
    if computer=="paper":
      return "paper defeats rock.you lose"
    else:
      return "rock smashes scissors.you win!"
  elif player=="paper":
    if computer=="rock":
      return "paper defeats rock.you win!"
    else:
      return "scissor cuts paper.you lose"
  elif player=="scissors":
    if computer=="rock":
      return "rock smashes scissors.you lose"
    else:
      return "scissors cuts paper.you win!"

choicey=get_choices()
result=check_win(choicey["player"],choicey["computer"])
print(result)
