class Blaze:
    def __init__(self):
        self.health = 100
        self.position = [0, 0]

    def move(self, direction):
        if direction == 'up':
            self.position[1] += 1
        elif direction == 'down':
            self.position[1] -= 1
        elif direction == 'left':
            self.position[0] -= 1
        elif direction == 'right':
            self.position[0] += 1

        print(f"Moved {direction}. New position: {self.position}")

    def jump(self):
        print(f"Jumped from position: {self.position}")
        self.position[1] += 2  # Simple jump mechanic
        print(f"Landed at position: {self.position}")

    def flame_attack(self):
        print("Flame attack unleashed!")
        # Attack logic here

# Example usage:
# blaze = Blaze()
# blaze.move('up')
# blaze.jump()
# blaze.flame_attack()