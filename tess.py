from PIL import Image
import pytesseract 
import pyttsx


f1="/home/arundhati/cv/ocr/test.jpg"
f2="/home/arundhati/cv/ocr/try.gif"
f3="/home/arundhati/cv/ocr/p.png"
f4="/home/arundhati/cv/ocr/tele.jpg"

text = pytesseract.image_to_string(Image.open(f1))
print text
text1 = pytesseract.image_to_string(Image.open(f2))
print text1
text2 = pytesseract.image_to_string(Image.open(f4))
print text2

engine = pyttsx.init()
engine.say(text2)
engine.runAndWait()
