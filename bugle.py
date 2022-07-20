import urllib.request
from tkinter import Tk
from tkinter.filedialog import askdirectory
path = askdirectory(title='Select Folder') # shows dialog box and return the path
print(path) 
for x in range(1,179):
    if x < 10:
        url = f'http://thebugle.leekworld.com/thebugle00{x}.mp3'
        urllib.request.urlretrieve(url, f'{path}/thebugle00{x}.mp3')
        print('downloading: ')
        print(url)


    if x >9 and x <100: 
        url = f'http://thebugle.leekworld.com/thebugle0{x}.mp3'
        urllib.request.urlretrieve(url, f'{path}/thebugle0{x}.mp3')
        print('downloading: ')
        print(url)




    if x > 100 and x<179:    
        url = f'http://thebugle.leekworld.com/thebugle0{x}.mp3'
        urllib.request.urlretrieve(url, f'{path}/thebugle0{x}.mp3')
        print('downloading: ')
        print(url)
