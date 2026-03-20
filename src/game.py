# BlazeXDimension Game Logic

class Game:
    def __init__(self):
        self.state = "initialized"
        self.score = 0

    def start(self):
        self.state = "running"
        print("Game started!")

    def update(self):
        if self.state == "running":
            # Game logic goes here
            print("Game is updating...")

    def end(self):
        self.state = "ended"
        print(f"Game ended! Final score: {self.score}")

if __name__ == '__main__':
    game = Game()
    game.start()
    for _ in range(5):  # simulated game loop
        game.update()
    game.end()