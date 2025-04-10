import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Приклад завдань (додайте повний список)
TASK_EXAMPLES = [
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
    "Приготувати нову страву",
    "Застав когось похвалити тебе",
    "Зроби так, щоб хтось обійняв тебе",
    "Попроси когось сказати слово задом наперед",
    "Змусь когось сказати 'вовк' без контексту",
    "Зроби так, щоб хтось завив як вовк",
    "Застав когось підняти руки догори",
    "Зроби, щоб хтось встав без причини",
    "Попроси когось заплющити очі на 5 секунд",
    "Зроби, щоб хтось сів на підлогу",
    "Змусь когось повторити за тобою фразу",
    "Отримай п'ять від будь-кого",
    "Зроби так, щоб хтось поплескав себе по голові",
    "Попроси когось показати танцювальний рух",
    "Змусь когось проспівати частину пісні",
    "Застав когось назвати тебе босом",
    "Отримай комплімент без прямого прохання",
    "Попроси когось зробити дивне обличчя",
    "Змусь когось сказати «мяу»",
    "Змусь когось сказати риму",
    "Застав когось розказати жарт",
    "Отримай підказку від когось (без пояснення для чого)",
    "Попроси когось порахувати до 10",
    "Змусь когось доторкнутися до чола",
    "Отримай будь-який предмет у подарунок",
    "Застав когось назвати своє улюблене число",
    "Змусь когось стрибнути",
    "Зроби так, щоб хтось запитав тебе: «Що ти задумав?»",
    "Попроси когось пройтись дзиґою",
    "Змусь когось показати емоцію «здивування»",
    "Застав когось зробити звук тварини",
    "Змусь когось закрити очі й вказати на північ",
    "Попроси когось придумати нове слово",
    "Застав когось сказати: «Ти сьогодні класно виглядаєш!»",
    "Попроси когось щось намалювати (на серветці, папері)",
    "Застав когось поворушити вухами (або зробити вигляд)",
    "Змусь когось сказати англійське слово",
    "Отримай від когось воду / напій",
    "Застав когось змінити місце сидіння",
    "Попроси когось розказати дитячий спогад",
    "Змусь когось згадати анекдот",
    "Застав когось доторкнутись до стіни",
    "Попроси когось щось приховати для тебе",
    "Застав когось показати улюблений танець",
    "Отримай чиюсь посмішку без жарту",
    "Застав когось тримати щось на голові",
    "Змусь когось пошепки щось сказати",
    "Отримай відповідь на питання, яке ще не задав",
    "Попроси когось подати тобі щось у стилі офіціанта",
    "Змусь когось загадати бажання",
    "Застав когось вимовити слово з 10 букв",
    "Змусь когось сказати: «Я виграв!»",
    "Попроси когось зобразити супергероя",
    "Змусь когось зробити селфі з тобою",
    "Попроси когось назвати тебе вигаданим іменем",
    "Отримай від когось жарт у відповідь на серйозне питання",
    "Застав когось назвати улюблений фрукт",
    "Попроси когось описати тебе трьома словами",
    "Змусь когось доторкнутись до підлоги",
    "Застав когось з'їсти щось із заплющеними очима",
    "Змусь когось принести тобі будь-що незвичне",
    "Застав когось пограти у «камінь-ножиці-папір»",
    "Отримай незвичну пораду",
    "Попроси когось вимовити скоромовку",
    "Змусь когось зробити щось однією рукою",
    "Застав когось сказати комплімент третій людині",
    "Попроси когось перерахувати 3 улюблені фільми",
    "Змусь когось доторкнутись до носа іншої людини",
    "Попроси когось сказати «Я прийшов з майбутнього»",
    "Застав когось встати й зробити уклін",
    "Змусь когось голосно сказати «О ні!»",
    "Попроси когось відкрити або закрити двері",
    "Змусь когось з'їсти щось незвичне (але їстівне)",
    "Застав когось тримати рівновагу на одній нозі",
    "Попроси когось назвати улюблений запах",
    "Змусь когось торкнутися до плеча іншої людини",
    "Застав когось зробити «повітряний поцілунок»",
    "Отримай будь-який смішний предмет"
]

def generate_tasks():
    """Генерує 6 унікальних завдань"""
    return random.sample(TASK_EXAMPLES, 6)


user_data = {}

def generate_tasks():
    """Генерує 6 унікальних завдань"""
    return random.sample(TASK_EXAMPLES, 6)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обробка команди /start"""
    user_id = update.effective_user.id
    user_data[user_id] = {
        'tasks': generate_tasks(),
        'statuses': [""] * 6  # Пусті статуси на початку
    }
    
    # Вітальне повідомлення з кнопкою
    start_keyboard = [[InlineKeyboardButton("Почати", callback_data="show_rules")]]
    await update.message.reply_text(
        text="Виконай завдання під час вечірки і не видай себе. Якщо тебе запідозрили під час виконання і сказали - це завдання, воно згорає ❌.Якщо в тебе вийшло, відміть як виконано ✅",
        reply_markup=InlineKeyboardMarkup(start_keyboard)
    )

async def show_rules(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Показує правила з кнопкою"""
    query = update.callback_query
    await query.answer()
    
    rules_keyboard = [[InlineKeyboardButton("Показати завдання", callback_data="show_all_tasks")]]
    await query.edit_message_text(
        text="Якщо завдання надто складе, недоречне до стилю вечірки або тупе - заміни його 🔁. Не дозволено заміняти, якщо тобі просто не подобається завдання.Якщо під час гри виясниться що у тебе таке ж завдання яке виконував інший гравець, можеш обрати - всеодно спробувати виконати його або замінити на інше",
        reply_markup=InlineKeyboardMarkup(rules_keyboard)
    )

async def send_all_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Відправляє всі завдання окремими повідомленнями"""
    query = update.callback_query
    await query.answer()
    user_id = update.effective_user.id
    
    # Відправляємо кожне завдання окремим повідомленням
    for i, task in enumerate(user_data[user_id]['tasks']):
        keyboard = [
            [
                InlineKeyboardButton("✅ Виконано", callback_data=f"done_{i}"),
                InlineKeyboardButton("❌ Пропустити", callback_data=f"skip_{i}"),
                InlineKeyboardButton("🔁 Замінити", callback_data=f"replace_{i}")
            ]
        ]
        
       status = user_data[user_id]['statuses'][i]
        await context.bot.send_message(
            chat_id=user_id,
            text=f"📌 Завдання {i+1}:\n{status}{task}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обробляє всі натискання кнопок"""
    query = update.callback_query
    await query.answer()
    user_id = update.effective_user.id
    
    if query.data == "show_rules":
        await show_rules(update, context)
    elif query.data == "show_all_tasks":
        await send_all_tasks(update, context)
    else:
        action, task_index = query.data.split("_")
        task_index = int(task_index)
        
        if action == "done":
            user_data[user_id]['statuses'][task_index] = "✅ "
        elif action == "skip":
            user_data[user_id]['statuses'][task_index] = "❌ "
        elif action == "replace":
            current_tasks = user_data[user_id]['tasks']
            available_tasks = [t for t in TASK_EXAMPLES if t not in current_tasks]
            if available_tasks:
                user_data[user_id]['tasks'][task_index] = random.choice(available_tasks)
                user_data[user_id]['statuses'][task_index] = ""
        
        # Оновлюємо конкретне завдання
        keyboard = [
            [
                InlineKeyboardButton("✅ Виконано", callback_data=f"done_{task_index}"),
                InlineKeyboardButton("❌ Пропустити", callback_data=f"skip_{task_index}"),
                InlineKeyboardButton("🔁 Замінити", callback_data=f"replace_{task_index}")
            ]
        ]
        status = user_data[user_id]['statuses'][task_index]
        await query.edit_message_text(
            text=f"📌 Завдання {task_index+1}:\n{status}{user_data[user_id]['tasks'][task_index]}",
            reply_markup=InlineKeyboardMarkup(rules_keyboard),parse_mode="HTML"
        )

def main() -> None:
    """Запуск бота"""
    application = Application.builder().token("7615231270:AAHWyL3-QGY6GUYFM46D5UP-dcAEQCymlEw").build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_button))
    
    print("Бот запущений...")
    application.run_polling()

if __name__ == "__main__":
    main()




