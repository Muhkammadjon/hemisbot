# from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# kb = [
#         [KeyboardButton(text="modul")],
#         [KeyboardButton(text="hemis")],
#         [KeyboardButton(text="variant makr")]
#     ]
# keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def make_row_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
    """
    Создаёт реплай-клавиатуру с кнопками в один ряд
    :param items: список текстов для кнопок
    :return: объект реплай-клавиатуры
    """
    row = [KeyboardButton(text=item) for item in items]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True, one_time_keyboard=True)