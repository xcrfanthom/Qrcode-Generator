import segno
import random

i = input("Enter a link or a phrase that you want it to be qrcoded: ")
n = input("Enter a size for the qrcode: ")
qrcode = segno.make_qr(i)
qrcode.save(
    f"{random.random()}.png",
    scale = n    
)