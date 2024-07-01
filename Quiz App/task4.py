import tkinter as tk
from tkinter import messagebox

# Define the questions and answers
questions = [
    {
        'question': 'What is the capital of France?',
        'correct_answer': 'Paris'
    },
    {
        'question': 'Who wrote "Romeo and Juliet"?',
        'correct_answer': 'William Shakespeare'
    },
    {
        'question': 'What is the largest mammal in the world?',
        'correct_answer': 'Blue whale'
    }
]

# Initialize variables to keep track of quiz progress
current_question = 0
score = 0

# Function to check the answer
def check_answer():
    global current_question, score
    user_answer = entry.get().strip()
    correct_answer = questions[current_question]['correct_answer']
    
    if user_answer.lower() == correct_answer.lower():
        score += 1
    
    current_question += 1
    
    if current_question < len(questions):
        display_question()
    else:
        messagebox.showinfo("Quiz Completed", f"You've completed the quiz!\nYour score: {score}/{len(questions)}")
        root.destroy()

# Function to display current question
def display_question():
    question_label.config(text=questions[current_question]['question'])
    entry.delete(0, tk.END)

# Set up the main GUI window
root = tk.Tk()
root.title("Interactive Quiz")

# Create widgets
question_label = tk.Label(root, text="", wraplength=400, justify="center", font=("Arial", 14))
entry = tk.Entry(root, width=40, font=("Arial", 12))
submit_button = tk.Button(root, text="Submit", command=check_answer, font=("Arial", 12))

# Pack widgets
question_label.pack(pady=20)
entry.pack(pady=10)
submit_button.pack(pady=20)

# Start the quiz
display_question()

# Run the main event loop
root.mainloop()
