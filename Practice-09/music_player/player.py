import os
import pygame


class MusicPlayer:
    def __init__(self, folder):
        self.folder = folder
        self.tracks = []
        self.index = 0

        for file in os.listdir(folder):
            if file.endswith(".mp3") or file.endswith(".wav"):
                self.tracks.append(file)

        self.tracks.sort()

    def load_track(self):
        if len(self.tracks) > 0:
            path = os.path.join(self.folder, self.tracks[self.index])
            pygame.mixer.music.load(path)

    def play(self):
        if len(self.tracks) > 0:
            self.load_track()
            pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def next_track(self):
        if len(self.tracks) > 0:
            self.index = (self.index + 1) % len(self.tracks)
            self.play()

    def previous_track(self):
        if len(self.tracks) > 0:
            self.index = (self.index - 1) % len(self.tracks)
            self.play()

    def get_current_track(self):
        if len(self.tracks) > 0:
            return self.tracks[self.index]
        return "No tracks"
