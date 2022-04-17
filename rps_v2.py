import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def valid_choice(choice, Selectors):
    while True:
        Selection = input(choice).lower()
        if Selection in Selectors:
            return Selection
        else:
            print("Not an option.\n"
                  "Try Again")


def main_menu():  # Yes, I know the term AI is being used very generously here.
    AI = {'1': Rocky_Rockstar(),
          '2': Crazy_Carl(),
          '3': Methodical_Micky(),
          '4': Hal()}

    game_type = valid_choice(
        "Choose match type:\n"
        "1. Human vs Rocky the Rockstar\n"
        "2. Human vs Crazy Carl\n"
        "3. Human vs Methodical Micky\n"
        "4. Human vs Hal\n", ["1", "2", "3", "4"])

    return Game(Human(), AI[game_type])


def play_again():
    while True:
        print("Would you like to play again?\n")
        choice = input("y / n\n").lower()
        if choice == 'y':
            print("REMATCH!")
            Play()
        elif choice == 'n':
            print("You fought well! \n"
                  "Come back again for more glory!!!")
            exit(0)
        else:
            print("Keep it a yes or no\n")


class Player:
    def move(self):
        pass

    def learn(self, Human_move, AI_Move):
        pass


class Human(Player):  # Human Player!
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()

    def move(self):
        return valid_choice("Select: Rock, Paper, or Scissors:",
                            ['rock', 'paper', 'scissors'])


class Rocky_Rockstar(Player):  # Rock Player!
    def move(self):
        return 'rock'


class Crazy_Carl(Player):  # Random Player!
    def move(self):
        return random.choice(moves)


class Methodical_Micky(Player):  # Cycle Player!
    def __init__(self):
        self.AI_move = 'rock'

    def move(self):
        return self.AI_move

    def learn(self, Human_move, AI_move):
        if Human_move == "rock":
            self.AI_move = "paper"
        elif Human_move == "paper":
            self.AI_move = "scissors"
        else:
            self.AI_move = "rock"


class Hal(Player):  # Learning Player!
    def __init__(self):
        self.AI_move = 'rock'

    def move(self):
        return self.AI_move

    def learn(self, AI_move, Human_move):
        self.AI_move = Human_move


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score_1 = 0
        self.score_2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        p1_wins = beats(move1, move2)
        if move1 == move2:
            print("TIE!")
        elif p1_wins:
            self.score_1 += 1
            print("Player 1 is Victorious!")
            print("Scoreboard:\n"
                  f"Player 1: {self.score_1}\n"
                  f"Player 2: {self.score_2}\n"
                  "Next Round! \n"
                  "FIGHT! \n")

        else:
            self.score_2 += 1
            print("Player 2 is Victorious!")
            print(f"Player 1: {self.score_1}\n"
                  f"Player 2: {self.score_2}\n"
                  "Next Round! \n"
                  "FIGHT!\n")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self, rounds):
        print("Game start!")
        for round in range(rounds):
            round += 1
            print(f"Round {round}:")
            self.play_round()
        if self.score_1 == self.score_2:
            print("TIE!")
        elif self.score_1 > self.score_2:
            print("Victory!")
        else:
            print("Defeat!")

        print("Score Board:\n")
        print(f"Player 1: {self.score_1}", f"Player 2: {self.score_2} \n")
        print("Game Over! \n")
        play_again()


def Play():
    menu = main_menu()
    rounds = int(valid_choice(
                "Enter Number of Rounds: \n",
                ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']))
    menu.play_game(rounds)


if __name__ == '__main__':
    Play()
