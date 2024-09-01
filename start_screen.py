import pygame


pygame.init()

# Define colors
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Screen dimensions
WIDTH, HEIGHT = 600, 600

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cellular Automaton Simulator")

# Set up font
font = pygame.font.SysFont(None, 48)

# FPS
FPS = 60
clock = pygame.time.Clock()


# Define Button class
class Button:
    def __init__(self, text, pos, color=GREY, hover_color=YELLOW):
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.rect = pygame.Rect(pos, (200, 50))
        self.rendered_text = font.render(self.text, True, BLACK)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.rendered_text, (self.rect.x + 20, self.rect.y + 10))

    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def update(self, mouse_pos):
        if self.is_hovered(mouse_pos):
            self.color = self.hover_color
        else:
            self.color = GREY


def start_screen():
    # Create buttons for different automata
    buttons = [
        Button("Game of Life", (200, 200)),
        Button("Brian's Brain", (200, 300))
    ]

    running = True
    while running:
        screen.fill(WHITE)

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.is_hovered(mouse_pos):
                        return button.text

        for button in buttons:
            button.update(mouse_pos)
            button.draw(screen)

        pygame.display.update()
        clock.tick(FPS)