"""
File: Owl
Name: Kai
----------------------
Choosing stanCode make you as wise as an owl.
You deserved the best coding class.
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon,GLabel,GArc
from campy.graphics.gwindow import GWindow

window = GWindow(width=800,height=420,title='As Wise As An Owl.py')


def main():
    """
    choose stanCode make you as wise as an owl.
    You deserved the best coding class.
    """
    background_screen()
    ear()
    body_of_owl()
    face_of_owl()
    feather()
    toes()
    arm()
    star()
    bot()
    board()


def background_screen():
    background = GRect(800, 420, x=0, y=0)
    background.fill_color = "#000099"
    background.color = "#000099"
    background.filled = True
    window.add(background)
    sunset = GArc(150, 200, 0, 180, x=30, y=80)
    sunset.fill_color = "#b36b00"
    sunset.color = "#b36b00"
    sunset.filled = True
    window.add(sunset)
    mountain = GPolygon()
    mountain.add_vertex((160, 25))
    mountain.add_vertex((35, 150))
    mountain.add_vertex((310, 150))
    mountain.fill_color = "#600080"
    mountain.color = "#600080"
    mountain.filled = True
    window.add(mountain)
    mountain2 = GPolygon()
    mountain2.add_vertex((600, 15))
    mountain2.add_vertex((750, 150))
    mountain2.add_vertex((300, 150))
    mountain2.fill_color = "#000066"
    mountain2.color = "#000066"
    mountain2.filled = True
    window.add(mountain2)
    mountain1 = GPolygon()
    mountain1.add_vertex((430, 40))
    mountain1.add_vertex((620, 160))
    mountain1.add_vertex((210, 160))
    mountain1.fill_color = "#6600cc"
    mountain1.color = "#6600cc"
    mountain1.filled = True
    window.add(mountain1)
    moon = GOval(250, 250, x=530, y=190)
    moon.fill_color = "#ffcc66"
    moon.color = "#ffbb33"
    moon.filled = True
    window.add(moon)
    moon1 = GOval(220, 220, x=510, y=180)
    moon1.fill_color = "#000099"
    moon1.color = "#000099"
    moon1.filled = True
    window.add(moon1)

def ear():
    ear_l = GPolygon()
    ear_l.add_vertex((430,10))
    ear_l.add_vertex((450,100))
    ear_l.add_vertex((550,100))
    ear_l.fill_color= "#ac7339"
    ear_l.filled = True
    window.add(ear_l)
    ear_r = GPolygon()
    ear_r.add_vertex((770, 10))
    ear_r.add_vertex((750, 100))
    ear_r.add_vertex((650, 100))
    ear_r.fill_color = "#ac7339"
    ear_r.filled = True
    window.add(ear_r)


def body_of_owl():
    body = GOval(250, 300, x=475, y=90)
    body.fill_color = "#ac7339"
    body.filled = True
    window.add(body)
    inner_body = GOval(150, 250, x=520, y=115)
    inner_body.fill_color = "#dfbf9f"
    inner_body.color = "#dfbf9f"
    inner_body.filled = True
    window.add(inner_body)


def face_of_owl():
    face_l = GOval(180,180,x=420,y=60)
    face_l.fill_color = "#ac7339"
    face_l.color = "#ac7339"
    face_l.filled = True
    window.add(face_l)
    face_r = GOval(180, 180, x=585, y=60)
    face_r.fill_color = "#ac7339"
    face_r.color = "#ac7339"
    face_r.filled = True
    window.add(face_r)
    beak = GPolygon()
    beak.add_vertex((510, 150))
    beak.add_vertex((680, 150))
    beak.add_vertex((595, 250))
    beak.fill_color = "#ffe066"
    beak.color = "#ffe066"
    beak.filled = True
    window.add(beak)
    inner_face_r = GOval(150, 150, x=600, y=75)
    inner_face_r.fill_color = "#dfbf9f"
    inner_face_r.color = "#dfbf9f"
    inner_face_r.filled = True
    window.add(inner_face_r)
    inner_face_l = GOval(150, 150, x=435, y=75)
    inner_face_l.fill_color = "#dfbf9f"
    inner_face_l.color = "#dfbf9f"
    inner_face_l.filled = True
    window.add(inner_face_l)
    eyeball_l = GOval(120, 120, x=450, y=90)
    eyeball_l.fill_color = "#ffffff"
    eyeball_l.color = "#ffffff"
    eyeball_l.filled = True
    window.add(eyeball_l)
    eyeball_r = GOval(120, 120, x=615, y=90)
    eyeball_r.fill_color = "#ffffff"
    eyeball_r.color = "#ffffff"
    eyeball_r.filled = True
    window.add(eyeball_r)
    inner_eyeball_l = GOval(100,100,x=460,y=100)
    inner_eyeball_l.fill_color = "#b35900"
    inner_eyeball_l.color = "#b35900"
    inner_eyeball_l.filled = True
    window.add(inner_eyeball_l)
    inner_eyeball_r = GOval(100, 100, x=625, y=100)
    inner_eyeball_r.fill_color = "#b35900"
    inner_eyeball_r.color = "#b35900"
    inner_eyeball_r.filled = True
    window.add(inner_eyeball_r)
    black_eyeball_r = GOval(80, 80, x=635, y=110)
    black_eyeball_r.fill_color = "#000000"
    black_eyeball_r.color = "#000000"
    black_eyeball_r.filled = True
    window.add(black_eyeball_r)
    black_eyeball_l = GOval(80, 80, x=470, y=110)
    black_eyeball_l.fill_color = "#000000"
    black_eyeball_l.color = "#000000"
    black_eyeball_l.filled = True
    window.add(black_eyeball_l)
    white_eyeball_l = GOval(20, 20, x=515, y=125)
    white_eyeball_l.fill_color = "#ffffff"
    white_eyeball_l.color = "#ffffff"
    white_eyeball_l.filled = True
    window.add(white_eyeball_l)
    white_eyeball_r = GOval(20, 20, x=680, y=125)
    white_eyeball_r.fill_color = "#ffffff"
    white_eyeball_r.color = "#ffffff"
    white_eyeball_r.filled = True
    window.add(white_eyeball_r)


def feather():
    feather1 = GPolygon()
    feather1.add_vertex((525, 260))
    feather1.add_vertex((565, 260))
    feather1.add_vertex((545, 300))
    feather1.fill_color = "#ac7339"
    feather1.color = "#ac7339"
    feather1.filled = True
    window.add(feather1)
    feather2 = GPolygon()
    feather2.add_vertex((575, 260))
    feather2.add_vertex((615, 260))
    feather2.add_vertex((595, 300))
    feather2.fill_color = "#ac7339"
    feather2.color = "#ac7339"
    feather2.filled = True
    window.add(feather2)
    feather3 = GPolygon()
    feather3.add_vertex((625, 260))
    feather3.add_vertex((665, 260))
    feather3.add_vertex((645, 300))
    feather3.fill_color = "#ac7339"
    feather3.color = "#ac7339"
    feather3.filled = True
    window.add(feather3)
    feather4 = GPolygon()
    feather4.add_vertex((600, 310))
    feather4.add_vertex((640, 310))
    feather4.add_vertex((620, 350))
    feather4.fill_color = "#ac7339"
    feather4.color = "#ac7339"
    feather4.filled = True
    window.add(feather4)
    feather5 = GPolygon()
    feather5.add_vertex((590, 310))
    feather5.add_vertex((550, 310))
    feather5.add_vertex((570, 350))
    feather5.fill_color = "#ac7339"
    feather5.color = "#ac7339"
    feather5.filled = True
    window.add(feather5)


def toes():
    toes1 = GOval(20, 40, x=505, y=350)
    toes1.fill_color = "#ffe066"
    toes1.color = "#000000"
    toes1.filled = True
    window.add(toes1)
    toes2 = GOval(20, 40, x=525, y=350)
    toes2.fill_color = "#ffe066"
    toes2.color = "#000000"
    toes2.filled = True
    window.add(toes2)
    toes3 = GOval(20, 40, x=545, y=350)
    toes3.fill_color = "#ffe066"
    toes3.color = "#000000"
    toes3.filled = True
    window.add(toes3)
    toes4 = GOval(20, 40, x=625, y=350)
    toes4.fill_color = "#ffe066"
    toes4.color = "#000000"
    toes4.filled = True
    window.add(toes4)
    toes5 = GOval(20, 40, x=645, y=350)
    toes5.fill_color = "#ffe066"
    toes5.color = "#000000"
    toes5.filled = True
    window.add(toes5)
    toes6 = GOval(20, 40, x=665, y=350)
    toes6.fill_color = "#ffe066"
    toes6.color = "#000000"
    toes6.filled = True
    window.add(toes6)


def arm():
    arm_r = GOval(80, 150, x=670, y=230)
    arm_r.fill_color = "#86592d"
    arm_r.color = "#86592d"
    arm_r.filled = True
    window.add(arm_r)
    arm_l = GOval(150, 80, x=350, y=230)
    arm_l.fill_color = "#86592d"
    arm_l.color = "#86592d"
    arm_l.filled = True
    window.add(arm_l)


def star():
    star1 = GRect(50,50,x=40,y=20)
    star1.fill_color = "#ffcc66"
    star1.color = "#ffcc66"
    star1.filled = True
    window.add(star1)
    star2 = GPolygon()
    star2.add_vertex((40, 20))
    star2.add_vertex((90, 20))
    star2.add_vertex((65, 40))
    star2.fill_color = "#000099"
    star2.color = "#000099"
    star2.filled = True
    window.add(star2)
    star3 = GPolygon()
    star3.add_vertex((40, 20))
    star3.add_vertex((40, 70))
    star3.add_vertex((60, 45))
    star3.fill_color = "#000099"
    star3.color = "#000099"
    star3.filled = True
    window.add(star3)
    star4 = GPolygon()
    star4.add_vertex((90, 20))
    star4.add_vertex((90, 70))
    star4.add_vertex((70, 45))
    star4.fill_color = "#000099"
    star4.color = "#000099"
    star4.filled = True
    window.add(star4)
    star5 = GPolygon()
    star5.add_vertex((40, 70))
    star5.add_vertex((90, 70))
    star5.add_vertex((65, 50))
    star5.fill_color = "#000099"
    star5.color = "#000099"
    star5.filled = True
    window.add(star5)
    star1 = GRect(70,70,x=250,y=30)
    star1.fill_color = "#ffcc66"
    star1.color = "#ffcc66"
    star1.filled = True
    window.add(star1)
    star2 = GPolygon()
    star2.add_vertex((250, 30))
    star2.add_vertex((250, 100))
    star2.add_vertex((275, 65))
    star2.fill_color = "#000099"
    star2.color = "#000099"
    star2.filled = True
    window.add(star2)
    star3 = GPolygon()
    star3.add_vertex((250, 30))
    star3.add_vertex((320, 30))
    star3.add_vertex((285, 55))
    star3.fill_color = "#000099"
    star3.color = "#000099"
    star3.filled = True
    window.add(star3)
    star4 = GPolygon()
    star4.add_vertex((320, 30))
    star4.add_vertex((295, 65))
    star4.add_vertex((320, 100))
    star4.fill_color = "#000099"
    star4.color = "#000099"
    star4.filled = True
    window.add(star4)
    star5 = GPolygon()
    star5.add_vertex((250, 100))
    star5.add_vertex((285, 75))
    star5.add_vertex((320, 100))
    star5.fill_color = "#000099"
    star5.color = "#000099"
    star5.filled = True
    window.add(star5)
    star1 = GRect(50,50,x=150,y=60)
    star1.fill_color = "#ffcc66"
    star1.color = "#ffcc66"
    star1.filled = True
    window.add(star1)
    star2 = GPolygon()
    star2.add_vertex((150, 60))
    star2.add_vertex((150, 110))
    star2.add_vertex((165, 85))
    star2.fill_color = "#600080"
    star2.color = "#600080"
    star2.filled = True
    window.add(star2)
    star3 = GPolygon()
    star3.add_vertex((150, 60))
    star3.add_vertex((175, 75))
    star3.add_vertex((200, 60))
    star3.fill_color = "#600080"
    star3.color = "#600080"
    star3.filled = True
    window.add(star3)
    star4 = GPolygon()
    star4.add_vertex((200, 60))
    star4.add_vertex((200, 110))
    star4.add_vertex((185, 85))
    star4.fill_color = "#600080"
    star4.color = "#600080"
    star4.filled = True
    window.add(star4)
    star5 = GPolygon()
    star5.add_vertex((150, 110))
    star5.add_vertex((200, 110))
    star5.add_vertex((175, 95))
    star5.fill_color = "#600080"
    star5.color ="#600080"
    star5.filled = True
    window.add(star5)

def bot():
    bot1 = GOval(15, 30, x=715, y=260)
    bot1.fill_color = "#ac7339"
    bot1.color = "#ac7339"
    bot1.filled = True
    window.add(bot1)
    bot2 = GOval(15, 30, x=715, y=310)
    bot2.fill_color = "#ac7339"
    bot2.color = "#ac7339"
    bot2.filled = True
    window.add(bot2)
    bot3 = GOval(15, 30, x=730, y=285)
    bot3.fill_color = "#ac7339"
    bot3.color = "#ac7339"
    bot3.filled = True
    window.add(bot3)
    bot4 = GOval(15, 30, x=695, y=260)
    bot4.fill_color = "#ac7339"
    bot4.color = "#ac7339"
    bot4.filled = True
    window.add(bot4)
    bot5 = GOval(15, 30, x=695, y=310)
    bot5.fill_color = "#ac7339"
    bot5.color = "#ac7339"
    bot5.filled = True
    window.add(bot5)
    bot6 = GOval(15, 30, x=680, y=285)
    bot6.fill_color = "#ac7339"
    bot6.color = "#ac7339"
    bot6.filled = True
    window.add(bot6)
    bot7 = GOval(15, 30, x=705, y=285)
    bot7.fill_color = "#ac7339"
    bot7.color = "#ac7339"
    bot7.filled = True
    window.add(bot7)
    bot8 = GOval(15, 30, x=705, y=340)
    bot8.fill_color = "#ac7339"
    bot8.color = "#ac7339"
    bot8.filled = True
    window.add(bot8)
    bot1 = GOval(30, 15, x=440, y=250)
    bot1.fill_color = "#ac7339"
    bot1.color = "#ac7339"
    bot1.filled = True
    window.add(bot1)
    bot2 = GOval(30, 15, x=440, y=270)
    bot2.fill_color = "#ac7339"
    bot2.color = "#ac7339"
    bot2.filled = True
    window.add(bot2)
    bot3 = GOval(30, 15, x=410, y=280)
    bot3.fill_color = "#ac7339"
    bot3.color = "#ac7339"
    bot3.filled = True
    window.add(bot3)
    bot4 = GOval(30, 15, x=410, y=260)
    bot4.fill_color = "#ac7339"
    bot4.color = "#ac7339"
    bot4.filled = True
    window.add(bot4)
    bot5 = GOval(30, 15, x=410, y=240)
    bot5.fill_color = "#ac7339"
    bot5.color = "#ac7339"
    bot5.filled = True
    window.add(bot5)
    bot6 = GOval(30, 15, x=380, y=250)
    bot6.fill_color = "#ac7339"
    bot6.color = "#ac7339"
    bot6.filled = True
    window.add(bot6)
    bot7 = GOval(30, 15, x=380, y=270)
    bot7.fill_color = "#ac7339"
    bot7.color = "#ac7339"
    bot7.filled = True
    window.add(bot7)


def board():
    board_back = GRect(370, 220, x=30, y=130)
    board_back.fill_color = "#ffff00"
    board_back.color = "#ffff00"
    board_back.filled = True
    window.add(board_back)
    board_back1 = GRect(360, 210, x=35, y=135)
    board_back1.fill_color = "#ff00ff"
    board_back1.color = "#ff00ff"
    board_back1.filled = True
    window.add(board_back1)
    board = GRect(350,200,x=40,y=140)
    board.fill_color = "#e60000"
    board.color = "#e60000"
    board.filled = True
    window.add(board)
    label = GLabel("stanCode",x=55,y=240)
    label.font = "SansSerif-80"
    label.color = "#ffffff"
    window.add(label)
    slogan = GLabel("Make you as wise", x=55, y=280)
    slogan.font = "SansSerif-40"
    slogan.color = "#ffffff"
    window.add(slogan)
    slogan1 = GLabel("as an owl.", x=55, y=320)
    slogan1.font = "SansSerif-40"
    slogan1.color = "#ffffff"
    window.add(slogan1)
    slogan2 = GLabel("You deserve the best coding class in Taiwan.", x=25, y=390)
    slogan2.font = "SansSerif-20"
    slogan2.color = "#ffffff"
    window.add(slogan2)


if __name__ == '__main__':
    main()
