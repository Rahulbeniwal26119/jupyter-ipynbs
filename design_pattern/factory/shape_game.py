#%%
import pygame



class Shape:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
    
    def draw(self):
        raise NotImplementedError

    def move(self, direction):
        if direction == 'up':
            self.y -= 4
        elif direction == 'down':
            self.y += 4
        elif direction == 'left':
            self.x -= 4
        elif direction == 'right':
            self.x += 4
        
    @staticmethod
    def factory(type):
        if type == 'square':
            return Square(100, 100)
        elif type == 'circle':
            return Circle(100, 100)
        else:
            raise ValueError(f'Unknown shape type: {type}')


class Square(Shape):

    def draw(self):
        pygame.draw.rect(
            screen, (255, 255, 0), pygame.Rect(self.x, self.y, 60, 60)
        )

class Circle(Shape):
    
    def draw(self):
        pygame.draw.circle(
            screen, (255, 255, 0), (self.x, self.y), 20
        )

x = 100
y = 100

window_dims = (800, 600)
screen = pygame.display.set_mode(window_dims)

player_quits = False

obj = Shape.factory('circle')

while not player_quits:
    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            player_quits = True
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: obj.move("up")
        if pressed[pygame.K_DOWN]: obj.move("down")
        if pressed[pygame.K_LEFT]: obj.move("left")
        if pressed[pygame.K_RIGHT]: obj.move("right")

        screen.fill((0, 0, 0))
        obj.draw()
    pygame.display.flip()

