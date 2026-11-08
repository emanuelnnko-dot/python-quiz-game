import random

# Create "list" called "questions" to store quiz questions
# Inside the "list", create several "dictionary" to store each question and its related multiple choices and answer
# Inside the "dictionary", make value of "choices" to be "list" for later itaration on it to print its element vertically
questions = [
    {
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

# Random rearrangement of questions inside the list
random.shuffle(questions)

score = 0
correct_answers_num = 0 # Will store number of correctly answered questions (to determine how many questions were answered correctly)

print("WELCOME TO QUIZ-GAME")
print("Game Info:")
print(" > Game will display different questions for you to answer correctly.")
print(" > You are required to choose the correct answer from question multiple choice answers.")
print(" > Make sure you enter the appropriate alphabet as your answer (either A, B, C or D).")
print()
input('Press "Enter" to start the game: ')
print()

# Create loops to iterate on "questions" and "choices" and print their associated data
for question in questions:
    while True:
        print("Question:")
        print(question["question"])

        for choice in question["choices"]:
            print(choice)

        # Store value of correct answer to be compared with user answer to determine if user answered correctly
        correct_answer = question["answer"]
        user_answer = input("Enter your answer: ").strip()
        print()
        legit_alphabet_choices = "A B C D" # Will be used to check if user answered question using unauthorized values
        # Check if user input is inappropriate e.g. empty, space or used other input values outside A, B, C or D.
        if not user_answer or user_answer.casefold() not in legit_alphabet_choices.casefold():
            # print()
            print("The question is repeted for you to answer appropriately.")
            print("Make sure you enter the respective alphabet of your correct answer (either A, B, C or D).")

            # Re-eterate within the while loop to print the question agin (when user answers question inappropriately)
            continue

        # If user answered correctly
        if user_answer.casefold() == correct_answer.casefold():
            score += 20
            correct_answers_num += 1

            print("Congratulations!, you have answered the previous question correctly.")
            print("20 points have been added to your score.")
            print()

            if correct_answers_num > 1:
                question_answered_correctly = "questions"
            else:
                question_answered_correctly = "question"
        else:
            print("Sorry, your answer on previous question is incorrect. \n")

        # Exit the while loop (when user answers appropriately) - so as to iterate inside the "for" loop (above) to display the next question
        break

print("Final Results:")
if correct_answers_num == len(questions):
    # For users who answered all questions correctly (number of correctly answered questions equal to number of all questions)
    print("Congratulations, you have done excellent. You managed to answer all questions correctly!")
    print(f"Your score is {score} points!")
elif correct_answers_num > 0 and correct_answers_num < len(questions):
    # For users who get atleast 1 question correctly and above but not all questions
    print(f"You have answered {correct_answers_num} {question_answered_correctly} correctly out of {len(questions)} questions, your final score is {score}.")
    if score >= 60 and score <= 80:
        print(f"Your score is {score}. Keep it up the good work.")
    else:
        print(f"Your score is {score}. Your score is not good, but still there is room for improvement.")
else:
    # For users who fail to answer any question
    print("Sorry, you failed to answer any question correctly.")
    print(f"Your score is {score}. You may try again.")
    