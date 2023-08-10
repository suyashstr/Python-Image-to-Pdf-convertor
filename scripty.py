import os
import img2pdf

with open("imagecontainbook.pdf","wb") as file:
     file.write(img2pdf.convert([i for i in os.listdir("C:\\Users\\suyash sunil mane\\OneDrive\\Desktop\\Scriptproject.py")if i.endswith(".jpg")]))
