import random

def response():
  possible_responses =  ["Hi!",
                         "Coding is fun.",
                         "I like cheese"]
  return random.choice(possible_responses)

def myMood():
  possible_responses =  ["happy",
                         "angry",
                         "sad",
                         "excited",
                         "bored",
                         "irritated"]
  return random.choice(possible_responses)

def convo():
  user_in = input("Hello! I am a chatbot. Type \"q\" to end the interaction \nHow are you?\n")
  quit_char = "q"
  
  while (user_in != quit_char):
    if("i feel" in user_in.lower()):
      print("Oh! I feel " + myMood())
    else:
      user_in = input(response() + "\n")

if __name__ == "__main__":
  convo()
