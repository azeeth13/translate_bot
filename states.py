from aiogram.fsm.state import StatesGroup,State

class Translate(StatesGroup):
    language=State()
    trans=State()
    voice=State()