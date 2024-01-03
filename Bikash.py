
import os
import time
import math
import json
import string
import random
import traceback
import asyncio
import datetime
import aiofiles
from random import choice 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid, UserNotParticipant, UserBannedInChannel
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid
from telegraph import upload_file
from database import Database


UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "https://t.me/BikashGadgetsTech")
BOT_OWNER = int(os.environ["BOT_OWNER"])
DATABASE_URL = os.environ["DATABASE_URL"]
db = Database(DATABASE_URL, "BgtConvertBot")

Bgt = Client(
    "Media To Link",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
)

START_TEXT = """**🥀 𝐇𝐞𝐲 {} 
𝐈 𝐚𝐦 𝐀 𝐒𝐢𝐦𝐩𝐥𝐞 𝐌𝐞𝐝𝐢𝐚 𝐓𝐨 𝐋𝐢𝐧𝐤 𝐂𝐨𝐧𝐯𝐞𝐫𝐭 𝐁𝐨𝐭**

𝐈 𝐀𝐦 𝐂𝐨𝐧𝐯𝐞𝐫𝐭 𝐕𝐢𝐝𝐞𝐨 𝐎𝐫 𝐅𝐢𝐥𝐞 𝐁𝐨𝐭𝐡 🥀

🥀 𝐌𝐚𝐝𝐞 𝐁𝐲 [𝐌𝐚𝐡𝐭𝐨 𝐀𝐧𝐣𝐚𝐥𝐢](https://t.me/QUEENx_GOD) 🥀

🥀 [𝐂𝐡𝐚𝐧𝐧𝐞𝐥](https://t.me/+1ipwZ6f0hWoxZmI1) 🥀

🥀 [𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/+fztuVtP1frMwYTk1) 🥀

"""

HELP_TEXT = """**𝐇𝐞𝐲, {} 𝐒𝐞𝐞 𝐌𝐲 𝐂𝐦𝐝:**

𝐉𝐮𝐬𝐭 𝐒𝐞𝐧𝐝 𝐀𝐧𝐲 𝐌𝐞𝐝𝐢𝐚 
𝐀𝐧𝐝 𝐈 𝐖𝐢𝐥𝐥 𝐔𝐩𝐥𝐨𝐚𝐝 
𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐩𝐡 𝐋𝐢𝐧𝐤

𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐂𝐦𝐝𝐬

/about : 𝐅𝐨𝐫 𝐀𝐛𝐨𝐮𝐭 𝐌𝐞
/bikash : 𝐀𝐛𝐨𝐮𝐭 𝐎𝐰𝐧𝐞𝐫
/helo : 𝐅𝐨𝐫 𝐌𝐨𝐫𝐞 𝐇𝐞𝐥𝐩
/start : 𝐒𝐭𝐚𝐫𝐭 𝐓𝐡𝐄 𝐁𝐨𝐭
/status : 𝐅𝐨𝐫 𝐁𝐨𝐭 𝐒𝐭𝐚𝐭𝐮𝐬
 
🥀 𝐌𝐚𝐝𝐞 𝐁𝐲 [𝐌𝐚𝐡𝐭𝐨 𝐀𝐧𝐣𝐚𝐥𝐢](https://t.me/QUEENx_GOD) 🥀

🥀 [𝐂𝐡𝐚𝐧𝐧𝐞𝐥](https://t.me/+1ipwZ6f0hWoxZmI1) 🥀

🥀 [𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/+fztuVtP1frMwYTk1) 🥀
 
 """

ABOUT_TEXT = """--** 𝐌𝐚𝐡𝐭𝐨 𝐀𝐛𝐨𝐮𝐭 𝐌𝐞**--🥀

🤖 **𝐍𝐚𝐦𝐞 :** [𝐌𝐞𝐝𝐢𝐚 𝐓𝐨 𝐋𝐢𝐧𝐤](https://telegram.me/{})

📢 **𝐂𝐡𝐚𝐧𝐧𝐞𝐥 :** [𝐌𝐀𝐇𝐓𝐎] (https://t.me/+1ipwZ6f0hWoxZmI1)

📢 **𝐔𝐩𝐝𝐚𝐭𝐞𝐬 :** [𝐌𝐀𝐇𝐓𝐎] (https://t.me/+fztuVtP1frMwYTk1)

👥 **𝐒𝐮𝐩𝐩𝐨𝐫𝐭 :** [𝐌𝐀𝐇𝐓𝐎] (https://t.me/AnjalixSupportxGroup)

🥀 **𝐂𝐡𝐚𝐭𝐭𝐢𝐧𝐠 :** [𝐌𝐀𝐇𝐓𝐎] (https://t.me/AnjalixSupportxGroup)

"""

FORCE_SUBSCRIBE_TEXT = "🥀 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐓𝐡𝐞𝐧 𝐓𝐫𝐲 𝐌𝐞 🥀"

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🥀 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 🥀', url='{UPDATE_CHANNEL}'),
        InlineKeyboardButton('𝐂𝐡𝐚𝐧𝐧𝐞𝐥', url='https://t.me/+1ipwZ6f0hWoxZmI1'),
        ],[
        InlineKeyboardButton('🥀 𝐇𝐨𝐦𝐞 🏘', callback_data='home'),
        InlineKeyboardButton('𝐀𝐛𝐨𝐮𝐭 🔰', callback_data='about'),
        InlineKeyboardButton('❌ 𝐂𝐥𝐨𝐬𝐞 ❌', callback_data='close')
        ]]
    )

HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🥀 𝐒𝐮𝐩𝐩𝐨𝐫𝐭',url='https://t.me/Bgt_Chat'),
        InlineKeyboardButton('𝐂𝐡𝐚𝐧𝐧𝐞𝐥', url='https://t.me/+1ipwZ6f0hWoxZmI1'),
        ],[
        InlineKeyboardButton('🥀 𝐇𝐨𝐦𝐞 🏘', callback_data='home'),
        InlineKeyboardButton('𝐀𝐛𝐨𝐮𝐭 🔰', callback_data='about'),
        InlineKeyboardButton('❌ 𝐂𝐥𝐨𝐬𝐞 ❌', callback_data='close')
        ]]
    )

ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 📢', url='{UPDATE_CHANNEL}'),
        InlineKeyboardButton('𝐂𝐡𝐚𝐧𝐧𝐞𝐥', url='https://t.me/+1ipwZ6f0hWoxZmI1'),
        ],[
        InlineKeyboardButton('🥀 𝐇𝐨𝐦𝐞 🏘', callback_data='home'),
        InlineKeyboardButton('🥀 𝐇𝐞𝐥𝐩 🌺', callback_data='help'),
        InlineKeyboardButton('❌ 𝐂𝐥𝐨𝐬𝐞 ❌', callback_data='close')
        ]]
    )


async def send_msg(user_id, message):
	try:
		await message.copy(chat_id=user_id)
		return 200, None
	except FloodWait as e:
		await asyncio.sleep(e.x)
		return send_msg(user_id, message)
	except InputUserDeactivated:
		return 400, f"{user_id} : 𝐃𝐞𝐚𝐜𝐭𝐢𝐯𝐚𝐭𝐞𝐝\n"
	except UserIsBlocked:
		return 400, f"{user_id} : 𝐔𝐬𝐞𝐫 𝐈𝐬 𝐁𝐥𝐨𝐜𝐤𝐞𝐝\n"
	except PeerIdInvalid:
		return 400, f"{user_id} : 𝐔𝐬𝐞𝐫 𝐈𝐃 𝐈𝐧𝐯𝐚𝐢𝐥𝐞𝐝\n"
	except Exception as e:
		return 500, f"{user_id} : {traceback.format_exc()}\n"


@Bgt.on_callback_query()
async def cb_handler(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            reply_markup=HELP_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT.format((await bot.get_me()).username),
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.message.delete()


@Bgt.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    if not await db.is_user_exist(update.from_user.id):
	    await db.add_user(update.from_user.id)
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
	reply_markup=START_BUTTONS
    )


@Bgt.on_message(filters.private & filters.command(["help"]))
async def help(bot, update):
    if not await db.is_user_exist(update.from_user.id):
	    await db.add_user(update.from_user.id)
    await update.reply_text(
        text=HELP_TEXT,
      	disable_web_page_preview=True,
	reply_markup=HELP_BUTTONS
    )


@Bgt.on_message(filters.private & filters.command(["about"]))
async def about(bot, update):
    if not await db.is_user_exist(update.from_user.id):
	    await db.add_user(update.from_user.id)
    await update.reply_text(
        text=ABOUT_TEXT.format((await bot.get_me()).username),
        disable_web_page_preview=True,
	reply_markup=ABOUT_BUTTONS
    )


@Bgt.on_message(filters.media & filters.private)
async def telegraph_upload(bot, update):
    if not await db.is_user_exist(update.from_user.id):
	    await db.add_user(update.from_user.id)
    if UPDATE_CHANNEL:
        try:
            user = await bot.get_chat_member(UPDATE_CHANNEL, update.chat.id)
            if user.status == "kicked":
                await update.reply_text(text="𝐘𝐨𝐮 𝐀𝐫𝐞 𝐁𝐚𝐧𝐧𝐞𝐝 !")
                return
        except UserNotParticipant:
            await update.reply_text(
		  text=FORCE_SUBSCRIBE_TEXT,
		  reply_markup=InlineKeyboardMarkup(
			  [[InlineKeyboardButton(text="𝐔𝐩𝐝𝐚𝐭𝐞𝐬 ", url=f"https://telegram.me/{UPDATE_CHANNEL}")]]
		  )
	    )
            return
        except Exception as error:
            print(error)
            await update.reply_text(text="🥀 𝐒𝐨𝐦𝐞𝐭𝐡𝐢𝐧𝐤 𝐖𝐫𝐨𝐧𝐠 ❌  𝐂𝐨𝐧𝐭𝐚𝐜𝐭 [𝐎𝐰𝐧𝐞𝐫](https://t.me/QUEENx_GOD) ", disable_web_page_preview=True)
            return
    medianame = "./DOWNLOADS/" + "QUEENx_GOD/MhConvertBot"
    text = await update.reply_text(
        text="🌹 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐓𝐨 𝐌𝐚𝐡𝐭𝐨 𝐀𝐧𝐣𝐚𝐥𝐢 𝐒𝐞𝐫𝐯𝐞𝐫 🌺 ...",
        disable_web_page_preview=True
    )
    await bot.download_media(
        message=update,
        file_name=medianame
    )
    await text.edit_text(
        text="🥀 𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐓𝐞𝐥𝐞𝐠𝐡𝐫𝐚𝐩𝐡 𝐋𝐢𝐧𝐤 ....",
        disable_web_page_preview=True
    )
    try:
        response = upload_file(medianame)
    except Exception as error:
        print(error)
        await text.edit_text(
            text=f"𝐄𝐫𝐫𝐨𝐫 :- {error}",
            disable_web_page_preview=True
        )
        return
    try:
        os.remove(medianame)
    except Exception as error:
        print(error)
        return
    await text.edit_text(
        text=f"🥀 𝐋𝐢𝐧𝐤 ➡️ https://telegra.ph{response[0]}\n\n [𝐌𝐚𝐡𝐭𝐨 𝐀𝐧𝐣𝐚𝐥𝐢](https://t.me/AnjalixSupportxGroup)",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="🥀 𝐎𝐞𝐩𝐞𝐧 𝐋𝐢𝐧𝐤 🇮🇳", url=f"https://telegra.ph{response[0]}"),
                    InlineKeyboardButton(text="🥀 𝐒𝐡𝐚𝐫𝐞 𝐋𝐢𝐧𝐤 🇮🇳", url=f"https://telegram.me/share/url?url=https://telegra.ph{response[0]}")
                ],
                [
                    InlineKeyboardButton(text="📢 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 📢", url=f"https://t.me/+fztuVtP1frMwYTk1")
                ],
                [
                    InlineKeyboardButton(text"🥀 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 🥀", url=f"https://t.me/AnjalixSupportxGroup")
                ],
                [
                    InlineKeyboardButton(text"🥀 𝐂𝐡𝐚𝐭𝐭𝐢𝐧𝐠 𝐆𝐫𝐨𝐮𝐩 🥀", url=f"https://t.me/AnjalixSupportxGroup")
                ]
            ]
        )
    )


@Bgt.on_message(filters.private & filters.command("broadcast") & filters.user(BOT_OWNER) & filters.reply)
async def broadcast(bot, update):
	broadcast_ids = {}
	all_users = await db.get_all_users()
	broadcast_msg = update.reply_to_message
	while True:
	    broadcast_id = ''.join([random.choice(string.ascii_letters) for i in range(3)])
	    if not broadcast_ids.get(broadcast_id):
	        break
	out = await update.reply_text(text=f"❇️ 𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 ✔️")
	start_time = time.time()
	total_users = await db.total_users_count()
	done = 0
	failed = 0
	success = 0
	broadcast_ids[broadcast_id] = dict(total = total_users, current = done, failed = failed, success = success)
	async with aiofiles.open('broadcast.txt', 'w') as broadcast_log_file:
	    async for user in all_users:
	        sts, msg = await send_msg(user_id = int(user['id']), message = broadcast_msg)
	        if msg is not None:
	            await broadcast_log_file.write(msg)
	        if sts == 200:
	            success += 1
	        else:
	            failed += 1
	        if sts == 400:
	            await db.delete_user(user['id'])
	        done += 1
	        if broadcast_ids.get(broadcast_id) is None:
	            break
	        else:
	            broadcast_ids[broadcast_id].update(dict(current = done, failed = failed, success = success))
	if broadcast_ids.get(broadcast_id):
	    broadcast_ids.pop(broadcast_id)
	completed_in = datetime.timedelta(seconds=int(time.time()-start_time))
	await asyncio.sleep(3)
	await out.delete()
	if failed == 0:
	    await update.reply_text(text=f"🥀 𝐁𝐫𝐨𝐚𝐝𝐂𝐚𝐬𝐭 𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐝 `{completed_in}`\n\n🥀 𝐓𝐨𝐭𝐚𝐥 𝐔𝐬𝐞𝐫 {total_users}.\n🥀 𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞 {done}, {success} 𝐒𝐮𝐜𝐜𝐞𝐬𝐬 {failed} 𝐅𝐚𝐢𝐥𝐞𝐝.", quote=True)
	else:
	    await update.reply_document(document='broadcast.txt', caption=f"🥀 𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭𝐞𝐝 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐈𝐧 `{completed_in}`\n\n🥀 𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭𝐞𝐝 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐓𝐨 {total_users} 𝐔𝐬𝐞𝐫𝐬✔️\n𝐁𝐫𝐨𝐚𝐝𝐂𝐚𝐬𝐭𝐞 𝐈𝐧 {done}, {success} 𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞 ✅ {failed} 𝐅𝐚𝐢𝐥𝐞𝐝 ❌")
	os.remove('broadcast.txt')


@Bgt.on_message(filters.private & filters.command("status"), group=5)
async def status(bot, update):
    total_users = await db.total_users_count()
    text = "**🥀 𝐁𝐨𝐭 𝐒𝐭𝐚𝐭𝐮𝐬 📊**\n"
    text += f"\n**🥀 𝐓𝐨𝐭𝐚𝐥 𝐔𝐬𝐞𝐫𝐬 🥀:** `{total_users}`"
    await update.reply_text(
        text=text,
        quote=True,
        disable_web_page_preview=True
    )


Bgt.run()
