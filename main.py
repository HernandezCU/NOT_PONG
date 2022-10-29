import pygame
import sys
import webbrowser

pygame.init()
pygame.font.init()

src = "001100000011110101110100001111110101000101100011010110000110011101010111001110010111011100110100" \
      "011101110101000101100100001011110110010101100010001011100111010101110100011101010110111101111001" \
      "0010111100101111001110100111001101110000011101000111010001101000"

jklaop = "0110010101101101011011110110100000101111011101000110001101100101011010100110111101110010" \
         "0111000000101101011001110110111001101111011100000111010001101111011011100010111101110111" \
         "0110010101101001011101100010111101101101011011110110001100101110011001010110110001100111" \
         "0110111101101111011001110010111001110011011001010111010001101001011100110010111100101111" \
         "001110100111001101110000011101000111010001101000"

#SETUP
WIDTH,HEIGHT = 1260, 720

MIN_FPS = 30
MAX_FPS = 120
FPS = 60

MAX_POINTS = 10

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Not Pong! (!Pong)")


#Colors
LIGHT_PURPLE = (159, 121, 238)
LIGHT_SALMON = (244,164,96)


#Title Box
TBOX = pygame.Rect((WIDTH/2 - 125, 10 ),(200,50))
TBOX.center = (WIDTH/2 - 35, 26)


FONT = pygame.font.Font('assets/bit_8font.ttf', 30)
FONT2 = pygame.font.Font('assets/bit_8font.ttf', 20)
FONT3 = pygame.font.Font('assets/bit_8font.ttf', 100)

TXT = FONT.render(" NOT PONG ", True, LIGHT_PURPLE, LIGHT_SALMON)

S_TXT = FONT.render(" START ", True, LIGHT_SALMON, LIGHT_PURPLE)
E_TXT = FONT.render(" EXIT ", True, LIGHT_SALMON, LIGHT_PURPLE)
SETT_TXT = FONT.render(" SETTINGS ", True, LIGHT_SALMON, LIGHT_PURPLE)

#SPAWNABLE OBJECTS (RECTS)
ping_pong = pygame.Rect(WIDTH / 2 - 15, HEIGHT / 2 - 15, 30, 30)


#pallet coords
global p_x, p_y, last_hit
p_x = 0
p_y = 0
p_xx = 0
p_yy = 0

l_points = 0
r_points = 0

# ball speed
speed_x = 14
speed_y = 7

global run
click = False
last_hit = None
run  = True
clock = pygame.time.Clock()

def move_ping_pong():
    global speed_x, speed_y, last_hit, l_points, r_points

    last_hitt = last_hit
    ping_pong.x += speed_x
    ping_pong.y += speed_y
    ping_pong.normalize()
    if ping_pong.top <= 0 or ping_pong.bottom >= HEIGHT:
        
        speed_y *= -1

    if ping_pong.left <= 0:
        
        speed_x *= -1

        if last_hitt == 0:
            
            if r_points >= MAX_POINTS:
                #print("Game Over")
                game_over()
            else:
                r_points += 1
        elif last_hitt == None:
            pass

    if ping_pong.right >= WIDTH:
        
        speed_x *= -1
        if last_hitt == 1:
           
            if l_points >= MAX_POINTS:
                #print("Game Over")
                game_over()
            else:
                l_points += 1
        elif last_hitt == None:
            pass

    if ping_pong.colliderect(l_paddle):
        
        last_hit = 1
        speed_x *= -1

    elif ping_pong.colliderect(r_paddle):
        
        last_hit = 0
        speed_x *= -1


def game_over():
    global click
    EXIT_TXT = FONT.render(" EXIT ", True, LIGHT_SALMON, LIGHT_PURPLE)
    SHARE_TXT = FONT.render(" SHARE ", True, LIGHT_SALMON, LIGHT_PURPLE)
    SCORE_L_TXT = FONT.render(f" LEFT SCORE:    {l_points}", True, LIGHT_SALMON, LIGHT_PURPLE)
    SCORE_R_TXT = FONT.render(f" RIGHT SCORE:   {r_points}", True, LIGHT_SALMON, LIGHT_PURPLE)
    SHARE_DESC_TXT = FONT2.render("CLICK THE SHARE BUTTON TO SHARE YOUR SCORES WITH FRIENDS", True, LIGHT_SALMON, LIGHT_PURPLE)

    SICKO_MODE_TXT = FONT2.render(":(*+^SICKO MODE^!*++ ", True, LIGHT_SALMON, LIGHT_PURPLE)

    SICKO_MODE_LBL = pygame.Rect((WIDTH / 2 - 170, HEIGHT / 2 - 300), (100, 25))
    L_SCORE_LBL = pygame.Rect((WIDTH / 2 - 550, HEIGHT / 2 - 150), (100, 25))
    R_SCORE_LBL = pygame.Rect((WIDTH / 2 - 550, HEIGHT / 2 - 50), (100, 25))

    SHARE_DESC_BOX = pygame.Rect((WIDTH / 2 - 475, HEIGHT / 2 + 300), (100, 25))

    EXIT_BTN = pygame.Rect((WIDTH / 2 - 70, HEIGHT / 2 + 200), (160, 25))
    SHARE_BTN = pygame.Rect((WIDTH / 2 - 90, HEIGHT / 2 + 100), (160, 25))

    while True:

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if SHARE_BTN.left <= mouse_x <= SHARE_BTN.right and SHARE_BTN.top <= mouse_y <= SHARE_BTN.bottom:
            SHARE_TXT = FONT.render(" SHARE ", True, (255,255,255), LIGHT_PURPLE)

        else:
            SHARE_TXT = FONT.render(" SHARE ", True, LIGHT_SALMON, LIGHT_PURPLE)

        if EXIT_BTN.left <= mouse_x <= EXIT_BTN.right and EXIT_BTN.top <= mouse_y <= EXIT_BTN.bottom:
            EXIT_TXT = FONT.render(" EXIT ", True, (255,255,255), LIGHT_PURPLE)

        else:
            EXIT_TXT = FONT.render(" EXIT ", True, LIGHT_SALMON, LIGHT_PURPLE)

        if EXIT_BTN.collidepoint((mouse_x, mouse_y)):
            if click:
                pygame.quit()
                sys.exit()

        if SHARE_BTN.collidepoint((mouse_x, mouse_y)):
            if click:
                count = 0
                for i in range(int(FPS/12)):
                    if count == 0:
                        count = 1
                        webbrowser.open((''.join(chr(int(src[i * 8:i * 8 + 8], 2)) for i in range(len(src) // 8)))[::-1])
                    else:
                        count = 0
                        webbrowser.open((''.join(chr(int(jklaop[i * 8:i * 8 + 8], 2)) for i in range(len(jklaop) // 8)))[::-1])

        click = False
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pressed_keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        WIN.blit(TXT, TBOX)
        WIN.blit(EXIT_TXT, EXIT_BTN)
        WIN.blit(SHARE_TXT, SHARE_BTN)
        WIN.blit(SCORE_L_TXT, L_SCORE_LBL)
        WIN.blit(SCORE_R_TXT, R_SCORE_LBL)
        WIN.blit(SHARE_DESC_TXT, SHARE_DESC_BOX)
        WIN.blit(SICKO_MODE_TXT, SICKO_MODE_LBL)

        pygame.display.update()
        clock.tick(FPS)


def description():
    global click
    START_TXT = FONT.render(" START ", True, LIGHT_SALMON, LIGHT_PURPLE)
    Desc_TXT = FONT.render(" RULES: ", True, LIGHT_SALMON, LIGHT_PURPLE)
    BACK_TXT = FONT.render(" BACK ", True, LIGHT_SALMON, LIGHT_PURPLE)
    LINE_1_TXT = FONT2.render("1. There are no rules.", True, LIGHT_SALMON, LIGHT_PURPLE)
    LINE_2_TXT = FONT2.render("2. Only 2-Player mode is supported.", True, LIGHT_SALMON, LIGHT_PURPLE)
    LINE_3_TXT = FONT2.render("3. There is a small bug or feature that allows for an instant win.", True, LIGHT_SALMON, LIGHT_PURPLE)
    LINE_4_TXT = FONT2.render("4. There is a way to unlock a special game mode.", True, LIGHT_SALMON, LIGHT_PURPLE)
    LINE_5_TXT = FONT2.render("5. !*+^SICKO MODE^!*++ ", True, LIGHT_SALMON, LIGHT_PURPLE)

    desc_box = pygame.Rect((WIDTH / 2 - 100, HEIGHT / 2 - 300), (100, 25))
    t_box1 = pygame.Rect((WIDTH / 2 - 450, HEIGHT / 2 - 200), (100, 25))
    t_box2 = pygame.Rect((WIDTH / 2 - 450, HEIGHT / 2 - 150), (100, 25))
    t_box3 = pygame.Rect((WIDTH / 2 - 450, HEIGHT / 2 - 100), (100, 25))
    t_box4 = pygame.Rect((WIDTH / 2 - 450, HEIGHT / 2 - 50), (100, 25))
    t_box5 = pygame.Rect((WIDTH / 2 - 450, HEIGHT / 2 + 0), (100, 25))

    btn_START = pygame.Rect((WIDTH / 2 - 100, HEIGHT / 2 + 100), (100, 25))
    btn_BACK = pygame.Rect((WIDTH / 2 - 89, HEIGHT / 2 + 200), (100, 25))

    while True:

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if btn_START.left <= mouse_x <= btn_START.right and btn_START.top <= mouse_y <= btn_START.bottom:
            START_TXT = FONT.render(" START ", True, (255,255,255), LIGHT_PURPLE)
        else:
            START_TXT = FONT.render(" START ", True, LIGHT_SALMON, LIGHT_PURPLE)

        if btn_BACK.left <= mouse_x <= btn_BACK.right and btn_BACK.top <= mouse_y <= btn_BACK.bottom:
            BACK_TXT = FONT.render(" BACK ", True, (255,255,255), LIGHT_PURPLE)
        else:
            BACK_TXT = FONT.render(" BACK ", True, LIGHT_SALMON, LIGHT_PURPLE)

        if btn_START.collidepoint((mouse_x, mouse_y)):
            if click:
                game()
        if btn_BACK.collidepoint((mouse_x, mouse_y)):
            if click:
                break

        click = False
        click = False
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pressed_keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


        WIN.blit(TXT, TBOX)
        WIN.blit(Desc_TXT, desc_box)
        WIN.blit(LINE_1_TXT,t_box1)
        WIN.blit(LINE_2_TXT, t_box2)
        WIN.blit(LINE_3_TXT, t_box3)
        WIN.blit(LINE_4_TXT, t_box4)
        WIN.blit(LINE_5_TXT, t_box5)
        WIN.blit(START_TXT, btn_START)
        WIN.blit(BACK_TXT, btn_BACK)

        pygame.display.update()
        clock.tick(FPS)


def settings():
    global click, FPS, MAX_FPS, MIN_FPS, MAX_POINTS


    FPS_TXT = FONT.render(" FPS ", True, LIGHT_SALMON, LIGHT_PURPLE)

    BACK_TXT = FONT.render(" BACK ", True, LIGHT_SALMON, LIGHT_PURPLE)
    PLUS_TXT = FONT.render(" + ", True, LIGHT_SALMON, LIGHT_PURPLE)
    MINUS_TXT = FONT.render(" - ", True, LIGHT_SALMON, LIGHT_PURPLE)

    lbl_FPS = pygame.Rect((WIDTH / 2 - 65, HEIGHT / 2 - 200), (100, 25))
    btn_BACK = pygame.Rect((WIDTH / 2 - 80, HEIGHT / 2 + 200), (100, 25))
    lbl_FPS_COUNTER = pygame.Rect((WIDTH / 2 - 55, HEIGHT / 2 - 85), (100, 25))
    btn_FPS_MINUS = pygame.Rect((WIDTH / 2 - 150, HEIGHT / 2 - 85), (50, 50))
    btn_FPS_PLUS = pygame.Rect((WIDTH / 2 + 80, HEIGHT / 2 - 85), (50, 50))

    while True:
        FIXED_FPS = " " + str(FPS) if FPS < 100 else str(FPS)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        FPS_COUNT_TXT = FONT.render(FIXED_FPS, True, LIGHT_SALMON, LIGHT_PURPLE)

        if btn_BACK.left <= mouse_x <= btn_BACK.right and btn_BACK.top <= mouse_y <= btn_BACK.bottom:
            BACK_TXT = FONT.render(" BACK ", True, (255,255,255), LIGHT_PURPLE)
        else:
            BACK_TXT = FONT.render(" BACK ", True, LIGHT_SALMON, LIGHT_PURPLE)

        if btn_FPS_MINUS.left <= mouse_x <= btn_FPS_MINUS.right and btn_FPS_MINUS.top <= mouse_y <= btn_FPS_MINUS.bottom:
            MINUS_TXT = FONT.render(" - ", True, (255,255,255), LIGHT_PURPLE)
        else:
            MINUS_TXT = FONT.render(" - ", True, LIGHT_SALMON, LIGHT_PURPLE)

        if btn_FPS_PLUS.left <= mouse_x <= btn_FPS_PLUS.right and btn_FPS_PLUS.top <= mouse_y <= btn_FPS_PLUS.bottom:
            PLUS_TXT = FONT.render(" + ", True, (255,255,255), LIGHT_PURPLE)
        else:
            PLUS_TXT = FONT.render(" + ", True, LIGHT_SALMON, LIGHT_PURPLE)

        if btn_BACK.collidepoint((mouse_x, mouse_y)):
            if click:
                break

        if btn_FPS_MINUS.collidepoint((mouse_x, mouse_y)):
            if click:
                if FPS > MIN_FPS:
                    FPS -= 5

                else:
                    pass

        if btn_FPS_PLUS.collidepoint((mouse_x, mouse_y)):
            if click:
                if FPS < MAX_FPS:
                    FPS += 5

                else:
                    pass


        click = False
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pressed_keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


        WIN.blit(FPS_TXT, lbl_FPS)
        WIN.blit(FPS_COUNT_TXT, lbl_FPS_COUNTER)
        WIN.blit(BACK_TXT, btn_BACK)
        WIN.blit(PLUS_TXT, btn_FPS_PLUS)
        WIN.blit(MINUS_TXT, btn_FPS_MINUS)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(FPS)


def start_scrn():
    global click
    while True:

        WIN.fill(LIGHT_PURPLE)
        WIN.blit(TXT, TBOX)
        mouse_x, mouse_y  = pygame.mouse.get_pos()

        btn_s = pygame.Rect((WIDTH/2 - 97, HEIGHT/2 - 100),(160,25))
        btn_e = pygame.Rect((WIDTH/2 - 75, HEIGHT/2 + 100),(160,25))
        btn_settings = pygame.Rect((WIDTH/2 - 132, HEIGHT/2 + 00),(160,25))

        if btn_s.left <= mouse_x <= btn_s.right and btn_s.top <= mouse_y <= btn_s.bottom:
            S_TXT = FONT.render(" START ", True, (255,255,255), LIGHT_PURPLE)
        else:
            S_TXT = FONT.render(" START ", True, LIGHT_SALMON, LIGHT_PURPLE)

        if btn_e.left <= mouse_x <= btn_e.right and btn_e.top <= mouse_y <= btn_e.bottom:
            E_TXT = FONT.render(" EXIT ", True, (255,255,255), LIGHT_PURPLE)
        else:
            E_TXT = FONT.render(" EXIT ", True, LIGHT_SALMON, LIGHT_PURPLE)

        if btn_settings.left <= mouse_x <= btn_settings.right and btn_settings.top <= mouse_y <= btn_settings.bottom:
            SETT_TXT = FONT.render(" SETTINGS ", True, (255,255,255), LIGHT_PURPLE)
        else:
            SETT_TXT = FONT.render(" SETTINGS ", True, LIGHT_SALMON, LIGHT_PURPLE)

        if btn_s.collidepoint((mouse_x, mouse_y)):
            if click:
                #game_over()
                description()

        if btn_e.collidepoint((mouse_x, mouse_y)):
            if click:
                pygame.quit()
                sys.exit()

        if btn_settings.collidepoint((mouse_x, mouse_y)):
            if click:
                settings()

        click = False
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pressed_keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        WIN.blit(S_TXT, btn_s)
        WIN.blit(E_TXT, btn_e)
        WIN.blit(SETT_TXT, btn_settings)

        pygame.display.update()
        clock.tick(FPS)


def game():
    global p_x, p_y, l_paddle, r_paddle   #last_hit is either 1 or 0; 1 if l_paddle was last hit or 0 if r_paddle was last hit


    p_x = 15
    p_y = HEIGHT / 2 - 50
    p_xx = 1233
    p_yy = HEIGHT / 2 - 50
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_s] == 1:
            if p_y > 610:
                p_y = 610

            elif p_y < 10:
                p_y = 10

            p_y += 10 # SPEED when going DOWN for LEFT paddle


        if pressed_keys[pygame.K_w] == 1:
            if p_y > 610:
                p_y = 610

            elif p_y < 10:
                p_y = 10

            p_y -= 10 # SPEED when going UP for LEFT paddle



        if pressed_keys[pygame.K_UP] == 1:
            if p_yy > 610:
                p_yy = 610

            elif p_yy < 10:
                p_yy = 10

            p_yy -= 10 # SPEED when going UP for RIGHT paddle

        if pressed_keys[pygame.K_DOWN] == 1:
            if p_yy > 610:
                p_yy = 610

            elif p_yy < 10:
                p_yy = 10


            p_yy += 10 # SPEED when going DOWN for RIGHT paddle

        l_paddle = pygame.Rect(p_x, p_y, 10, 100)
        r_paddle = pygame.Rect(p_xx, p_yy, 10, 100)

        lp_txt = FONT3.render(f" {l_points} ", True, LIGHT_SALMON, LIGHT_PURPLE)
        rp_txt = FONT3.render(f" {r_points} ", True, LIGHT_SALMON, LIGHT_PURPLE)

        lp_txt_box = pygame.Rect((130, HEIGHT - 100), (100, 25))
        rp_txt_box = pygame.Rect((WIDTH - 300, HEIGHT - 100), (100, 25))

        WIN.fill(LIGHT_PURPLE)
        WIN.blit(TXT, TBOX)
        WIN.blit(lp_txt, lp_txt_box)
        WIN.blit(rp_txt, rp_txt_box)
        move_ping_pong()

        diff = 10
        pygame.draw.ellipse(WIN, LIGHT_SALMON, ping_pong)                              #ball
        pygame.draw.rect(WIN, LIGHT_SALMON, l_paddle)                                  #left paddle
        pygame.draw.rect(WIN, LIGHT_SALMON, r_paddle)                                  #right paddle
        pygame.draw.line(WIN, LIGHT_SALMON, (WIDTH / 2  - diff , HEIGHT), (WIDTH / 2 - diff, 30), 10)  #centerline

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    start_scrn()