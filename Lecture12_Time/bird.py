from pico2d import load_image
import random
import game_framework

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

RUN_SPEED_PPS = 300.0

class Bird:
    def __init__(self):
        self.image = load_image('bird_animation.png')
        self.x, self.y = random.randint(100,1500), random.randint(400,550)
        self.frame = 0
        self.dir = 1
        pass



    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        if self.x < 50:
            self.dir = 1
        elif self.x > 1550:
            self.dir = -1

        pass

    def draw(self):
        bottom = (2 - ( int(self.frame) // 5)) * 166
        left = (int(self.frame) % 5) * 182
        if self.dir == 1:
            self.image.clip_draw(left,  bottom, 182, 166, self.x, self.y,91,83)
        else:
            self.image.clip_composite_draw(left ,  bottom, 182, 166,0,'h', self.x, self.y,91,83)
        pass
