import random
import turtle
from random import randrange, random

# --------- DATA ------------

phi_eksak = 3.141592653589793238462643383279502884197169399375105820974944592307816406286  # Nilai PI
N = 101  # Jumlah KOREK atau JARUM
d = 50  # Jarak antar garis paralel (satuan dalam 'pixel')
l = 40  # Panjang KOREK atau JARUM ( satuan dalam 'pixel')
Q = 0
# Jumlah KOREK atau JARUM yang memotong garis paralel (Di inisialisasikan masih berjumlah 0)

# ----------- SETTING KERTAS DAN GARIS -------------------

# Set kertas dan Pen untuk simulasi

kertas = turtle.Screen()
kertas.title("Simulasi Monte Carlo - Buffon Needle's Problem")
kertas.screensize(250, 250)  # ukuran kertas 25 x 25 cm
line = turtle.Turtle()
line.hideturtle()

# ----------- K E R T A S (25cm x 25cm) -------------------

line.color('black')
line.speed("fast")
line.pu()
line.setpos(-125, -95)
line.pd()
line.forward(250)
line.left(90)
line.forward(250)
line.left(90)
line.forward(250)
line.left(90)
line.forward(250)
line.left(90)

# ------------------------------

# Menggambar garis paralel
# dengan jarak antar garis (d) = 50, dan panjangnya =  250 (atau 25cm)
line.speed("slow")
line.color('black')
for i in range(-45, 125, d):
    line.pu()
    line.setpos(-125, i)
    line.pd()
    line.fd(250)

# ---------- SIMULASI --------------------

# Memulai simulasi Monte Carlo - Buffon's Needle
line.color('orange')
line.speed("fast")
for j in range(N):
    line.pu()
    line.goto(randrange(-85, 86, 1), randrange(-55, 116, 1))
    x1 = line.xcor()  # titik awal
    y1 = line.ycor()
    line.seth(360*random())  # sudut teta
    line.pd()
    line.fd(l)  # garis sepanjang l
    x2 = line.xcor()  # titik akhir
    y2 = line.ycor()

    if y1 <= y2:
        proyeksi = y2 - y1  # menghitung panjang garis proyeksi korek atau jarum terhadap sumbu y
        x = d - (y1 % d)
        # menghitung jarak dari ujung bawah korek atau jarum ke garis pararel atas
    else:
        proyeksi = y1 - y2  # menghitung panjang garis proyeksi korek atau jarum terhadap sumbu x
        x = d - (y2 % d)
        # menghitung jarak dari ujung atas korek atau jarum ke garis pararel bawah
    if x <= proyeksi:  # jika x < proyeksi maka korek memotong garis
        Q += 1  # menghitung korek yang mengenai garis pararel

phi_approx = (2 * l * N) / (d * Q)  # Rumus utama mencari pi estimasi
error = phi_eksak - phi_approx

print("---------------------------------------------------------------")
print("Korek atau Jarum yang mengenai garis = " + str(Q))
print("Phi Estimasi                         = " + str(phi_approx))
print("Phi Eksak                            = " + str(phi_eksak))
print("Nilai error                          = " + str(error))
