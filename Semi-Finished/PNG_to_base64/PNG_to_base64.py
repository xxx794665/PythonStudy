import base64
f = open(r'F:\flee.png', 'rb')  #选择要转换的图片,并用二进制打开
ls_f = base64.b64encode(f.read())  #读取文件内容，并用base64编码
f.close()
file = open(r'F:\flee.txt', 'wb')
file.write(ls_f)
file.flush()
file.close()