# SEN5105 - Introduction to Programming - Python
# Python Basics Trivia Game
# Developed by: [Tayfun Guler]

class Question:
    """
    Represents a trivia question about basic Python knowledge.
    Stores the question, multiple choice answers, and the index of the correct answer.
    """

    def __init__(self, question, options, correct_index):
        """
        Initializes a trivia question about Python.
        """
        self.question = question
        self.options = options
        self.correct_index = correct_index

    def display_and_check(self):
        """
        Shows the question and options, then checks if the answer is correct.
        """
        print(f"Question: {self.question}")
        for index, option in enumerate(self.options, 1):
            print(f"{index}. {option}")
        user_response = int(input("Choose your answer (1-4): "))
        return user_response == self.correct_index


def play_game(questions):
    """
    Runs the trivia game, alternating between two players.
    Scores are kept, and a winner is declared at the end.
    """
    scores = [0, 0]  # Player scores
    for player in range(2):
        print(f"\nPlayer {player + 1}, it's your turn!")
        for i in range(player * 5, player * 5 + 5):
            if questions[i].display_and_check():
                print("Correct!")
                scores[player] += 1
            else:
                print("Wrong answer.")

    # Displaying final scores and winner
    print("\nGame Over. Scores:")
    for player, score in enumerate(scores, 1):
        print(f"Player {player}: {score} points")
    if scores[0] > scores[1]:
        print("Player 1 wins!")
    elif scores[0] < scores[1]:
        print("Player 2 wins!")
    else:
        print("It's a tie!")


def main():
    """
    Prepares a set of 10 basic Python trivia questions and starts the game.
    """
    trivia_questions = [
        Question("What is the keyword to define a function in Python?", ["func", "def", "function", "declare"], 2),
        Question("Which operator is used for exponentiation?", ["^", "**", "exp", "pow"], 2),
        Question("How do you start a comment in Python?", ["//", "#", "--", "/*"], 2),
        Question("Which of these data types does Python not inherently support?",
                 ["Lists", "Tuples", "Arrays", "Dictionaries"], 3),
        Question("What keyword is used to create a loop in Python?", ["loop", "for", "while", "repeat"], 2),
        # 5 more questions for Player 2
        Question("How do you convert a string to an integer?", ["int()", "strToInt()", "convert()", "toInt()"], 1),
        Question("What symbol is used to define a dictionary in Python?", ["{}", "[]", "()", "//"], 1),
        Question("Which of these is not a Python looping structure?", ["for", "while", "do-while", "foreach"], 3),
        Question("What method is used to append an item to a list?", ["add()", "push()", "append()", "insert()"], 3),
        Question("Which keyword is used to handle exceptions?", ["try", "except", "catch", "error"], 2)
    ]

    play_game(trivia_questions)


if __name__ == "__main__":
    main()
