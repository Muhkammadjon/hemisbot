import asyncio
import sys
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, File, FSInputFile
# from aiogram.types.document import Document
from modul import modul
from mk import mk
from hemis import hemis
# from aiogram.methods.get_file import GetFile
#from keyboard import keyboard

from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from keyboard import make_row_keyboard
from statesgroup import File_choosing

from antichat import Antichat

bot=Bot("6989556455:AAF3ZLJnhksMR8teVBJaYdr1NhtjL4Vfiqg")
dp=Dispatcher()

@dp.message(F.text=="/start")
async def start(message: Message):
    shablon=FSInputFile('shablon.docx')
    await message.answer('Assalomu aleykum\nBotdan foydalanish uchun shablon qoidalari bilan tanishing')
    await message.answer_document(shablon)
    

file_names = ["Modul", "Hemis", "VM"]
keyingisi = ["next"]

# @dp.message(F.text=="/modul")
# async def modul(message: Message):
#     # document = message.document
#     # await bot.download(document)
#     await message.answer('faylni yuboring')

@dp.message(F.document)
async def file_handle(message: File, state: FSMContext):
    print(message.document.file_name)
    if not message.document.file_name.endswith('.docx'):
        await message.answer("Xato fayl qisqartmasi berildi")
    else:
        file_id = message.document.file_id
        # print(file_id)
        file = await bot.get_file(file_id)
        # print(file)
        file_path = file.file_path
        
        await bot.download_file(file_path, f"docx_file//{message.document.file_unique_id}.docx")
        filename1=f"docx_file//{message.document.file_unique_id}.docx"
        filename2=f"docx_file_tax//{message.document.file_unique_id}.docx"
        await message.reply(text='fayl qabul qilindi')
        
        global filename
        filename=File_choosing(filename1, filename2)
        


        await message.answer(
            text="Fayl turini belgilang:",
            reply_markup=make_row_keyboard(file_names)
        )
        # Устанавливаем пользователю состояние "выбирает название"
        await state.set_state(File_choosing.choosing_file_order)
    

@dp.message(
    File_choosing.choosing_file_order, 
    F.text.in_(file_names)
)
async def file_chosen(message: Message, state: FSMContext):
    await state.update_data(chosen_file=message.text.lower())
    file_order=message.text
    if file_order == "Modul":
        try:
            await modul(filename.filename1,filename.filename2)
        except:
            await message.answer("Faylda xatolik faylni tekshirib qayta yuklang")            
        #print("1")
    if file_order == "Hemis":
        try:
            await hemis(filename.filename1,filename.filename2)
        except:
            await message.answer("Faylda xatolik faylni tekshirib qayta yuklang")
            
        #print("2")
    if file_order == "VM":
        try:
            await mk(filename.filename1,filename.filename2)
        except:
            await message.answer("Faylda xatolik faylni tekshirib qayta yuklang")
            
        #print("3")        
    #await message.answer(text=f"{file_order}")
    await message.answer(
        text="keyingi bosqichga o'tish uchun tugmani bosing",
        reply_markup=make_row_keyboard(keyingisi)
    )
    await state.set_state(File_choosing.choosing_file_send)
    

@dp.message(
    File_choosing.choosing_file_send,
    F.text.in_(keyingisi)
)
async def file_send(message: Message, state: FSMContext):
    #print("send")
    #await state.update_data(chosen_file_send=message.text.lower())
    #await message.answer("tax")
    filename_tax=FSInputFile(filename.filename2,"tayyor.docx")
    await message.answer_document(filename_tax)
    await message.answer('tayyor')


#@dp.message(F.document)
async def filehandle_download(message: File): 
    # print(message)
    # await message.reply()
    # await message.reply(text='fayl qabul qilindi', reply_markup=keyboard)
    file_id = message.document.file_id
    # print(file_id)
    file = await bot.get_file(file_id)
    # print(file)
    file_path = file.file_path
    
    await bot.download_file(file_path, f"docx_file//{message.document.file_unique_id}.docx")
    filename1=f"docx_file//{message.document.file_unique_id}.docx"
    filename2=f"docx_file_tax//{message.document.file_unique_id}.docx"
    await message.reply(text='fayl qabul qilindi', reply_markup=keyboard)
    # print(filename1)
    await filehandle1(message, filename1, filename2)
    

#@dp.message(F.text=="modul")
async def filehandle_modul(message):
    await message.answer('modul')
    print(message.document.file_id)


async def filehandle1(message, filename1, filename2):
    # await bot.send_message(text="Qaysi sayt uchun")
    # print(message)
    # await message.answer('render')
    await modul(filename1,filename2)
    # await message.answer('render tugandi')
    await filehandle_send(message, filename2)
    
async def filehandle_send(message, filename2):
    # await message.answer('ishladi2')
    filename2_tax=FSInputFile(filename2,"tayyor.docx")
    await message.answer_document(filename2_tax)
    await message.answer('tayyor')
    


async def main():
    dp.message.middleware(Antichat(1))
    # await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    asyncio.run(main())
