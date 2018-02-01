import pytesseract
from PIL import Image
import os

file_path='0001.jpg'

print('开始转换……')
text=pytesseract.image_to_string(Image.open(file_path),lang='chi_sim')
print('文件转换完毕')
text = ''.join(text.split())
f=open('text.txt','w')
f.write(text)
f.close()
print(text)
print('文件写入完毕')






