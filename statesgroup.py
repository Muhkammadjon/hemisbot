from tkinter import SEL
from aiogram.fsm.state import StatesGroup, State

class File_choosing(StatesGroup):
    def __init__(self, filename1, filename2) -> None:
        self.filename1 = filename1
        self.filename2 = filename2
        

    choosing_file_order = State()
    
    choosing_file_send = State()