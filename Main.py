import pygame
from random import randint
from conf import screen_width, screen_height, valid_literal


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
default_font = pygame.font.SysFont('courier', 14)
text_rect = pygame.Surface(
    (100, 100), 
    pygame.SRCALPHA, 
    32
).convert_alpha()


def close_application():
    pygame.display.quit()
    pygame.quit()
    exit(0)

def print_word(rect, word):
    text_rect.fill((50, 50, 50))
    text_rect.blit(default_font.render(word, True, ((128, 128, 255))), (0, 0))



def main():
    words = []
    current_word = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_application()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print(words)
                    close_application()

                if event.key == pygame.K_SPACE and current_word:
                    words.append(current_word)
                    current_word = ""

                if event.key in valid_literal:
                    letter = pygame.key.name(event.key)
                    # check if shift is pressed
                    if pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                        letter = letter.upper()
                    current_word += letter                 

                if event.key == pygame.K_BACKSPACE:
                    current_word = current_word[:len(current_word) - 1]
                    # print(pygame.key.name(event.key))

        screen.fill((50, 50, 50))  
        print_word(text_rect, current_word)
        screen.blit(text_rect, (100, 100))
        pygame.display.update()


if __name__ == "__main__":
    main()
