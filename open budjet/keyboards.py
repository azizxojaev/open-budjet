from aiogram import types


async def startReply():
    btn = types.ReplyKeyboardRemove()
    btn = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row("🗳 Ovoz berish", "💰 Balans")
    btn.row("🔗 Referal ssilka", "📝 Qo'llanma")
    return btn

async def balanceReply():
    btn = types.ReplyKeyboardRemove()
    btn = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row("💳 Yechib olish")
    btn.row("🚫 Bekor qilish")
    return btn


async def referalInline():
    btn = types.InlineKeyboardMarkup()
    btn.add(
        types.InlineKeyboardButton("Do'stlarni Taklif Qilish⤴️", callback_data='0')
    )
    return btn