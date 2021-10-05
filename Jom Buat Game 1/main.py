import pygame
from random import randint

pygame.init()
pygame.font.init()

class Catcher:
    def __init__(self, x, y, width, height, color=(0, 155, 0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        self.is_active = False

    def toggle(self, state=False):
        self.is_active = state

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height), int(self.is_active))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


class Gold:
    def __init__(self, x, color=(100, 140, 0)):
        self.color = color
        self.width = 32
        self.height = 32
        self.x = x - self.width / 2
        self.y = 0

    def update(self, deltatime):
        self.y += 100 * deltatime

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

    def collide(self, catcher):
        _rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return _rect.collidelist(catcher)

def generate_gold(lanes):
    lane = lanes[randint(0, 3)]
    return Gold(lane + lane_width/2)


if __name__ == '__main__':
    WIDTH = 800
    HEIGHT = 900
    FPS = 60

    window = pygame.display.set_mode((WIDTH, HEIGHT))

    lane_width = WIDTH/4
    lanes = [lane_width*n for n in range(4)]
    clock = pygame.time.Clock()

    catchers = tuple([Catcher(lane + lane_width/2 - 32, HEIGHT - 64, 64, 32) for lane in lanes])
    golds = []
    active_catcher = None

    spawn_cooldown = 120
    spawn_timer = 0

    running = True
    while running:
        dt = clock.tick(FPS) / 1000

        window.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        key_pressed = pygame.key.get_pressed()
        if active_catcher is None:
            if key_pressed[pygame.K_q]:
                active_catcher = catchers[0]
            elif key_pressed[pygame.K_w]:
                active_catcher = catchers[1]
            elif key_pressed[pygame.K_e]:
                active_catcher = catchers[2]
            elif key_pressed[pygame.K_r]:
                active_catcher = catchers[3]
        else:
            active_catcher.toggle(True)

        if not key_pressed[pygame.K_q] and active_catcher == catchers[0]:
            active_catcher.toggle(False)
            active_catcher = None
        elif not key_pressed[pygame.K_w] and active_catcher == catchers[1]:
            active_catcher.toggle(False)
            active_catcher = None
        elif not key_pressed[pygame.K_e] and active_catcher == catchers[2]:
            active_catcher.toggle(False)
            active_catcher = None
        elif not key_pressed[pygame.K_r] and active_catcher == catchers[3]:
            active_catcher.toggle(False) 
            active_catcher = None

        spawn_timer += 1
        if spawn_timer == spawn_cooldown:
            golds.append(generate_gold(lanes))
            spawn_timer = 0

        for catcher in catchers:
            catcher.draw(window)

        for gold in golds:
            gold.update(dt)
            gold.draw(window)
            
            collide_index = gold.collide([catcher.get_rect() for catcher in catchers])
            if collide_index != -1 and catchers[collide_index].is_active:
                print("Collide!")
                golds.remove(gold)

            if gold.y > HEIGHT:
                print("Removed!")
                golds.remove(gold)

        pygame.display.update()

    pygame.quit()
