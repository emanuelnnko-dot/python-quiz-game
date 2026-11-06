import random

# Variable to store question ID for later comparison of asked question vs its correct answer
# latest_asked_question_id = None

# Create questions list to store quiz questions - each question will be dictionary inside the list
questions = [
    {
        # "question_id": 1,
        "question": "In which country is mount Kilimanjaro located?",
        "choices": ["A. Uganda", "B. Kenya", "C. Tanzania", "D. Rwanda"],
        "answer": "C"
    },
    {
        "question": "In which country is Masai-mara park located?",
        "choices": ["A. Tanzania", "B. Uganda", "C. Rwanda", "D. Kenya"],
        "answer": "D"
    },
    {
        "question": "Which countries share lake Victoria?",
        "choices": ["A. Tanzania, Uganda and Kenya", "B. Uganda, Kenya and South Sudan", "C. Rwanda, Burundi and DRC", "D. Tanzania, DRC and Burundi"],
        "answer": "A"
    },
    {
        "question": "What is the capital city of DR-Congo?",
        "choices": ["A. Lubumbashi", "B. Brazzaville", "C. Kinshasa", "D. Bukavu"],
        "answer": "C"
    },
    {
        "question": "What is the capital city of Rwanda?",
        "choices": ["A. Bujumbura", "B. Kigali", "C. Entebe", "D. Goma"],
        "answer": "B"
    }
]

# print(questions)
random.shuffle(questions)

score = 0
correct_answers_num = 0
# Create loops to iterate on questions and choices
for question in questions:
    print(question["question"])
    for choice in question["choices"]:
        print(choice)
    correct_answer = question["answer"]
    user_answer = input("Enter your answer: ").strip()
    print()
    if user_answer.casefold() == correct_answer.casefold():
        score += 20
        correct_answers_num += 1
        if correct_answers_num > 1:
            question_answered_correctly = "questions"
        else:
            question_answered_correctly = "question"

if correct_answers_num == len(questions):
    print("Congratulations, you have done excellent. You managed to answer all questions correctly!.")
    print(f"Your score is {score} points!")
elif correct_answers_num > 0 and correct_answers_num < len(questions):
    print(f"You have answered {correct_answers_num} {question_answered_correctly} correctly out of {len(questions)} questions, your final score is {score}")
    if score >= 60 and score <= 80:
        print(f"Your score is {score}. Keep it up the good work")
    else:
        print(f"Your score is {score}. Your score is not good, but still there is room for improvement.")
else:
    print("Sorry, you failed to answer any question correctly.")
    print(f"Your score is {score}. You may try again")
    