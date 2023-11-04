import pygame
import random

pygame.init()

szer_okna = 550
wys_okna = 400

okno = pygame.display.set_mode((szer_okna, wys_okna))

wys_pal = 80
szer_pal = 10
x_p_pal = szer_okna - szer_pal
y_p_pal = wys_okna/2 - wys_pal/2
y_l_pal = wys_okna/2 - wys_pal/2
x_l_pal = 0
obszar_p_pal = pygame.Rect(x_p_pal, y_p_pal, szer_pal, wys_pal)
obszar_l_pal = pygame.Rect(x_l_pal, y_l_pal, szer_pal, wys_pal)

r_pilki = 10
x_pilki = szer_okna/2
y_pilki = random.randint(r_pilki, wys_okna - r_pilki)
kierunek_x = 1
kierunek_y = 1

#liczenie punktów
punkty = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_p_pal = y_p_pal - 20
            if event.key == pygame.K_DOWN:
                y_p_pal = y_p_pal + 20
                

    okno.fill((0,0,0))

    x_pilki = x_pilki + kierunek_x
    y_pilki = y_pilki + kierunek_y
    if y_pilki + r_pilki >=wys_okna or y_pilki - r_pilki <= 0:
        kierunek_y = kierunek_y * -1
    if x_pilki + r_pilki >= szer_okna - szer_pal:
        if y_pilki >= y_p_pal and y_pilki <+ y_p_pal + wys_pal:
            kierunek_x = kierunek_x * -1
            punkty =punkty + 1
    if x_pilki - r_pilki <= szer_pal:
        kierunek_x = kierunek_x * -1
    if x_pilki > szer_okna:
        kierunek_x = 0
        kierunek_y = 0
        y_pilki = wys_okna*2
        czcionka = pygame.font.SysFont('Arial',30)
        obraz_napisu = czcionka.render('KONIEC GRY', 1, (255,255,255))
        okno.blit(obraz_napisu,(szer_okna/2, 120))
    
    y_l_pal = y_pilki - wys_pal/2 
    obszar_p_pal = pygame.Rect(x_p_pal, y_p_pal, szer_pal, wys_pal)
    obszar_l_pal = pygame.Rect(x_l_pal, y_l_pal, szer_pal, wys_pal)

    pygame.draw.rect(okno,(255,0,0), obszar_p_pal)
    pygame.draw.rect(okno,(0,255,0), obszar_l_pal)
    pygame.draw.circle(okno, (0,0,255), (x_pilki, y_pilki), r_pilki)
#zapisywanie punktów
    czcionka = pygame.font.SysFont('Arial',15)
    obraz_napisu = czcionka.render(str(punkty), 1, (255,255,255))
    okno.blit(obraz_napisu,(szer_okna/2, 20))
#zatrzymanie pętli
    pygame.time.wait(10)
#odświeżanie 
    pygame.display.update()

