questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A. Harper Lee", "B. J.K. Rowling", "C. George Orwell", "D. Mark Twain"],
        "answer": "A"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Michelangelo"],
        "answer": "C"
    }
]
def run_quiz(questions):
    score = 0

    for i, question in enumerate(questions):
        print(f"\nQuestion {i+1}: {question['question']}")
        for option in question['options']:
            print(option)

        answer = input("Enter your answer (A, B, C, or D): ").upper()

        if answer == question['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}.")

    print(f"\nYou scored {score} out of {len(questions)}.")

if __name__ == "__main__":
    run_quiz(questions)
