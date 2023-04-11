class script(object):
    START_TXT = """<b><i>Hello 👋 {},

My Name Is <a href=https://t.me/{}>{}</a>...!!

I Can Provide Movies. A Telegram Auto Filter Bot. Its Easy To Use Me.

Just Add Me To Your Group As Admin, Hit The ℹ️ Help Button For More Info...!!</b></i>"""

    HELP_TXT = """<b><i>Hello 👋 {},

<b>Here Is The Help For My Commands.</b></i>"""

    ABOUT_TXT = """<b>➥ My name: {}
➥ Creator: <a href='https://t.me/zautekm'>Zaute Km</a>
➥ Library: <a href='https://docs.pyrogram.org/'>Pyrogram</a>
➥ Language: Python 𝟹
➥ Data Base: <a href='https://www.mongodb.com/'>MongoDB</a>
➥ Bot Server: <a href='https://heroku.com'>Heroku</a>
➥ Build Status: v2.0.1 [ Beta ]"""
    
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Dingdi will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Film Corner Bot should have admin privillage.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - add a filter in chat.
• /filters - list all the filters of a chat.
• /del - delete a specific filter in chat.
• /delall - delete the whole filters in a chat (chat owner only)."""

    BUTTON_TXT = """Help: <b>Buttons</b>

- tgmoviebot support both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Film Corner Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format.

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/josprojects)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    FILLINGS_TXT = """Help: <b>Fillings</b>

You can also customise the contents of your message with contextual data. For example, you could mention a user by name in the filter message, or mention them in a filter!

<b>Supported fillings:</b>
- <code>{first}</code>: The user's first name.
- <code>{last}</code>: The user's last name.
- <code{username}</code>: The user's username.
- <code>{mention}</code>: Mentions the user with their firstname.
- <code>{id}</code>: The user's ID.
- <code>{dcid}</code>: The user's DC ID.
- <code>{chatname}</code>: The chat's name.
- <code>{query}</code>: Any Replied Message.

<b>Example:</b>
<b>- Save a filter using the mention.</b>
-> <code>/filter test Hello {mention} This Is your Username : {username} And This Is your ID : {id}.</code>
"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- It helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - connect a particular chat to your PM.
• /disconnect  - disconnect from a chat.
• /connections - list all your connections."""

    AUTO_MANUEL_TXT = """Help: <b>Filters</b>

<b>Select a filters type Below:</b>"""

    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>
• /paste [text] - paste the given text on Pasty
• /paste [reply] - paste the replied text on Pasty

<b>NOTE:</b>
• Film Corner Bot should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    TGRAPH_TXT = """Help: <b>TGraph & Paste</b>

Do as you wish with telegra.ph module!

<b>Commands and Usage:</b>
• /tgmedia or /tgraph - upload supported media (within 5MB) to telegraph.

<b>NOTE:</b>
• Film Corner Bot should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    INFO_TXT = """Help: <b>Information</b>

Get information about something!

<b>Commands and Usage:</b>
• /id - get id of a specified user.
• /info  - get information about a user.
• /json - get the json details of a message.

<b>NOTE:</b>
• Film Corner Bot should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""
   
    GTRANS_TXT = """Help: <b>Google Translator</b>

Translate texts to a specific language!

<b>Commands and Usage:</b>
• /tr [language code][reply] - translate replied message to specific language.

<b>NOTE:</b>
• Film Corner Bot should have admin privillage.
• These commands works on both pm and group.
• Film Corner Bot can translate texts to 200+ languages."""

    SEARCH_TXT = """Help: <b>IMDb</b>

Search many things without leaving telegram!

<b>Commands and Usage:</b>
• /imdb  - get the film information from IMDb source.
• /search  - get the film information from various sources.

<b>NOTE:</b>
• Film Corner Bot should have admin privillage.
• More search tools can be found on inline.
• Those commands works on both pm and group."""

    PURGE_TXT = """Help: <b>Purge</b>

Need to delete lots of messages? That's what purges are for!

<b>Commands and Usage:</b>
• /purge - delete all messages from the replied to message, to the current message.

<b>NOTE:</b>
• Film Corner Bot should have admin privillage.
• These commands works on group.
• These commands can be used by Only admin."""
    
    ADMIN_TXT = """Help: <b>Admin Mods</b>

<b>NOTE:</b>
This module only works for my admins

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

    STATUS_TXT = """<b>Total Files:</b> <code>{}</code>
<b>Total Users:</b> <code>{}</code>
<b>Total Chats:</b> <code>{}</code>
<b>Used Storage:</b> <code>{}</code> MiB
<b>Free Storage:</b> <code>{}</code> MiB"""
    
    SHARE_TXT = """Help: <b>Sharing Text Maker</b>

a bot to create a link to share text in the telegram.

<b>Commands and Usage:</b>
• /share (text or reply to message)

<b>NOTE:</b>
• Film Corner Bot should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}"""  
