import webbrowser
import os
import tkinter as tk


def webOpen(filename):
    webbrowser.get('"C:\\Program Files\\Mozilla Firefox\\firefox.exe" %s').open(filename, new=2)


def anonWebOpen(filename):
    webbrowser.get('"X:\\Tor Browser\\Browser\\firefox.exe" %s').open(filename, new=2)


def to_series9_format(name):
    temp = ''
    for char in name:
        temp += char if char != ' ' else '-'
    return str(temp)


def to_google_format(name):
    temp = ''
    for char in name:
        temp += char if char != ' ' else '+'
    return str(temp)


def to_vodlocker_format(name):
    temp = ""
    for char in name:
        temp += char if char != ' ' else '+'
    return str(temp)


if __name__ == '__main__':
    # get clipboard data
    root = tk.Tk()
    # keep the window from showing
    root.withdraw()
    data = root.clipboard_get()
    webOpen(r'https://www.google.com/search?&q=' + to_google_format(data) +
            ' دانلود')
    webOpen('https://www7.series9.to/movie/search/' + to_series9_format(data))
    webOpen(r'https://www.google.com/search?q=intitle%3A%22index+of%22+' + to_google_format(data) + r' (mp4|mkv|avi)')
    webOpen(r'https://vidcloud9.com/search.html?keyword=' + to_vodlocker_format(data))
    anonWebOpen(r'https://www.pirate-bay.net/search?q=' + to_google_format(data))
    webOpen(r'https://rarbgmirror.org/torrents.php?search=' + to_google_format(data) + r'&order=seeders&by=DESC')

