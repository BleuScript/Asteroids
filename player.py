import circleshape

class Player(circleshape.CircleShape): # type: ignore
    def __init__(self, x, y):
        super().__init__(self.PLAYER_RADIUS)
        self.rotation = 0 # type: ignore

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) # type: ignore
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5 # type: ignore
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2) # type: ignore

    self.rotation = 0 # type: ignore