import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg2_img = pg. transform.flip(bg_img, True, False)#練習8
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg. transform.flip(kk_img, True, False)#練習2
    
    kk_rct = kk_img.get_rect() #練習10－1　こうかとんRectの抽出
    kk_rct.center = 300, 200#練習10－2　中心座標の設定
    screen.blit(kk_img, kk_rct)#練習10－5
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        key_lst = pg.key.get_pressed()
        #print(key_lst[pg.K_UP])
        a = -1
        b = 0
        if key_lst[pg.K_UP]:
            kk_rct.move_ip(0, -1)
        if key_lst[pg.K_DOWN]:
            kk_rct.move_ip(0, 1)
        if key_lst[pg.K_RIGHT]:
            kk_rct.move_ip(2, 0)
        if key_lst[pg.K_LEFT]:
            kk_rct.move_ip(-1, 0)
        kk_rct.move_ip(a, b)
        x = tmr%3200#練習9
        screen.blit(bg_img, [-x, 0])#練習6
        screen.blit(bg2_img, [-x + 1600, 0])#練習7
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(kk_img, kk_rct)#練習4
        pg.display.update()
        tmr += 1        
        clock.tick(200)#練習5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()