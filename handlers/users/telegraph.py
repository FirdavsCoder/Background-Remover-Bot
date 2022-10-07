from aiogram import types

from loader import dp, bot
from utils import photo_link
from utils import remove_background



@dp.message_handler(content_types = 'photo')
async def photo_hanndler(msg: types.Message):
	photo = msg.photo[-1]
	link = await photo_link(photo)
	await msg.answer(link)
	await msg.answer("Fon olinmoqda iltimos kuting! 5-10 sekund kuting!")
	new_photo = await remove_background(link)
	await msg.reply_document(document = new_photo, caption = "Background removed successfully!")
