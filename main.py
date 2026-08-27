import random

print("===================================")
print("       🎯 QUIZ GENERATOR")
print("===================================")

questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["A. Lahore", "B. Islamabad", "C. Karachi", "D. Peshawar"],
        "answer": "B"
    },
    {
        "question": "Which language are we using to build this quiz?",
        "options": ["A. Java", "B. C++", "C. Python", "D. HTML"],
        "answer": "C"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Processing Unit",
            "B. Computer Personal Unit",
            "C. Central Program Utility",
            "D. Computer Processing User"
        ],
        "answer": "A"
    },
    {
        "question": "Which data type is used to store True or False?",
        "options": ["A. String", "B. Integer", "C. Boolean", "D. Float"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used to start a comment in Python?",
        "options": ["A. //", "B. #", "C. <!--", "D. **"],
        "answer": "B"
    }
]

random.shuffle(questions)

score = 0

for number, question_data in enumerate(questions, start=1):

    print(f"\nQuestion {number}: {question_data['question']}")

    for option in question_data["options"]:
        print(option)

    user_answer = input("Your answer (A/B/C/D): ").upper()

    if user_answer == question_data["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer was {question_data['answer']}.")

print("\n===================================")
print("             QUIZ OVER")
print("===================================")

print(f"You scored {score} out of {len(questions)}.")

percentage = (score / len(questions)) * 100

print(f"Your percentage: {percentage:.1f}%")

if percentage == 100:
    print("🏆 Perfect score! Amazing!")
elif percentage >= 80:
    print("🌟 Excellent work!")
elif percentage >= 60:
    print("👍 Good job! Keep practicing.")
elif percentage >= 40:
    print("📚 Not bad, but you can improve.")
else:
    print("💪 Keep learning and try again!")

print("===================================")