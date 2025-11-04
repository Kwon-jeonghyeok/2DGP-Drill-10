from pico2d import load_image
import random

class Bird:
    def __init__(self):
        self.image = load_image('bird_animation.png')
        self.x, self.y = random.randint(100,1500), random.randint(400,550)
        self.frame = 0
        self.dir = 1
        pass



    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 182, 182, 166, self.x, self.y, 91, 83)
        pass
