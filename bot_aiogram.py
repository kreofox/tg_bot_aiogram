import telebot


from aiogram import Bot 
from aiogram import Dispatcher
from aiogram import executor
from aiogram import types

bot = Bot('TOKEN')
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"]) #content_types=["start"]--> Tracks only the attached team. It is also possible without start 
async def start(message: types.Message):
    await message.answer("Hello") #Abbreviated code--> await bot.send_message(message.chat.id, "hello")    
    
@dp.message_handler()
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup(row_width = 2) #row_width -->How much will the button be on the row 
    markup.add(types.InlineKeyboardButton("site", url = "https://"))
    markup.add(types.InlineKeyboardButton("hello", callback_data= "hello"))
    await message.reply("hello",reply_markup=markup)

@dp.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)

@dp.message_handler(commands=["reply"])
async def reply(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True) #one_time_keyboard = True -->Shows once and then hides 
    markup.add(types.KeyboardButton("site"))
    markup.add(types.KeyboardButton("Photo"))
    await message.answer("hello", reply_markup= markup)

executor.start_polling(dp)