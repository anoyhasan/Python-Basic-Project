def simple_quiz_app():
    questions = {
        "What is the capital of France?": "Paris",
        "Who wrote 'Hamlet'?": "Shakespeare",
        "What is 2 + 2?": "4",
    }

    score = 0
    for (
        question,
        correct_answer,
    ) in questions.items():
        user_answer = input(question + " ")

        if user_answer.strip().lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")

    print(f"\nYour final score is: {score}/{len(questions)}")

    if score == len(questions):
        print("Perfect score! Well done!")
    elif score > len(questions) / 2:
        print("Great job!")
    else:
        print("Better luck next time!")


simple_quiz_app()
