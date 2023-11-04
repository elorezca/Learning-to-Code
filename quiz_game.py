import time

# Define your quiz questions as a list of dictionaries. Each dictionary contains a question, options, and the correct answer.
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["1. London", "2. Berlin", "3. Paris", "4. Rome"],
        "correct_answer": "3"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["1. Earth", "2. Mars", "3. Jupiter", "4. Venus"],
        "correct_answer": "2"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["1. Oxygen", "2. Carbon Dioxide", "3. Hydrogen", "4. Nitrogen"],
        "correct_answer": "2"
    }
]

# Initialize variables to keep track of the user's score and their correct/incorrect answers.
score = 0
correct_answers = []
incorrect_answers = []
total_time_spent = 0

def display_results():
    print(f"Your final score is: {score}/{len(quiz_questions)}")
    print(f"Total time spent: {total_time_spent:.2f} seconds")

def add_question():
    question = input("Please enter a question: ")
    options = input("Please enter options separated by commas (e.g., option1, option2, option3, option4): ").split(", ")
    correct_answer = input("Please enter the correct option using (1/2/3/4): ")

    new_question = {
        "question": question,
        "options": options,
        "correct_answer": correct_answer
    }

    quiz_questions.append(new_question)
    print("Question added successfully!")

    return new_question

# Iterate through the quiz questions.
for i, question_data in enumerate(quiz_questions, 1):
    print(f"Question {i}: {question_data['question']}")
    for option in question_data["options"]:
        print(option)
    
    user_answer = ""
    start_time = time.time()

    while True:    
        user_answer = input("Your answer (1/2/3/4): ")
        if user_answer in ["1", "2", "3", "4"]:
            break
        else:
                print("Invalid input. Please enter a number between 1 and 4.")
    
    elapsed_time = time.time() - start_time
    total_time_spent += elapsed_time

    if elapsed_time > 10:
        print("Time's up! You didn't answer in time.")
    else:
        if user_answer == question_data["correct_answer"]:
            score += 1
            correct_answers.append(question_data["question"])
        else:
            incorrect_answers.append(question_data["question"])

display_results()

print("")

# Display the final results.
print(f"Your final score is: {score}/{len(quiz_questions)}")

print("")

print(f"Total time spent: {total_time_spent:.2f} seconds")

print("")

if correct_answers:
    print("You answered the following questions correctly:")
    for question in correct_answers:
        print(question)
if incorrect_answers:
    print("You answered the following questions incorrectly:")
    for question in incorrect_answers:
        print(question)