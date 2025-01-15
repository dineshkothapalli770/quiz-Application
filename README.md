Quiz Application
This is a simple quiz application written in Python. The application presents a series of questions with multiple choice answers, and the user inputs their answer for each question. The application then provides feedback on whether the answer was correct and displays the final score at the end.

Features
Multiple choice questions
User input for answers
Feedback on correct and incorrect answers
Displays final score
Questions
The questions for the quiz are stored in a JSON file named questions.json. Here is an example of the questions used in the application:

JSON
[
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
Public code references from 1 repository
Usage
Clone the repository:
sh
git clone https://github.com/dineshkothapalli770/quiz-Application.git
Navigate to the project directory:
sh
cd quiz-Application
Run the application:
sh
python quiz_application.py
How It Works
The application works by reading the questions from the questions.json file and presenting each question to the user. The user inputs their answer, and the application checks if the answer is correct. It then provides feedback and updates the score. At the end of the quiz, the final score is displayed.
