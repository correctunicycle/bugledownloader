import urllib.request

for x in range(1,10):
    
    url = 'http://thebugle.leekworld.com/thebugle00'+ str(x) + '.mp3'
    urllib.request.urlretrieve(url, 'insert path for file storage here, example path shown in the other for loops will also need to be replaced with your path'+ str(x) + '.mp3')
    print('downloading: ')
    print(url)


for x in range(10,100):
    
    url = 'http://thebugle.leekworld.com/thebugle0'+ str(x) + '.mp3'
    urllib.request.urlretrieve(url, '/Users/john/Documents/TimesOnlineBugle/bugle0'+ str(x) + '.mp3')
    print('downloading: ')
    print(url)




for x in range(100,179):
    
    url = 'http://thebugle.leekworld.com/thebugle'+ str(x) + '.mp3'
    urllib.request.urlretrieve(url, '/Users/andy/Documents/TimesOnlineBugle/bugle'+ str(x) + '.mp3')
    print('downloading: ')
    print(url)
