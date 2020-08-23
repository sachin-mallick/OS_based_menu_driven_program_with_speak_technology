import os
import pyttsx3

print("******************************* Hello !! Welcome to the Menu Driven Program Services ********************************")
pyttsx3.speak("\n\n\n\n\n\n  Helloo ! \n\n\n Welcome to the Menu driven program services \n\n\n")
pyttsx3.speak(" My Name is Alexx , and I am here to help you!")

print()
while True:   
    print("Hey !! what you want to execute ? \n\n" ,end='')
    pyttsx3.speak("Please write the task you want to execute ")
    i = input()
    if("execute" in i) and ("chrome" in i) :
        print("Chrome Browser is executing... Please Wait !!")
        os.system("chrome")
    elif("execute" in i) and (("mediaplayer" in i) or ("songplayer" in i)):
        print("Media Player is executing... Please Wait !!")
        os.system("wmplayer")
    elif("execute" in i) and (("notepad" in i)or("editor" in i)):
        print("Text Editor is executing... Please Wait !!")
        os.system("notepad")
    
    elif("execute" in i) and (("paint" in i) or ("drawing software" in i)):
        print("Paint is executing... Please Wait !!")
        os.system("mspaint")
    elif("date" in i):
        os.system("date")
    elif("calculator" in i):
        print("Calculator is executing... Please Wait !!")
        os.system("calc")    
    
    
    elif("execute" in i) and ("youtube" in i):
        print("Youtube is executing... Please Wait !!")
        os.system("chrome www.youtube.com")
    elif("execute" in i) and ("linkedin" in i):
        print("linkedin is executing... Please Wait !!")
        os.system("chrome www.linkedin.com")
    
    
    
   
    elif(("show" in i)or("list of" in i))and("directory" in i):  
        print("We are going to display list of all directories.... Please Wait !!")
        os.system("dir")  
    elif("clear" in i)and("screen" in i):
        os.system("cls")     
                      
    elif("exit" in i):
        pyttsx3.speak("Hope you have enjoyed our Services. Thank you and have a nice day...!!!")
        print("GOOD BYE.....!")
        print("\n************************************************************************************************************************")
        os.system(exit())
        break