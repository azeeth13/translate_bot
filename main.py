import asyncio
import logging
import sys
import os
from os import getenv
from typing import Any, Dict
from token_1 import TOKEN,text_to_voice
from aiogram import Bot, Dispatcher, F, Router, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message,CallbackQuery,FSInputFile
from states import Translate
from googletrans import Translator
from buttons import *


t=Translator()

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML)) 

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message,state: FSMContext) -> None:

    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!",reply_markup=menu)
    await state.set_state(Translate.language)

@dp.message(F.text,Translate.language)
async def echo_handler(message: Message, state:FSMContext) -> None:
    translate_text=message.text
    await state.update_data(
        {'translate_text':translate_text}
        )
    await state.set_state(Translate.trans)
    await message.answer('Enter a word ')

@dp.message(Translate.trans)
async def translate(message: Message, state:FSMContext) -> None:
    text=message.text
    d=await state.get_data()
    perevod=d.get('translate_text')
    if perevod == 'Uz -> Ru':
        inform=t.translate(text,dest='ru').text
        await message.answer(f'Your word:\n{inform}',reply_markup=voice)
        text_to_voice(inform,'ru')
    
    elif perevod == 'Ru -> Uz':
        inform=t.translate(text,dest='uz').text
        await message.answer(f'Your word:\n{inform}',reply_markup=voice)
        text_to_voice(inform,'tr')

    elif perevod == 'Uz -> En':
        inform=t.translate(text,dest='en').text
        await message.answer(f'Your word:\n{inform}',reply_markup=voice)
        text_to_voice(inform,'en')

    
    elif perevod == 'En -> Uz':
        inform=t.translate(text,dest='uz').text
        await message.answer(f'Your word:\n{inform}',reply_markup=voice)    
        text_to_voice(inform,'tr')
    await state.set_state(Translate.voice)



@dp.callback_query(Translate.voice)
async def voice_to(call:CallbackQuery,state:FSMContext):
    audio=FSInputFile('wordvoice.mp3')
    await bot.send_audio(call.message.chat.id,audio)
    os.remove('wordvoice.mp3')
    await state.clear






















async def main() -> None:
   
    
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())