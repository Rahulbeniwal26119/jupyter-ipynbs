from .model import Projectile

__all__ = ['print_projectile']


def print_projectile(projectile=None):
    if not projectile:
        projectile = Projectile(1, 1)
    print(f"Mass: {projectile.mass}")
    print(f"Velocity: {projectile.velocity}")