class script(object):
    START_TXT = """<b><i>Hello 👋 {},

I Am Not Only <a href=https://t.me/{}>{}</a> To Assist You But Also Employed At <a href='https://t.me/+-IowXvOTa2cyMGQ9'>Film Corner</a> Group By <a href='https://t.me/PR0FESS0R_TG'>PR0FESS0R-TG</a> So You Can't Get My Service By Adding Me To Your Group So Don't Waste Your Time & Data 😉

Better You Click Below & Join <a href='https://t.me/+-IowXvOTa2cyMGQ9'>Film Corner</a> & Feel The Experience Of Downloading Unlimited Movies/Series ✅

For More Information Click ℹ️ Help</b></i>"""

    HELP_TXT = """<b><i>Hello 👋 {},

I Can Guide You Through All Of <a href=https://t.me/{}>{}</a>'s Cool Features & How To Properly Use Them. Use The Buttons Below To Navigate Through All Of The Modules</b></i>"""

    ABOUT_TXT = """꧁֍FILM CORNER BOT֍꧂

ツ Creator : PR0FESS0R-TG 
❖ Language : Python3
❖ Hosted : Heroku
❖ Version : 10.0
❖ Farmework : Pyrogram
❖ Database : MongoDB
֎ Bot : Indian 🇮🇳"""

    FILMCORNER_TXT = """ミ★ FILM CORNER ★彡

☞ Sᴛᴏʀᴀɢᴇ Oғ Nᴇᴡ & Oʟᴅ Mᴏᴠɪᴇs/Sᴇʀɪᴇs
☞ Aᴠᴀɪʟᴀʙʟᴇ Iɴ Mᴀɴʏ Sɪᴢᴇs & Lᴀɴɢᴜᴀɢᴇs
☞ Rᴇᴄᴇɪᴠᴀʙʟᴇ Iɴ Vᴀʀɪᴏᴜs Qᴜᴀʟɪᴛʏ

👑
PR0FESS0R-TG"""

    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter Is The Feature Were Users Can Set Automated Replies For a Particular keyword And Dingdi Will Respond Whenever a Keyword isy Found The Message 

<b>NOTE:</b>
1. Film Corner Bot Should Have Admin Privillage.
2. Only Admins Can Add Filters In a Chat.
3. Alert Buttons Have a Limit Of 64 Characters.

<b>Commands and Usage:</b>
• /filter - Add a Filter In Chat.
• /filters - List All The Filters Of a Chat.
• /del - Delete a Specific Filter In Chat.
• /delall - Delete The Whole Filters In a Chat (Chat Owner Only)."""

    BUTTON_TXT = """Help: <b>Buttons</b>

- Film Corner Bot Support Both URL And Alert Inline Buttons.

<b>NOTE:</b>
1. Telegram Will Not Allows You To Send Buttons Without Any Content, So Content Is Mandatory.
2. Film Corner Bot Supports Buttons With Any Telegram Media Type.
3. Buttons Should Be Properly Parsed As Markdown Format.

<b>URL Buttons:</b>
<code>[Button Text](buttonurl:https://t.me/xxxxxxxxxxxxx)</code>

<b>Alert Buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    FILLINGS_TXT = """Help: <b>Fillings</b>

- You Can Also Customize The Contents Of Your Message With Contextual Data. For Example, You Could Mention a User By Name In The Filter Message, Or Mention Then In a Filter..!

<b>Supported fillings:</b>
- <code>{first}</code>: The User's First Name.
- <code>{last}</code>: The User's Last Name.
- <code{username}</code>: The User's Username.
- <code>{mention}</code>: Mentions The User With Their Firstname.
- <code>{id}</code>: The User's ID.
- <code>{dcid}</code>: The User's DC ID.
- <code>{chatname}</code>: The Chat's Name.
- <code>{query}</code>: Any Replied Message.

<b>Example:</b>
<b>- Save a Filter Using The Mention.</b>
-> <code>/filter Test Hello {mention} This Is your Username : {username} And This Is your ID : {id}.</code>
"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make Me The Admin Of Your Channel If It's Private.
2. Make Sure That Your Channel Does Not Contains Camrips, Porn And Fake Files.
3. Forward The Last Message To Me With Quotes. I'll Add All The Files In That Channel To My DataBase."""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used To Connect Bot To PM For Managing Filters 
- It Helps To Avoid Spamming In Groups.

<b>NOTE:</b>
1. Only Admins Can Add a Connection.
2. Send <code>/connect</code> For Connecting Me To Your PM.

<b>Commands and Usage:</b>
• /connect  - Connect a Particular Chat To Your PM.
• /disconnect  - Disconnect From a Chat.
• /connections - List All Your Connections."""

    AUTO_MANUEL_TXT = """Help: <b>Filters</b>

<b>Select a Filters Type Bellow</b>"""
    
    TGRAPH_TXT = """Help: <b>T-Graph</b>

- Do As You Wish With Telegraph Module..!

<b>Commands and Usage:</b>
• /tgmedia Or /tgraph - Upload Supported Media (Within 5MB) To Telegraph.

<b>NOTE:</b>
• Film Corner Bot Should Have Admin Privillage.
• These Commands Works On Both PM And Group.
• These Commands Can Be Used By Any Group Member."""

    INFO_TXT = """Help: <b>Information</b>

- Get Information About Something..!

<b>Commands and Usage:</b>
• /id - Get ID Of a Specified User.
• /info  - Get Information About a User.
• /json - Get The JSON Details Of a Message.

<b>NOTE:</b>
• Film Corner Bot Should Have Admin Privillage.
• These Commands Works On Both PM And Group.
• These Commands Can Be Used By Any Group Member."""
   
    GTRANS_TXT = """Help: <b>Google Translator</b>

- Translate Texts To a Specific Language..!

<b>Commands and Usage:</b>
• /tr [language code][reply] - Translate Replied Message To Specific Language.

<b>NOTE:</b>
• Film Corner Bot Should Have Admin Privillage.
• These Commands Works On Both PM And Group.
• Film Corner Bot Can Translate Texts To 200+ Languages."""

    SEARCH_TXT = """Help: <b>IMDB</b>

- Search Many Things Without Leaving Telegram..!

<b>Commands and Usage:</b>
• /imdb  - Get The Film Information From IMDB Source.
• /search  - Get The Film Information From Various Sources.

<b>NOTE:</b>
• Film Corner Bot Should Have Admin Privillage.
• More Search Tools Can Be Found On Inline.
• Those Commands Works On Both PM And Group."""

    PURGE_TXT = """Help: <b>Purge</b>

- Need To Delete Lots Of Messages..? That's What Purges Are For..!

<b>Commands and Usage:</b>
• /purge - Delete All Messages From The Replied To Message, To The Current Message.

<b>NOTE:</b>
• Film Corner Bot Should Have Admin Privillage.
• These Commands Works On Group.
• These Commands Can Be Used By Only Admin."""
    
    ADMIN_TXT = """Help: <b>Admin Mods</b>

<b>NOTE:</b>
This Module Only Works For My Admins 

<b>Commands and Usage:</b>
• /logs - to get the rescent errors.
• /stats - to get status of files in db.
• /delete - to delete a specific file from db.
• /users - to get list of my users and ids.
• /chats - to get list of the my chats and ids.
• /leave - to leave from a chat.
• /disable - do disable a chat.
• /ban_users - to ban a user.
• /unban_users - to unban a user.
• /channel - to get list of total connected channels.
• /broadcast - to broadcast a message to all users."""

    SHARE_TXT = """Help: <b>Sharing Text Maker</b>

- This Bot Create a Link To Share Text In The Telegram.

<b>Commands and Usage:</b>
• /share (Text Or Reply To Message)

<b>NOTE:</b>
• Film Corner Bot Should Have Admin Privillage.
• These Commands Works On Both PM And Group.
• These Commands Can Be Used By Any Group Member."""

    STATUS_TXT = """<b>Total Files:</b> <code>{}</code>
<b>Total Users:</b> <code>{}</code>
<b>Total Chats:</b> <code>{}</code>
<b>Used Storage:</b> <code>{}</code> MiB
<b>Free Storage:</b> <code>{}</code> MiB"""
    
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}"""  
