# https://pytube.io/en/latest/index.html
# https://stackoverflow.com/questions/70060263/pytube-attributeerror-nonetype-object-has-no-attribute-span
# en caso de error
# AttributeError: 'NoneType' object has no attribute 'span'
# ir C:\Python38\lib\site-packages\pytube\parser.py
# cambiar esta linea  152: func_regex = re.compile(r"function\([^)]+\)")
# por esta 152: func_regex = re.compile(r"function\([^)]?\)")

from tkinter import *
from tkinter.font import BOLD
from tkinter import filedialog
from tkinter import ttk

import downloadYbt

root = Tk()
root.title('Download Youtube')
root.iconbitmap('download.ico')
root.resizable(0,0)

varOpcion = IntVar()
varVideo = IntVar()
varAudio = IntVar()
savePath = StringVar()
ruta = StringVar()

def abrirFichero():
    ruta.set(filedialog.askopenfilename(title="Abrir", filetypes=[("Texto","*.txt")]))

def opcion():
    if(varOpcion.get()==1):
        urlText.config(state='normal')
        botonAbrir.config(state='disabled')
        v.config(state='active')
        a.config(state='active')
    elif(varOpcion.get()==2):
        urlText.config(state='disabled')
        botonAbrir.config(state='normal')
        v.config(state='active')
        a.config(state='active')
        

def audioVideo():
    if(varVideo.get()==1):
        down.config(state='active')
    if(varAudio.get()==1):
        down.config(state='active')

def browse():
    downloadDirectory = filedialog.askdirectory(initialdir='YOUR DIRECTORY PATH', title="Guarda Video")

    savePath.set(downloadDirectory)

def download():
    if(varOpcion.get()==1):

        if(varVideo.get()==1 and varAudio.get()==1):
            downloadYbt.simpleDownload(urlText.get(), destino.get(), True, True)
        else:
            if(varVideo.get()==1):
                downloadYbt.simpleDownload(urlText.get(), destino.get(), True, False)
            if(varAudio.get()==1):
                downloadYbt.simpleDownload(urlText.get(), destino.get(), False, True)
    elif(varOpcion.get()==2):

        if(varVideo.get()==1 and varAudio.get()==1):
            downloadYbt.multipleDownload(ruta.get(), destino.get(), True, True)
        else:
            if(varVideo.get()==1):
                downloadYbt.multipleDownload(ruta.get(), destino.get(), True, False)
            if(varAudio.get()==1):
                downloadYbt.multipleDownload(ruta.get(), destino.get(), False, True)

miFrame = Frame(root, width='280', height='190')
miFrame.pack()

url = Label(miFrame, text='URL:', font=('Comic Sans MS',12,BOLD)).grid(row=0,column=1,padx=5, pady=5)
urlText = Entry(miFrame, width=35, state='disabled')
urlText.grid(row=0,column=2, pady=5, padx=5)

archivo = Label(miFrame, text='ArchivoURL:', font=('Comic Sans MS',12,BOLD)).grid(row=1,column=1,padx=5, pady=5)
botonAbrir = Button(miFrame, text='Abrir txt', font=('Arial',10,BOLD), command=abrirFichero, state='disabled')
botonAbrir.grid(row=1,column=2,padx=5, pady=5)


Radiobutton(miFrame, variable=varOpcion, value=1, command=opcion).grid(row=0, column=0, padx=5)
Radiobutton(miFrame, variable=varOpcion, value=2, command=opcion).grid(row=1, column=0, padx=5)

separt = ttk.Separator(miFrame, orient='horizontal').grid(row=2, columnspan=3, ipadx=150)


v = Checkbutton(miFrame, text="Video", variable=varVideo, font=('Comic Sans MS',12,BOLD), command=audioVideo, state='disabled')
v.grid(row=3, column=0, padx=5)
a = Checkbutton(miFrame, text="Audio", variable=varAudio, font=('Comic Sans MS',12,BOLD), command=audioVideo, state='disabled')
a.grid(row=3, column=1, padx=5)

down = Button(miFrame, text='DownLoad', font=('Comic Sans MS',12,BOLD), state='disabled', command=download)
down.grid(row=3,column=2, pady=5)

destinoLabel = Label(miFrame, text="Destino", font=('Comic Sans MS',12,BOLD), padx=5, pady=5)
destinoLabel.grid(row=4,column=0, pady=10, padx=5)

destino = Entry(miFrame, textvariable=savePath, font=12)
destino.grid(row=4,column=1, pady=10, padx=5)

destinoButton = Button(miFrame, text="Browse", font=('Comic Sans MS',12,BOLD), command=browse)
destinoButton.grid(row=4,column=2, pady=10, padx=5)


root.mainloop()