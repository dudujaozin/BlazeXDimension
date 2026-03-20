import random

class Particle:
    def __init__(self, position, velocity, lifespan):
        self.position = position
        self.velocity = velocity
        self.lifespan = lifespan

    def update(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.lifespan -= 1

    def is_alive(self):
        return self.lifespan > 0

class ParticleEffect:
    def __init__(self, position):
        self.particles = []
        self.position = position

class ExplosionEffect(ParticleEffect):
    def __init__(self, position):
        super().__init__(position)
        for _ in range(50):  # Number of particles
            velocity = [random.uniform(-1, 1) for _ in range(2)]
            lifespan = random.randint(20, 40)
            self.particles.append(Particle(position.copy(), velocity, lifespan))

    def update(self):
        for particle in self.particles:
            particle.update()
        self.particles = [p for p in self.particles if p.is_alive()]

class FireEffect(ParticleEffect):
    def __init__(self, position):
        super().__init__(position)
        for _ in range(30):
            velocity = [0, random.uniform(1, 2)]  # Particles will move upwards
            lifespan = random.randint(10, 20)
            self.particles.append(Particle(position.copy(), velocity, lifespan))

class SparkEffect(ParticleEffect):
    def __init__(self, position):
        super().__init__(position)
        for _ in range(20):  # Number of spark particles
            velocity = [random.uniform(-0.5, 0.5), random.uniform(-2, 0)]
            lifespan = random.randint(5, 15)
            self.particles.append(Particle(position.copy(), velocity, lifespan))

class BloodEffect(ParticleEffect):
    def __init__(self, position):
        super().__init__(position)
        for _ in range(25):  # Number of blood particles
            velocity = [random.uniform(-0.5, 0.5), random.uniform(-1, 0)]
            lifespan = random.randint(15, 30)
            self.particles.append(Particle(position.copy(), velocity, lifespan))
