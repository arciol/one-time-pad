import random
import string
import time
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

counter=(''.join(random.choices(string.ascii_uppercase, k=3)))

def choose_file():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename(initialdir='./', initialfile='*.txt', \
 filetypes=[("*.TXT", "*.txt")]) # show an "Open" dialog box and return the path to the selected file
    return filename

def welcome():
    komunikat="Witaj w koderze One-Time-Pad"
    spaces=0
    for chars in range(len(komunikat)):
        if komunikat[chars]==' ':
            spaces+=1
    print("="*(len(komunikat)+spaces+1))
    print("=",komunikat,"=")
    print("="*(len(komunikat)+spaces+1))

def menu():
    decision=int(input("Aby zakodować tekst wpisz 1\n Aby odkodować tekst wpisz 2 \n"))

    if (decision==1):
        print("Wybierz plik, którego zawartość chcesz zakodować: ")
        file_path=choose_file()
        f = open (file_path, "r")
        f_content=(f.read())
        text=f_content

        print('Tekst wejściowy: ', text)

        text=f_content.upper()
        text=text.replace(" ","")

        print('Tekst zaszyfrowany: ', Encrypt(text),'\n')
        print(input("Wcisnij enter aby zakonczyc "))
    elif (decision==2):
        print("Wybierz plik, którego zawartość chcesz odkodować: ")
        file_path=choose_file()
        f = open (file_path, "r")
        f_content=(f.read())
        newText=f_content
        print('Tekst wejściowy: ', newText)
        print('Tekst odszyfrowany: ', Decrypt(newText),'\n')
        print(input("Wcisnij enter aby zakonczyc "))
    else:
        print('Wybierz 1 lub 2!')
        print(input("Wcisnij enter aby zakonczyc "))
    f.close()
    return 0


#szyfrowanie 
def Encrypt(text):
    spacje=0
    for a in range(0, len(text)):
        if ord(text[a])==32:
            spacje+=1
    key=(''.join(random.choices(string.ascii_uppercase, k=len(text)-spacje)))

    print("Klucz: ",key)
    newText=''
    for i in range(0,len(text)):
        if text[i]==" ":
            newSign=""
        else:
            sumSigns=ord(text[i])+ord(key.upper()[i])
            move=sumSigns%26
            newSign=chr(move+65)
        newText+=newSign

    f_key=open("./"+counter+"__OTP_key.txt","w")
    f_key.write(key)
    f_key.close()

    f_newText=open("./"+counter+"__OTP_encoded.txt","w")
    f_newText.write(newText)
    f_newText.close()
    return newText

#deszyfrowanie
def Decrypt(newText):
    print("Wybierz plik z kluczem odkodowującym: ")
    file_path=choose_file()
    f = open (file_path, "r")
    f_content=(f.read())
    key=f_content
    print("Klucz: ", key)
    decrypted=''
    for i in range(0,len(newText)):
        diffSigns=ord(newText[i])-ord(key.upper()[i])
        if diffSigns<0:
            diffSigns=26-abs(diffSigns)
        newSign=chr(65+diffSigns)
        decrypted+=newSign
    f_decrypted=open("./"+counter+"__OTP_decoded.txt","w")
    f_decrypted.write(decrypted)
    f_decrypted.close()
    return decrypted

welcome()
menu()
