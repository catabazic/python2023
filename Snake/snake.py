import sys
import json
import pygame
import random
from pygame import Rect
from pygame.math import Vector2

RIGHT = Vector2(1, 0)
LEFT = Vector2(-1, 0)
UP = Vector2(0, -1)
DOWN = Vector2(0, 1)

# define global variable
clicked = False
best_sore = int(0)
table_dimension = None
obstacles = None
table_x = 650
table_y = 750


class button():
    # colours for button and text
    button_col = (255, 0, 0)
    hover_col = (75, 225, 255)
    click_col = (50, 150, 255)
    text_col = pygame.Color('black')
    width = 90
    height = 45

    def __init__(self, x, y, text):
        """
        Initializarea clasei

        :param x: coordonatul x pentur buton, de unde incepe
        :param y: coordonatul y pentru buton, de unde incepe
        :param text: textul care va fi afisat pe buton
        """
        self.x = x
        self.y = y
        self.text = text

    def draw_button(self):
        """
        Functia afiseaza butonul pe ecran si verifica daca a fost apasat sau nu

        :return:  True - in caz ca butonul a fpst apasat
                  False - in caz contrar
        """
        global clicked
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # create pygame Rect object for the button
        button_rect = Rect(self.x - 45, self.y - 22, self.width, self.height)

        # check mouseover and clicked conditions
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(screen, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_col, button_rect)
        else:
            pygame.draw.rect(screen, self.button_col, button_rect)

        # add shading to button
        pygame.draw.line(screen, pygame.Color('white'), (self.x - 45, self.y - 22),
                         (self.x - 45 + self.width, self.y - 22), 2)
        pygame.draw.line(screen, pygame.Color('white'), (self.x - 45, self.y - 22),
                         (self.x - 45, self.y - 22 + self.height), 2)
        pygame.draw.line(screen, pygame.Color('black'), (self.x - 45, self.y - 22 + self.height),
                         (self.x - 45 + self.width, self.y - 22 + self.height), 2)
        pygame.draw.line(screen, pygame.Color('black'), (self.x - 45 + self.width, self.y),
                         (self.x - 45 + self.width, self.y - 22 + self.height), 2)

        # add text to button
        text_img = pygame.font.Font(None, 15).render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x - 45 + int(self.width / 2) - int(text_len / 2), self.y - 22 + 10))
        return action


class Game:
    def __init__(self):
        """
        Initializarea clasei
        """
        self.snake = Snake()
        self.fruit = Fruit()
        self.check_fruit()

    def update(self):
        """
        La fiecare iteratie updateaza datele care vor fi afisate
        """
        self.snake.move_snake()
        self.check_eat_fruit()
        self.check_game_over()

    def draw_elements(self):
        """
        Afiseaza toate elementele pe ecran
        """
        self.draw_grass()
        self.snake.draw_snake()
        self.fruit.draw_fruit()
        self.draw_score()
        self.draw_obstacles()

    def draw_grass(self):
        """
        Functie pentru desenarea tablei de joc
        """
        ok = 0
        for col in range(table_dimension):
            if table_dimension % 2 == 0:
                if ok == 0:
                    ok = 1
                else:
                    ok = 0
            for row in range(table_dimension):
                if ok == 0:
                    body_rect = pygame.Rect(col * cell_size + 25, row * cell_size + 90, cell_size, cell_size)
                    pygame.draw.rect(screen, (34, 139, 34), body_rect)
                    ok = 1
                else:
                    body_rect = pygame.Rect(col * cell_size + 25, row * cell_size + 90, cell_size, cell_size)
                    pygame.draw.rect(screen, (0, 128, 0), body_rect)
                    ok = 0

    def draw_obstacles(self):
        """
        Deseneaza toate obstacolele care sunt permise de dimensiunea tablei
        """
        global obstacles
        for obstacle in obstacles:
            if 0 <= obstacle['x'] < table_dimension - 1 and 0 <= obstacle['y'] < table_dimension and not ((obstacle[
                                                                                                               'x'] == table_dimension / 2 or
                                                                                                           obstacle[
                                                                                                               'x'] == table_dimension / 2 - 1 or
                                                                                                           obstacle[
                                                                                                               'x'] == table_dimension / 2 - 2) and
                                                                                                          obstacle[
                                                                                                              'y'] == table_dimension / 2):
                fruit_rect = pygame.Rect(obstacle['x'] * cell_size + 25, obstacle['y'] * cell_size + 90, cell_size,
                                         cell_size)
                pygame.draw.rect(screen, pygame.Color('black'), fruit_rect)

    def draw_score(self):
        """
        Afiseaza scorul prezent si scorul cel mai bun
        """
        global best_sore
        if len(self.snake.body) - 3 > int(best_sore):
            best_sore = str(len(self.snake.body) - 3)

        apple = pygame.image.load("plus/apple.png").convert_alpha()
        apple_size = (20, 20)
        apple = pygame.transform.scale(apple, apple_size).convert_alpha()

        cup = pygame.image.load("plus/cup.png").convert_alpha()
        cup_size = (20,20)
        cup = pygame.transform.scale(cup, cup_size).convert_alpha()


        # score = 'The best score is '
        score = str(best_sore)
        score_surface = pygame.font.Font(None, 30).render(score, True, 'red')
        int_x = 550
        int_y = 10
        score_rect = score_surface.get_rect(center=(int_x, int_y))
        cup_rect = cup.get_rect(midright=(score_rect.left-5, 10))
        screen.blit(cup, cup_rect)
        screen.blit(score_surface, score_rect)

        # score = 'The score is '
        score = str(len(self.snake.body) - 3)
        score_surface = pygame.font.Font(None, 30).render(score, True, 'red')
        int_x = 450
        int_y = 10
        score_rect = score_surface.get_rect(center=(int_x, int_y))
        apple_rect = apple.get_rect(midright=(score_rect.left-5, 10))
        screen.blit(apple, apple_rect)
        screen.blit(score_surface, score_rect)

    def check_eat_fruit(self):
        """
        Verifica daca sarpele nu a mancat fructul
        """
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.new_fruit()
            self.snake.level_up()
            self.check_fruit()

    def check_fruit(self):
        """
        Verifica daca noul frunct nu este pus peste sarpe, sau peste obstacol
        """
        for block in self.snake.body[1:]:
            if self.fruit.pos == block:
                self.fruit.new_fruit()
                self.check_fruit()
                break
        for obstacle in obstacles:
            if obstacle['x'] == self.fruit.x and obstacle['y'] == self.fruit.y:
                self.fruit.new_fruit()
                self.check_fruit()
                break

    def check_game_over(self):
        """
        Verifica daca sarpele nu se mananca pe el insusi, nu da cu capul de marginea tablei sau de obstacol
        """
        if not 0 <= self.snake.body[0].x < table_dimension or not 0 <= self.snake.body[0].y < table_dimension:
            self.game_over()

        for block in self.snake.body[1:]:
            if self.snake.body[0] == block:
                self.game_over()

        global obstacles
        for obstacle in obstacles:
            if self.snake.body[0].x == obstacle['x'] and self.snake.body[0].y == obstacle['y']:
                self.game_over()

    def game_over(self):
        """
        Se termina jocul
        """
        global game_while
        game_while = False
        main_game_over()


class Snake:
    def __init__(self):
        """
        Initializeaza clasa, creaza corpul sarpelui si directia by default e spre dreapta
        """
        self.body = [Vector2(int(table_dimension / 2), int(table_dimension / 2)),
                     Vector2(int(table_dimension / 2 - 1), int(table_dimension / 2)),
                     Vector2(int(table_dimension / 2 - 2), int(table_dimension / 2))]
        self.direction = RIGHT

    def draw_snake(self):
        """
        Deseneaza sarpele
        """
        body_rect = pygame.Rect(self.body[0].x * cell_size + 25, self.body[0].y * cell_size + 90, cell_size, cell_size)
        pygame.draw.rect(screen, (152, 251, 152), body_rect)
        for block in self.body[1:]:
            body_rect = pygame.Rect(block.x * cell_size + 25, block.y * cell_size + 90, cell_size, cell_size)
            pygame.draw.rect(screen, pygame.Color('green'), body_rect)

    def move_snake(self):
        """
        Modifica pozitia sarpelui stergand ultimul element din acesta si adaugand unul in directia coresponzatoare
        """
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def level_up(self):
        """
        Adauga un nou element element catre corpul sarpelui
        """
        self.body.insert(len(self.body), self.body[1])


class Fruit:
    def __init__(self):
        """
        Initializarea fructului
        """
        self.new_fruit()

    def draw_fruit(self):
        """
        Deseneaza fructul pe pozitia acestuia
        """
        fruit_rect = pygame.Rect(self.pos.x * cell_size + 25, self.pos.y * cell_size + 90, cell_size, cell_size)
        pygame.draw.rect(screen, pygame.Color('red'), fruit_rect)

    def new_fruit(self):
        """
        Adauga coordonatele x si y in mod random pentru fruct
        """
        self.x = random.randint(0, table_dimension - 1)
        self.y = random.randint(0, table_dimension - 1)
        self.pos = Vector2(self.x, self.y)


def main_menu():
    """
    Meniul principal pentru joc
    In timp ce jucatorul nu apasa pe Start, va ramane in meniu
    """
    start = button(table_x * 2 / 6, 420, 'Start')
    quit_button = button(table_x * 4 / 6, 420, 'Quit!')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((175, 215, 70))

        game_ovr = 'SNAKE'
        game_surface = pygame.font.Font(None, 70).render(game_ovr, True, 'red')
        int_x = table_x / 2
        int_y = 150
        score_rect = game_surface.get_rect(center=(int_x, int_y))
        screen.blit(game_surface, score_rect)

        game_ovr = 'When you are ready, press Start!'
        game_surface = pygame.font.Font(None, 30).render(game_ovr, True, 'red')
        int_x = table_x / 2
        int_y = 300
        score_rect = game_surface.get_rect(center=(int_x, int_y))
        screen.blit(game_surface, score_rect)

        if start.draw_button():
            print("Start")
            main_game()
            break
        if quit_button.draw_button():
            pygame.quit()
            sys.exit()

        pygame.display.update()


def main_game():
    """
    Functia ce simuleaza jocul. La fiecare apasare a tastei de directie aceasta se schimba.
    Jocul ruleaza pana jucatorul nu pierde sau nu iese voluntar din joc.
    """
    good_buy = button(table_x / 2, table_y - 30, 'Quit?')
    while game_while:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and game.snake.direction != DOWN:
                    game.snake.direction = UP
                elif event.key == pygame.K_DOWN and game.snake.direction != UP:
                    game.snake.direction = DOWN
                elif event.key == pygame.K_LEFT and game.snake.direction != RIGHT:
                    game.snake.direction = LEFT
                elif event.key == pygame.K_RIGHT and game.snake.direction != LEFT:
                    game.snake.direction = RIGHT

        screen.fill((175, 215, 70))
        game.draw_elements()

        if good_buy.draw_button():
            print("Quit")

        pygame.display.update()
        clock.tick(60)


def main_game_over():
    """
    Interfata dupa ce jucatorul pierde. Acesta are posibilitaea de a incepe un alt joc sau de a iesi.
    """
    yes_button = button(table_x * 2 / 6, 420, 'Yes!')
    quit_button = button(table_x * 4 / 6, 420, 'Quit!')
    global game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((175, 215, 70))

        game_ovr = 'GAME OVER'
        game_surface = pygame.font.Font(None, 70).render(game_ovr, True, 'red')
        int_x = table_x / 2
        int_y = 150
        score_rect = game_surface.get_rect(center=(int_x, int_y))
        screen.blit(game_surface, score_rect)

        score = 'The best score is '
        score += str(best_sore)
        score_surface = game_font.render(score, True, 'red')
        int_x = table_x / 2
        int_y = 200
        score_rect = score_surface.get_rect(center=(int_x, int_y))
        screen.blit(score_surface, score_rect)

        score = 'Now score is '
        score += str(len(game.snake.body) - 3)
        score_surface = game_font.render(score, True, 'red')
        int_x = table_x / 2
        int_y = 225
        score_rect = score_surface.get_rect(center=(int_x, int_y))
        screen.blit(score_surface, score_rect)

        again = 'Try again?'
        again_surface = pygame.font.Font(None, 60).render(again, True, 'blue')
        int_x = table_x / 2
        int_y = 320
        score_rect = again_surface.get_rect(center=(int_x, int_y))
        screen.blit(again_surface, score_rect)

        if yes_button.draw_button():
            print("YES!!")
            game = None
            game = Game()
            global game_while
            game_while = True
            main_game()
            break

        if quit_button.draw_button():
            pygame.quit()
            sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    '''
    Deschidem fisierul json pentru a extrage obstacolele si dimensiunea tablei.
    '''
    if len(sys.argv) != 2:
        print("Usage: python snake.py <config_file.json>")
        sys.exit(1)

    config_file = sys.argv[1]

    try:
        with open(config_file, 'r') as file:
            game_configuration = json.load(file)

        table_dimension = game_configuration['dimensiuneTabla']
        obstacles = game_configuration['obstacole']
        cell_size = 600 / table_dimension

        print("Dimensiune tabla:", table_dimension)
        print("Lista de obstacole:", obstacles)
        for obstacle in obstacles:
            print(obstacle)
            print(type(obstacle))

        pygame.init()
        screen = pygame.display.set_mode((table_x, table_y))
        clock = pygame.time.Clock()

        SCREEN_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(SCREEN_UPDATE, 150)
        game_font = pygame.font.Font(None, 25)

        game_while = True
        game = Game()
        main_menu()

    except FileNotFoundError:
        print(f"Fișierul {config_file} nu a fost găsit.")
    except json.JSONDecodeError:
        print(f"Fișierul {config_file} nu este un fișier JSON valid.")

# main_menu()
