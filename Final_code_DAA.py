import pygame
import sys
import math

class SierpinskiTriangle:
    def __init__(self):
        self.width, self.height = 800, 600
        self.background_color = (255, 255, 255)
        self.border_color = (0, 0, 0)
        self.text_color = (0, 0, 0)
        self.depth_limit = 6
        self.animation_speed = 0.05
        self.triangle_count = 0
        self.footer_text = "Moez Mustafa | Roll: 01-134212-088"

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sierpinski Triangle")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 24)
        self.log_font = pygame.font.Font(None, 18)

    def draw_triangle(self, vertices, color):
        pygame.draw.polygon(self.screen, color, vertices, 1)
        pygame.draw.lines(self.screen, self.border_color, True, vertices, 1)

    def draw_number(self, vertices, number):
        text = self.font.render(str(number), True, self.text_color)
        centroid = [(vertices[0][0] + vertices[1][0] + vertices[2][0]) // 3,
                    (vertices[0][1] + vertices[1][1] + vertices[2][1]) // 3]
        self.screen.blit(text, centroid)

    def sierpinski(self, vertices, depth, number, color_index):
        if depth > 0:
            self.draw_triangle(vertices, self.border_color)
            self.draw_number(vertices, number)

            v1 = ((vertices[0][0] + vertices[1][0]) // 2, (vertices[0][1] + vertices[1][1]) // 2)
            v2 = ((vertices[1][0] + vertices[2][0]) // 2, (vertices[1][1] + vertices[2][1]) // 2)
            v3 = ((vertices[2][0] + vertices[0][0]) // 2, (vertices[2][1] + vertices[0][1]) // 2)

            self.sierpinski([vertices[0], v1, v3], depth - 1, number * 3, color_index + 1)
            self.sierpinski([v1, vertices[1], v2], depth - 1, number * 3 + 1, color_index + 1)
            self.sierpinski([v3, v2, vertices[2]], depth - 1, number * 3 + 2, color_index + 1)

    def game(self):
        vertices = [(self.width // 2, 50), (50, self.height - 50), (self.width - 50, self.height - 50)]
        depth = 0

        while True:
            self.screen.fill(self.background_color)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        depth = min(self.depth_limit - 1, depth + 1)
                    elif event.key == pygame.K_DOWN:
                        depth = max(0, depth - 1)
                    elif event.key == pygame.K_ESCAPE:
                        return "menu"

            self.triangle_count = 3 ** depth

            count_text = self.font.render(f"Triangles: {self.triangle_count}", True, self.text_color)
            self.screen.blit(count_text, (10, 10))

            formula_text = self.font.render(f"Formula: 3^{depth}", True, self.text_color)
            self.screen.blit(formula_text, (self.width - formula_text.get_width() - 20, 10))

            footer = self.log_font.render(self.footer_text, True, self.text_color)
            self.screen.blit(footer, (self.width - footer.get_width() - 10, self.height - footer.get_height() - 10))

            if depth > 0:
                self.sierpinski(vertices, depth, 0, 0)

            pygame.display.flip()
            self.clock.tick(5)

    def main(self):
        current_state = "menu"

        while True:
            if current_state == "menu":
                current_state = self.main_menu()
            elif current_state == "game":
                current_state = self.game()

    def main_menu(self):
        angle = 0
        while True:
            self.screen.fill(self.background_color)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return "game"

            angle += self.animation_speed
            v1 = (self.width // 2 + int(200 * math.cos(angle)), 100)
            v2 = (self.width // 2 + int(200 * math.cos(angle + 2 * math.pi / 3)), 500)
            v3 = (self.width // 2 + int(200 * math.cos(angle + 4 * math.pi / 3)), 500)
            self.draw_triangle([v1, v2, v3], self.border_color)

            title_text = self.font.render("Sierpinski Triangle", True, self.text_color)
            start_text = self.font.render("Press SPACE to start", True, self.text_color)

            self.screen.blit(title_text, (self.width // 2 - title_text.get_width() // 2, 50))
            self.screen.blit(start_text, (self.width // 2 - start_text.get_width() // 2, 100))

            footer = self.log_font.render(self.footer_text, True, self.text_color)
            self.screen.blit(footer, (self.width - footer.get_width() - 10, self.height - footer.get_height() - 10))

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    sierpinski = SierpinskiTriangle()
    sierpinski.main()
