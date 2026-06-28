import random
import time

# ---------------- QUESTIONS ---------------- #

questions = {
    "easy": [
        {
            "question": "Who is known as the God of Cricket?",
            "options": ["A. MS Dhoni", "B. Sachin Tendulkar", "C. Virat Kohli", "D. Rohit Sharma"],
            "answer": "B"
        },
        {
            "question": "How many players are there in one cricket team?",
            "options": ["A. 10", "B. 11", "C. 12", "D. 9"],
            "answer": "B"
        },
        {
            "question": "Which country invented cricket?",
            "options": ["A. India", "B. Australia", "C. England", "D. Pakistan"],
            "answer": "C"
        }
    ],

    "medium": [
        {
            "question": "Who won the 2011 Cricket World Cup?",
            "options": ["A. India", "B. Australia", "C. England", "D. Pakistan"],
            "answer": "A"
        },
        {
            "question": "Which country hosted the 2019 Cricket World Cup?",
            "options": ["A. India", "B. England", "C. Australia", "D. South Africa"],
            "answer": "B"
        },
        {
            "question": "Who is called Captain Cool?",
            "options": ["A. Virat Kohli", "B. Rohit Sharma", "C. MS Dhoni", "D. Hardik Pandya"],
            "answer": "C"
        }
    ],

    "hard": [
        {
            "question": "Who scored the first ODI double century?",
            "options": ["A. Virender Sehwag", "B. Rohit Sharma", "C. Sachin Tendulkar", "D. Chris Gayle"],
            "answer": "C"
        },
        {
            "question": "Who has the most ODI centuries?",
            "options": ["A. Virat Kohli", "B. Sachin Tendulkar", "C. Ricky Ponting", "D. Rohit Sharma"],
            "answer": "B"
        },
        {
            "question": "Which bowler has taken the most wickets in Test cricket?",
            "options": ["A. Shane Warne", "B. Muttiah Muralitharan", "C. Anil Kumble", "D. James Anderson"],
            "answer": "B"
        }
    ]
}

# ---------------- FUNCTIONS ---------------- #

def save_score(name, score):
    with open("score.txt", "a") as file:
        file.write(f"{name}:{score}\n")


def show_leaderboard():
    print("\n========== LEADERBOARD ==========")

    try:
        with open("score.txt", "r") as file:
            scores = []

            for line in file:
                name, score = line.strip().split(":")
                scores.append((name, int(score)))

            scores.sort(key=lambda x: x[1], reverse=True)

            for i, (name, score) in enumerate(scores, start=1):
                print(f"{i}. {name} - {score}")

    except FileNotFoundError:
        print("No scores available.")


# ---------------- MAIN PROGRAM ---------------- #

print("=" * 40)
print("      CRICKET QUIZ GAME")
print("=" * 40)

name = input("Enter Your Name: ")

print("\nChoose Difficulty")
print("1. Easy")
print("2. Medium")
print("3. Hard")

choice = input("Enter Choice: ")

if choice == "1":
    level = "easy"
elif choice == "2":
    level = "medium"
elif choice == "3":
    level = "hard"
else:
    print("Invalid Choice!")
    exit()

quiz = random.sample(questions[level], len(questions[level]))

score = 0

print("\nYou have 10 seconds for each question.")

for q in quiz:

    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    start = time.time()

    answer = input("Your Answer: ").upper()

    end = time.time()

    if end - start > 10:
        print(" Time Out!")
        continue

    if answer == q["answer"]:
        print(" Correct!")
        score += 1
    else:
        print(" Wrong! Correct Answer:", q["answer"])

print("\n" + "=" * 40)
print("QUIZ COMPLETED")
print("=" * 40)

print("Player :", name)
print("Score :", score, "/", len(quiz))

percentage = (score / len(quiz)) * 100
print("Percentage :", percentage, "%")

if percentage == 100:
    print(" Outstanding!")
elif percentage >= 80:
    print(" Excellent!")
elif percentage >= 60:
    print(" Very Good!")
elif percentage >= 40:
    print(" Good!")
else:
    print(" Keep Practicing!")

save_score(name, score)

show_leaderboard()

print("\nThank you for playing!")