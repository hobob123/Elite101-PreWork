import random

def response():
  possible_responses =  ["Hi,",
                         "Coding is fun.",
                         "I like cheese"]
  return random.choice(possible_responses)

def myMood():
  possible_responses =  ["happy",
                         "angry",
                         "sad",
                         "excited",
                         "bored",
                         "irritate"]
  return random.choiced(possible_responses)

def convo():
  user_in = input("Hello! I am a chatbot. Type \"q\" to end the interaction \nHow are you?\n")
  quit_char = "q"
  print("hi")
  while (user_in != quit_char):
    user_in = input(response() + "\n")
    if(user_in.to_lowercase().contains("i feel")):
      print("Oh! I feel " + myMood())


if __name__ == "__main__":
  convo()
