from tkinter import *
from tkinter import filedialog
# from pydub import AudioSegment
from pygame import mixer
from tkinter import messagebox

# song_list = []

class MusicPlayer:

    def __init__(self, window):
        window.geometry('510x280'), window.title('Mp3 Player')
        self.load = Button(window, text='Load', width=10, command=self.load1, bg='grey')
        self.play = Button(window, text='Play', width=10, command=self.play1, bg='green')
        self.pause = Button(window, text='Pause', width=10, command=self.pause1, bg='yellow')
        self.stop = Button(window, text='Stop', width=10, command=self.stop1, bg='red')
        self.snglst = Listbox(window, width=30, height=15).grid(column=4)
        self.load.grid(column=0, row=1), self.play.grid(column=1, row=1), self.pause.grid(column=2, row=1), self.stop.grid(column=3, row=1)

        self.music_file = False
        self.playing_state = False

    def load1(self):
        self.music_file = filedialog.askopenfilename()

    def play1(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
        else:
            messagebox.showinfo(title=None, message='Load a song')

    def pause1(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
        else:
            mixer.music.unpause()
            self.playing_state = False

    def stop1(self):
        mixer.music.stop()


root = Tk()
root.config(bg='cyan')
# root.iconbitmap()
app = MusicPlayer(root)
root.mainloop()
