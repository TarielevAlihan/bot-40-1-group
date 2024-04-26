from aiogram import Router, F, types
from config import database
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup


survey_router = Router()


class BookSurvey(StatesGroup):
    name = State()
    age = State()
    occupation = State()
    salary_or_grade = State()


@survey_router.message(Command("stop"))
@survey_router.message(F.text.lower() == "стоп")
async def stop(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Спасибо за прохождение опроса!")

@survey_router.message(Command("survey"))
async def start_survey(message: types.Message, state: FSMContext):
    await state.update_data(survey=message.text)
    await state.set_state(BookSurvey.name)
    await message.answer("Как вас зовут?")


@survey_router.message(BookSurvey.name)
async def process_name(message: types.Message, state: FSMContext):
    age_text = message.text
    if not age_text.isdigit():
        await message.answer("Пожалута введите ваш возраст числами")
        return
    if age_text < '18':
        await message.answer("какая у вас средняя оценка в школе")

    if age_text >= '18':
        await message.answer("Какая у вас заработная плата")

    if age_text <= '7':
        await message.answer('Ты слишком маленький иди в садик')
        await state.clear()
        await message.answer("Спасибо за прохождение опроса!")

    if age_text >='60':
        await message.answer('Извините вы стары для опроса')
        await state.clear()
        await message.answer("Спасибо за прохождение опроса!")



    await state.update_data(name=message.text)
    await state.set_state(BookSurvey.age)
    await message.answer("Какой у вас род занятий")

@survey_router.message(BookSurvey.occupation)
async def process_age(message: types.Message, state: FSMContext):
    await state.update_data(occupation=message.text)
    await state.set_state(BookSurvey.salary_or_grade)
    await message.answer("Какая у вас зарплата")


@survey_router.message(BookSurvey.salary_or_grade)
async def process_gender(message: types.Message, state: FSMContext):
    await state.update_data(salary_or_grade=message.text)
    await message.answer("Спасибо за пройденный опрос!")
    await state.clear()


