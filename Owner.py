from pyrogram import Client, filters



from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Bgt.on_message(
    filters.command("bikash")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/471ef129b9c1b479676fd.jpg",
        caption=f"""🥀 𝐌𝐚𝐡𝐭𝐨 𝐀𝐧𝐣𝐚𝐥𝐢 𝐈𝐬 𝐎𝐰𝐧𝐞𝐫 𝐎𝐟 𝐀𝐧𝐣𝐚𝐥𝐢 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 🌺, 𝐂𝐥𝐢𝐜𝐤 𝐁𝐞𝐥𝐨𝐰 𝐁𝐮𝐭𝐭𝐨𝐧 𝐅𝐨𝐫 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐚𝐡𝐭𝐨 𝐀𝐧𝐣𝐚𝐥𝐢 ♕, 𝐈𝐟 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩𝐬 𝐎𝐫 𝐎𝐭𝐡𝐞𝐫𝐬 𝐋𝐢𝐧𝐤, 𝐓𝐡𝐞𝐧 𝐂𝐥𝐢𝐜𝐤 𝐏𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧 𝐁𝐮𝐭𝐭𝐨𝐧 𝐂𝐥𝐢𝐜𝐤 𝐎𝐭𝐡𝐞𝐫𝐬 𝐁𝐮𝐭𝐭𝐨𝐧 & 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐎𝐫 𝐆𝐫𝐨𝐮𝐩.. 🥀 [𝐂𝐡𝐚𝐧𝐧𝐞𝐥](https://t.me/+2wa4knauqJk0N2Y1)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 𝐌𝐚𝐡𝐭𝐨 𝐀𝐧𝐣𝐚𝐥𝐢 🥀", url=f"https://t.me/QUEENx_GOD")
            ],          
            [
                    InlineKeyboardButton(
                        "🥀 𝐏𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧 🥀", url=f"https://t.me/QUEENx_GOD")
                ],
                [
                    InlineKeyboardButton(
                        "🥀 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 🥀", url=f"https://t.me/AnjalixSupportxGroup"
                    ),
                    InlineKeyboardButton(
                        "🥀 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 🥀", url=f"https://t.me/+fztuVtP1frMwYTk1")
                ]
            ]
        ),
    )
