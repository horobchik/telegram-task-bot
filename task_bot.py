import random
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Список завдань
tasks = [
    "Прочитати 10 сторінок книги",
    "Зробити 20 віджимань",
    "Вивчити 5 нових слів англійською",
    "Провести 15 хвилин на свіжому повітрі",
    "Написати щоденниковий запис",
    "Прибрати на робочому столі",
    "Поздоровитися з трьома друзями",
    "Випити склянку води",
    "Зробити розтяжку 5 хвилин",
    "Планування на завтра",
    "Медитація 5 хвилин",
    "Приготувати нову страву"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Вибираємо 6 унікальних випадкових завдань
    selected_tasks = random.sample(tasks, 6)
    
    # Формуємо повідомлення
    message = "🌟 Ось 6 завдань для тебе на сьогодні:\n\n"
    message += "\n".join(f"▫️ {task}" for task in selected_tasks)
    
    # Відправляємо повідомлення
    await update.message.reply_text(message)

def main() -> None:
    # Токен вашого бота
    TOKEN = "7615231270:AAHWyL3-QGY6GUYFM46D5UP-dcAEQCymlEw"
    
    # Створюємо Application
    application = Application.builder().token(TOKEN).build()
    
    # Реєструємо обробник команди /start
    application.add_handler(CommandHandler("start", start))
    
    # Запускаємо бота
    print("Бот запущений...")
    application.run_polling()

if __name__ == '__main__':
    main()