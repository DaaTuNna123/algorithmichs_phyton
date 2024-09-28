from sprite_object import *

# Weapon class inherits from AnimatedSprite
class Weapon(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/weapon/shotgun/0.png', scale=0.4, animation_time=90):
        # Initialize AnimatedSprite properties
        super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
        # Scale images for the animation
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        # Set weapon position at the bottom center of the screen
        self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
        # Initialize reloading state and other variables
        self.reloading = False
        self.num_images = len(self.images)
        self.frame_counter = 0
        self.damage = 50

    # Animate the shot, playing a reloading animation
    def animate_shot(self):
        # Check if the weapon is reloading
        if self.reloading:
            # Prevent the player from shooting while reloading
            self.game.player.shot = False
            # Trigger animation frames based on timing
            if self.animation_trigger:
                # Rotate images to show the next frame
                self.images.rotate(-1)
                # Update the current image
                self.image = self.images[0]
                # Increment frame counter
                self.frame_counter += 1
                # Check if animation is complete
                if self.frame_counter == self.num_images:
                    # Finish reloading
                    self.reloading = False
                    # Reset frame counter
                    self.frame_counter = 0

    # Draw the weapon on the screen
    def draw(self):
        self.game.screen.blit(self.images[0], self.weapon_pos)

    # Update the weapon state
    def update(self):
        # Handle animation timing
        self.check_animation_time()
        # Update the weapon's animation
        self.animate_shot()