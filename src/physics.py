class Physics:
    def __init__(self):
        pass

    def gravity(self, mass1, mass2, distance):
        G = 6.67430e-11  # gravitational constant
        force = G * (mass1 * mass2) / distance ** 2
        return force

    def velocity(self, distance, time):
        return distance / time if time > 0 else 0

    def collision_detection(self, obj1, obj2):
        return (obj1['x'] < obj2['x'] + obj2['width'] and
                obj1['x'] + obj1['width'] > obj2['x'] and
                obj1['y'] < obj2['y'] + obj2['height'] and
                obj1['y'] + obj1['height'] > obj2['y'])
