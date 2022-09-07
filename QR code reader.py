from pyzbar.pyzbar import decode
from PIL import Image
# reading image
img = Image.open('myqr.png')
c0nt=decode(img)
print(c0nt[0].data.decode())