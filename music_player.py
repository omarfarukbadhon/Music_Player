# Required modules and libraries
from tkinter import *
import pygame
import os


# Main Track for Music player
class MusicPlayer:
    def __init__(self, root):
        self.root = root
        # Title of the window
        self.root.title("Martin Music Player")
        # Window Geometry
        self.root.geometry("800x300")
        # Initiating Pygame
        pygame.init()
        # Initiating Pygame Mixer
        pygame.mixer.init()
        # Declaring track Variable
        self.track = StringVar()
        # Declaring Status Variable
        self.status = StringVar()

        # Creating track for playing song status
        song_track = LabelFrame(self.root, text="Playing song track", font=("times new roman", 15, "italic"),
                                bg="black", fg="white", bd=5, relief=GROOVE)
        song_track.place(x=0, y=0, width=500, height=200)
        song_track1 = Label(song_track, textvariable=self.track, font=("times new roman", 12, "italic"),
                            bg="black", fg="white").grid(row=0, column=0, padx=10, pady=5)
        song_track2 = Label(song_track, textvariable=self.status, font=("times new roman", 15, "italic"),
                            bg="black", fg="white").grid(row=1, column=0, padx=10, pady=5)

        # Creating Button Frame
        button_frame = LabelFrame(self.root, text="Control track", font=("times new roman", 15, "italic"), bg="grey",
                                  fg="white", bd=5, relief=GROOVE)
        button_frame.place(x=0, y=200, width=500, height=100)
        # Inserting Play Button
        playbtn = Button(button_frame, text="Play", command=self.playsong, width=6, height=1,
                         font=("times new roman", 16, "italic"), fg="navyblue", bg="grey").grid(row=0, column=0,
                                                                                                padx=15, pady=20)
        # Inserting Pause Button
        playbtn = Button(button_frame, text="Pause", command=self.pausedsong, width=8, height=1,
                         font=("times new roman", 16, "italic"), fg="navyblue", bg="grey").grid(row=0, column=1,
                                                                                                padx=15, pady=20)

        # Inserting Stop Button
        playbtn = Button(button_frame, text="Stop", command=self.stopsong, width=6, height=1,
                         font=("times new roman", 16, "italic"), fg="navyblue", bg="grey").grid(row=0, column=3,
                                                                                                padx=15, pady=20)
        # Creating playlist frame
        playlist_frame = LabelFrame(self.root, text="Music Playlist", font=("times new roman", 15, "italic"),
                                    bg="black", fg="white", bd=5, relief=GROOVE)
        playlist_frame.place(x=500, y=0, width=300, height=300)

        # Inserting scrollbar
        scrollbar = Scrollbar(playlist_frame, orient=VERTICAL)
        # Inserting Playlist listbox
        self.playlist = Listbox(playlist_frame, yscrollcommand=scrollbar.set, selectbackground="grey",
                                selectmode=SINGLE, font=("times new roman", 12, "italic"), bg="black", fg="white",
                                bd=5, relief=GROOVE, height=300)
        # Applying scrollbar to listbox
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)

        # changing the directory for fetching songs
        os.chdir("H:\\phone\\music")
        # Fetching all song
        music_track_list = os.listdir()
        # Inserting all song in the playlist
        # serial = 1
        for track in music_track_list:
            # track = str(serial) + "." + track
            self.playlist.insert(END, track)
            # serial += 1

    # Define play song function
    def playsong(self):
        """load the selected song and play it"""
        # Displaying selected song title
        self.track.set(self.playlist.get(ACTIVE))
        # Displaying status
        self.status.set("-Playing")
        # loading selected song
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        # Play the loaded song
        pygame.mixer.music.play()

    def stopsong(self):
        """To stop the loaded song"""
        # Displaying status
        self.status.set("-Stopped")
        # stop the loaded song
        pygame.mixer.music.stop()

    def pausedsong(self):
        """To pause the loaded song"""
        # Displaying status
        self.status.set("-Paused")
        # paused the loaded song
        pygame.mixer.music.pause()


# creating tkinter container
root = Tk()
# pass the root through MusicPlayer class
MusicPlayer(root)
# root window looping
root.mainloop()



