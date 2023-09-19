class script(object):
    START_TXT = """<b>Hᴇʟʟᴏ 👋 {},

Mʏ Nᴀᴍᴇ Is <b><a href=https://t.me/{}>{}</a>, I ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴍᴀɴʏ Mᴏᴠɪᴇs, Sᴇʀɪᴇs & Tᴠ Sʜᴏᴡs.

<b>Cʜᴇᴄᴋ /help ғᴏʀ ᴍᴏʀᴇ.</b>
"""
    HELPS_TXT = """Hᴇʏ Wᴇʟᴄᴏᴍᴇ Tᴏ Mʏ Hᴇʟᴘ Sᴇᴄᴛɪᴏɴ Iғ Yᴏᴜ Sᴇᴇᴍ Lᴏꜱᴛ Oʀ Hᴀᴠᴇ A Dᴏᴜʙᴛ Uꜱᴇ Tʜᴇ Bᴜᴛᴛᴏɴꜱ Bᴇʟᴏᴡ Tᴏ Nᴀᴠɪɢᴀᴛᴇ Tʜʀᴏᴜɢʜ Iᴛ !"""

    HELP_TXT = """<b>Hᴇʟᴘ :</b>

Tʜɪs ʙᴏᴛ ɪs ᴡᴏʀᴋ ɪɴ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ ʙᴏᴛʜ. Iᴛs ᴠᴇʀʏ ᴇᴀsʏ ᴛᴏ sᴇᴀʀᴄʜ ᴇᴘɪsᴏᴅᴇs ɪɴ ᴛʜɪs ʙᴏᴛ.

<b>Hᴏᴡ Tᴏ Sᴇᴀʀᴄʜ ?</b>
• Fɪʀsᴛ ᴄʜᴇᴄᴋ ᴀᴠᴀɪʟᴀʙʟᴇ sᴇʀɪᴀʟs ᴡɪᴛʜ /serials 
• Tʜᴇɴ ᴛʏᴘᴇ ʏᴏᴜʀ sᴇʀɪᴀʟ ɴᴀᴍᴇ 
• ᴡɪᴛʜ sᴇᴀsᴏɴs ᴀɴᴅ ᴇᴘɪsᴏᴅᴇ ɴᴜᴍʙᴇʀ
• ᴀɴᴅ ᴀʟsᴏ ᴀᴅᴅ ǫᴀᴜʟɪᴛʏ ɪɴ ʟᴀsᴛ ʟɪɴᴇ ᴛᴏ sᴇᴀʀᴄʜ ᴏɴʟʏ ᴏɴᴇ ǫᴀᴜʟɪᴛʏ.
• ᴛʜᴇɴ sᴇɴᴅ ᴛᴏ ʙᴏᴛ

<b>Exᴀᴍᴘʟᴇ :</b>
<code>Serial Name S01E01</code>
<b>Aʟsᴏ Sᴇᴀʀᴄʜ ʟɪᴋᴇ ᴛʜɪs 👇👇</b>
<code>Serial Name S01E10 360p</code>

Iғ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴜɴᴅᴇʀsᴛᴀɴᴅ ᴛʜᴇɴ ᴡᴀᴛᴄʜ ᴛʜɪs ʜᴇʟᴘ ᴠɪᴅᴇᴏ 👇"""

    ABOUT_TXT = """<b>Aʙᴏᴜᴛ :</b>

Tʜɪs ɪs ᴏғғɪᴄɪᴀʟ ʙᴏᴛ ᴏғ @Rkrishnaa_rk ᴄʜᴀɴɴᴇʟ. Iᴛs ᴍᴀᴅᴇ ғᴏʀ ᴏᴜʀ ʟᴏᴠᴇʟʏ Sᴜʙsᴄʀɪʙᴇʀs.😘 Tʜɪs ʙᴏᴛ ᴘʀᴏᴠɪᴅᴇ ᴍᴀɴʏ Mᴏᴠɪᴇs, Sᴇʀɪᴇs & Sᴇʀɪᴀʟs. Tᴏ  ᴄʜᴇᴄᴋ ᴀᴠᴀɪʟᴀʙʟᴇ sᴇʀɪᴀʟ ᴜsᴇ ᴛʜɪs /serials 

<b>Fᴇᴀᴛᴜʀᴇs :</b>
• Aʟʟ ᴇᴘɪsᴏᴅᴇs ᴏғ ᴀᴠᴀɪʟᴀʙʟᴇ sᴇʀɪᴀʟs.
• Aʟʟ ǫᴜᴀʟɪᴛʏ ᴏғ ᴛʜᴇsᴇ sʜᴏᴡs ᴀʀᴇ ᴀᴠᴀɪʟᴀʙʟᴇ.
• Wᴏʀᴋ ɪɴ ɢʀᴏᴜᴘ ᴏʀ ᴘᴍ.
• Aʟsᴏ ᴀᴅᴅ ғɪʟᴛᴇʀs ɪɴ ʙᴏᴛ.
• Bᴏᴛ ɪs ғᴀsᴛᴇʀ ᴀɴᴅ sᴍᴏᴏᴛʜ. 😎 

<b>Cᴏᴘʏʀɪɢʜᴛ :</b>
Wᴇ ᴅᴏɴᴛ ᴏᴡɴ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ. Iᴛs ᴛᴀᴋᴇɴ ғʀᴏᴍ ᴀɴᴏᴛʜᴇʀ ᴄʜᴀɴɴᴇʟs ᴏʀ ɪɴᴛᴇʀɴᴇᴛ. Iғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴄᴏɴᴛᴇɴᴛ ɪɴ ʙᴏᴛ ᴛʜᴇɴ ʀᴇᴘᴏʀᴛ ᴜs.

<b>Tʜᴀɴᴋ Yᴏᴜ ❤️</b>"""

    MANUELFILTER_TXT = """<b>Fɪʟᴛᴇʀs:</b>

Fɪʟᴛᴇʀ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜsᴇʀs ᴄᴀɴ sᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇs ғᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ Bᴏᴛ ᴡɪʟʟ ʀᴇsᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪs ғᴏᴜɴᴅ ᴛʜᴇ ᴍᴇssᴀɢᴇ

<b>Nᴏᴛᴇ:</b>
𝟷. Bᴏᴛ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
𝟸. ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴀᴅᴅ ғɪʟᴛᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ.
𝟹. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴs ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏғ 𝟼𝟺 ᴄʜᴀʀᴀᴄᴛᴇʀs.

<b>Cᴏᴍᴍᴀɴᴅs ᴀɴᴅ Usᴀɢᴇ:</b>
• /filter - ᴀᴅᴅ ᴀ ғɪʟᴛᴇʀ ɪɴ ᴄʜᴀᴛ
• /filters - ʟɪsᴛ ᴀʟʟ ᴛʜᴇ ғɪʟᴛᴇʀs ᴏғ ᴀ ᴄʜᴀᴛ
• /del - ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ғɪʟᴛᴇʀ ɪɴ ᴄʜᴀᴛ
• /delall - ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ғɪʟᴛᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ (ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)
"""

    BUTTON_TXT = """<b>Bᴜᴛᴛᴏɴs:</b>

Bᴏᴛ Sᴜᴘᴘᴏʀᴛs ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴs.

<b>Nᴏᴛᴇ:</b>
𝟷. Tᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ sᴇɴᴅ ʙᴜᴛᴛᴏɴs ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, sᴏ ᴄᴏɴᴛᴇɴᴛ ɪs ᴍᴀɴᴅᴀᴛᴏʀʏ.
𝟸. Bᴏᴛ sᴜᴘᴘᴏʀᴛs ʙᴜᴛᴛᴏɴs ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
𝟹. Bᴜᴛᴛᴏɴs sʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀsᴇᴅ ᴀs ᴍᴀʀᴋᴅᴏᴡɴ ғᴏʀᴍᴀᴛ

<b>URL ʙᴜᴛᴛᴏɴs:</b>
<code> [ Button Text ](buttonurl:https://t.me)</code>

<b>Aʟᴇʀᴛ ʙᴜᴛᴛᴏɴs:</b>
<code> [ Button Alert ](buttonalert:This Is Alert message)</code>"""

    AUTOFILTER_TXT = """Aᴜᴛᴏғɪʟᴛᴇʀ ᴍᴏᴅᴜʟᴇ sᴇᴀʀᴄʜᴇs ɪᴍᴅʙ ғᴏʀ ᴍᴏᴠɪᴇ ᴅᴇᴛᴀɪʟs ᴀɴᴅ ᴅʙ ғᴏʀ ғɪʟᴇs ᴀɴᴅ sᴇɴᴅs ʀᴇsᴜʟᴛs ғᴏʀ ᴇᴀᴄʜ ᴍᴇssᴀɢᴇ ɪɴ ᴀ ɢʀᴏᴜᴘ

Eɴᴀʙʟᴇ : /autofilter on
Dɪsᴀʙʟᴇ : /autofilter off

Nᴏᴛᴇ :- Aᴜᴛᴏғɪʟᴛᴇʀ ɪs ᴇɴᴀʙʟᴇᴅ ʙʏ ᴅᴇғᴀᴜʟᴛ"""

    CONNECTION_TXT = """<b>Connections</b>
<b>Cᴏɴɴᴇᴄᴛɪᴏɴs:</b>

- Usᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʙᴏᴛ ᴛᴏ PM ғᴏʀ ᴍᴀɴᴀɢɪɴɢ ғɪʟᴛᴇʀs 
- ɪᴛ ʜᴇʟᴘs ᴛᴏ ᴀᴠᴏɪᴅ sᴘᴀᴍᴍɪɴɢ ɪɴ ɢʀᴏᴜᴘs.

<b>Nᴏᴛᴇ:</b>
𝟷. Oɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴀᴅᴅ ᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ.
𝟸. Sᴇɴᴅ <code>/connect Group Id</code>

<b>Cᴏᴍᴍᴀɴᴅs ᴀɴᴅ Usᴀɢᴇ:</b>
• /connect - ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ PM
• /disconnect - ᴅɪsᴄᴏɴɴᴇᴄᴛ ғʀᴏᴍ ᴀ ᴄʜᴀᴛ
• /connections - ʟɪsᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴs"""

    EXTRAMOD_TXT = """<b>Exᴛʀᴀ Mᴏᴅᴜʟᴇs:</b>

<b>Nᴏᴛᴇ:</b>
ᴛʜᴇsᴇ ᴀʀᴇ ᴛʜᴇ ᴇxᴛʀᴀ ғᴇᴀᴛᴜʀᴇs ᴏғ Bᴏᴛ 

<b>Cᴏᴍᴍᴀɴᴅs ᴀɴᴅ Usᴀɢᴇ:<b>
• /id - ɢᴇᴛ ɪᴅ ᴏғ ᴀ sᴘᴇᴄɪғɪᴇᴅ ᴜsᴇʀ.
• /info - ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜsᴇʀ.
• /imdb  - ɢᴇᴛ ᴛʜᴇ ғɪʟᴍ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғʀᴏᴍ IMDʙ sᴏᴜʀᴄᴇ.
"""

    ADMIN_TXT = """<b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<u><b>Basic Command</b></u>
• /logs • /stats
• /delete • /users
• /chats • /leave
• /disable • /ban
• /unban • /channel
• /broadcast
• /group_broadcast 
• /invite • /restart
• /usend  • /gsend 
"""

    STATUS_TXT = """
<b><u>Database Status:</b></u>
• Total Files: {}
• Total Users: {}
• Total Chats: {}
• Used DB Storage: {} 
• Free DB Storage: {} 

<b><u>Server Status:</b></u>
• CPU: {} %
• RAM: {} %
• Disk: {}
• Used: {}({}%)
• Free: {}

♻️ <b>Bot Restarted On:</b> 6 Aug 2023 at 07:20:33 (Asia/Kolkata)
"""


    LOG_TEXT_G = """#NewGroup
<b> Group = {a}(<code>{b}</code>)</b>
<b> G Id = @{c}
<b> Total Member = {d}</b>
<b> Added By = {e}</b>
By {f}
"""

    LOG_TEXT_P = """#NewUser
**Name:-** {}
**UserName:-** @{}
**User ID:-** {}
**Direct link:-** {}
Else:- tg://openmessage?user_id={} """

    REPORTME = """<b>Rᴇᴘᴏʀᴛ :</b>

Bʏ ᴜsɪɴɢ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ. ʏᴏᴜ ᴄᴀɴ ᴄᴏɴᴛᴀᴄᴛ ᴍʏ ᴏᴡɴᴇʀ. ʀᴇᴘᴏʀᴛ ᴀɴʏᴛʜɪɴɢ ᴏғ ᴀɴʏ ᴛʏᴘᴇ ᴀʙᴏᴜᴛ ᴛʜɪs ʙᴏᴛ ᴏʀ ᴇʟsᴇ.

<b>Hᴏᴡ ɪᴛ Wᴏʀᴋs 🙂?</b>
>> Sᴇɴᴅ ᴍᴇ ᴛʜᴇ ᴍᴇssᴀɢᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ʀᴇᴘᴏʀᴛ.
>> Rᴇᴘʟʏ ᴛʜᴀᴛ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ /report .

<b>Dᴏɴᴇ ✅.. I ᴡɪʟʟ ғᴏʀᴡᴀʀᴅ ᴛʜᴀᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍʏ Oᴡɴᴇʀ.</b>"""

    BATCH_TXT = """<b>Bᴀᴛᴄʜ ᴏʀ FɪʟᴇSʜᴀʀᴇ ᴍᴏᴅᴜʟᴇ ʟᴇᴛs ᴜsᴇʀs ɢᴇɴᴇʀᴀᴛᴇ ᴀ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ ᴛᴏ ᴍᴜʟᴛɪᴘʟᴇ ᴍᴇssᴀɢᴇs ғʀᴏᴍ ᴛʜᴇɪʀ ᴄʜᴀɴɴᴇʟ.

<u>Sᴛᴇᴘs :</u></b>

[1] Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴀs ᴀᴅᴍɪɴ
[2] Sᴇɴᴅ /batch (First Message Link) (Second Message Link)
[3] Wᴇʟʟ ᴅᴏɴᴇ ʏᴏᴜ ʜᴀᴠᴇ ᴀ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ ᴛᴏ ʏᴏᴜʀ ᴍᴇssᴀɢᴇs"""
    SETTINGS_TXT = """<b>ѕeттιngѕ:</b>

sᴇᴛᴛɪɴɢs ɪs ᴍᴏsᴛ ɪᴍᴘᴏʀᴛᴀɴᴛ ғᴇᴀᴛᴜʀᴇs ɪɴ ᴛʜɪs ʙᴏᴛ.
~ ʏᴏᴜ ᴄᴀɴ ᴇᴀsɪʟʏ ᴄᴜsᴛᴏᴍɪᴢᴇ ᴛʜɪs ʙᴏᴛ ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

<b>Nᴏᴛᴇ:</b>
1. ᴏɴʟʏ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴄʜᴀɴɢᴇs sᴇᴛᴛɪɴɢs.
2. ɪᴛ ᴡᴏʀᴋs ᴏɴʟʏ ᴡʜᴇɴ ʏᴏᴜ ᴀʟʀᴇᴀᴅʏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

<b>coммand and υѕeѕ:</b>
• /settings - ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs ᴀs ʏᴏᴜʀ ᴡɪsʜ"""
