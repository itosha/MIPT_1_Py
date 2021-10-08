import pygame
from pygame.draw import *

def model_alien(Body_color):
    BD_Alien = [
        (Body_color, (514, 760,  52, 118)), #Body
        (Body_color, (499, 838,  31,  40)), #L_leg_start
        (Body_color, (493, 868,  25,  58)),
        (Body_color, (484, 901,  31,  28)),
        (Body_color, (457, 904,  43,  25)), #L_leg_end
        (Body_color, (544, 850,  34,  37)), #R_leg_start
        (Body_color, (556, 877,  25,  55)),
        (Body_color, (556, 913,  28,  28)),
        (Body_color, (568, 913,  55,  22)), #R_leg_end
        (Body_color, (556, 769,  31,  31)), #R_arm_start
        (Body_color, (577, 784,  31,  22)), #+Apple
        (Body_color, (595, 790,  34,  19)),
        (Body_color, (616, 787,  25,  19)),
        ((255,   0,   0), (619, 751,  55,  52)),
        ((  0, 255,   0), (643, 727,   7,  22)), #R_arm_end
        (Body_color, (499, 766,  31,  28)), #L_arm_start
        (Body_color, (490, 787,  22,  19)),
        (Body_color, (469, 796,  31,  19)),
        (Body_color, (466, 799,  19,  19)),
        ((255, 255,   0), (469, 793,   7,   7)),
        ((255, 255,   0), (460, 790,   7,   7)),
        ((255, 255,   0), (454, 796,   7,   7)),
        ((255, 255,   0), (454, 805,   7,   7)),
        ((255, 255,   0), (457, 817,   7,   7)),
        ((255, 255,   0), (466, 823,   7,   7)), #L_arm_end
        ((  0,   0,   0), (514, 691,  34,  34)), #eye_bel
        ((  0,   0, 255), (532, 709,   7,  10)), #Eyes_pupil
        ((  0,   0,   0), (571, 700,  25,  25)), #eye_bel
        ((  0,   0, 255), (583, 709,   7,  10)), #Eyes_pupil
        (Body_color, (592, 667,  19,  19)),
        (Body_color, (601, 655,  10,  16)),
        (Body_color, (604, 646,  16,  16)),
        (Body_color, (610, 634,  25,  16)),
        (Body_color, (625, 631,  16,  16)),
        (Body_color, (646, 631,  25,  31)),
        ((255, 255,   0), (649, 619,  13,  13)),
        ((255, 255,   0), (661, 622,  13,  13)),
        ((255, 255,   0), (667, 631,  13,  13)),
        ((255, 255,   0), (670, 643,  13,  13)),
        ((255, 255,   0), (664, 655,  13,  13)),
        ((255, 255,   0), (655, 664,  13,  13)),
        ((255, 255,   0), (643, 658,  13,  13)),
        ((255, 255,   0), (637, 646,  13,  13)), #R_antenna_end
        (Body_color, (499, 661,  13,  19)),
        (Body_color, (490, 643,  19,  19)),
        (Body_color, (484, 628,  16,  22)),
        (Body_color, (472, 610,  28,  22)),
        ((255, 255,   0), (499, 619,  10,  10)),
        ((255, 255,   0), (499, 610,  10,  10)),
        ((255, 255,   0), (496, 604,  10,  10)),
        ((255, 255,   0), (490, 601,  10,  10)),
        ((255, 255,   0), (484, 598,  10,  10)),
        ((255, 255,   0), (478, 601,  10,  10)),
        ((255, 255,   0), (472, 604,  10,  10)),
        ((255, 255,   0), (466, 607,  10,  10)),
        ((255, 255,   0), (463, 613,  10,  10)),
        ((255, 255,   0), (466, 619,  10,  10)),
        ((255, 255,   0), (469, 625,  10,  10)), #L_antenna_end
        ((255, 255,   0), (520, 760,  10,  10)),
        ((255, 255,   0), (523, 763,  10,  10)),
        ((255, 255,   0), (526, 766,  10,  10)),
        ((255, 255,   0), (529, 769,  10,  10)),
        ((255, 255,   0), (532, 772,  10,  10)),
        ((255, 255,   0), (535, 769,  10,  10)),
        ((255, 255,   0), (538, 769,  10,  10)),
        ((255, 255,   0), (541, 766,  10,  10)),
        ((255, 255,   0), (544, 763,  10,  10)),
        ((255, 255,   0), (547, 763,  10,  10)),  ]
    return BD_Alien

def model_Ufo(color_frame, color_big_window, color_small_window):
    BD_Ufo = [
        (color_frame, ( 10, 400, 370, 100)), #Back
        (color_big_window, ( 58, 379, 250,  88)), #Cabine
        (color_small_window, ( 25, 442,  40,  19)), #Lamp_start
        (color_small_window, ( 70, 463,  40,  19)),
        (color_small_window, (124, 475,  40,  19)),
        (color_small_window, (193, 475,  40,  19)),
        (color_small_window, (247, 463,  40,  19)), #Lamp_pred-end
        (color_small_window, (304, 445,  40,  19))]
    return BD_Ufo

def model_Clouds(Color1, Color2):
    BD_Clouds =	[
    (Color1, (-143,  91, 490, 130)),
    (Color1, (-158, 244, 670, 130)),
    (Color1, ( 271, 295, 670, 112)),
    (Color1, ( 358, 148, 670, 112)),
    (Color2, (-188, 208, 520, 130)),
    (Color2, ( 139,  79, 760, 130)),
    (Color2, ( 109, 379, 760, 130)),]
    return BD_Clouds

def Alien(place, face_color, body_color, posx, posy):
    BD_Alien = model_alien(body_color)
    polygon(place, face_color,
        (( 73, 103), (173, 102),
         (137, 183), (90, 183)))
    aalines(place, face_color, True,
        (( 73, 103), (173, 102),
         (137, 183), (90, 183)))
    for i in range(len(BD_Alien)):
        color = BD_Alien[i][0]
        delta__x = -427
        delta__y = -580
        x = posx + delta__x + BD_Alien[i][1][0]
        y = posy + delta__y + BD_Alien[i][1][1]
        height = BD_Alien[i][1][3]
        wid    = BD_Alien[i][1][2]
        ellipse(place, color, (x, y, wid, height))

def Ufo(place, color_frame, color_big_window, color_small_window, posx, posy):
    triangle = pygame.Surface((330, 360), pygame.SRCALPHA, 32)
    BD_Ufo = model_Ufo(color_frame, color_big_window, color_small_window)
    polygon(triangle, (221, 223, 175),((150, 60), (0, 360), (330, 360)))
    triangle.set_alpha(128)
    place.blit(triangle, (0, 0))
    for i in range(len(BD_Ufo)):
        color = BD_Ufo[i][0]
        delta__x = -10
        delta__y = -370
        x = posx + delta__x + BD_Ufo[i][1][0]
        y = posy + delta__y + BD_Ufo[i][1][1]
        height = BD_Ufo[i][1][3]
        wid    = BD_Ufo[i][1][2]
        ellipse(place, color, (x, y, wid, height))



def Clouds(place, Color1, Color2):
    BD_Clouds = model_Clouds(Color1, Color2)
    for i in range(len(BD_Clouds)):
        color = BD_Clouds[i][0]
        x = BD_Clouds[i][1][0]
        y = BD_Clouds[i][1][1]
        height = BD_Clouds[i][1][3]
        wid    = BD_Clouds[i][1][2]
        ellipse(place, color, (x, y, wid, height))