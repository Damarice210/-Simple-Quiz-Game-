import time

# Questions for the quiz
questions = [
    {
        "question": "What is the keyword to define a function in Python?",
        "options": ["a) def", "b) function", "c) fun", "d) define"],
        "answer": "a"
    },
    {
        "question": "Which movie features the character Jack Sparrow?",
        "options": ["a) Pirates of the Caribbean", "b) Titanic", "c) Inception", "d) Avatar"],
        "answer": "a"
    },
    {
        "question": "What is the output of 3 ** 2 in Python?",
        "options": ["a) 6", "b) 9", "c) 8", "d) 12"],
        "answer": "b"
    },
    {
        "question": "Which movie won the Best Picture Oscar in 2020?",
        "options": ["a) 1917", "b) Joker", "c) Parasite", "d) Ford v Ferrari"],
        "answer": "c"
    },
    {
        "question": "What is the correct syntax for a comment in Python?",
        "options": ["a) //", "b) /* */", "c) <!-- -->", "d) #"],
        "answer": "d"
    }
]

def run_quiz():
    score = 0
    print("Welcome to the Quiz! 🏆\n")
    time.sleep(1)

    for i, q in enumerate(questions):
        print(f"Question {i + 1}: {q['question']}")
        for option in q["options"]:
            print(option)
        answer = input("Your answer (a/b/c/d): ").strip().lower()

        if answer == q["answer"]:
            print("Correct! 🎉\n")
            score += 1
        else:
            print(f"Oops! The correct answer was {q['answer']}. ❌\n")
        time.sleep(1)

    print(f"Quiz Over! Your final score is {score} out of {len(questions)}.")
    time.sleep(1)

    # Play again option
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        run_quiz()
    else:
        print("Thanks for playing! Goodbye! 👋")

# Start the quiz
run_quiz()
