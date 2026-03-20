class AssetManager:
    def __init__(self):
        self.sprites = {}
        self.sounds = {}
        self.fonts = {}

    def load_sprite(self, name, path):
        # Logic to load sprite
        self.sprites[name] = path

    def load_sound(self, name, path):
        # Logic to load sound
        self.sounds[name] = path

    def load_font(self, name, path):
        # Logic to load font
        self.fonts[name] = path

    def get_sprite(self, name):
        return self.sprites.get(name)

    def get_sound(self, name):
        return self.sounds.get(name)

    def get_font(self, name):
        return self.fonts.get(name)