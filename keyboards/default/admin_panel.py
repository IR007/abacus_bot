from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

admin_panel_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🆕 Yangi test qo'shish"),
            KeyboardButton("🔄 Testni tahrirlash")
        ],
        [
            KeyboardButton("⏹ Noaktiv testlar"),
            KeyboardButton("▶️ Aktiv testlar")
        ],
        [
            KeyboardButton("📚 Fanlar"),
            KeyboardButton("🔢 Sinflar")
        ],
    ],
    resize_keyboard=True
)

add_remove_science_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🆕 Yangi fan qo'shish"),
            KeyboardButton("🔄 Fanni o'zgartirish")
        ],
        [
            KeyboardButton("⬅️ Orqaga")
        ]
    ],
    resize_keyboard=True
)

add_remove_class_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🆕 Yangi sinf qo'shish"),
            KeyboardButton("🔄 Sinfni o'zgartirish")
        ],
        [
            KeyboardButton("⬅️ Orqaga")
        ]
    ],
    resize_keyboard=True
)
