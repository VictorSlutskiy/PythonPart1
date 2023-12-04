import sqlite3
import telebot
from functools import partial
from telebot import types
from random import sample

bot = telebot.TeleBot('6546851500:AAG43n51q8FjjS-d5mHrpgDCAoYDp6wyEpY')


def get_question():
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        option1 TEXT,
        option2 TEXT,
        option3 TEXT,
        option4 TEXT,
        answer TEXT
    );''')
    cursor.execute('SELECT * FROM questions ORDER BY RANDOM() LIMIT 10')
    questions = cursor.fetchall()
    conn.commit()
    conn.close()
    return questions


def check_answer(user_answer, correct_answer):
    return user_answer.lower() == correct_answer.lower()


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,
                     f"Привет, {message.from_user.first_name} {message.from_user.last_name}! Добро пожаловать в викторину. Готовы начать?")


@bot.message_handler(commands=['quiz'])
def quiz(message):
    questions = get_question()
    if questions:
        send_question(message, questions, 0,0)


def send_question(message, questions, index,correct_answers):
    question_data = questions[index]
    question_text = question_data[1]
    options = question_data[2:6]
    correct_answer = question_data[6]

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    for option in options:
        markup.add(types.KeyboardButton(option))

    bot.send_message(message.chat.id, question_text, reply_markup=markup)
    bot.register_next_step_handler(message, partial(check_and_reply, correct_answer=correct_answer, questions=questions, index=index, correct_answers=correct_answers))


def check_and_reply(message, correct_answer, questions, index,correct_answers):
    user_answer = message.text
    if check_answer(user_answer,correct_answer):
        correct_answers += 1
    index+=1
    if index < len(questions):
        send_question(message, questions, index,correct_answers)
    else:
        bot.send_message(message.chat.id,f"Количество правильных ответов: {correct_answers}")


bot.polling(none_stop=True)
