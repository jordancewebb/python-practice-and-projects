#Makes Tickets for ROF Project.
import pyautogui

#This dictionary will contain all the information necessary to fill out a ring of fire project ticket

dict = {'Requestor': 'Joshua Brown', 'Title': 'ROF addition in' +
Room.toString(),'Description': 'Added USB-C Dongle', 'Building Location':
        Room.name, 'Room location': Room.number, 'Callback number' : '252-328-9830',
        'Responsible': 'Jordance Webb',  }
#This will be a constructor for the room data structure, representing a classroom on campus
class Room:
    def __init__(self, building, number):
        self.building = building
        self.number = number

    def toString()
        return self.building + " " + self.number


def fillForm():
    relDistance = 28
    pyautogui.click()
        
     
