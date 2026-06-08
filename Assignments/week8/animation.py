import pygame
import sys
import math
import random
import colorsys

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()

frames = []
for i in range(2, 7):
    img = pygame.image.load(f'Untitled_Artwork {i}.jpg')
    frames.append(img)


class RippleRing:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 0
        self.max_radius = random.randint(80, 180)
        self.speed = random.uniform(2, 5)
        self.width = random.randint(1, 3)
        self.alpha = 255
        hue = random.uniform(180, 320)
        sat = random.uniform(70, 100)
        bright = random.uniform(80, 100)
        self.color = [int(c * 255) for c in colorsys.hsv_to_rgb(hue / 360, sat / 100, bright / 100)]

        self.sparkles = []
        num_sparkles = random.randint(5, 15)
        for _ in range(num_sparkles):
            angle = random.uniform(0, math.pi * 2)
            self.sparkles.append({
                "angle": angle,
                "radius_offset": 0,
                "speed": random.uniform(0.5, 2),
                "size": random.randint(1, 3)
            })

    def update(self):
        self.radius += self.speed
        self.alpha = int(255 * (1 - self.radius / self.max_radius))

        for s in self.sparkles:
            s["radius_offset"] += s["speed"]

        return self.radius < self.max_radius

    def draw(self, screen):
        if self.alpha > 0:
            color_with_alpha = (*self.color, self.alpha)
            pygame.draw.circle(screen, color_with_alpha,
                               (int(self.x), int(self.y)),
                               int(self.radius), self.width)

            for s in self.sparkles:
                particle_radius = self.radius + s["radius_offset"] * 3
                if particle_radius < self.max_radius and particle_radius > 0:
                    px = self.x + math.cos(s["angle"]) * particle_radius
                    py = self.y + math.sin(s["angle"]) * particle_radius
                    sparkle_alpha = int(self.alpha * 0.8)
                    sparkle_color = (*self.color, sparkle_alpha)
                    pygame.draw.circle(screen, sparkle_color,
                                       (int(px), int(py)), s["size"])


class Windmill:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.rotation_speed = -5
        self.windmill = pygame.image.load('Untitled_Artwork.png').convert_alpha()
        self.head = pygame.image.load('windmill_head.png').convert_alpha()
        self.head_rect = self.head.get_rect(topleft=(self.x + 70, self.y + 250))
        self.head_center = self.head_rect.center

    def update(self):
        self.angle += self.rotation_speed
        if self.angle >= 360:
            self.angle -= 360

    def draw(self, screen):
        screen.blit(self.windmill, (self.x, self.y))
        rotated_head = pygame.transform.rotate(self.head, self.angle)
        rotated_rect = rotated_head.get_rect(center=self.head_center)
        screen.blit(rotated_head, rotated_rect)


class Birb:
    def __init__(self, x, y):
        self.image = pygame.image.load('birb.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))

        flip = random.choice([True, False])
        if flip:
            self.image = pygame.transform.flip(self.image, True, False)

        self.rect = self.image.get_rect(center=(x, y))
        self.speed_x = random.choice([-5, -4, 4, 5])
        self.speed_y = random.choice([-5, -4, 4, 5])

        self.bounce_count = 0
        self.max_bounces = random.randint(2, 5)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left <= 0 or self.rect.right >= screen.get_width():
            self.speed_x = -self.speed_x
            self.bounce_count += 1
        if self.rect.top <= 0 or self.rect.bottom >= screen.get_height():
            self.speed_y = -self.speed_y
            self.bounce_count += 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def should_remove(self):
        if self.bounce_count >= self.max_bounces:
            return True

        return (self.rect.right < -100 or
                self.rect.left > screen.get_width() + 100 or
                self.rect.bottom < -100 or
                self.rect.top > screen.get_height() + 100)


windmill = Windmill(60, 0, 0)
birbs = []
ripples = []

current_frame = 0
frame_rate = 6

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            birbs.append(Birb(event.pos[0], event.pos[1]))

            num_ripples = random.randint(2, 5)
            for _ in range(num_ripples):
                offset_x = random.uniform(-10, 10)
                offset_y = random.uniform(-10, 10)
                ripples.append(RippleRing(event.pos[0] + offset_x, event.pos[1] + offset_y))

    current_frame += 1
    if current_frame >= len(frames):
        current_frame = 0
    windmill.update()

    for birb in birbs[:]:
        birb.update()
        if birb.should_remove():
            birbs.remove(birb)

    alive_ripples = []
    for ripple in ripples:
        if ripple.update():
            ripple.draw(screen)
            alive_ripples.append(ripple)
    ripples = alive_ripples

    screen.fill((0, 0, 0))
    screen.blit(frames[current_frame], (0, 0))
    windmill.draw(screen)

    for ripple in ripples:
        ripple.draw(screen)

    for birb in birbs:
        birb.draw(screen)

    pygame.display.flip()
    clock.tick(frame_rate)

pygame.quit()
sys.exit()