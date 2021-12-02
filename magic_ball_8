import random

def magic_ball():

    afirmative = [ "It is certain.", "It is decidedly so.", "Without a doubt.", "Yes definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes." ]
    non_commitial = ["Reply hazy, try again.", "Ask again later.","Better not tell you now.", "Cannot predict now.", "Concentrate and ask again"]
    negative = ["Don't count on it.","My reply is no.", "My sources say no.", "Outlook not so good." ,"Very doubtful."]

    mass_random = random.randint(1, 3)
    if mass_random == 1:
        answr_random = random.randint(0, len(afirmative))
        print(afirmative[answr_random])
    elif mass_random == 2:
        answr_random = random.randint(0, len(non_commitial))
        print(non_commitial[answr_random])
    elif mass_random == 3:
        answr_random = random.randint(0, len(negative))
        print(negative[answr_random])
    
    print("You have another question? - y = yes, n = no - ")
    s = input().lower()
    if s == "y":
        print("Ask your question my dear friend : ")
        answer = input()
        magic_ball()
    else:
        print("Okay. I have an insult to you ... :(")


print("Ask your question my dear friend : ")
answer = input()
magic_ball()

