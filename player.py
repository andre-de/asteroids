from circleshape import *
from constants import *
from shot import *
import math

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0


    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, -1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()


    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):

        if self.shot_timer > 0:
            return

        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)

        self.shot_timer = 0.3
    
        # Convert rotation to radians
        angle_rad = math.radians(self.rotation)
    
        # Calculate velocity components using trigonometry
        shot.velocity = pygame.Vector2(
            -math.sin(angle_rad) * PLAYER_SHOOT_SPEED,
            math.cos(angle_rad) * PLAYER_SHOOT_SPEED)  # Negative because y increases downward
        
        return shot  # Make sure you're adding this to your shots group!    
             