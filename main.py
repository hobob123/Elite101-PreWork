import random

def response():
  possible_responses =  ["hi",
                         "coding is fun",
                         "I like cheese"]
  return random.choice(possible_responses)


def convo():
  user_in = input("Hello! I am a chatbot. Type \"q\" to end the interaction \nHow are you?\n")
  quit_char = "q"
  
  while (user_in != quit_char):
    print("hi")


if __name__ == "__main__":
  convo()
