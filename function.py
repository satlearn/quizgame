# Implement the quiz functionality
import sqlite3
from quiz import *

def present_quiz(questions):
    score = 0
    for q in questions:
        print(f"\nQuestion: {q['question']}")
        for i, option in enumerate(q['options'], start=1):
            print(f"{i}. {option}")
        user_answer = input("Your answer (enter the option number): ")
        #if user_answer.isdigit() and int(user_answer) == q['options'].index(q['answer']) + 1:
        if int(user_answer) == q['options'].index(q['answer'])+1:
            score += 1
    return score


def main():
    name = input("Enter your name: ")
    print(f"Hi {name}, Welcome to the Quiz game :)")
    conn = sqlite3.connect('python_project3/quiz_app.db')
    cursor = conn.cursor()

    # Check if the user exists, if not, add them to the 'users' table
    cursor.execute("SELECT user_id FROM users WHERE name = ?", (name,))
    user_data = cursor.fetchone()
    if user_data is None:
        cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
        conn.commit()
        user_id = cursor.lastrowid
    else:
        user_id = user_data[0]

    conn.close()

    # Present the quiz to the user
    score = present_quiz(quiz_questions)

    # Save the quiz attempt in the database
    conn = sqlite3.connect('python_project3/quiz_app.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO quiz_attempts (user_id, score) VALUES (?, ?)", (user_id, score))
    conn.commit()
    conn.close()

    print(f"\nQuiz completed! Your score is: {score} out of {len(quiz_questions)}")

if __name__ == "__main__":
    main()
