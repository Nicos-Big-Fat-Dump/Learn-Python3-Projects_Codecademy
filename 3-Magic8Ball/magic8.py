import random

name = input("What is your name? ")
question = input("Now ask me a question. ")
answer = ''
randomNum = random.randint(1,9)

s1 = "Yes - definitely"
s2 = "It is decidedly so"
s3 = "Without a doubt"
s4 = "Reply hazy, try again"
s5 = "Ask again later"
s6 = "Better not tell you now"
s7 = "My sources say no"
s8 = "Outlook not so good"
s9 = "Very doubtful"

gospel = [s1,s2,s3,s4,s5,s6,s7,s8,s9]

if not (randomNum >= 10 or randomNum <= 0):
  answer = gospel[randomNum-1]
  print(answer)
else:
  print("Error")
