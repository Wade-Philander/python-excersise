
#Code only works for .wav files

from playsound import playsound
import pygame
from pygame import mixer
from tkinter import *
from tkinter import filedialog

#playsound('Barry-White-Let-the-music-play.mp3')

root = Tk()
root.title('My Mp3 Player')
root.geometry("1000x300")
pygame.mixer.init()

# Intialize pygame MixerBarry-White-Let-the-music-play.wav

#Add song function
def add_song():
    root.song = filedialog.askopenfilename(filetypes=(("wav Files","*.wav"),("all files", "*.*")))   #This allows add song to go and search your song through the directery you insert
    
    root.song = root.song.replace("/home/user/Documents/PYTHON/","") #renaming the song/removing /home/user/Documents/PYTHON/ and just showing the title of the song
    root.song = root.song.replace(".wav","") #replacing it with nothing but removing the mp3
    song_box.insert(END, root.song)

# Play the song
def play():
    
    song = song_box.get(ACTIVE)+".wav"
    #song = f'/home/user/Documents/PYTHON/{song}.wav'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()

# Stop playing song
def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()


#Define Playlist Box
song_box = Listbox(root, bg="white", fg="blue", width=60, selectbackground="Black", selectforeground="white")

song_box.grid(pady=20)


play_btn= Button(root, text="Play Button", command=play)
pause_btn= Button(root, text="Pasue Button", command=pause)
unpause_btn= Button(root, text="Unpause Button", command=unpause)
stop_btn= Button(root, text="Stop Button", command=stop)



#add song to list box
add_song_btn= Button(root, text="Add Song", command=add_song)

#Control frames
controls_frame = Frame(root)
controls_frame.grid()

add_song_btn.grid(row=1, column=0)
play_btn.grid( row=1, column=1)
pause_btn.grid( row=1, column=2)
unpause_btn.grid( row=1, column=3)
stop_btn.grid( row=1, column=4)



'''
# creating a Menu

my_menu = Menu(root)
root.config(=my_menu)

# Add song to menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(Label="Add Song", menu=add_song_menu)
add_song_menu.add_command(Label="Add one song to playlsit", command=add_song)
'''

root.mainloop()