
def ask():
    print("what is your question?")
    que = input()
    return que


def check_question(input):
    size = len(input)
    print(size)
    if input[size-1] == '?':
        return True
    else:
        print("I’m sorry, I can only answer questions")
        return False


def main():
    question = ""
    while question != "quit":
        question = ask()
        is_question = check_question(question)


main()
