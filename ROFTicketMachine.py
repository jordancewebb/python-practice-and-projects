#Makes Tickets for ROF Project.
import pyautogui
import xlsxwriter 
import json
import pyperclip

#This dictionary will contain all the information necessary to fill out a ring of fire project ticket
#Makes Tickets for ROF Project.

dJson = {'Requestor': 'Joshua Brown', 'Title': 'ROF addition in ' + rJson[Building] + ' ' + rJson[Number], 'Description': 'Added USB-C Dongle', 'Building Location':rJson[Building}, 'Room location': rJson[Number], 'Callback number' : '252-328-9830','Responsible': 'Jordance Webb',  }
#This will be a json for the room data structure, representing a classroom on campus
rJson = {'Building': null, 'Number': null,}

#Collects room information from command line and stores them in a stack
def collectRoom():
    
def fillForm():
    #for debugging purposes, prints json contents to console
    print (json.dumps(dJson, indent = 4))
    print (json.dumps(dJson, indent = 4))

    #test that the functions from imported classes/modules actually work
    distance = 28
    counter = 5
    while(counter > 0):
        pyautogui.dragRel(0, distance, duration = 0.2)
        pyperclip.copy(dJson['Title'])
        pyautogui.hotkey("ctrl", "V")
        counter = counter - 1

#Driver portion    
def main():
    fillForm()        
    exit()

if __name__ == "__main__":
    main() 
    
