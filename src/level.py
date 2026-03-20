class Level:
    def __init__(self, name):
        self.name = name
        self.platforms = []
        self.obstacles = []

    def add_platform(self, platform):
        self.platforms.append(platform)

    def add_obstacle(self, obstacle):
        self.obstacles.append(obstacle)

    def describe(self):
        return f"Level: {self.name}, Platforms: {len(self.platforms)}, Obstacles: {len(self.obstacles)}"