import os
from tkinter import *
from tkinter import filedialog
import pygame

# Ilovani ishga tushirish uchun asosiy oynani yaratish
root = Tk()
root.title("Music Player")
root.geometry("500x400")

pygame.mixer.init()

# Ovoz yozuvlari ro'yxati va pleylist
songs = []
current_song = ""
paused = False


# Musiqa fayllarini yuklash uchun funksiya
def load_music():
    global current_song
    root.directory = filedialog.askdirectory()
    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext in [".mp3", ".wav", ".ogg"]:
            songs.append(song)

    for song in songs:
        song_list.insert("end", song)
    song_list.select_set(0)
    current_song = songs[song_list.curselection()[0]]


# Musiqa ijro etish funksiyasi
def play_music():
    global current_song, paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.load(os.path.join(root.directory, current_song))
        pygame.mixer.music.play(loops=0)


# Musiqa pauza qilish funksiyasi
def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused = True


# Keyingi musiqa ijro etish funksiyasi
def next_music():
    global current_song, paused
    next_song_index = song_list.curselection()[0] + 1
    if next_song_index > len(songs) - 1:
        next_song_index = 0
    song_list.select_clear(0, 'end')
    song_list.select_set(next_song_index)
    current_song = songs[next_song_index]
    play_music()


# Oldingi musiqa ijro etish funksiyasi
def prev_music():
    global current_song, paused
    prev_song_index = song_list.curselection()[0] - 1
    if prev_song_index < 0:
        prev_song_index = len(songs) - 1
    song_list.select_clear(0, 'end')
    song_list.select_set(prev_song_index)
    current_song = songs[prev_song_index]
    play_music()


# Menyu yaratish
menubar = Menu(root)
root.config(menu=menubar)
organise_menu = Menu(menubar, tearoff=False)
organise_menu.add_command(label="Select Folder", command=load_music)
menubar.add_cascade(label="Organise", menu=organise_menu)

# Ovoz yozuvlari ro'yxati
song_list = Listbox(root, bg="black", fg="white", width=100, height=15)
song_list.pack()

# Tugmalar uchun rasm ob'ektlarini yaratish
play_button_photo = PhotoImage(file="play (1).png")
pause_button_photo = PhotoImage(file="pause (1).png")
next_button_photo = PhotoImage(file="next.png")
prev_button_photo = PhotoImage(file="previous.png")

# Boshqaruv tugmalarini yaratish
control_frame = Frame(root)
control_frame.pack(pady=20)
play_button = Button(control_frame, image=play_button_photo, borderwidth=0, command=play_music)
pause_button = Button(control_frame, image=pause_button_photo, borderwidth=0, command=pause_music)
next_button = Button(control_frame, image=next_button_photo, borderwidth=0, command=next_music)
prev_button = Button(control_frame, image=prev_button_photo, borderwidth=0, command=prev_music)

# Tugmalarni joylashtirish
play_button.grid(row=0, column=0, padx=7, pady=10)
pause_button.grid(row=0, column=1, padx=7, pady=10)
next_button.grid(row=0, column=2, padx=7, pady=10)
prev_button.grid(row=0, column=3, padx=7, pady=10)

# Ilovani ishga tushirish
root.mainloop()
