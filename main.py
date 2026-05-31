import pygame as pg 
import math 
import os 
import numpy as np
 


pg.init()

Width, Height = 800,800
WIN = pg.display.set_mode((Width,Height))
pg.display.set_caption("Planet Simulation")


# Color variables for simulations
WHITE = (255,255,255)
YELLOW = (255,255,0)
BLUE = (100, 149, 237)
RED = (185,84,57)
DARK_GREY = (169,169,169)
DARK_YELLOW = (255, 140, 0)



# Planet class for attribute handling 
class Planet(): 
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 250/AU # 1 AU = 100 pixels 
    TIMESTEP = 3600*24 # 1 day



    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass 


        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0
    
    def draw(self, win):
        x = self.x * self.SCALE + Width/2
        y = self.y * self.SCALE + Height/2
        pg.draw.circle(win, self.color, (x,y), self.radius)

        if len(self.orbit) >2:
            updated_points = []
            for point in self.orbit:
                x,y = point
                x = x*self.SCALE + Width/2
                y = y*self.SCALE + Height/2
                updated_points.append((x,y))
            pg.draw.lines(win, self.color, False, updated_points, 2)



    
    # Calculating the force of gravity between systems in our simulation 
    def attraction(self,other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y -self.y
        distance = math.sqrt(distance_x**2 + distance_y**2)

        # here we are calculating the distance of the planet from the sun, if the other object is the sun the, we'll overwrite the distance of the object from the sun
        if other.sun:
            self.distance_to_sun = distance


        # actual physics behind the scenes 
        force = self.G *self.mass*other.mass/distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta)* force
        force_y = math.sin(theta)* force
        return force_x, force_y
    
    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue 
            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx/self.mass * self.TIMESTEP
        self.y_vel += total_fy/self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel *self.TIMESTEP
        self.orbit.append((self.x,self.y))






def main():
    run = True
    clock = pg.time.Clock()

    
    sun = Planet(0,0,30, YELLOW, 1.98892 * 10**30)
    sun.sun = True


    # Planet data
    mercury = Planet(0.387*Planet.AU, 0, 8, DARK_GREY, 3.30*10**23)
    mercury.y_vel = -47.4*1000

    venus = Planet(0.723*Planet.AU, 0, 14, DARK_YELLOW, 4.865*10**24)
    venus.y_vel = -35.027*1000

    earth = Planet(-1*Planet.AU, 0, 16, BLUE, 5.9742*10**24)
    earth.y_vel = 29.783*1000

    mars  = Planet(-1.524*Planet.AU, 0 , 12, RED, 6.39*10**23)
    mars.y_vel = 24.4 *1000
    


    planets = [sun,mercury,venus, earth, mars]


    # Pg configuration
    while run:
        clock.tick(120)
        WIN.fill((0,0,0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        
        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)

        pg.display.update()
    pg.quit()

main()