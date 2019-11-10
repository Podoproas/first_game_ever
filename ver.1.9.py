import threading
from math import *
from random import *
from time import sleep

from pygame import *

init()


def letter_upper(letter):
    if letter in "qwertyuioplkjhgfdsazxcvbnm":
        return chr(ord(letter) - (ord("a") - ord("A")))
    return letter


def options_check(event1):
    global option_changing, started
    if option_changing != [False] * 5:
        option_changing = [False, False, False, False, False]
        return
    if texts[14][1].collidepoint(mouseX, mouseY):
        option_changing[0] = True
    if texts[15][1].collidepoint(mouseX, mouseY):
        option_changing[1] = True
    if texts[16][1].collidepoint(mouseX, mouseY):
        option_changing[2] = True
    if texts[17][1].collidepoint(mouseX, mouseY):
        option_changing[3] = True
    if texts[18][1].collidepoint(mouseX, mouseY):
        option_changing[4] = True
    if texts[19][1].collidepoint(mouseX, mouseY):
        started = 0


def save_all():
    try:
        OandS = open(r"C:\Users\Public\rhgtp.in", "w")
        OandS.write("162890%" + " " + str(key_up) + " " + str(key_right) + " " + str(key_down) + " " + str(
            key_left) + " " + str(key_weap) + "\n")
        OandS.write("163069% " + str(now_x) + " " + str(now_y) + "\n")
        OandS.write("137472% ")
        for elem in enemies:
            OandS.write(str(elem) + " ")
        OandS.write("\n141589% ")
        for elem in weapons:
            OandS.write(str(elem) + " ")
        OandS.write("\n176315% " + str(player.pos[0]) + " " + str(player.pos[1]) + "\n100598% " + str(speed) + "\n")
    except:
        pass


def create_all_texts():
    global texts, font1
    consts = [[70, 100], [35, 165], [200, 165], [35, 265], [200, 265], [35, 215], [200, 215], [35, 315], [200, 315],
              [600, 400], [240, 400]]
    font1 = font.Font("AirstreamNF.ttf", 65)
    texts = [font1.render("Menu", True, (0, 0, 0)),  # Menu ------- 0 (0)
             font1.render("Continue", True, (0, 0, 0)),  # Continue --- 1 (0)(1)
             font1.render("Options", True, (0, 0, 0)),  # Options ---- 2 (0)
             font1.render("Exit", True, (0, 0, 0)),  # Exit ------- 3 (0)(1)
             font1.render("Pause", True, (0, 0, 0)),  # Pause ------ 4 (1)
             font1.render("New game", True, (0, 0, 0)),  # New Game --- 5 (0)(1)
             font1.render("Main menu", True, (0, 0, 0)),  # Main Menu -- 6 (1)
             font1.render("Game over...", True, (0, 0, 0)),  # Game Over -- 7
             font1.render("Level UP!", True, (0, 0, 0)),  # Level Up --- 8
             font1.render("Controls", True, (0, 0, 0)),  # Controls --- 9
             font.Font("AirstreamNF.ttf", 40).render("UP", True, (0, 0, 0)),  # ------------ 10
             font.Font("AirstreamNF.ttf", 40).render("RIGHT", True, (0, 0, 0)),  # ------------ 11
             font.Font("AirstreamNF.ttf", 40).render("DOWN", True, (0, 0, 0)),  # ------------ 12
             font.Font("AirstreamNF.ttf", 40).render("LEFT", True, (0, 0, 0)),  # ------------ 13
             font.Font("AirstreamNF.ttf", 40).render(letter_upper(key_up), True, (130, 225, 100)),  # ------------ 14
             font.Font("AirstreamNF.ttf", 40).render(letter_upper(key_right), True, (130, 225, 100)),  # ------------ 15
             font.Font("AirstreamNF.ttf", 40).render(letter_upper(key_down), True, (130, 225, 100)),  # ------------ 16
             font.Font("AirstreamNF.ttf", 40).render(letter_upper(key_left), True, (130, 225, 100)),  # ------------ 17
             font.Font("AirstreamNF.ttf", 40).render(letter_upper(key_weap), True, (130, 225, 100)),  # ------------ 18
             font.Font("AirstreamNF.ttf", 60).render("Back", True, (0, 0, 0))]  # ------------ 19

    for i in range(len(texts)):
        texts[i] = [texts[i], texts[i].get_rect()]
        if i < 9:
            texts[i].append([width // 2 - texts[i][1][2] // 2, constants[i]])
        else:
            texts[i].append(consts[i - 9])
        texts[i][1][0], texts[i][1][1] = texts[i][2]
        texts[i].append(texts[i][2])

    font1 = font.Font("AirstreamNF.ttf", 32)


def key_up_checker(started):
    global shooting
    if started == 1:
        if not pause and i.button == 1:
            shooting = False
        elif pause:
            pause_check()


def key_down_checker(started):
    global pause, coordinates_text, freeze
    if started == 1:
        music_check(i.key)
        weapon_change_check(i.key)
        if i.key == 27 and not pause:
            pause = True
        elif i.key == K_F3 and not coordinates_text:
            coordinates_text = True
        elif i.key == K_F3:
            coordinates_text = False
        elif i.key == K_m and not freeze:
            freeze = True
        elif i.key == K_m and freeze:
            freeze = False
        else:
            player_move_check(i.key)


def fly(bullets):
    if not pause:
        ii = 0
        while ii < len(bullets):
            if bullets[ii]._flight():
                bullets.pop(ii)
                ii -= 1
            ii += 1
    return bullets


def blit_texts(list1, back):
    screen.blit(back, (0, 0))
    for i in list1:
        if i < len(texts):
            screen.blit(texts[i][0], texts[i][1])


def try_norm(list1):
    for i in list1:
        if texts[i][2][0] > texts[i][1][0]:
            texts[i][1][0] += 1
        elif texts[i][2][0] < texts[i][1][0]:
            texts[i][1][0] -= 1


def frame_check():
    if started == 0 or pause:
        if texts[1][1].collidepoint(mouseX, mouseY):
            texts[1][2] = [texts[1][3][0] + 50, texts[1][3][1]]
        else:
            texts[1][2] = texts[1][3][:]

        if texts[5][1].collidepoint(mouseX, mouseY):
            texts[5][2] = [texts[5][3][0] + 50, texts[5][3][1]]
        else:
            texts[5][2] = texts[5][3][:]

        if texts[3][1].collidepoint(mouseX, mouseY):
            texts[3][2] = [texts[3][3][0] + 50, texts[3][3][1]]
        else:
            texts[3][2] = texts[3][3][:]

    if started == 0:
        if texts[2][1].collidepoint(mouseX, mouseY):
            texts[2][2] = [texts[2][3][0] + 50, texts[2][3][1]]
        else:
            texts[2][2] = texts[2][3][:]

    if pause:
        if texts[6][1].collidepoint(mouseX, mouseY):
            texts[6][2] = [texts[6][3][0] + 50, texts[6][3][1]]
        else:
            texts[6][2] = texts[6][3][:]

    if started == 2:
        if texts[14][1].collidepoint(mouseX, mouseY):
            texts[14][2] = [texts[14][3][0] + 50, texts[14][3][1]]
        else:
            texts[14][2] = texts[14][3][:]

        if texts[15][1].collidepoint(mouseX, mouseY):
            texts[15][2] = [texts[15][3][0] + 50, texts[15][3][1]]
        else:
            texts[15][2] = texts[15][3][:]

        if texts[16][1].collidepoint(mouseX, mouseY):
            texts[16][2] = [texts[16][3][0] + 50, texts[16][3][1]]
        else:
            texts[16][2] = texts[16][3][:]

        if texts[17][1].collidepoint(mouseX, mouseY):
            texts[17][2] = [texts[17][3][0] + 50, texts[17][3][1]]
        else:
            texts[17][2] = texts[17][3][:]

        if texts[18][1].collidepoint(mouseX, mouseY):
            texts[18][2] = [texts[18][3][0] + 50, texts[18][3][1]]
        else:
            texts[18][2] = texts[18][3][:]

        if texts[19][1].collidepoint(mouseX, mouseY):
            texts[19][2] = [texts[19][3][0] + 50, texts[19][3][1]]
        else:
            texts[19][2] = texts[19][3][:]


def bullet_change(now_x1, now_y1, now_x2, now_y2):
    for bull in bullets:
        bull.pos[0] += (now_x2 - now_x1)
        bull.pos[1] += (now_y2 - now_y1)


def level_up_check():
    global started, scr, speed
    if len(enemies) == 0:
        speed += 1
        started = 2
        scr = level_up


def death_check(enemy):
    global started, scr
    if enemy.pos.colliderect(player.pos):
        started = 2
        scr = game_over


def move_him(enemy):
    dist = 10000
    if abs(enemy.pos[0] - player.pos[0]) < dist and abs(enemy.pos[1] - player.pos[1]) < dist and not freeze:
        enemy._line_move(player.pos[0], player.pos[1])


def merge(i):
    while i != 0 and enemies[i].pos.colliderect(enemies[i - 1].pos):
        if enemies[i - 1].hp < enemies[i].hp:
            enemies[i].hp += enemies[i - 1].hp
            enemies.pop(i - 1)
            i -= 1
        else:
            enemies[i - 1].hp += enemies[i].hp
            enemies.pop(i)
            i -= 1
    return i


def enemy_cicle():
    enemies.sort(key=lambda x: x.dist)
    if started == 1:
        i = 0
        while i < len(enemies):
            death_check(enemies[i])
            i = merge(i)
            move_him(enemies[i])
            i += 1


def READ_ALL_IN_THIS_FILE(VERY_NESSARY_TEXT_FILE_FOR_SAVES):
    for i in range(100):
        for j in range(150):
            VERY_NESSARY_TEXT_FILE_FOR_SAVES.write(choice(["0", "1", " "]))
        VERY_NESSARY_TEXT_FILE_FOR_SAVES.write("\n")


def quit_check(i):
    if i.type == QUIT:
        save_all()
        OandS.close()
        quit()
        sys.exit()


def music_check(key):
    global music_play
    if key == K_q and not music_play:
        mixer.music.unpause()
        music_play = True
    elif key == K_q and music_play:
        mixer.music.pause()
        music_play = False


def player_move_check(key):  # [W, D, S, A]
    if key == eval("K_" + key_up):
        is_moving[0] = True
    elif key == eval("K_" + key_right):
        is_moving[1] = True
    elif key == eval("K_" + key_down):
        is_moving[2] = True
    elif key == eval("K_" + key_left):
        is_moving[3] = True


def player_stop_check(key):  # [W, D, S, A]
    if key == K_w or key == K_UP:
        is_moving[0] = False
    elif key == K_d or key == 275:
        is_moving[1] = False
    elif key == K_s or key == K_DOWN:
        is_moving[2] = False
    elif key == K_a or key == 276:
        is_moving[3] = False


def create_all_new(cont):
    global player, now_x, now_y, bullets, enemies, is_moving, shoot_check, weapons, enemies_cord_set, pistol_ind, speed, timer1, shooting, coordinates_text, key_up, key_right, key_down, key_left, key_weap, img_types
    img_types = [(pistol, pistol_icon), (minigun, minigun_icon), (shotgun, shotgun_icon)]
    bullets = []
    player = PlayerObj(player_up, width // 2, hight // 2, 7 + speed)
    is_moving = [False, False, False, False]  # [W, D, S, A]
    pistol_ind = -1
    timer1 = threading.Timer(0, print())
    shooting = False
    coordinates_text = False
    enemies_cord_set = set()
    if not let_us_be_cool or not cont:
        enemies = []
        weapons = []
        now_x = -width * 6
        now_y = -hight * 6
        create_enemies(100, speed)
        create_weapons(randint(20, 25))
        key_up, key_right, key_down, key_left, key_weap = "w", "d", "s", "a", "e"
    else:
        inp = OandS.readline().rstrip().split()
        while inp != []:
            if inp[0] == "163069%":
                now_x = int(inp[1])
                now_y = int(inp[2])
            elif inp[0] == "137472%":
                enemies = []
                create_enemies(len(inp[1:]), speed, inp[1:])
            elif inp[0] == "162890%":
                key_up, key_right, key_down, key_left, key_weap = inp[1:]
            elif inp[0] == "141589%":
                weapons = []
                create_weapons(len(inp[1:]), inp[1:])
            elif inp[0] == "176315%":
                player.pos[0], player.pos[1] = int(inp[1]), int(inp[2])
            elif inp[0] == "100598%":
                speed = int(inp[1])
            inp = OandS.readline().rstrip().split()
        try:
            now_x
            now_y
        except:
            now_x = -width * 6
            now_y = -hight * 6
        try:
            enemies
        except:
            enemies = []
            create_enemies(100, speed)
        try:
            weapons
        except:
            weapons = []
            create_weapons(randint(20, 25))
        create_all_texts()
        OandS.close()


def menu_check():
    global started, scr
    if texts[5][1].collidepoint(mouseX, mouseY):
        started = 1
        create_all_new(False)
    elif texts[1][1].collidepoint(mouseX, mouseY):
        started = 1
        create_all_new(True)
    elif texts[3][1].collidepoint(mouseX, mouseY):
        save_all()
        OandS.close()
        quit()
        sys.exit()
    elif texts[2][1].collidepoint(mouseX, mouseY):
        started = 2
        scr = options


def pause_check():
    global pause, started
    if texts[1][1].collidepoint(mouseX, mouseY):
        pause = False
    if texts[6][1].collidepoint(mouseX, mouseY):
        started = 0
        pause = False
    if texts[5][1].collidepoint(mouseX, mouseY):
        pause = False
        started = 1
        create_all_new(False)
    if texts[3][1].collidepoint(mouseX, mouseY):
        save_all()
        OandS.close()
        quit()
        sys.exit()


def blit_new():
    if not pause and started == 1:
        screen.blit(background, (now_x, now_y))
        for bull in bullets:
            screen.blit(bull.img, bull.pos)
        for enemy in enemies:
            if enemy.pos.colliderect(screen.get_rect()):
                screen.blit(enemy.img, enemy.pos)
        for weapon in weapons:
            if weapon.pos.colliderect(screen.get_rect()):
                screen.blit(weapon.img, weapon.pos)
        screen.blit(player.weapon.icon, (width - player.weapon.icon_pos[2], 0))
        screen.blit(textSurfaceObj1, (0, 0))
        if player.weapon.bullets >= 0:
            text = font1.render(str(player.weapon.bullets), True, red)
            screen.blit(text, (width - (text.get_rect()[2]), player.weapon.icon_pos[3]))
        else:
            text = font1.render("Infinity", True, red)
            screen.blit(text, (width - (text.get_rect()[2]), player.weapon.icon_pos[3]))
        if coordinates_text:
            text = font1.render(str(abs(now_x) + player.pos[0] - 8) + " " + str(abs(now_y) + player.pos[1] - 8), True,
                                red)
            screen.blit(text, (0, (hight - text.get_rect()[3])))
        screen.blit(player.img, player.pos)


def create_enemies(num, enemy_speed, saved=None):
    global enemies_cord_set, enemies
    if saved is None:
        for i in range(num):
            rand_x = randint(-width * 5, width * 5)
            rand_y = randint(-width * 5, width * 5)
            while abs(rand_x - player.pos[0]) < 400 and abs(rand_y - player.pos[1]) < 400:
                rand_x = randint(-width * 5, width * 5)
                rand_y = randint(-hight * 5, hight * 5)
            enemies.append(EnemyObj(enemy_img, rand_x, rand_y, 3 + enemy_speed, 1))
            enemies_cord_set.add((enemies[-1].center[0], enemies[-1].center[1]))
    else:
        for i in range(0, len(saved), 3):
            enemies.append(EnemyObj(enemy_img, int(saved[i]), int(saved[i + 1]), 3 + enemy_speed, int(saved[i + 2])))
            enemies_cord_set.add((enemies[-1].center[0], enemies[-1].center[1]))


def enemies_change(stepx, stepy):
    global enemies_cord_set
    for i in range(len(enemies)):
        enemies_cord_set.discard((enemies[i].center[0], enemies[i].center[1]))
        enemies[i].pos[0] += stepx
        enemies[i].pos[1] += stepy
        enemies[i].center[:2] = [enemies[i].pos[0] + enemies[i].pos[2] // 2, enemies[i].pos[1] + enemies[i].pos[3] // 2]
        enemies_cord_set.add((enemies[i].center[0], enemies[i].center[1]))


def weapons_change(stepx, stepy):
    for i in range(len(weapons)):
        weapons[i].pos[0] += stepx
        weapons[i].pos[1] += stepy
        weapons[i].center = [weapons[i].pos[0] + weapons[i].pos[2] // 2, weapons[i].pos[1] + weapons[i].pos[3] // 2,
                             ((weapons[i].pos[0] + weapons[i].pos[2] // 2 - weapons[i].pos[0]) ** 2 +
                              (weapons[i].pos[1] + weapons[i].pos[3] // 2 - weapons[i].pos[1]) ** 2) ** 0.5]


def create_weapons(num, saved=None):
    global weapons
    if saved is None:
        for i in range(num):
            if randint(0, 1):
                weapons.append(WeaponObj(1, randint(-width * 5, width * 5), randint(-hight * 5, hight * 5), 1, 200))
            else:
                weapons.append(
                    WeaponObj(2, randint(-width * 5, width * 5), randint(-hight * 5, hight * 5), 15, 40, 5, 12))
    else:
        for i in range(0, num, 7):
            weapons.append(
                WeaponObj(int(saved[i + 6]), int(saved[i]), int(saved[i + 1]), int(saved[i + 2]), int(saved[i + 3]),
                          int(saved[i + 4]), int(saved[i + 5])))


def shot_check():
    global bullets, timer1
    if not timer1.is_alive() and shooting:
        shoot_one()
        timer1 = threading.Timer(player.weapon.shoot_speed / 20, sleep(0))
        timer1.start()


def shoot_one():
    global bullets
    if player.weapon.bullets != 0:
        player.weapon.bullets -= 1
        for i in range(player.weapon.bull_per_shot):
            bull_finish_x = randint(int(mouseX - (((player.center[0] - mouseX) ** 2 + (
                        player.center[1] - mouseY) ** 2) ** 0.5) ** 0.5 * player.weapon.accuracy), int(mouseX + (((
                                                                                                                              player.center[
                                                                                                                                  0] - mouseX) ** 2 + (
                                                                                                                              player.center[
                                                                                                                                  1] - mouseY) ** 2) ** 0.5) ** 0.5 * player.weapon.accuracy))
            bull_finish_y = randint(int(mouseY - (((player.center[0] - mouseX) ** 2 + (
                        player.center[1] - mouseY) ** 2) ** 0.5) ** 0.5 * player.weapon.accuracy), int(mouseY + (((
                                                                                                                              player.center[
                                                                                                                                  0] - mouseX) ** 2 + (
                                                                                                                              player.center[
                                                                                                                                  1] - mouseY) ** 2) ** 0.5) ** 0.5 * player.weapon.accuracy))
            if (player.center[0], player.center[1]) != (bull_finish_x, bull_finish_y):
                bullets.append(
                    BulletObj(bullet_img, player.center[0], player.center[1], 10, bull_finish_x, bull_finish_y,
                              player.center[0], player.center[1]))


def weapon_change_check(key):
    global player, pistol_ind
    if key == eval("K_" + key_weap):
        i = 0
        while i < len(weapons):
            if ((weapons[i].center[0] - player.center[0]) ** 2 + (
                    weapons[i].center[1] - player.center[1]) ** 2) ** 0.5 < 120:
                if weapons[i].icon == player.weapon.icon and player.weapon.bullets >= 0 and weapons[i].bullets > 0:
                    player.weapon.bullets += weapons[i].bullets
                    weapons.pop(i)
                    i -= 1
                else:
                    weapons[i], player.weapon = player.weapon, weapons[i]
                    player.weapon.pos[0] = -1
                    player.weapon.pos[1] = -1
                    weapons[i].pos[0] = player.pos[0]
                    weapons[i].pos[1] = player.pos[1]
                    pistol_ind = i
            i += 1


def player_revolution():
    x = (atan2(player.center[0] - mouseX, player.center[1] - mouseY) / pi) * 180
    player.img = transform.rotate(player_up, x)


def enemies_revolution():
    for enemy in enemies:
        now = enemy_img.get_rect()
        enemy.img = transform.scale(enemy_img, (now[2] + enemy.hp, now[3] + enemy.hp))
        x = (atan2(enemy.center[0] - player.center[0], enemy.center[1] - player.center[1]) / pi) * 180
        enemy.img = transform.rotate(enemy.img, x)
        enemy.pos[2], enemy.pos[3] = enemy.img.get_rect()[2], enemy.img.get_rect()[3]


class PlayerObj:
    def __init__(self, img, x, y, step):
        self.img = img
        self.x = x
        self.y = y
        self.step = step
        self.pos = img.get_rect().move(x, y)
        self.pos[0], self.pos[1] = self.pos[0] - self.pos[2] // 2, self.pos[1] - self.pos[3] // 2
        self.weapon = WeaponObj(1, -1, -1, 1)
        # self.weapon = WeaponObj(0, -1, -1, 15, -1, 0, 1)
        self.center = [self.pos[0] + self.pos[2] // 2,
                       self.pos[1] + self.pos[3] // 2,
                       ((self.pos[0] + self.pos[2] // 2 - self.pos[0]) ** 2 + (
                                   self.pos[1] + self.pos[3] // 2 - self.pos[1]) ** 2) ** 0.5]

    def _move(self, is_moving, step=7):
        global now_x, now_y
        i, j = now_x, now_y

        if is_moving[0] and self.pos[1] >= hight // 2:
            self.pos[1] -= step
        elif is_moving[0] and now_y + step <= 0:
            now_y += step
            enemies_change(0, step)
            weapons_change(0, step)
        elif is_moving[0] and now_y + step > 0 and self.pos[1] > step:
            self.pos[1] -= step

        if is_moving[1] and self.pos[0] <= width // 2:
            self.pos[0] += step
        elif is_moving[1] and now_x - step >= -(9 * width):
            now_x -= step
            enemies_change(-step, 0)
            weapons_change(-step, 0)
        elif is_moving[1] and now_x - step < -(9 * width) and self.pos[0] < width - self.pos[3] - step:
            self.pos[0] += step

        if is_moving[2] and self.pos[1] <= hight // 2:
            self.pos[1] += step
        elif is_moving[2] and now_y - step >= -(9 * hight) + 15:
            now_y -= step
            enemies_change(0, -step)
            weapons_change(0, -step)
        elif is_moving[2] and now_y - step > -(9 * hight) - 15 and self.pos[1] < hight - self.pos[3] - step:
            self.pos[1] += step

        if is_moving[3] and self.pos[0] >= width // 2:
            self.pos[0] -= step
        elif is_moving[3] and now_x + step <= 0:
            now_x += step
            enemies_change(step, 0)
            weapons_change(step, 0)
        elif is_moving[3] and now_x + step > 0 and self.pos[0] > step:
            self.pos[0] -= step

        enemies_revolution()

        bullet_change(i, j, now_x, now_y)
        self.center = [self.pos[0] + self.pos[2] // 2, self.pos[1] + self.pos[3] // 2, (
                    (self.pos[0] + self.pos[2] // 2 - self.pos[0]) ** 2 + (
                        self.pos[1] + self.pos[3] // 2 - self.pos[1]) ** 2) ** 0.5]


class BulletObj:
    def __init__(self, img, x, y, step, mX, mY, player_pos_0, player_pos_1):
        self.img = img
        self.x = x
        self.y = y
        self.step = step
        self.pos = img.get_rect().move(x, y)
        self.mX = mX
        self.mY = mY
        self.pX = player_pos_0
        self.pY = player_pos_1

    def _flight(self):
        global enemies
        length = ((self.mX - self.pX) ** 2 + (self.mY - self.pY) ** 2) ** 0.5
        if length != 0:
            self.pos[0] += (self.step * 2) * (self.mX - self.pX) / length
            self.pos[1] += (self.step * 2) * (self.mY - self.pY) / length
        new_set = set()
        i = 0
        while i < len(enemies):
            if self.pos.colliderect(enemies[i].pos):
                enemies[i].hp -= 1
                if enemies[i].hp <= 0:
                    enemies_cord_set.discard((enemies[i].center[0], enemies[i].center[1]))
                    enemies.pop(i)
                self.pos[0] = -1
                break
            i += 1
        return self.pos[0] > width or self.pos[0] < 0 or self.pos[1] > hight or self.pos[1] < 0


class WeaponObj:
    def __init__(self, img_type, x, y, shoot_speed, bullets=-1, accuracy=1, bull_per_shot=1):
        self.img_type = img_type
        self.img = img_types[img_type][0]
        self.icon = img_types[img_type][1]
        self.x = x
        self.y = y
        self.pos = img_types[img_type][0].get_rect().move(x, y)
        self.icon_pos = img_types[img_type][1].get_rect().move(x, y)
        self.shoot_speed = shoot_speed
        self.bullets = bullets
        self.accuracy = accuracy
        self.bull_per_shot = bull_per_shot
        self.center = [self.pos[0] + self.pos[2] // 2, self.pos[1] + self.pos[3] // 2,
                       ((self.pos[0] + self.pos[2] // 2 - self.pos[0]) ** 2 +
                        (self.pos[1] + self.pos[3] // 2 - self.pos[1]) ** 2) ** 0.5]

    def __str__(self):
        return str(self.pos[0]) + " " + str(self.pos[1]) + " " + str(self.shoot_speed) + " " + str(
            self.bullets) + " " + str(self.accuracy) + " " + str(self.bull_per_shot) + " " + str(self.img_type)


class EnemyObj:
    def __init__(self, img, x, y, step, hp=1):
        self.img = img
        self.x = x
        self.y = y
        self.step = step
        self.pos = img.get_rect().move(x, y)
        self.center = [self.pos[0] + self.pos[2] // 2, self.pos[1] + self.pos[3] // 2,
                       ((self.pos[0] + self.pos[2] // 2 - self.pos[0]) ** 2 +
                        (self.pos[1] + self.pos[3] // 2 - self.pos[1]) ** 2) ** 0.5]
        self.hp = hp
        self.dist = ((now_x - self.center[0]) ** 2 + (now_y - self.center[1]) ** 2) ** 0.5

    def _line_move(self, pX, pY):
        global enemies_cord_set
        length = ((self.pos[0] - pX) ** 2 + (self.pos[1] - pY) ** 2) ** 0.5
        if length != 0:
            enemies_cord_set.discard((self.center[0], self.center[1]))
            early_x = self.pos[0]
            early_y = self.pos[1]
            self.pos[0] -= self.step * (self.pos[0] - pX) / length
            self.pos[1] -= self.step * (self.pos[1] - pY) / length
            self.center[:2] = [self.pos[0] + self.pos[2] // 2, self.pos[1] + self.pos[3] // 2]
            enemies_cord_set.add((self.center[0], self.center[1]))
            self.dist = ((now_x - self.center[0]) ** 2 + (now_y - self.center[1]) ** 2) ** 0.5

    def __str__(self):
        return (str(self.pos[0]) + " " + str(self.pos[1]) + " " + str(self.hp))


# VERY_NESSARY_TEXT_FILE_FOR_SAVES = open("preferances", "w")
# READ_ALL_IN_THIS_FILE(VERY_NESSARY_TEXT_FILE_FOR_SAVES)

background = image.load('background.png')
menu = image.load('clishe.jpg')
pause_img = transform.flip(menu, True, True)
options = transform.flip(menu, True, False)
player_up = image.load('player_up.png')
bullet_img = image.load('bullet.png')
enemy_img = image.load("enemy.png")
game_over = image.load("game_over.png")
level_up = image.load("level_up.png")
pistol_icon = image.load("pistol.png")
pistol = transform.scale(pistol_icon, (pistol_icon.get_rect()[2] // 3, pistol_icon.get_rect()[3] // 3))
minigun_icon = image.load("minigun.png")
minigun = transform.scale(minigun_icon, (minigun_icon.get_rect()[2] // 3, minigun_icon.get_rect()[3] // 3))
shotgun_icon = image.load("shotgun.png")
shotgun = transform.scale(shotgun_icon, (shotgun_icon.get_rect()[2] // 3, shotgun_icon.get_rect()[3] // 3))

mixer.music.load('main_music.mp3')
music_play = True
# mixer.music.play(-1)

width, hight = 640, 480
# width, hight = map(int, input().split())
icon = image.load('icon.png')
display.set_icon(icon)
screen = display.set_mode((width, hight))
display.set_caption('ver. 1.9')

fpsClock = time.Clock()
started = 0
freeze = False
FPS = 100
pause = False
red = (255, 0, 0)
speed = 0
key_up, key_right, key_down, key_left, key_weap = "w", "d", "s", "a", "e"
option_changing = [False] * 5
constants = [35, 155, 285, 360, 35, 215, 285, 0, 0, 228]
just_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
             19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

create_all_texts()

try:
    OandS = open(r"C:\Users\Public\rhgtp.in")
    let_us_be_cool = True
except:
    OandS = open(r"C:\Users\Public\rhgtp.in", "w")
    OandS.close()
    OandS = open(r"C:\Users\Public\rhgtp.in")
    let_us_be_cool = False

while True:
    if started == 0:
        for i in event.get():
            quit_check(i)
            if i.type == KEYDOWN:
                music_check(i.key)
            if i.type == MOUSEMOTION:
                mouseX, mouseY = i.pos
                frame_check()
            if i.type == MOUSEBUTTONUP:
                mouseX, mouseY = i.pos
                menu_check()
        try_norm([1, 2, 3, 5])
        blit_texts([0, 1, 2, 3, 5], menu)
        display.update()
        fpsClock.tick(FPS)
    elif started == 2:
        for i in event.get():
            quit_check(i)
            if scr == options:
                if i.type == MOUSEBUTTONDOWN:
                    mouseX, mouseY = i.pos
                    options_check(i)
                if i.type == MOUSEMOTION:
                    frame_check()
                try_norm(just_nums[9:20])
                blit_texts(just_nums[9:20], options)
            else:
                if i.type == MOUSEBUTTONUP:
                    started = 0
                screen.blit(scr, (0, 0))
        display.update()
    else:
        for i in event.get():
            quit_check(i)
            if i.type == KEYDOWN:
                key_down_checker(started)
            if i.type == KEYUP:
                player_stop_check(i.key)
            if i.type == MOUSEMOTION:
                mouseX, mouseY = i.pos
                frame_check()
                player_revolution()
            if i.type == MOUSEBUTTONDOWN:
                mouseX, mouseY = i.pos
                if not pause and i.button == 1:
                    shooting = True
            if i.type == MOUSEBUTTONUP:
                key_up_checker(started)
        bullets = fly(bullets)
        textSurfaceObj1 = font1.render(str(len(enemies)), True, red)

        if pause:
            try_norm([1, 3, 5, 6])
            blit_texts([1] + just_nums[3:7], pause_img)
        else:
            shot_check()
            level_up_check()
            enemy_cicle()
            player._move(is_moving, player.step)
            blit_new()

        display.update()
        fpsClock.tick(FPS)

        if speed == 100:
            quit()
            sys.exit()
