import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Список усіх завдань
ALL_TASKS = [
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
    "Застав когось похвалити тебе", "Зроби так, щоб хтось обійняв тебе", "Попроси когось сказати слово задом наперед", "Змусь когось сказати 'вовк' без контексту", "Зроби так, щоб хтось завив як вовк", "Застав когось підняти руки догори", "Зроби, щоб хтось встав без причини", "Попроси когось заплющити очі на 5 секунд", "Зроби, щоб хтось сів на підлогу", "Змусь когось повторити за тобою фразу", "Отримай п’ять від будь-кого", "Зроби так, щоб хтось поплескав себе по голові", "Попроси когось показати танцювальний рух", "Змусь когось проспівати частину пісні", "Застав когось назвати тебе босом", "Отримай комплімент без прямого прохання", "Попроси когось зробити дивне обличчя", "Змусь когось сказати «мяу»", "Змусь когось сказати риму", "Застав когось розказати жарт", "Отримай підказку від когось (без пояснення для чого)", "Попроси когось порахувати до 10", "Змусь когось доторкнутися до чола", "Отримай будь-який предмет у подарунок", "Застав когось назвати своє улюблене число", "Змусь когось стрибнути", "Зроби так, щоб хтось запитав тебе: «Що ти задумав?»", "Попроси когось пройтись дзиґою", "Змусь когось показати емоцію «здивування»", "Застав когось зробити звук тварини", "Змусь когось закрити очі й вказати на північ", "Попроси когось придумати нове слово", "Застав когось сказати: «Ти сьогодні класно виглядаєш!»", "Попроси когось щось намалювати (на серветці, папері)", "Застав когось поворушити вухами (або зробити вигляд)", "Змусь когось сказати англійське слово", "Отримай від когось воду / напій", "Застав когось змінити місце сидіння", "Попроси когось розказати дитячий спогад", "Змусь когось згадати анекдот", "Застав когось доторкнутись до стіни", "Попроси когось щось приховати для тебе", "Застав когось показати улюблений танець", "Отримай чиюсь посмішку без жарту", "Застав когось тримати щось на голові", "Змусь когось пошепки щось сказати", "Отримай відповідь на питання, яке ще не задав", "Попроси когось подати тобі щось у стилі офіціанта", "Змусь когось загадати бажання", "Застав когось вимовити слово з 10 букв", "Змусь когось сказати: «Я виграв!»", "Попроси когось зобразити супергероя", "Змусь когось зробити селфі з тобою", "Попроси когось назвати тебе вигаданим іменем", "Отримай від когось жарт у відповідь на серйозне питання", "Застав когось назвати улюблений фрукт", "Попроси когось описати тебе трьома словами", "Змусь когось доторкнутись до підлоги", "Застав когось з'їсти щось із заплющеними очима", "Змусь когось принести тобі будь-що незвичне", "Застав когось пограти у «камінь-ножиці-папір»", "Отримай незвичну пораду", "Попроси когось вимовити скоромовку", "Змусь когось зробити щось однією рукою", "Застав когось сказати комплімент третій людині", "Попроси когось перерахувати 3 улюблені фільми", "Змусь когось доторкнутись до носа іншої людини", "Попроси когось сказати «Я прийшов з майбутнього»", "Застав когось встати й зробити уклін", "Змусь когось голосно сказати «О ні!»", "Попроси когось відкрити або закрити двері", "Змусь когось з’їсти щось незвичне (але їстівне)", "Застав когось тримати рівновагу на одній нозі", "Попроси когось назвати улюблений запах", "Змусь когось торкнутися до плеча іншої людини", "Застав когось зробити «повітряний поцілунок»", "Отримай будь-який смішний предмет"

]

# Словники для зберігання стану
user_tasks = {}
user_task_status = {}

def generate_tasks():
    """Генерує список з 6 унікальних завдань"""
    return random.sample(ALL_TASKS, 6)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обробник команди /start"""
    user_id = update.effective_user.id
    user_tasks[user_id] = generate_tasks()
    user_task_status[user_id] = ["➖"] * 6
    await show_tasks(update, context)

async def show_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Відображає список завдань з кнопками"""
    user_id = update.effective_user.id
    tasks = user_tasks.get(user_id, generate_tasks())
    statuses = user_task_status.get(user_id, ["➖"] * 6)
    
    # Формування клавіатури
    keyboard = [
        [
            InlineKeyboardButton("✅", callback_data=f"done_{i}"),
            InlineKeyboardButton("❌", callback_data=f"delete_{i}"),
            InlineKeyboardButton("♻️", callback_data=f"replace_{i}")
        ]
        for i in range(len(tasks))
    ]
    
    # Формування тексту повідомлення
    message_lines = [
        f"{i+1}. {status} {task}"
        for i, (task, status) in enumerate(zip(tasks, statuses))
    ]
    message_text = "📌 Ваші поточні завдання:\n\n" + "\n".join(message_lines)
    
    # Відправка або оновлення повідомлення
    if update.callback_query:
        await update.callback_query.edit_message_text(
            text=message_text,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    else:
        await update.message.reply_text(
            text=message_text,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обробник натискань кнопок"""
    query = update.callback_query
    await query.answer()
    
    user_id = update.effective_user.id
    action, task_index = query.data.split("_")
    task_index = int(task_index)
    
    # Ініціалізація даних, якщо потрібно
    if user_id not in user_tasks:
        user_tasks[user_id] = generate_tasks()
    if user_id not in user_task_status:
        user_task_status[user_id] = ["➖"] * 6
    
    # Обробка різних дій
    if action == "replace":
        available_tasks = [t for t in ALL_TASKS if t not in user_tasks[user_id]]
        if available_tasks:
            user_tasks[user_id][task_index] = random.choice(available_tasks)
            user_task_status[user_id][task_index] = "➖"
    
    elif action == "done":
        user_task_status[user_id][task_index] = "✅"
    
    elif action == "delete":
        user_tasks[user_id][task_index] = "---"
        user_task_status[user_id][task_index] = "❌"
    
    await show_tasks(update, context)

def main() -> None:
    """Точка входу програми"""
    application = Application.builder().token("ВАШ_ТОКЕН").build()
    
    # Додавання обробників
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler, pattern=r"^(done|delete|replace)_\d+$"))
    
    # Запуск бота
    application.run_polling()

if __name__ == "__main__":
    main()
