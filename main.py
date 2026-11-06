import random

# Create questions list to store quiz questions - each question will be dictionary inside the list
question = [
    {
        "question": "In which country is mount Kilimanjaro located?",
        "choices": ["A. Uganda", "B. Kenya", "C. Tanzania", "D. Rwanda"],
        "answer": "C"
    },
    {
        "question": "In which country is Masai-mara park located?",
        "choices": ["A. Tanzania", "B. Uganda", "C. Rwanda", "D. Kenya"],
        "answer": "D"
    }
]

print(question)
random.shuffle(question)

print(question)