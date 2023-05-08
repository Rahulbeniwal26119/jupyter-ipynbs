__all__ = ['Projectile', '_internal_function']


class Projectile:
    def __init__(self, mass, velocity):
        self.mass = mass
        self.velocity = velocity


def _internal_function():
    print("This function is not exported")
