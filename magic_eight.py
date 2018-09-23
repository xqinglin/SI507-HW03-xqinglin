from random import randint

def ask():
    print("what is your question?")
    que = input()
    return que
def pick_an_answer():
    answer_list = []
    answer_list.append("It is certain.")
    answer_list.append("It is decidedly so.")
    answer_list.append("Without a doubt.")
    answer_list.append("Yes - definitely.")
    answer_list.append("You may rely on it.")
    answer_list.append("As I see it, yes.")
    answer_list.append("Most likely.")
    answer_list.append("Outlook good.")
    answer_list.append("Yes.")
    answer_list.append("Signs point to yes.")
    answer_list.append("Reply hazy, try again")
    answer_list.append("Ask again later.")
    answer_list.append("Better not tell you now.")
    answer_list.append("Cannot predict now.")
    answer_list.append("Concentrate and ask again.")
    answer_list.append("Don't count on it.")
    answer_list.append("My reply is no.")
    answer_list.append("My sources say no.")
    answer_list.append("Outlook not so good.")
    answer_list.append("Very doubtful.")
    return answer_list[randint(0, 19)]
answer = pick_an_answer()
question = ask()

<<<<<<< HEAD
=======
name = ask();
def check_question(input){

}
>>>>>>> check_question
