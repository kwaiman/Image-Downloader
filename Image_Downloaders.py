import requests
import os

def image_dl():
    urlName = input('Please provide the URL name.\n')
    r = requests.get(urlName, stream = True)
    r.raw.decode_content = True
    pathAnswer = 0
    while pathAnswer != 1 and pathAnswer != 2:
        pathAnswer = int(input('Do you want to save the images on (1) Desktop, or (2) Downloads folder?\nPlease return 1 or 2\n'))
        if pathAnswer == 1:
            pathName = 'Desktop'
            break
        elif pathAnswer == 2:
            pathName = 'Downloads'
            break
        print('Please enter 1 or 2.\n')
    fileName = input('Please enter the file name you want to be saved.\n') + '.jpeg'
    fullPathName = pathName + '/' + fileName
    # Change the directory to the user's home directory
    homeDir = os.path.expanduser('~')
    os.chdir(homeDir)
    # download the image(file) to the selected path
    with open(fullPathName,'wb') as f:
        f.write(r.content)

# URL for testing: https://cdn.cdnparenting.com/articles/2018/06/27181318/lord-shiva-1800672_1280-696x464.jpg

image_dl()
