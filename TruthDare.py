from random import randint

#name of players
name = ["Mac","Joe","Tim","Bill"]

#number of players
number = len(name)

#person asking
question = name[randint(0,number-1)]

#person answering
answer = name[randint(0,number-1)]

#print
print("Question : ",question)
print("Answer : ",answer)
