import sys, random
random.seed(1) # make the simulation the same each time, easier to debug
import pygame
import pymunk
import pymunk.pygame_util
from pygame.locals import *



def add_ball(space):

    mass = 3
    radius = 25
    inertia = pymunk.moment_for_circle(mass, 0, radius, (0,0))
    body = pymunk.Body(mass, inertia)
    mousepos = pygame.mouse.get_pos()
    body.position = mousepos

    shape = pymunk.Circle(body, radius, (0,0))
    shape.friction = 1
    space.add(body, shape)
    return shape

def add_L(space):
    """Add a inverted L shape with two joints"""
    rotation_center_body = pymunk.Body(body_type = pymunk.Body.STATIC)
    rotation_center_body.position = (300,300)

    rotation_limit_body = pymunk.Body(body_type = pymunk.Body.STATIC)
    rotation_limit_body.position = (200,300)

    body = pymunk.Body(10, 10000)
    body.position = (300,300)
    l1 = pymunk.Segment(body, (-150, 0), (255.0, 0.0), 5.0)
    l2 = pymunk.Segment(body, (-150.0, 0), (-150.0, -50.0), 5.0)
    l1.friction = 1
    l2.friction = 1
    l1.mass = 8
    l2.mass = 1

    rotation_center_joint = pymunk.PinJoint(body, rotation_center_body, (0,0), (0,0))
    joint_limit = 25
    rotation_limit_joint = pymunk.SlideJoint(body, rotation_limit_body, (-100,0), (0,0), 0, joint_limit)

    space.add(l1, body, rotation_center_joint, rotation_limit_joint)
    return l1

def main():
    pygame.init()
    running = True
    bg = (100,100,100)
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("pymunk test")
    clock = pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = (0.0, 900.0)

    lines = add_L(space) #this is the part that makes the inverted L
    balls = []
    draw_options = pymunk.pygame_util.DrawOptions(screen)

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    ball_shape = add_ball(space)
                    balls.append(ball_shape)

        screen.fill(bg)

        balls_to_remove = []
        for ball in balls:
            if ball.body.position.y > 550:
                balls_to_remove.append(ball)

        for ball in balls_to_remove:
            space.remove(ball, ball.body)
            balls.remove(ball)

        space.debug_draw(draw_options)
        space.step(1/60.0)
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()