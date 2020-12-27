import PyPDF2
from comtypes.client import CreateObject
import pygame as pygame


def menu():
    print('''   "welcome to audio book"
1 => play
2 => pause
3 => change page 
4 => exit''')


def genaudio(num, text):
    outfile = "output/audiobook_page{}.wav".format(num + 1)
    stream.Open(outfile, SpeechLib.SSFMCreateForWrite)
    engine.AudioOutputStream = stream
    engine.speak(text)
    stream.Close()


# pdf to text
book = open('sample - Copy.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

engine = CreateObject("SAPI.SpVoice")
stream = CreateObject("SAPI.SpFileStream")
from comtypes.gen import SpeechLib

for num in range(pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    genaudio(num, text)

page = 1
pygame.mixer.init()
pygame.mixer.music.load('output/audiobook_page{}.wav'.format(page))
pause = False
while True:
    menu()  # print menu
    print("selected page:", page)
    x = input()
    if x == '1':
        if pause:
            pygame.mixer.music.unpause()
            pause = False
        else:
            pygame.mixer.music.play()
    elif x == '2':
        pygame.mixer.music.pause()
        pause = True
    elif x == '3':
        print("enter pg no between:{} and {}".format(1, pages))
        while True:
            page = int(input())
            if 1 <= page <= pages:
                break
            else:
                print("enter valid page nos")
        pygame.mixer.music.load('output/audiobook_page{}.wav'.format(page))
    elif x == '4':
        break
    else:
        print('invalid option')

print("thank you for using audio book")
