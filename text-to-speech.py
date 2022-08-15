# modules
import pyttsx3
import os
# downloading packages
os.system("pip install pyttsx3")
os.system('cls')
# engine here 
#

"""
Made By Ishann
"""


def main():
    # getting voice gender -
    voicetype = input('''Choose Gender :  
Options - 
 - Male 
 - Female 
\n''')
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
#validationnn
   
    if voicetype == 'Female':
        engine.setProperty('voice', voices[1].id)
    # voice 

    # You Can Change The Path .!
    path = './text'
    #don't touch!

    dirs = os.listdir(path)
    #logic

    for file in dirs:
        files = file

    with open(f'./{path}/{files}') as f:
        
        contents = f.read()
        print('Text File Readed')
        engine.say(contents)
    #don't touch at all or u will get busted
        engine.runAndWait()


main()


"""
Made By Ishann
"""
