import pygame
from random import randint
import time

pygame.init()

#jendela
latar = (48, 227, 202)
jendela = pygame.display.set_mode((500,500))
jendela.fill(latar)
timer = pygame.time.Clock()

#Persegi
class Area():
    def __init__ (self, x=0, y=0, w=10, h=10, color=None):
        self.rect = pygame.Rect(x, y, w, h,)
        self.fill_color = color
    
    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(jendela, self.fill_color, self.rect)

    def outline(self, frame_color, thickness):
        pygame.draw.rect(jendela, frame_color, self.rect, thickness)

    def sentuh(self, x, y):
        return self.rect.collidepoint(x, y)

class Label(Area):
    def set_text(self, tulisan, fsize=12, text_color=(64, 81, 78)):
        self.tulisan = pygame.font.SysFont('verdana', fsize).render(tulisan, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        jendela.blit(self.tulisan, (self.rect.x + shift_x, self.rect.y + shift_y ))
#warna
wkartu = (17, 153, 158)
woutline = (64, 81, 78)

wklik = (0, 255, 51)
nklik = (255, 0, 0)

wmenang = (0, 255, 128)
wkalah = (255, 102, 102)

#kartu
kartu = []
jumlah_kartu = 4


x = 70

start_time = time.time()
curtime = start_time

timetext = Label(0, 0, 50, 50, latar)
timetext.set_text('WAKTU:', 30, woutline )
timetext.draw(20,20)

timtext = Label(50, 55, 50, 40, latar)
timtext.set_text('0', 30, woutline )
timtext.draw(0,0)
#skor
skrtext = Label(380, 0, 50, 50, latar)
skrtext.set_text('SKOR:', 30, woutline )
skrtext.draw(20,20)

skor = Label(425, 55, 50, 50, latar)
skor.set_text('0', 30, woutline )
skor.draw(0,0)

for i in range (jumlah_kartu) :
    kartu_baru = Label(x, 170, 70, 100, wkartu)
    kartu_baru.outline(woutline, 10)
    kartu_baru.set_text('klik', 30)
    kartu.append(kartu_baru)
    x += 100

waktu = 0
nilai = 0


while True :
    if waktu == 0 :
        waktu = 2
        klik = randint(1, jumlah_kartu)
        for i in range (jumlah_kartu):
            kartu[i].color(wkartu)
            if (i + 1) == klik :
                kartu[i].draw(10, 40)
            else:
                kartu[i].fill()
    else:
        waktu -= 1

    #cek
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            for i in range(jumlah_kartu):
                if kartu[i].sentuh(x, y):
                    if i + 1 == klik:
                        kartu[i].color(wklik)
                        nilai += 1
                    else:
                        kartu[i].color(nklik)
                        nilai -= 1
                    kartu[i].fill()
                    skor.set_text(str(nilai), 40, woutline)
                    skor.draw(0,0)

    newtime = time.time()
    if newtime - start_time >= 11:
        klh = Label(0,0,500,500,wkalah)
        klh.set_text('Yah kamu kalah', 60, woutline)
        klh.draw(110,180) 
        break   

    if int(newtime) - int(curtime) == 1:
        timtext.set_text(str(int(newtime - start_time)), 40,wkalah)
        timtext.draw(0,0)
        curtime = newtime

    if nilai >= 5:
        mng = Label(0,0,500,500,wmenang)
        mng.set_text('Kamu menang', 60, woutline)
        mng.draw(110,180)
        break

    pygame.display.update()
    timer.tick(40)

pygame.display.update()