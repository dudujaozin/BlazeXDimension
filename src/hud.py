class HUD:
    def __init__(self):
        self.health = 100
        self.energy = 100
        self.score = 0
        self.combo_counter = 0
        self.floating_texts = []

    def update_health(self, amount):
        self.health = max(0, min(100, self.health + amount))  # Health between 0 and 100

    def update_energy(self, amount):
        self.energy = max(0, min(100, self.energy + amount))  # Energy between 0 and 100

    def update_score(self, points):
        self.score += points

    def increment_combo(self):
        self.combo_counter += 1

    def add_floating_text(self, text):
        self.floating_texts.append(text)

    def display(self):
        print(f"Health: {self.health}")
        print(f"Energy: {self.energy}")
        print(f"Score: {self.score}")
        print(f"Combo: {self.combo_counter}")
        print("Floating Texts:")
        for text in self.floating_texts:
            print(text)
        
# Example usage:
# hud = HUD()
# hud.update_health(-10)
# hud.update_energy(-5)
# hud.update_score(50)
# hud.increment_combo()
# hud.add_floating_text("Great combo!")
# hud.display()