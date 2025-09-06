import pyttsx3
from PyPDF2 import PdfReader
from tkinter.filedialog import askopenfilename

book = askopenfilename()
reader = PdfReader(book)
pages = len(reader.pages)
player = pyttsx3.init()
player.setProperty('rate', 200)
player.setProperty('volume', 0.8)

for i in range (pages):
    page = reader.pages[i]
    text = page.extract_text()
    player.say(text)
    player.runAndWait()