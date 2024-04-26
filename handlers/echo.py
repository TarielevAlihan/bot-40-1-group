from aiogram import Router, types


echo_router = Router()

@echo_router.message()
async def echo(message: types.Message):
    # logging.info(message)
    await message.answer("Я не понимаю вас, поробуйте следующие команды: \n"
    "/start - начать диалог\n"
    "/picture - отправить картинку")



@echo_router.message()
async def echo_message(message: types.Message):
    words = message.text.split()
    reversed_words = words[::-1]
    reversed_message = ' '.join(reversed_words)
    await message.reply(reversed_message)