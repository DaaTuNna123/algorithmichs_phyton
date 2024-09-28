import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *


class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        pg.event.set_grab(True)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)  # Set a timer for regular updates
        self.new_game()

    def new_game(self):
        self.map = Map(self)  # Create the game map
        self.player = Player(self)  # Create the player character
        self.object_renderer = ObjectRenderer(self)  # Handle rendering of objects
        self.raycasting = RayCasting(self)  # Perform raycasting to generate 3D view
        self.object_handler = ObjectHandler(self)  # Manage in-game objects and interactions
        self.weapon = Weapon(self)  # Handle the player's weapon
        self.sound = Sound(self)  # Play sound effects and music
        self.pathfinding = PathFinding(self)  # Implement pathfinding for enemies
        pg.mixer.music.play(-1)  # Start background music

    def update(self):
        self.player.update()  # Update player position and actions
        self.raycasting.update()  # Update raycasting for each frame
        self.object_handler.update()  # Update objects and their behavior
        self.weapon.update()  # Update weapon state and animations
        pg.display.flip()  # Update the display with rendered content
        self.delta_time = self.clock.tick(FPS)  # Calculate and limit frame rate
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')  # Set window title to display FPS

    def draw(self):
        # self.screen.fill('black')  # Optionally clear the screen
        self.object_renderer.draw()  # Draw objects (walls, sprites)
        self.weapon.draw()  # Draw the player's weapon
        # self.map.draw()  # Optionally draw the map
        # self.player.draw()  # Optionally draw the player

    def check_events(self):
        self.global_trigger = False  # Reset global trigger flag
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()  # Quit the game
            elif event.type == self.global_event:
                self.global_trigger = True  # Set global trigger for regular updates
            self.player.single_fire_event(event)  # Handle player actions from events

    def run(self):
        while True:
            self.check_events()  # Check for events (keyboard, mouse, etc.)
            self.update()  # Update game logic for each frame
            self.draw()  # Draw the game state to the screen

if __name__ == '__main__':
    game = Game()
    game.run()