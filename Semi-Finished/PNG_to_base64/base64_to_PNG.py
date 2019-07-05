import base64
png = open('base64.txt', 'rb')
imgdata = base64.b64decode(png.read())
file = open('base64.png', 'wb')
file.write(imgdata)
file.close()
