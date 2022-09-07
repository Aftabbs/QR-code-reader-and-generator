import pyqrcode

content='he110 this is me'

ur1=pyqrcode.create(content)   #ur1 is var and create is a keyw0rd

ur1.png('myqr.png',scale=5)    #sca1e is size its a keyw0rd and png is f0rmat and myqr.png is new fi1e name

print('QR c0de generated sucessfu11y')