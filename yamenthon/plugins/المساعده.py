import re

from telethon import Button, events
from telethon.events import CallbackQuery
from ..core import check_owner, pool

from . import zedub

from ..Config import Config
from . import mention

HELP = f"✨ **�┊مـࢪحبـاً عـزيـزي** {mention} **𖤦**\n**🎉┊أهلاً وسهلاً بك في قائمة المساعدة والدعم الفني!**\n**📚┊هنا ستجد كل ما تحتاجه لاستخدام السورس بكل سهولة ويسر.**\n\n🔹 **🧧┊قائمة المساعدة:**\n  ✔️ **🛃┊شروحات مفصلة لكل الأوامر**\n ✔️ **⚙️┊إعدادات متنوعة لتخصيص تجربتك**\n  ✔️ **📜┊أقسام منظمة للوصول السريع**\n\n**📌┊لا تتردد في استكشاف الأقسام المختلفة للعثور على ما تحتاجه!**\n**🎀┊تابعنا للحصول على آخر التحديثات والميزات الجديدة:**\n [ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 ♥️](t.me/YamenThon)\n  **💫┊نتمنى لك تجربة ممتعة وسهلة مع سورسنا!**"  
rep_temp = """
┏───────────────┓
│ ◉ ʙᴏᴛ ʏᴀᴍᴇɴᴛʜᴏɴ ɪs ʀᴜɴɴɪɴɢ ɴᴏᴡ
┣───────────────┫
│ ● ɴᴀᴍᴇ ➪  {mention}
│ ● ʏᴀᴍᴇɴᴛʜᴏɴ ➪ {repver}
│ ● ᴘʏᴛʜᴏɴ ➪ {pyver}
│ ● ᴘʟᴀᴛғᴏʀᴍ ➪ 𐌺᧐yᥱδ
│ ● ᴘɪɴɢ ➪ {ping}
│ ● ᴜᴘ ᴛɪᴍᴇ ➪ {uptime}
│ ● ᴀʟɪᴠᴇ sɪɴᴇᴄ ➪ {reppa}
│ ● ᴍʏ ᴄʜᴀɴɴᴇʟ ➪ [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/YamenThon)
┗───────────────┛"""


if Config.TG_BOT_USERNAME is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)
    @check_owner
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        await zedub.get_me()
        if query.startswith("مساعده") and event.query.user_id == zedub.uid:
            buttons = [
                [Button.inline("𝗦𝗼𝘂𝗿𝗰𝗲 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉𓅛✓", data="BAQIR")],
                [Button.inline("البـحـث والتحميـل ✨️", data="zdownload")],
                [
                    Button.inline("البـوت 🤖", data="botvr"),
                    Button.inline("الحساب 👤", data="acccount"),
                ],
                [
                    Button.inline("المكالمات & الميـوزك 🎶", data="zmusic"),
                ],
                [
                    Button.inline("المجمـوعـة 🛗", data="groupvr"),
                    Button.inline("الفـارات 🎛", data="varszed"),
                ],
                [
                    Button.inline("التسليـه والتحشيش 🎭", data="funzed"),
                ],
                [
                    Button.inline("المرفقـات 🗃", data="extras"),
                    Button.inline("الادوات 🧰", data="toolzed"),
                ],
                [
                    Button.inline("الذكـاء الاصطنـاعـي 🔮", data="zchatgpt"),
                ],
                [
                    Button.inline("اوامــر منوعــه جديـدة 🥏", data="zchatgpt1"),
                ],
                [
                    Button.inline("السوبـرات 🧿", data="superrrr"),
                    Button.inline("التجميـع 🎰", data="pointrrr"),
                ],
                [
                    Button.inline("🌟 اوامــر 𝐕𝐈𝐏 🌟", data="asheqalsamt"),
                ],
            ]
            result = builder.article(
                title="zedub",
                text=HELP,
                buttons=buttons,
                link_preview=False,
            )
        if query.startswith("الفحص") and event.query.user_id == zedub.uid:
            uptime = await get_readable_time((time.time() - StartTime))
            boot_time_timestamp = psutil.boot_time()
            bt = datetime.fromtimestamp(boot_time_timestamp)
            start = datetime.now()
            end = datetime.now()
            ms = (end - start).microseconds / 1000
            _, check_sgnirts = check_data_base_heal_th()
            if gvarstatus("r_date") is not None:
                rrd = gvarstatus("r_date")
                rrt = gvarstatus("r_time")
                reppa = f"{rrd}┊{rrt}"
            else:
                reppa = f"{bt.year}/{bt.month}/{bt.day}"
            rme = await zedub.get_me()
            r_name = f"{rme.first_name}{rme.last_name}" if rme.last_name else rme.first_name
            r_username = rme.username if rme.username else "Repthon"
            USERID = zedub.uid if Config.OWNER_ID == 0 else Config.OWNER_ID
            ALIVE_NAME = gvarstatus("ALIVE_NAME") if gvarstatus("ALIVE_NAME") else "-"
            mention = f"[{ALIVE_NAME}](tg://user?id={USERID})"
            rep_caption = gvarstatus("ALIVE_TEMPLATE") or rep_temp
            caption = rep_caption.format(
                mention=mention,
                uptime=uptime,
                reppa=rrd,
                rrd=rrd,
                rrt=rrt,
                telever=version.__version__,
                repver=repversion,
                pyver=python_version(),
                dbhealth=check_sgnirts,
                ping=ms,
            )
            buttons = [[Button.inline(r_name, f"https://t.me/{r_username}")]]
            result = builder.article(
                title="zedub",
                text=caption,
                buttons=buttons,
                link_preview=False,
            )
        await event.answer([result] if result else None)


@zedub.zed_cmd(pattern="مساعده")
async def help(event):
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await zedub.inline_query(Config.TG_BOT_USERNAME, "مساعده")
    await response[0].click(event.chat_id)
    await event.delete()


@zedub.zed_cmd(pattern="الفحص")
async def help(event):
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await zedub.inline_query(Config.TG_BOT_USERNAME, "الفحص")
    await response[0].click(event.chat_id)
    await event.delete()


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ZEDHELP")))
@check_owner
async def _(event):
    butze = [
                [Button.inline("𝗦𝗼𝘂𝗿𝗰𝗲 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉𓅛✓", data="BAQIR")],
        [
            Button.inline("البـحـث والتحميـل ✨️", data="zdownload")
        ],
        [
            Button.inline("البـوت 🤖", data="botvr"),
            Button.inline("الحساب👤", data="acccount")
        ],
        [
            Button.inline("المكالمات & الميـوزك 🎶", data="rmusic")
        ],
        [
            Button.inline("المجمـوعـة 🛗", data="groupvr"),
            Button.inline(" الفـارات 🎛", data="varszed")
        ],
        [
            Button.inline("التسليـه والتحشيش 🎭", data="funzed")
        ],
        [
            Button.inline("المرفقـات 🗃", data="extras"),
            Button.inline("الادوات 🧰", data="toolzed")
        ],
        [
            Button.inline("الذكـاء الاصطنـاعـي 🔮", data="zchatgpt")
        ],
        [
            Button.inline("اوامــر منوعــه جديـدة 🥏", data="yamen")
        ],
        [
            Button.inline("السوبـرات 🧿", data="superrrr"),
            Button.inline("التجميـع 🎰", data="pointrrr"),
        ],
        [
                    Button.inline("🌟 اوامــر 𝐕𝐈𝐏 🌟", data="asheqalsamt"),
                ],
    ]
    await event.edit(HELP, buttons=butze, link_preview=False)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"rmusic")))
@check_owner
async def zed_help(event):
    zelzal = "⤶ عـذراً عـزيـزي 🤷🏻‍♀\n⤶ هـذه اللوحه لا تشتغل في الخاص\n⤶ لـ إظهـار لوحـة المسـاعـدة 👇\n\n⤶ ارســل (.مساعده) في اي مجمـوعـه"
    try:
        await event.edit(
            "[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المكالمـات والميـوزك 🎸](t.me/YamenThon) .\n\n**「❖╎اليك عـزيـزي شـࢪوحـات اوامـر المكالمـات وتشغيـل الاغـاني في المكالمـات (الميوزك) :**\n\n",
            buttons=[
                [
                    Button.inline("المكالمـات", data="rrcall"),
                ],
                [
                    Button.inline("الميـوزك", data="rrmusic"),
                ],
                [Button.inline("رجوع", data="ZEDHELP")],
            ],
        link_preview=False)
    except Exception:
        await event.answer(zelzal, cache_time=0, alert=True)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"BAQIR")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - قنـوات السـورس](t.me/YamenThon) .
**- القنـاة الرسمية:**
**⪼** @YamenThon

**- قنـاة التحديثات:**
**⪼** @YamenThon1

**- قنـاة الفـارات:**
**⪼** @YamenThon_vars

**- قنـاة الكلايـش**
**⪼** @YamenThon_cklaish

**- قنـاة تداولات المطور**
**⪼** @Q_A_VI

**- مطور السورس**
**⪼** @T_A_Tl
☆☆☆☆☆☆☆☆☆☆☆☆☆☆""",
        buttons=[
            [Button.inline("رجوع", data="ZEDHELP")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"yamen")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - قـائمــة الاوامــر المنوعه 🎉](https://t.me/YamenThon)
⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆
**⚡ قـائـمـة أوامـر الـبـوت الـمـنـوعـة ⚡️**

**🔹 الـتـثـبـيـت والـحـسـاب 🔹**
`.مسح` - **برد على الرسالة لمسحها يعمل في الخاص و الجروبات** 
`.تثبيت` - **لـتـثـبـيـت الـرسـالـة (يـعـمـل فـي الـجـروبـات والـخـاص بـشـرط أن تـكـون مـشـرف)**
`.حالتي` - **لـمـعـرفـة حـالـة حـسـابـك (مـقـيـد أم لا) 🔍**
`.بوتي` - **لـمـعـرفـة يـوزر بـوتـك الـمـسـاعـد 🤖**

**🌙 الـحـالـة والـتـواجـد 🌞**
`.نائم` - **وضع تـوقـيـع نـائـم بـجـانـب اسـمـك 😴**
`.مستيقظ` - **وضـع تـوقـيـع مـسـتـيـقـظ بـجـانـب اسـمـك ☀️**

**👥 الـتـاك والـمـنـشـن 📢**
`.غادر` **لمغادرة الجروب استخدم هاذا الامر داخل المجموعة **
`.تاك` + نـص -** لـعـمـل تـاك لـجـمـيـع أعـضـاء الـجـروب 📣**
`.ايقاف` التاك - **لـإيـقـاف الـتـاك الـجـاري 🛑**
`.منشن` + نـص -** لـعـمـل مـنـشـن لـلـشـخـص (يـجـب الـرد عـلـيـه) 💬**

**💻 الـبـرمـجـة والـتـجـارب 🔧**
`.تجربه `+ كـود - **لـتـجـربـة أي كـود بـرمـجـي 🖥️**
.حساب العمر + سـنـة - **لـحـسـاب عـمـرك مـن سـنـة الـمـيـلـاد 🎂**
`.احسب` يقوم بحل المسائل الرياضيه  مثال 5 + 8💌
`.بريد` يقوم بإنشاء بريد إفتراضي تستطيع السجيل في المواقع

**🌐 الـإنـتـرنـت والـسـرعـة ⚡**
`.بنك` - **لـقـيـاس سـرعـة اسـتـجـابـة الـسـورس ⏱️**
`.الانترنت` - **لـقـيـاس سـرعـة الـرفـع والـتـحـمـيـل 📊**

**🗣️ أمـر الـنـطـق 🔉**
`.انطق` + نـص - **لـتـحـويـل الـنـص إلـى صـوت (يـدعـم عـدة لـغـات) 🌍**

**🤖 أمـر صـنـع وإدارة الـبـوتـات 🛠️**
`.صنع بوت` + اسـم + يـوزر - **لـإنـشـاء بـوت جـديـد عـبـر بـوت فـاذر 🤖✨**
`.تعديل` + **يـوزر الـبـوت - لـلـتـحـكـم فـي الـبـوت (تـغـيـير اسـم، وصـف، صـورة، إلـخ) 🎛️**

**📌 مـلاحـظـات هـامـة:**
**✔ تأكد من كتابة اليوزر بدون @ عند استخدام .صنع بوت**
**✔ احفظ التوكن في مكان آمن لأنه مفتاح التحكم بالبوت 🔑**
**❌ عند حذف البوت، لا يمكن استعادته مرة أخرى ⚠️**
**🎉 استمتع بتجربة فريدة مع بوت يمثون! 🚀**

[𓆩 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𓆪](https://t.me/YamenThon)""",
        buttons=[
            [Button.inline("رجوع", data="ZEDHELP")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"rrcall")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المكالمـات والميـوزك 🎸](t.me/YamenThon) .
**- الامـر :**
**⪼** `.بدء مكالمه`
**⪼** `.انهاء مكالمه`
**⪼** `.انضم`
**⪼** `.خروج`
**⪼** `.دعوه` + معرف/ايدي/بالـرد
**⪼** `.عنوان` + نص
**⪼** `.معلومات المكالمه`

**- اوامـر الكتـم في المكالمات :**
**⪼** `.اسكت`  + معرف/ايدي/بالـرد
**⪼** `.الغاء اسكت`  + معرف/ايدي/بالـرد


**- الوصـف :**
اوامـر واعدادات المكالمـات والمحادثات الصوتيـة والمرئيـة في المجموعـات والقنـوات 

ج**- ملاحظـه :**
هناك بعض الدول تعاني من حظر الانضمام الى المكالمات على تطبيق تيليجرام لسبب مجهول مثل دولة اليمن ودول اخرى
الحل هو استخدام vpn لتخطي الحظر اثناء الانضمام الى المكالمات

**- الاستخـدام :**
ارسـل احـد الاوامر بالاعلـى""",
        buttons=[
            [Button.inline("رجوع", data="rmusic")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"rrmusic")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المكالمـات والميـوزك 🎸](t.me/YamenThon) .
**- الامـر :**
**⪼** `.شغل` + رابـط او بالـرد ع مقطـع صوتـي
**⪼** `.فيد` + رابـط او بالـرد ع مقطـع فيديـو

**- اوامـر تشغيـل اجباريـه مـع تخطـي قائمـة التشغيـل :**
**⪼** `.شغل 1` + رابـط او بالـرد ع مقطـع صوتـي
**⪼** `.فيد 1` + رابـط او بالـرد ع مقطـع فيديـو

**⪼** `.قائمة التشغيل`
**⪼** `.توقف`
**⪼** `.كمل`
**⪼** `.تخطي`


**- الوصـف :**
اوامـر تشغيـل المقاطـع الصوتيـه والفيديـو في المكالمـات والمحادثات الصوتيـة والمرئيـة في المجموعـات والقنـوات 🎧🎸

**- الاستخـدام :**
ارسـل احـد الاوامر بالاعلـى""",
        buttons=[
            [Button.inline("رجوع", data="rmusic")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"superrrr")))
@check_owner
async def _(event):
    await event.edit(
        "[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - النشـر التڪـراري العـام (الـسوبـرات) 🎡](t.me/YamenThon) .\n\n**「❖╎اليك عـزيـزي شـࢪوحـات اوامـر النشـر والسوبـرات :**\n\n",
        buttons=[
            [
                Button.inline("النشـر التكـراري 🏟", data="spamrrr"),
            ],
            [
                Button.inline("السـوبـرات عــام 🧿", data="superrrrr"),
            ],
            [Button.inline("رجوع", data="ZEDHELP")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"spamrrr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر النشــر التلقــائي 🌐](t.me/YamenThon) .
**- اوامـر النشـر الخاصه بالقنـوات :**
**⪼** `.تلقائي`
**الامـر + (معـرف/ايـدي/رابـط) القنـاة المـراد النشـر التلقـائي منهـا .. استخـدم الامـر داخـل قناتك✓**

**⪼** `.ستوب`
**الامـر + (معـرف/ايـدي/رابـط) القنـاة المـراد ايقـاف النشـر التلقـائي منهـا .. استخـدم الامـر داخـل قناتك ✓**

**- اوامـر نشـر السوبـرات :**
**⪼** `.مكرر` + الوقت بالثواني + العدد + النص
**الامـر بـدون علامـة + .. استخـدم الامـر داخـل مجموعـة السوبـر ✓**

**⪼** `.ايقاف التكرار`
**لـ ايقـاف النشـر التلقـائي في السوبـر ✓**


**- الوصـف :**
**النشـر التلقائـي** هي عبارة عن خاصيه تسمح لـ البوت الموجود بحسابك بنشـر منشورات تلقائيـه بقناتك من قنـاة انت تحددهـا
**امـر مكـرر** هي عبارة عن امر تكرار تسمح لـ البوت الموجود بحسابك بنشـر منشورات بتكرار معين في مجموعات السوبر والبيع والشراء

**- ملاحظـه 🧧:**
- اوامـر النشـر الخـاصه بالقنـوات صـارت تدعـم القنـوات الخاصه ايضـاً والمعـرفات والروابـط ايضاً الى جـانب الايـدي .. ع عكس بقية السورسات 🏂🎗
🛃 سيتـم اضـافة المزيـد من اوامــر النشـر التلقـائي بالتحديثـات الجـايه

**- الاستخـدام :**
ارسـل احـد الاوامـر اعـلاه""",
        buttons=[
            [Button.inline("رجوع", data="superrrr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"superrrrr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 - النشـر التڪـراري العـام (الـسوبـرات) 🎡](t.me/YamenThon) .
**⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆**
**「❖╎قـائمـة اوامـر السـوبـر (النشـر العـام) الخاصـه بـ سـورس يـــمنثون ♾ :**

`.سوبر`
**⪼ الامـر + عـدد الثـوانـي + عـدد مـرات التكـرار (بالـرد ع رسـالة او ميديـا)**
**⪼ لـ النشـر التكـراري العـام بكـل مجموعـات قائمـة السـوبـر ( خـاص بجماعـة بالسـوبـرات ) ...✓**
ٴ┄─┄─┄─┄┄─┄─┄─┄─┄┄
`.ايقاف سوبر`
**⪼ استخـدم الامـر داخـل المجموعـة المحـدده ...**
**⪼ لـ إيقـاف النشـر العـام عـن مجموعـة معينـه ...✓**
ٴ┄─┄─┄─┄┄─┄─┄─┄─┄┄
`.ايقاف السوبرات`
**⪼ لـ إيقـاف النشـر التكـراري العـام عـن جميـع المجموعـات ...✓**
ٴ┄─┄─┄─┄┄─┄─┄─┄─┄┄
`.اضف سوبر`
**⪼ استخـدم الامـر داخـل المجموعـة المحـدده ...**
**⪼ لـ اضافة مجموعـة محـددة لـ قائمـة مجموعـات السوبـر ...✓**
ٴ┄─┄─┄─┄┄─┄─┄─┄─┄┄
`.حذف سوبر`
**⪼ استخـدم الامـر داخـل المجموعـة المحـدده ...**
**⪼ لـ حـذف مجموعـة محـددة مـن قائمـة مجموعـات السوبـر ...✓**
ٴ┄─┄─┄─┄┄─┄─┄─┄─┄┄
`.السوبرات`
**⪼ لـ جلب قائمـة مجموعـات السوبـر الخاصـه بك ...✓**
ٴ┄─┄─┄─┄┄─┄─┄─┄─┄┄
`.حذف السوبرات`
**⪼ لـ حـذف وتصفيـر قائمـة مجموعـات السوبـر الخاصـه بك ...✓**
ٴ┄─┄─┄─┄┄─┄─┄─┄─┄┄
**⪼ مـلاحظــات هـامــه :**
- اوامـر السوبـرات إضـافة جديـدة خاصـه وحصريـه بسـورس يـــمنثون¹ فقـط ...
- تحديثات السوبـر متواصـلة لـ إضـافة كـل ماهـو جديـد بالتحديثـات الجايـه ...
- نسعـى جاهـدين لـ جعـل اوامـر السوبـر سهـله وسلسـه لـكي توفـر لكـم الجهـد والتعب ...
- شكـر خـاص لـ منصبيـن السـورس علـى افكـارهم الرائعـه والمفيـده ...""",
        buttons=[
            [Button.inline("رجوع", data="superrrr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"pointrrr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر تجميــع النقــاط 🛂](t.me/YamenThon) .

`.المليار`  /  `.ايقاف المليار`

`.العرب`  /  `.ايقاف العرب`

`.الجوكر`  /  `.ايقاف الجوكر`

`.العقاب`  /  `.ايقاف العقاب`

`.المليون`  /  `.ايقاف المليون`

`.برليون`  /  `.ايقاف برليون`

`.تناهيد`  /  `.ايقاف تناهيد`

`.اليمن`  /  `.ايقاف اليمن`

`.مهدويون`  /  `.ايقاف مهدويون`

`.دعمكم`  /  `.ايقاف دعمكم`

`.هايبر`  /  `.ايقاف هايبر`

**⪼ لـ تجميـع النقـاط مـن البـوت المطلـوب .. تلقـائيـاً ✓**

**⪼** `.اضف فار بوت التجميع`
**بالـرد ع معـرف البـوت الجديـد لـ اضافته لـ السـورس ..**

`.تجميع`  /  `.ايقاف تجميع`
**⪼ لـ تجميـع النقـاط مـن البـوت المضاف لـ الفـارات .. تلقـائيـاً ✓**

`.بوت التجميع`
**⪼ لـ عـرض بوت التجميـع المضـاف لـ الفـارات ..**

**「❖╎قـائمـة اوامــر اضافـات التجميـع الجديـدة حصريـاً ♾ :**

`.لانهائي المليار` / `.لانهائي الجوكر` / `.لانهائي العقاب` / `.لانهائي العرب` / `.لانهائي المليون` / `.لانهائي برليون` / `.لانهائي تناهيد` / `.لانهائي اليمن`
**⪼ لـ تجميـع النقـاط مـن البـوت بـدون تـوقـف (لانهـائـي ♾) .. تلقـائيـاً ✓**

`.هدية المليار` / `.هدية الجوكر` / `.هدية العقاب` / `.هدية دعمكم` / `.هدية العرب` / `.هدية المليون` / `.هدية هايبر` / `.هدية برليون` / `.هدية تناهيد` / `.هدية اليمن` / `.هدية مهدويون`
**⪼ لـ تجميـع نقـاط الهديـة اليوميـة مـن البـوتات ..**

`.نقاط المليار` / `.نقاط الجوكر` / `.نقاط العقاب` / `.نقاط دعمكم` / `.نقاط العرب` / `.نقاط المليون` / `.نقاط هايبر` / `.نقاط برليون` / `.نقاط تناهيد` / `.نقاط اليمن` / `.نقاط مهدويون`
**⪼ لـ عـرض ومعرفـة عـدد النقـاط فـي البـوت ..**

`.تحويل المليار` / `.تحويل الجوكر` / `.تحويل العقاب` / `.تحويل العرب` / `.تحويل المليون` / `.تحويل هايبر` / `.تحويل برليون` / `.تحويل تناهيد` / `.تحويل اليمن` / `.تحويل مهدويون`
**⪼ الامـر + عـدد النقـاط لـ الشخـص المـراد تحويـل النقـاط اليـه**
**⪼ لـ تحويـل النقـاط مـن حسابـك في البـوت الى شخـص عبـر عـدد النقـاط ..**

`.تحويل دعمكم`
**⪼ الامـر + ايـدي الشخـص + عـدد النقـاط لـ الشخـص المـراد تحويـل النقـاط اليـه**

`.كود دعمكم` / `.كود هايبر`
**⪼ الامـر + الكـود المـراد فحصـه**
**⪼ لـ كشـط الكـود والحصـول علـى نقـاط الكـود .. تلقـائيـاً ✓**""",
        buttons=[
            [Button.inline("رجوع", data="ZEDHELP")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"zchatgpt")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الذكـاء الاصطنـاعـي 🛸](t.me/YamenThon) .
**- الامـر :**
**⪼** `.س` + سـؤالك او بالـرد ع رسالـة

**- الوصـف :**
اوامـر الذكاء الاصطناعي ChatGpt لـ الـرد عن جميـع تساؤلاتك مهمـا كان نوعهـا
تستطيع ان تقوم بحلول المسائل الرياضيه والالغاز وايجاد حلول واجابات منطقيه عن كل تساؤلاتك بواسطة تقنية الذكاء الاصطناعي المتطورة

**- ملاحظـه :**
سوف يتم اضافة المزيـد من اوامـر الذكـاء الاصطناعـي في التحديثـات القادمـه لمواكبـة كل ماهـو جديـد

**- الاستخـدام :**
ارسـل .س ثم سؤلك او بالـرد ع رسالة

**- مثـال :**
.س من هو مكتشف الجاذبية الارضية""",
        buttons=[
            [Button.inline("رجوع", data="ZEDHELP")],
        ],
    link_preview=False)

############ البوت ############
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"botvr")))
@check_owner
async def _(event):
    zelzal = "⤶ عـذراً عـزيـزي 🤷🏻‍♀\n⤶ هـذه اللوحه لا تشتغل في الخاص\n⤶ لـ إظهـار لوحـة المسـاعـدة 👇\n\n⤶ ارســل (.مساعده) في اي مجمـوعـه"
    try:
        await event.edit(
            "[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البـــوت 🦾🤖](t.me/YamenThon) .\n\n**「❖╎اليك عـزيـزي شـࢪوحـات اوامـر البـوت المسـاعد :**\n\n",
            buttons=[
                [
                    Button.inline("تحديث", data="updatevr"),
                ],
                [
                    Button.inline("اعاده تشغيل", data="resitvr"),
                    Button.inline("ايقاف البوت", data="stopvr"),
                ],
                [
                    Button.inline("الفحص", data="alivzed"),
                ],
                [
                    Button.inline("السليب (النوم)", data="sleep"),
                    Button.inline("سرعة الانترنت", data="netzed"),
                ],
                [
                    Button.inline("نظـام البـوت", data="syszed"),
                ],
                [
                    Button.inline("سورس", data="sourcevr"),
                    Button.inline("يـــمنثون", data="zedvr"),
                ],
                [
                    Button.inline("الاذاعه", data="ethaavr"),
                ],
                [
                    Button.inline("المطور المساعد", data="devvr"),
                ],
                [Button.inline("رجــوع", data="ZEDHELP")],
            ],
        link_preview=False)
    except Exception:
        await event.answer(zelzal, cache_time=0, alert=True)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"syszed")))
@check_owner
async def _(event):
    await event.edit(
        "[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - ادوات النظــام 🤖](t.me/YamenThon) .\n\n**「❖╎اليك عـزيـزي شـࢪوحـات اوامـر نظـام البـوت المسـاعد :**\n\n",
        buttons=[
            [
                Button.inline("النظـام", data="syszzz"),
            ],
            [
                Button.inline("الفـرمتـه", data="rmzzz"),
                Button.inline("السـرعـة", data="fszzz"),
            ],
            [Button.inline("فـاراتـي", data="envzzz")],
            [Button.inline("تاريـخ التنصيب", data="datzzz")],
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"syszzz")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البـــوت 🦾🤖](t.me/YamenThon) .
**- الامـر :**
**⪼** `.النظام`

**- الوصـف :**
لـ لعـرض معلومـات نظـام البـوت الخـاص بك كـ :
السيرفـر ونوعـه واصـداره
والمعالجـات واستخداماتهـا
والذاكـرة واستخداماتهـا
والتحميـل والرفـع
واصدارات اللغـه والمكتبـه
... الـخ

**- الاستخـدام :**
ارسـل الامـر   `.النظام`""",
        buttons=[
            [Button.inline("رجوع", data="syszed")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"rmzzz")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البـــوت 🦾🤖](t.me/YamenThon) .
**- الامـر :**
**⪼** `.فرمته`

**- الوصـف :**
لـ حذف ومسح المجلدات والملفات والعمليات المخزنه مؤقتـاً في سيرفر البوت الخاص بك

**- الاستخـدام :**
ارسـل الامـر   `.فرمته`""",
        buttons=[
            [Button.inline("رجوع", data="syszed")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"fszzz")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البـــوت 🦾🤖](t.me/YamenThon) .
**- الامـر :**
**⪼** `.السرعه`

**- الوصـف :**
لـ قياس سرعة الرفع والتحميل في سيرفر البوت الخاص بك

**- الاستخـدام :**
ارسـل الامـر   `.السرعه`""",
        buttons=[
            [Button.inline("رجوع", data="syszed")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"envzzz")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البـــوت 🦾🤖](t.me/YamenThon) .
**- الامـر :**
**⪼** `.فاراتي`

**- الوصـف :**
لـ جلب قائمـة بجميـع فـارات التنصيب الخاصـه بك

**- الاستخـدام :**
ارسـل الامـر   `.فاراتي`""",
        buttons=[
            [Button.inline("رجوع", data="syszed")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"datzzz")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البـــوت 🦾🤖](t.me/YamenThon) .
**- الامـر :**
**⪼** `.تاريخ التنصيب`

**- الوصـف :**
لـ عـرض تاريـخ بـدء تنصيبك على سـورس يـــمنثون
بالوقـت والتـاريـخ والمدة المنقضيـه لـ آخـر تنصيب لك

**- الاستخـدام :**
ارسـل الامـر   `.تاريخ التنصيب`""",
        buttons=[
            [Button.inline("رجوع", data="syszed")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"updatevr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البـــوت 🦾🤖](t.me/YamenThon) .
**- الامـر :**
**⪼** `.تحديث`

**- الوصـف :**
لـ تحديث البوت في حال كان هناك تحديثات جديده للسورس او في حال نزول تحديثات في قناة السورس
هناك امرين للتحديث الاول :

**⪼** `.تحديث الان`
هذا الامر للتحديث البسيط والسريع وهو المطلوب 

**⪼** `.تحديث البوت`
هذا الامر للتحديث الجذري للبوت وهو بمثابة اعاده التنصيب من اول عمليه بعد المربعات وهو امر غير مطلوب الا في حال نزلت تحديثات جذريه وتم التنويه عليها بقناة السورس

**- الاستخـدام :**
ارسـل الامـر   `.تحديث`""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"resitvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البـــوت 🦾🤖](t.me/YamenThon) .
**- الامـر :**
**⪼** `.اعاده تشغيل`

**- الوصـف :**
لترسيت واعاده تشغيل البوت في حال حدوث اخطاء نادراً او في حال كنت تريد ايقاف عمليه جاريه لا تستجيب ل امـر الايقاف الخاص بها

**- ملاحظـه هامـه :**
لا تقم بتكرار هذا الامر اكثر من مره باليوم الواحد والا سوف يسبب توقف البوت الخاص بك

**- الاستخـدام :**
ارسـل الامـر   `.اعاده تشغيل`""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"stopvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البـــوت 🦾🤖](t.me/YamenThon) .
**- الامـر :**
**⪼** `.ايقاف البوت`

**- الوصـف :**
لـ ايقاف البوت عن العمل نهائيـاً والغـاء تنصيبك ..
في حال استخدمت الامر وتريد اعاده تشغيل البوت من جديد
كل ماعليك هو التشغيل اليدوي من هيروكو

**- الاستخـدام :**
ارسـل الامـر   `.ايقاف البوت`""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"alivzed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البـــوت 🦾🤖](t.me/YamenThon) .
**- الامـر :**
**⪼** `.فحص`

**- الوصـف :**
لـ فحص قاعدة البيانات وعـرض اصـدار السورس ولغة بايثـون واصـدار مكتبة تيليثون

**- الاستخـدام :**
ارسـل الامـر   `.فحص`""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"sleep")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البـــوت 🦾🤖](t.me/YamenThon) .
**- الامـر :**
**⪼** `.سليب`
**⪼** `.سليب_ميديا`

**- الوصـف :**
لـ جعل الحساب في وضع النـوم او الإسبات ويتم ايقافه عند ارسالك لـ اي رسالة

**- الاستخـدام :**
`.سليب`  **او**  `.سليب` + سبب

`.سليب_ميديا`  **او**  `.سليب_ميديا` + سبب
**بالـرد ع صـورة او ميديـا**""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"netzed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البـــوت 🦾🤖](t.me/YamenThon) .
**- الامـر :**
**⪼** `.الانترنت`
**⪼** `.الانترنت صورة`

**- الوصـف :**
لـ عرض سرعة الانتـرنت (الرفـع & التحميـل) في سيرفـر البوت الخاص بك على شكـل صـورة

**- الاستخـدام :**
ارسـل الامـر   `.الانترنت صورة`""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"sourcevr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البـــوت 🦾🤖](t.me/YamenThon) .
**- الامـر :**
**⪼** `.سورس`

**- الوصـف :**
لـ عـرض اصـدار السـورس ومعـرف البوت المساعد واسم تطبيق التنصيب

**- الاستخـدام :**
ارسـل الامـر   `.سورس`""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"zedvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البـــوت 🦾🤖](t.me/YamenThon) .
**- الامـر :**
**⪼** `.يـــمنثون`

**- الوصـف :**
لـ عـرض قنـوات السـورس

**- الاستخـدام :**
ارسـل الامـر   `.يـــمنثون`""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ethaavr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البـــوت 🦾🤖](t.me/YamenThon) .
**- الامـر :**
**⪼** `.الاذاعه`

**- الوصـف :**
لـ عـرض اوامـر الاذاعـه الخاصـه بسـورس يـــمنثون

**- الاستخـدام :**
ارسـل الامـر   `.الاذاعه`""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"devvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البـــوت 🦾🤖](t.me/YamenThon) .
**- الامـر :**
**⪼** `.رفع مطور`
**لـ رفـع شخـص مطـور مسـاعـد معـك بالبـوت**

**⪼** `.تنزيل مطور`
**- لـ تنزيـل الشخـص مطـور مسـاعـد مـن البـوت**

**⪼** `.المطورين`
**- لـ عـرض قائمـة بمطـورين البـوت الخـاص بـك 🧑🏻‍💻📑**

**⪼** `.وضع المطور تفعيل`
**لـ تفعيـل وضـع المطـورين المسـاعدين**

**⪼** `.وضع المطور تعطيل`
**لـ تعطيـل وضـع المطـورين المسـاعدين**

**⪼** `.تحكم كامل`
**- اعطـاء المطـورين المرفـوعيـن صلاحيـة التحكـم الكـاملـه بالاوامــر ✓**

**⪼** `.تحكم آمن`
**- اعطـاء المطـورين المرفـوعيـن صلاحيـة التحكـم الآمـن لـ الاوامــر الامنـه فقـط ✓**

**⪼** `.تحكم` + اسم الامـر
**اعطـاء المطـورين المرفـوعيـن صلاحيـة التحكـم بأمـر واحـد فقـط او عـدة اوامـر معينـه ✓ .. مثـال (.تحكم ايدي) او (.تحكم ايدي فحص كتم)**

**⪼** `.ايقاف تحكم كامل`
**- ايقـاف صلاحيـة التحكـم الكـاملـه بالاوامــر للمطـورين المرفـوعيـن ✓**

**⪼** `.ايقاف تحكم آمن`
**- ايقـاف صلاحيـة التحكـم الآمـن لـ الاوامــر الآمنـه للمطـورين المرفـوعيـن ✓**

**⪼** `.ايقاف تحكم` + اسم الامـر
**- ايقـاف صلاحيـة التحكـم المعطـاه لـ امـر واحـد فقـط او عـدة اوامـر للمطـورين المرفـوعيـن ✓ .. مثـال (.ايقاف تحكم ايدي) او (.ايقاف تحكم ايدي فحص كتم)**

**⪼** `.التحكم`  /  `.التحكم المعطل`



**- الوصـف :**
لـ رفـع واضافة شخص متحكم معك بالبوت حيث يستطيع استخدام الاوامر مثلك تماماً

**- ملاحظـه هـامه :**
لا تقم برفع احد انت غير واثق فيه لان المتحكم يستطيع استخدام الاوامر في شي ماراح يرضيك او يسبب لك احراج اذا استخدم امر مثل اوامر التوجيه ... الخ

**- الاستخـدام :**
ارسـل احـد الاوامـر اعـلاه""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"groupvr")))
@check_owner
async def _(event):
    zelzal = "⤶ عـذراً عـزيـزي 🤷🏻‍♀\n⤶ هـذه اللوحه لا تشتغل في الخاص\n⤶ لـ إظهـار لوحـة المسـاعـدة 👇\n\n⤶ ارســل (.مساعده) في اي مجمـوعـه"
    try:
        await event.edit(
            "[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه 🛗](t.me/YamenThon) .\n\n**「❖╎اليك عـزيـزي شـࢪوحـات اوامـر المجمــوعــه :**\n\n",
            buttons=[
                [
                    Button.inline("اوامــر المجمــوعــه¹", data="group1vr"),
                ],
                [
                    Button.inline("اوامــر المجمــوعــه²", data="group2vr"),
                ],
                [
                    Button.inline("اوامــر المجمــوعــه³", data="group3vr"),
                ],
                [
                    Button.inline("مكافح التكرار", data="nospam"),
                    Button.inline("المنـع", data="noway"),
                ],
                [
                    Button.inline("الاضـافه والتفليـش", data="group0vr"),
                ],
                [
                    Button.inline("التحذيرات", data="warnzed"),
                    Button.inline("الترحيبـات", data="group4vr"),
                ],
                [
                    Button.inline("الــردود", data="group5vr"),
                ],   
                [
                    Button.inline("كشف المجوعات", data="group6vr"),
                ],
                [Button.inline("رجــوع", data="ZEDHELP")],
            ],
        link_preview=False)
    except Exception:
        await event.answer(zelzal, cache_time=0, alert=True)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"warnzed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه¹](t.me/YamenThon) .
**- الامـر :**
**⪼** `.تحذير`
**⪼** `.التحذيرات`
**⪼** `.حذف التحذيرات`


**- الوصـف :**
لـ تحذير شخص في المجموعة فاذا وصلت 3 تحذيرات يتم طرده من المجموعة
تستطيع ايضاً وضع سبب لتحذير الشخص تابع الاستخدام بالاسفل


**- الاستخـدام :**
`.تحذير`
**بالـرد ع شخـص لـ تحذيره او باضافة معرف/ايدي الشخص للامر**

`.التحذيرات`
**بالـرد ع شخـص لـ جلب عدد تحذيراتـه**

`.حذف التحذيرات`
**بالـرد ع شخـص لـ حذف تحذيراتـه**

`.تحذير + سبب`
**بالـرد ع شخـص لـ تحذيره او باضافة معرف/ايدي الشخص للامر**

**- مثـال :**
`.تحذير يزحف للبنات`
**بالـرد ع شخص او باضافة معرف/ايدي الشخص للامر**""",
        buttons=[
            [Button.inline("رجوع", data="groupvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"group4vr")))
@check_owner
async def _(event):
    await event.edit(
        """**- الامـر :**
**⪼** `.ترحيب`
**⪼** `.حذف الترحيب`
**⪼** `.الترحيبات`

**- الوصـف :**
لـ اضافة ترحيب في المجموعة للترحيب بالاعضاء الجدد اثناء الانضمام 
حيث يقوم البوت بارسال رساله ترحيبيه تلقائيـه انت تقوم باضافتها مسبقاً

**- المتغيـرات الاضافيـه :**
{mention}  اضافه منشن
{title}  اضافة اسم كروب الترحيب
{count}  اضافة عدد اعضاء الكروب
{first}  اضافة الاسم الاول
{last}  اضافة الاسم الاخر
{fullname}  اضافة الاسم الكامل
{userid}  اضافة ايدي الشخص
{username}  اضافة معرف الشخص
{my_first}  اضافة اسمك الاول
{my_fullname}  اضافة اسمك الكامل
{my_last}  اضافة اسمك الاخر
{my_mention}  اضافة تاك حسابك
{my_username}  اضافة معرفك

**- الاستخـدام :**
`.ترحيب` + نص الترحيب
`.ترحيب` بالـرد ع رسالـه ترحيبيـه 
`.ترحيب` بالـرد ع ميديـا تحتهـا نـص
`.حذف الترحيب`
`.الترحيبات`

**- مثـال :**
`.ترحيب اططلـق 🥳 دخـول {mention}, نـورت مجمـوعتنـا {title} `""",
        buttons=[
            [Button.inline("رجوع", data="groupvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"group5vr")))
@check_owner
async def _(event):
    await event.edit(
        """**- الامـر :**
**⪼** `.رد`
**⪼** `.حذف رد`
**⪼** `.ردودي`
**⪼** `.حذف الردود`

**- الوصـف :**
لـ اضافة رد في المجموعة لكلمـه معينـه كما في بوتات الحماية بالضبط عندما يقوم حد بارسال الكلمه سوف يتم الرد عليه تلقائياً بالرد الذي قمت باضافته لهذه الكلمه

**- المتغيـرات الاضافيـه :**
{mention}  اضافه منشن
{title}  اضافة اسم كروب الترحيب
{count}  اضافة عدد اعضاء الكروب
{first}  اضافة الاسم الاول
{last}  اضافة الاسم الاخر
{fullname}  اضافة الاسم الكامل
{userid}  اضافة ايدي الشخص
{username}  اضافة معرف الشخص
{my_first}  اضافة اسمك الاول
{my_fullname}  اضافة اسمك الكامل
{my_last}  اضافة اسمك الاخر
{my_mention}  اضافة تاك حسابك
{my_username}  اضافة معرفك

**- الاستخـدام :**
`.رد` + نص الـرد بالـرد ع كلمـة الـرد
`.رد` + نص الـرد بالـرد ع ميديـا
`.حذف رد` + كلمـة الـرد
`.ردودي`
`.حذف الردود`

**- مثـال :**
`.رد اططلـق 🥳 من يصيحني {mention}, لبيه سم آمر حبيبي`
بالــرد ع معرفـك مثـلاً""",
        buttons=[
            [Button.inline("رجوع", data="groupvr")],
        ],
    link_preview=False)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"group6vr")))
@check_owner
async def _(event):
    await event.edit(
        """**- الامـر :**
**⪼** `.كشف المجموعة`


**- الوصـف :**
لـ كشف المجموعة وجميع معلومات وتفاصيـل المجموعـة ارسل الامر داخل اي مجموعه """,
        buttons=[
            [Button.inline("رجوع", data="groupvr")],
        ],
    link_preview=False)   

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"group1vr")))
@check_owner
async def _(event):
    await event.edit(
        "[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه¹ 🛗](t.me/YamenThon) .\n\n**「❖╎اليك عـزيـزي شـࢪوحـات اوامـر المجمــوعــه¹ :**\n\n",
        buttons=[
            [
                Button.inline("البوتات", data="botveiw"),
                Button.inline("قفل البوتات", data="botlock"),
            ],
            [
                Button.inline("قفل الاضافه", data="addlock"),
                Button.inline("قفل الدخول", data="golock"),
            ],
            [
                Button.inline("قفل تعديل الميديا", data="edmdlock"),
            ],
            [
                Button.inline("قفل الروابط", data="urlock"),
                Button.inline("قفل المعرفات", data="userlock"),
            ],
            [
                Button.inline("قفل التوجيه", data="forlock"),
                Button.inline("قفل الانلاين", data="inilock"),
            ],
            [
                Button.inline("قفل الميديا", data="medlock"),
            ],
            [
                Button.inline("قفل الفارسيه", data="farslock"),
                Button.inline("قفل الفشار", data="fuklock"),
            ],
            [
                Button.inline("الاعدادات", data="setelock"),
                Button.inline("قفل الكل", data="alllock"),
            ],
            [Button.inline("تقييـد المحتـوى", data="lolzed")],
            [Button.inline("رجوع", data="groupvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"botveiw")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه¹](t.me/YamenThon) .
**- الامـر :**
**⪼** `.البوتات`

**- الوصـف :**
لـ كشـف وتنظيف مجموعتـك من البوتات .. لمنع التصفير والتفليش والتخريب

**- الاستخـدام :**
ارسـل الامـر   `.البوتات`   في مجموعتك""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"botlock")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه¹](t.me/YamenThon) .
**- الامـر :**
**⪼** `.قفل البوتات`
`.فتح البوتات`

**- الوصـف :**
لـ فتـح او قفـل البوتـات بالطـرد التلقائـي .. الامر يمنع حتى المشـرفين من اضافـة البوتات .. في حـال اراد احد المشرفين رفـع بوت وتصفير مجموعتك اثنـاء غيابـك.

**- الاستخـدام :**
ارسـل الامـر   `.قفل البوتات`   في مجموعتك""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"addlock")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه¹](t.me/YamenThon) .
**- الامـر :**
**⪼** `.قفل الاضافه`
`.فتح الاضافه`

**- الوصـف :**
لـ فتـح او قفـل اضافـة الاعضـاء بالطـرد .. مـع تحذيـر صاحـب الاضـافه

**- الاستخـدام :**
ارسـل الامـر   `.قفل الاضافه`   في مجموعتك""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"golock")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه¹](t.me/YamenThon) .
**- الامـر :**
**⪼** `.قفل الدخول`
`.فتح الدخول`

**- الوصـف :**
لـ فتـح او قفـل الدخـول بالرابـط بالطـرد التلقائـي .. حيث يقـوم بطـرد المنضم تلقائيـاً .. مـع ارسـال رسـاله تحذيريـه

**- الاستخـدام :**
ارسـل الامـر   `.قفل الدخول`   في مجموعتك""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"medlock")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه¹](t.me/YamenThon) .
**- الامـر :**
**⪼** `.قفل الميديا`
**⪼** `.فتح الميديا`

**- الوصـف :**
لـ فتـح او قفـل الوسائـط بالمسـح + تقييـد المرسـل من صلاحيـة ارسال الوسائط تلقائيـاً .. مع السمـاح له بارسـال الرسـائل فقـط .. يفيدكـم لـ منـع التفليـش الاباحـي في حال غيابكـم او انشغـالكم .. يسمـح للمشـرفين فقـط بارسـال الوسائـط

**- الاستخـدام :**
ارسـل الامـر   `.قفل الميديا`   في مجموعتك""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"edmdlock")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه¹](t.me/YamenThon) .
**- الامـر :**
**⪼** `.قفل تعديل الميديا`
**⪼** `.فتح تعديل الميديا`

**- الوصـف :**
لـ فتـح او قفـل تعديـل الوسائـط بالمسـح + تحذيـر المرسـل تلقائيـاً .. يفيدكـم لـ منـع التفليـش عبـر التعديـل في حال غيابكـم او انشغـالكم .. لايسمـح حتى للمشـرفين بتعديـل الوسائـط

**- الاستخـدام :**
ارسـل الامـر   `.قفل تعديل الميديا`   في مجموعتك اللتي تريـد منـع تعديـل الوسائـط فيهـا""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"urlock")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه¹](t.me/YamenThon) .
**- الامـر :**
**⪼** `.قفل الروابط`
`.فتح الروابط`

**- الوصـف :**
لـ فتـح او قفـل الروابـط بالمسـح التلقائـي .. مع تحذير الشخص المرسل

**- الاستخـدام :**
ارسـل الامـر   `.قفل الروابط`   في مجموعتك""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"userlock")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه¹](t.me/YamenThon) .
**- الامـر :**
**⪼** `.قفل المعرفات`
`.فتح المعرفات`

**- الوصـف :**
لـ فتـح او قفـل المعرفـات بالمسـح التلقائـي .. مع تحذير الشخص المرسل

**- الاستخـدام :**
ارسـل الامـر   `.قفل المعرفات`   في مجموعتك""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"forlock")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه¹](t.me/YamenThon) .
**- الامـر :**
**⪼** `.قفل التوجيه`
`.فتح التوجيه`

**- الوصـف :**
لـ فتـح او قفـل رسـائل التوجيـه المعـاد توجيههـا من القنـوات بالمسـح التلقائـي .. مع تحذير الشخص المرسل

**- الاستخـدام :**
ارسـل الامـر   `.قفل التوجيه`   في مجموعتك""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"inilock")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه¹](t.me/YamenThon) .
**- الامـر :**
**⪼** `.قفل الانلاين`
`.فتح الانلاين`

**- الوصـف :**
لـ فتـح او قفـل رسائل الانلايـن والهمسـات بالمسـح التلقائـي .. مع تحذير الشخص .. يسمـح للمشرفين فقـط بارسال الانلايـن

**- الاستخـدام :**
ارسـل الامـر   `.قفل الانلاين`   في مجموعتك""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"farslock")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه¹](t.me/YamenThon) .
**- الامـر :**
**⪼** `.قفل الفارسيه`
`.فتح الفارسيه`

**- الوصـف :**
لـ فتـح او قفـل مسـح رسـائل الايرانيين وبوتات الاعلانات الفارسيه تلقائيـاً .. مـع تحذيـر الشخـص المرسـل

**- الاستخـدام :**
ارسـل الامـر   `.قفل الفارسيه`   في مجموعتك""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"fuklock")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه¹](t.me/YamenThon) .
**- الامـر :**
**⪼** `.قفل الفشار`
`.فتح الفشار`

**- الوصـف :**
لـ مسـح رسـائل الفشار والسب والتكفير تلقائيـاً .. مـع تحذيـر الشخـص المرسـل

**- الاستخـدام :**
ارسـل الامـر   `.قفل الفشار`   في مجموعتك""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"alllock")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه¹](t.me/YamenThon) .
**- الامـر :**
**⪼** `.قفل الكل`
`.فتح الكل`

**- الوصـف :**
لـ قفـل او فتـح كـل الاوامـر السابقـه

**- الاستخـدام :**
ارسـل الامـر   `.قفل الكل`   في مجموعتك""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"setelock")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه¹](t.me/YamenThon) .
**- الامـر :**
**⪼** `.الاعدادات`

**- الوصـف :**
لـ عـرض اعـدادات المجمـوعـه

**- الاستخـدام :**
ارسـل الامـر   `.الاعدادات`   في مجموعتك""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"lolzed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه](t.me/YamenThon) .
**- الامـر :**
**⪼** `.قيد`

**- الوصـف :**
لـ تقييـد محتـوى مجمـوعتك او قنـاتك

لـ المايعرف ماذا يعني تقييد محتوى ؟!
هي اضافه قامت شركة تيليجرام مؤخراً باضافتها للمجموعات او القنوات لجعلها مقيدة اي يمنع اي شخص من النسخ والتوجيه او اخذ لقطة شاشة منها

**- الاستخـدام :**
ارسـل الامـر
`.قيد`
في مجموعتك او قناتك""",
        buttons=[
            [Button.inline("رجوع", data="botvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"group2vr")))
@check_owner
async def _(event):
    await event.edit(
        "[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه² 🛗](t.me/YamenThon) .\n\n**「❖╎اليك عـزيـزي شـࢪوحـات اوامـر المجمــوعــه² :**\n\n",
        buttons=[
            [
                Button.inline("الرابط", data="urlveiw"),
                Button.inline("تاك all", data="tagvr"),
            ],
            [
                Button.inline("رفع مشرف", data="addmnvr"),
                Button.inline("رفع مالك", data="creatorvr"),
            ],
            [
                Button.inline("رسائلي/رسائله", data="msgvr"),
                Button.inline("اسمي/اسمه", data="delmsgvr"),
            ],
            [
                Button.inline("حذف رسائلي", data="delmsgvr"),
            ],
            [
                Button.inline("الاحداث", data="iundlt"),
                Button.inline("المعلومات", data="infoovr"),
            ],
            [
                Button.inline("الاعضاء", data="memver"),
                Button.inline("المشرفين", data="creatorrvr"),
                Button.inline("البوتات", data="botssvr"),
            ],
            [
                Button.inline("الصورة وضع", data="photoadd"),
                Button.inline("التثبيت", data="pinvr"),
            ],
            [Button.inline("المحذوفين", data="zomby")],
            [Button.inline("مسح المحظورين", data="delbans")],
            [Button.inline("رجوع", data="groupvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"urlveiw")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه²](t.me/YamenThon) .
**- الامـر :**
**⪼** `.الرابط`

**- الوصـف :**
لـ جـلب رابـط المجمـوعـة + يجب ان تكون مشرفـاً فيهـا

**- الاستخـدام :**
ارسـل الامـر   `.الرابط`   في مجموعتك""",
        buttons=[
            [Button.inline("رجوع", data="group2vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"tagvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه²](t.me/YamenThon) .
**- الامـر :**
**⪼** `.تاك`
`.all`

**- الوصـف :**
الامـر + كلمـه او بالـرد ع رسـالـه لـ عمـل تـاك بشكـل متقطـع لـ الكـل بالمجمـوعـة

**- الاستخـدام :**
ارسـل الامـر   `.تاك`  +  نص او بالـرد ع رسـاله في مجموعتك
لـ ايقاف التاك ارسـل `.ايقاف التاك`

**- مثـال :**
`.تاك السلام عليكم`
`.ايقاف التاك`""",
        buttons=[
            [Button.inline("رجوع", data="group2vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"addmnvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه²](t.me/YamenThon) .
**- الامـر :**
**⪼** `.رفع مشرف`
`.تنزيل مشرف`

**- الوصـف :**
لـ رفـع الشخـص مشـرفـاً بالكـروب بصـلاحيات محـدوده فقـط وليس كامل الصلاحيـات

**- الاستخـدام :**
ارسـل الامـر   `.رفع مشرف`   بالـرد ع شخص في مجموعتك""",
        buttons=[
            [Button.inline("رجوع", data="group2vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"creatorvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه²](t.me/YamenThon) .
**- الامـر :**
**⪼** `.رفع مالك`
`.تنزيل مالك`

**- الوصـف :**
لـ رفـع الشخـص مشـرفـاً بالكـروب بكامل الصـلاحيات

**- الاستخـدام :**
ارسـل الامـر   `.رفع مالك`   بالـرد ع شخص في مجموعتك""",
        buttons=[
            [Button.inline("رجوع", data="group2vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"msgvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه²](t.me/YamenThon) .
**- الامـر :**
**⪼** `.رسائلي`
**⪼** `.رسائله`

**- الوصـف :**
(.رسائلي) لـ عـرض عـدد رسـائلك في المجمـوعـة
(.رسائله) لـ عـرض عـدد رسائل شخـص في المجمـوعـة

**- الاستخـدام :**
`.رسائلي`
او  `.رسائله`   بالـرد ع شخص في المجمـوعـة""",
        buttons=[
            [Button.inline("رجوع", data="group2vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"msgvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه²](t.me/YamenThon) .
**- الامـر :**
**⪼** `.اسمي`
**⪼** `.اسمه`

**- الوصـف :**
(.اسمي) لـ عـرض اسمـك على شكـل ماركداون
(.اسمه) لـ عـرض اسم شخص على شكـل ماركداون

**- الاستخـدام :**
`.اسمي`
`.اسمه`
**بالـرد ع شخص او باضافة معرف او ايدي للامـر**
`.اسمه` + كلمـه
**بالـرد ع شخص او باضافة معرف او ايدي للامـر 
يسوي تاك بكلمه للشخص**""",
        buttons=[
            [Button.inline("رجوع", data="group2vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"delmsgvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه²](t.me/YamenThon) .
**- الامـر :**
**⪼** `.حذف رسائلي`
**⪼** `.مسح`

**- الوصـف :**
`.حذف رسائلي` + عـدد
لـ حـذف رسـائلك في المجمـوعـة بالعـدد .. كلمـا ضفت عـدد اكبـر كلمـا كان الحـذف اكبـر
`.مسح` 
بالـرد ع أي رسـاله لحذفهـا

**- الاستخـدام :**
`.حذف رسائلي` + عـدد

**- مثـال :**
`.حذف رسائلي 1000`

**- ملاحظـه :**
**اذا كنت تريد حذف جميـع رسائلك في المجمـوعـة استخـدم امريـن :**
`.رسائلي`
**راح يعطيك عـدد رسائلك**
**ثم ارسل بعدهـا :**
`.حذف رسائلي` + نفـس العـدد""",
        buttons=[
            [Button.inline("رجوع", data="group2vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"iundlt")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه²](t.me/YamenThon) .
**- الامـر :**
**⪼** `.الاحداث`
`.الاحداث م`

**- الوصـف :**
(`.الاحداث` + عدد)لـ جـلب آخـر الرسـائـل المحـذوفـه مـن آخـر احـداث المجمـوعـة بـ العـدد
(`.الاحداث م`) لجـلب رسـائل الميديـا المحذوفـة من آخر الااحـداث

**- الاستخـدام :**
ارسـل الامـر    `.الاحداث` 7""",
        buttons=[
            [Button.inline("رجوع", data="group2vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"infoovr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه²](t.me/YamenThon) .
**- الامـر :**
**⪼** `.المعلومات`

**- الوصـف :**
لـ جـلب معلومـات وتفاصيـل كاملـه عن اي مجمـوعـة او قنـاة مثل اسم المجموعه الحالي والاسم السابق وتاريخ الانشاء والمالك وعدد المشرفين و عدد الاعضاء المتصلين والمحظورين .. الـخ

**- الاستخـدام :**
ارسـل الامـر    `.المعلومات` داخـل المجمـوعـة او القنـاة""",
        buttons=[
            [Button.inline("رجوع", data="group2vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"memver")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه²](t.me/YamenThon) .
**- الامـر :**
**⪼** `.الاعضاء`

**- الوصـف :**
لـ عـرض قائمـة او ملـف بـ اعضـاء المجمـوعـة او القنـاة

**- الاستخـدام :**
ارسـل الامـر   (.الاعضاء)   داخـل المجمـوعـة او القنـاة
او  (.الاعضاء + معرف او رابـط) المجمـوعـة او القنـاة""",
        buttons=[
            [Button.inline("رجوع", data="group2vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"creatorrvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه²](t.me/YamenThon) .
**- الامـر :**
**⪼** `.المشرفين`

**- الوصـف :**
لـ عـرض قائمـة او ملـف بـ مشرفيـن المجمـوعـة او القنـاة

**- الاستخـدام :**
ارسـل الامـر   (.المشرفين)   داخـل المجمـوعـة او القنـاة
او  (.المشرفين + معرف او رابـط) المجمـوعـة او القنـاة""",
        buttons=[
            [Button.inline("رجوع", data="group2vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"botssvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه²](t.me/YamenThon) .
**- الامـر :**
**⪼** `.البوتات`

**- الوصـف :**
لـ عـرض قائمـة او ملـف بـ بوتـات المجمـوعـة او القنـاة

**- الاستخـدام :**
ارسـل الامـر   (.البوتات)   داخـل المجمـوعـة او القنـاة
او  (.البوتات + معرف او رابـط) المجمـوعـة او القنـاة""",
        buttons=[
            [Button.inline("رجوع", data="group2vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"photoadd")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه²](t.me/YamenThon) .
**- الامـر :**
**⪼** `.الصورة وضع`
`.الصورة حذف`

**- الوصـف :**
(.الصورة وضع) لـ وضـع او تغييـر صـورة المجمـوعـة
(.الصورة حذف) لـ حـذف صـورة المجمـوعـة

**- الاستخـدام :**
ارسـل الامـر   (.الصورة وضع)   بالـرد على صـورة في المجمـوعـة
او  (.الصورة حذف)""",
        buttons=[
            [Button.inline("رجوع", data="group2vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"pinvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه²](t.me/YamenThon) .
**- الامـر :**
**⪼** `.تثبيت`
`.الغاء تثبيت`
`.الغاء تثبيت الكل`

**- الوصـف :**
بالـرد على رسـاله معينـه لـ تثبيتهـا او الغـاء تثبيتهـا في المجمـوعـة او القنـاة

**- الاستخـدام :**
ارسـل الامـر   (.تثبيت)   بالـرد على رسـاله في المجمـوعـة
او  (.الغاء تثبيت)""",
        buttons=[
            [Button.inline("رجوع", data="group2vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"zomby")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه²](t.me/YamenThon) .
**- الامـر :**
**⪼** `.المحذوفين`
`.المحذوفين تنظيف`

**- الوصـف :**
لـ عـرض او تنظيـف المجمـوعـة او القنـاة من الحسـابات المحذوفـه

**- الاستخـدام :**
ارسـل الامـر   (.المحذوفين)   داخـل المجمـوعـة او القنـاة
او  (.المحذوفين تنظيف)""",
        buttons=[
            [Button.inline("رجوع", data="group2vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"delbans")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه²](t.me/YamenThon) .
**- الامـر :**
**⪼** `.مسح المحظورين`

**- الوصـف :**
لـ مسـح قائمـة المحظـورين في المجمـوعـة او القنـاة

**- الاستخـدام :**
ارسـل الامـر   (.مسح المحظورين)   داخـل المجمـوعـة او القنـاة""",
        buttons=[
            [Button.inline("رجوع", data="group2vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"group3vr")))
@check_owner
async def _(event):
    await event.edit(
        "[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه³ 🛗](t.me/YamenThon) .\n\n**「❖╎اليك عـزيـزي شـࢪوحـات اوامـر المجمــوعــه³ :**\n\n",
        buttons=[
            [
                Button.inline("كتم", data="mutevr"),
                Button.inline("حظر", data="banvr"),
            ],
            [
                Button.inline("طرد", data="kickvr"),
                Button.inline("تقييد", data="tkkkvr"),
            ],
            [
                Button.inline("مغادره", data="byby"),
                Button.inline("طرد البوتات", data="banbot"),
            ],
            [Button.inline("المحذوفين", data="zoomby")],
            [Button.inline("مسح المحظورين", data="dellbans")],
            [Button.inline("رجوع", data="groupvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"mutevr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه³](t.me/YamenThon) .
**- الامـر :**
**⪼** `.كتم` + السبب بالـرد
`.كتم` + معرف/ايدي + السبب

**- مثـال :**
(.كتم يزحف للبنات) بالـرد ع شخص
(.كتم + معرف/ايدي + يزحف للبنات)

**- الوصـف :**
لـ كتـم شخص سـواء في المجمـوعـة او الخـاص اذا ارسلت الامر في المجموعة سوف ينكتم في المجموعة واذا في الخاص سوف ينكتم من الخاص فقط ماعدا اوامر الكتم العام فانهما تكتم الشخص من الخاص وجميع المجموعات والقنوات التي انت مشرف فيهـا

**- الاستخـدام :**
لـ الكتم ارسـل
`.كتم`   بالـرد ع شخص
`.كتم`   + معـرف/ايـدي الشخـص
`.الغاء كتم`   بالـرد ع شخص
`.الغاء كتم`   + معـرف/ايـدي الشخـص

**لـ الكتم العـام ارسـل**
`.ك عام`   بالـرد ع شخص
`.ك عام`   + معـرف/ايـدي الشخـص
`.الغاء ك عام`   بالـرد ع شخص
`.الغاء ك عام`   + معـرف/ايـدي الشخـص""",
        buttons=[
            [Button.inline("رجوع", data="group3vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"banvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه³](t.me/YamenThon) .
**- الامـر :**
**⪼** `.حظر` + السبب بالـرد
`.حظر` + معرف/ايدي + السبب

**- مثـال :**
(.حظر يزحف للبنات) بالـرد ع شخص
(.حظر + معرف/ايدي + يزحف للبنات)

**- الوصـف :**
لـ حظـر شخص سـواء في المجمـوعـة او الخـاص اذا ارسلت الامر في المجموعة سوف ينحظر من المجموعة واذا في الخاص سوف ينحظر من الخاص فقط
ماعدا اوامر الحظر العام فانهما تحظر الشخص من الخاص وجميع المجموعات والقنوات التي انت مشرف فيهـا

**- الاستخـدام :**
لـ الحظر ارسـل
`.حظر`   بالـرد ع شخص
`.حظر`   + معـرف/ايـدي الشخـص
`.الغاء حظر`   بالـرد ع شخص
`.الغاء حظر`   + معـرف/ايـدي الشخـص

**لـ الحظر العـام ارسـل**
`.ح عام`   بالـرد ع شخص
`.ح عام`   + معـرف/ايـدي الشخـص
`.الغاء ح عام`   بالـرد ع شخص
`.الغاء ح عام`   + معـرف/ايـدي الشخـص""",
        buttons=[
            [Button.inline("رجوع", data="group3vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"kickvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه³](t.me/YamenThon) .
**- الامـر :**
**⪼** `.طرد`

**- الوصـف :**
لـ طـرد شخص من المجمـوعـة سوف ينطرد مجرد طرد فقط وليس حظر مع استطاعته العوده للمجموعة مرة اخرى

**- الاستخـدام :**
ارسـل الامـر   `.طرد`   بالـرد ع شخص
او   `.طرد`   + معـرف/ايـدي الشخـص""",
        buttons=[
            [Button.inline("رجوع", data="group3vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"tkkkvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه³](t.me/YamenThon) .
**- الامـر :**
**⪼** `.تقييد`

**- الوصـف :**
لـ تقييـد شخص من المجمـوعـة

**- الاستخـدام :**
ارسـل الامـر   `.تقييد`   بالـرد ع شخص
او   `.تقييد`   + معـرف/ايـدي الشخـص""",
        buttons=[
            [Button.inline("رجوع", data="group3vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"nospam")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر مكـافح التكــرار 🛡](t.me/YamenThon) .
**- الامـر :**
**⪼** `.ضع التكرار`

**- الوصـف :**
لـ منـع التكـرار في المجمـوعـة وتقييـد المستخـدم عند التكـرار تلقائيـاً

**- الاستخـدام :**
**لـ تفعيـل المكافـح ارسـل :**
`.ضع التكرار`  + **عـدد التكـرار**

**لـ تعطيـل المكافـح ارسـل :**
`.ضع التكرار`  + **عـدد كبيـر جـداً**""",
        buttons=[
            [Button.inline("رجوع", data="groupvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"noway")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المنــع 🚫](t.me/YamenThon) .
**- الامـر :**
**⪼** `.منع`
**⪼** `.الغاء منع`
**⪼** `.قائمة المنع`

**- الوصـف :**
لـ منـع كلمـة ومسحهـا تلقائيـاً عند ارسالهـا في الدردشـة

**- الاستخـدام :**
`.منع`  + **الكلمـه المـراد منعهـا**
`.الغاء منع`  + **الكلمـه المـراد الغـاء منعهـا**
`.قائمة المنع`""",
        buttons=[
            [Button.inline("رجوع", data="groupvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"group0vr")))
@check_owner
async def _(event):
    await event.edit(
        "[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الاضـافه والتفليـش 👾](t.me/YamenThon) .\n\n**「❖╎اليك عـزيـزي شـࢪوحـات اوامـر الاضـافه والتفليـش :**\n\n",
        buttons=[
            [
                Button.inline("الاضافه", data="addvr"),
            ],
            [
                Button.inline("التفليش", data="zerovr"),
            ],
            [
                Button.inline("حظر_الكل", data="banall"),
                Button.inline("طرد_الكل", data="kickall"),
            ],
            [
                Button.inline("كتم_الكل", data="mutall"),
            ],
            [Button.inline("مسح المحظورين", data="dellbans")],
            [Button.inline("رجوع", data="groupvr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"addvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه³](t.me/YamenThon) .
**- الامـر :**
**⪼** `.ضيف`
**⪼** `.اضافه`
**⪼** `.انضمام`

**- الوصـف :**
(.ضيف) لـ اضافة وسحب اعضـاء من مجمـوعـة الى مجمـوعـة آخـرى
(.اضافه) لـ اضافة شخص الى مجمـوعـة او قنـاة
(.انضمام) لـ الانضمام الى مجمـوعـة او قنـاة

**- الاستخـدام :**
**اولاً امر اضافة الاعضـاء :
**ارسـل الامـر التالـي في مجمـوعتـك
`.ضيف`   **+  معـرف المجمـوعـة المـراد سحب الاعضـاء منهـا**
**بشـرط ان تكـون المجمـوعـة المـراد سحب الاعضـاء منهـا مجمـوعـة عامـه بمعـرف وليست خاصـه**


**ارسـل الامـر التالـي في مجمـوعتـك او قنـاتك
`.اضافه`   +  معـرف/ايـدي الشخـص الذي تريد اضافته

او `.انضمام`   +  معـرف/رابـط القناة او المجموعة""",
        buttons=[
            [Button.inline("رجوع", data="group0vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"zerovr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه³](t.me/YamenThon) .
**- الامـر :**
**⪼** `.تفليش`
`.تفليش بالطرد`

**- الوصـف :**
لـ تصفيـر جميـع اعضـاء المجمـوعـة + يجب ان يكون لديك اشـراف فيهـا بصلاحيات الحظـر

**- الاستخـدام :**
ارسـل احـد الاوامـر التالـيه في المجمـوعـة المـراد تفليشهـا
`.تفليش`
`.تفليش بالطرد`""",
        buttons=[
            [Button.inline("رجوع", data="group0vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"banall")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه³](t.me/YamenThon) .
**- الامـر :**
**⪼** `.حظر_الكل`

**- الوصـف :**
لـ حظـر جميـع اعضـاء المجمـوعـة عبـر بوت الحمايـة + لا تحتاج صلاحيات اشراف فيها كل الي تحتاجـه فقط رتبه ادمن او اعلى في بوت الحماية الموجود بالمجمـوعـة

**- الاستخـدام :**
ارسـل الامـر التالـي في المجمـوعـة المـراد تفليشهـا
`.حظر_الكل`
لـ ايقـاف عمليـة الحظـر الجاريـه
ارسـل    `.ايقاف التفليش`""",
        buttons=[
            [Button.inline("رجوع", data="group0vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"kickall")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه³](t.me/YamenThon) .
**- الامـر :**
**⪼** `.طرد_الكل`

**- الوصـف :**
لـ طـرد جميـع اعضـاء المجمـوعـة عبـر بوت الحمايـة + لا تحتاج صلاحيات اشراف فيها كل الي تحتاجـه فقط رتبه ادمن او اعلى في بوت الحماية الموجود بالمجمـوعـة

**- الاستخـدام :**
ارسـل الامـر التالـي في المجمـوعـة المـراد تفليشهـا
`.طرد_الكل`
لـ ايقـاف عمليـة الطـرد الجاريـه
ارسـل    `.ايقاف التفليش`""",
        buttons=[
            [Button.inline("رجوع", data="group0vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"mutall")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه³](t.me/YamenThon) .
**- الامـر :**
**⪼** `.كتم_الكل`

**- الوصـف :**
لـ كتـم جميـع اعضـاء المجمـوعـة عبـر بوت الحمايـة + لا تحتاج صلاحيات اشراف فيها كل الي تحتاجـه فقط رتبه ادمن او اعلى في بوت الحماية الموجود بالمجمـوعـة

**- الاستخـدام :**
ارسـل الامـر التالـي في المجمـوعـة المـراد كتـم اعضـائهـا
`.كتم_الكل`
لـ ايقـاف عمليـة الكتـم الجاريـه
ارسـل    `.ايقاف التفليش`""",
        buttons=[
            [Button.inline("رجوع", data="group0vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"byby")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه³](t.me/YamenThon) .
**- الامـر :**
**⪼** `.غادر`
`.مغادره`
`.اطردني`

**- الوصـف :**
لـ مغـادرة المجمـوعـة او القنـاة

**- الاستخـدام :**
ارسـل الامـر التالـي في المجمـوعـة او القنـاة
`.مغادره`""",
        buttons=[
            [Button.inline("رجوع", data="group3vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"banbot")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه³](t.me/YamenThon) .
**- الامـر :**
**⪼** `.البوتات طرد`
`.البوتات`

**- الوصـف :**
لـ كشف وطرد البوتات الموجـوده بالمجمـوعـه

**- الاستخـدام :**
ارسـل الامـر   `.البوتات`   للكشف عن البوتات
`.البوتات طرد`   لطـرد البوتـات""",
        buttons=[
            [Button.inline("رجوع", data="group3vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"zoomby")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه³](t.me/YamenThon) .
**- الامـر :**
**⪼** `.المحذوفين`
`.المحذوفين تنظيف`

**- الوصـف :**
لـ عـرض او تنظيـف المجمـوعـة او القنـاة من الحسـابات المحذوفـه

**- الاستخـدام :**
ارسـل الامـر   (.المحذوفين)   داخـل المجمـوعـة او القنـاة
او  (.المحذوفين تنظيف)""",
        buttons=[
            [Button.inline("رجوع", data="group3vr")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"dellbans")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المجمــوعــه³](t.me/YamenThon) .
**- الامـر :**
**⪼** `.مسح المحظورين`

**- الوصـف :**
لـ مسـح قائمـة المحظـورين في المجمـوعـة او القنـاة

**- الاستخـدام :**
ارسـل الامـر   (.مسح المحظورين)   داخـل المجمـوعـة او القنـاة""",
        buttons=[
            [Button.inline("رجوع", data="group0vr")],
        ],
    link_preview=False)

############ الفارات ############
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"varszed")))
@check_owner
async def _(event):
    zelzal = "⤶ عـذراً عـزيـزي 🤷🏻‍♀\n⤶ هـذه اللوحه لا تشتغل في الخاص\n⤶ لـ إظهـار لوحـة المسـاعـدة 👇\n\n⤶ ارســل (.مساعده) في اي مجمـوعـه"
    try:
        await event.edit(
            "[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الفــارات 🧬](t.me/YamenThon) .\n\n**「❖╎اليك عـزيـزي شـࢪوحـات اوامـر الفــارات :**\n\n",
            buttons=[
                [
                    Button.inline("فارات الفحص", data="alivevar"),
                    Button.inline("فارات الحماية", data="pmvars"),
                ],
                [Button.inline("فارات الوقتي", data="namevar")],
                [Button.inline("فارات السورس", data="sourcevar")],
                [Button.inline("رجــوع", data="ZEDHELP")],
            ],
        link_preview=False)
    except Exception:
        await event.answer(zelzal, cache_time=0, alert=True)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"namevar")))
@check_owner
async def _(event):
    await event.edit(
        "[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر فــارات الوقتــي 🕰](t.me/YamenThon) .\n\n**「❖╎اليك عـزيـزي شـࢪوحـات اوامـر فــارات الوقتــي :**\n\n",
        buttons=[
            [
                Button.inline("تغيير اسمي في السورس 🌐", data="nameprvr"),
            ],
            [
                Button.inline("نبذة وقتيه", data="biolokvar"),
                Button.inline("صورة وقتيه", data="phovarlok"),
            ],
            [
                Button.inline("زخارف الوقتي", data="timevar"),
                Button.inline("زخارف الوقتيه", data="timavar"),
            ],
            [
                Button.inline("رمز الاسم الوقتي", data="symnamvar"),
            ],
            [
                Button.inline("المنطقه الزمنيه", data="contrytime"),
            ],
            [Button.inline("رجوع", data="varszed")],
            [Button.inline("رجــوع", data="ZEDHELP")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"sourcevar")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الفــارات](t.me/YamenThon) .
ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الـفــارات 🎛 .
⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆
「❖╎قائـمه اوامر تغييـر فـارات الصـور بأمـر واحـد فقـط - لـ اول مـره ع سـورس تليثـون يوزر بـوت 🦾 : 

**⪼** `.اضف صورة الحماية` بالـرد ع صـورة او ميديـا

**⪼** `.اضف صورة الفحص` بالـرد ع صـورة او ميديـا
**⪼** قنـاة كلايـش الفحـص @YamenThon_cklaish

**⪼** `.اضف صورة الوقتي` بالـرد ع صـورة او ميديـا

**⪼** `.اضف صورة الاوامر` بالـرد ع صـورة او ميديـا

**⪼** `.اضف صورة السورس` بالـرد ع صـورة او ميديـا

**⪼** `.اضف صورة الكتم` بالـرد ع صـورة او ميديـا

**⪼** `.اضف صورة البوت` بالـرد ع صـورة او ميديـا لـ اضـافة صـورة ستـارت للبـوت

**⪼** `.اوامر الفارات` لعـرض بقيـة اوامـر الفـارات


**「❖╎قائـمه اوامر تغييـر كليشـة الايـدي** : 

**⪼** `.اضف ايموجي الايدي` بالـرد ع الرمـز او الايموجـي

**⪼** `.اضف عنوان الايدي` بالـرد ع نـص العنـوان

**⪼** `.اضف خط الايدي` بالـرد ع الخـط او المستقيـم

**⪼** `.اضف كليشة` الايدي بالـرد ع الكليشـه مـن القنـاة @YamenThon_cklaish


**「❖╎قائـمه اوامر تغييـر بقيـة الفـارات بأمـر واحـد فقـط** : 

**⪼** `.اضف كليشة الحماية` بالـرد ع الكليشـة
**⪼* قنـاة كلايـش حمايـة الخـاص @YamenThon_cklaish

**⪼** `.اضف كليشة الفحص` بالـرد ع الكليشـة
**⪼** قنـاة كلايـش الفحـص @YamenThon_cklaish

**⪼** `.اضف كليشة الحظر` بالـرد ع الكليشـة

**⪼** `.اضف كليشة البوت` بالـرد ع الكليشـة لـ اضـافة كليشـة ستـارت

**⪼** `.اضف رمز الوقتي` بالـرد ع رمـز

**⪼** `.اضف زخرفة الوقتي` بالـرد ع ارقـام الزغـرفه

**⪼** `.اضف البايو الوقتي` بالـرد ع البـايـو

**⪼** `.اضف اسم المستخدم` بالـرد ع اسـم

**⪼** `.اضف كروب الرسائل` بالـرد ع ايدي الكـروب

**⪼** `.اضف كروب السجل` بالـرد ع ايدي الكـروب

**⪼** `.اضف ايديي` بالـرد ع ايدي حسـابك

**⪼** `.اضف نقطة الاوامر` بالـرد ع الـرمز الجديـد

**⪼** `.اضف نوم الترحيب` بالـرد ع رقـم الساعة لبداية نوم الترحيب المؤقت

**⪼** `.اضف رسائل` الحماية بالـرد ع رقـم لعدد رسائل تحذيـرات حماية الخاص


**⪼** `.جلب فار` + اسـم الفـار

**⪼** `.حذف فار` + اسـم الفـار

**⪼** `.رفع مطور` بالـرد ع الشخـص لرفعـه مطـور تحكـم كامـل بالاوامـر

**⪼** `.حذف فار المطورين`

**「❖╎قائـمه اوامر تغييـر المنطقـة الزمنيـة للوقـت** 🌐: 

**⪼** `.ضع وقت اليمن` 

**⪼** `.ضع وقت مصر` 

**⪼** `.ضع وقت الامارات` 

**⪼** `.ضع وقت ايران` 

**⪼** `.ضع وقت الجزائر` 

**⪼** `.ضع وقت المغرب` 

**⪼** `.ضع وقت تركيا`

**⪼** `.ضع وقت العراق`

[ 𓆩 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𓆪](https://t.me/YamenThon)""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"contrytime")))
@check_owner
async def _(event):
    await event.edit(
        "[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر فــارات المنطقـه الزمنيـة 🌐](t.me/YamenThon) .\n\n**「❖╎اليك عـزيـزي شـࢪوحـات اوامـر فــارات المنطقـه الزمنيـة :**\n\n",
        buttons=[
            [Button.inline("وقت اليمن", data="yemenvar")],
            [Button.inline("وقت مصر", data="msrvar")],
            [Button.inline("وقت سوريا", data="syriavar")],
            [Button.inline("وقت الـعراق", data="iraqvar")],
            [Button.inline("اوقـات جميـع الدول 🌐", data="kyamio")],
            [Button.inline("رجوع", data="namevar")],
            [Button.inline("رجــوع", data="ZEDHELP")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"symnamvar")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الفــارات](t.me/YamenThon) .
**- الامـر :**
**⪼** `.اضف رمز الوقتي`

**- الوصـف :**
لـ تغيير الرمز الذي يظهر بداية الوقت عندما يكون الاسم الوقتي شغال

**- الاستخـدام :**
بالـرد على اي رمز بالامـر   `.اضف رمز الوقتي`""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"phovarlok")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الفــارات](t.me/YamenThon) .
**- الامـر :**
**⪼** `.اضف صورة الوقتي`

**- الوصـف :**
لوضع صورة لـ حسابك كبروفايل وعليها وقت عند تشغيل الصورة الوقتيه

**- الاستخـدام :**
بالـرد على صورة بالامـر   `.اضف صورة الوقتي`""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"biolokvar")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الفــارات](t.me/YamenThon) .
**- الامـر :**
**⪼** `.اضف البايو`

**- الوصـف :**
لوضع بايو محدد لـ حسابك يشتغل عند تفعيل البايو الوقتي

**- الاستخـدام :**
بالـرد على نص بالامـر   `.اضف البايو`""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"timevar")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الفــارات](t.me/YamenThon) .
**- الامـر :**

**⪼** `.الوقتي 1`
**⪼** `.الوقتي 2`
**⪼** `.الوقتي 3`
**⪼** `.الوقتي 4`
**⪼** `.الوقتي 5`
**⪼** `.الوقتي 6`
**⪼** `.الوقتي 7`
**⪼** `.الوقتي 8`
**⪼** `.الوقتي 9`
**⪼** `.الوقتي 10`
**⪼** `.الوقتي 11`
**⪼** `.الوقتي 12`
**⪼** `.الوقتي 13`
**⪼** `.الوقتي 14`

**- الوصـف :**
هذا الامر يقوم بتغييـر زخرفـة ارقام الاسم الوقتي للعديد من الزخارف حسب اختيارك للامر

**- الاستخـدام :**
فقط ارسـل اي امر من الاوامر اعلاه""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"nameprvr")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الفــارات](t.me/YamenThon) .
**- الامـر :**
**⪼** `تغيير اسمي`

**- الوصـف :**
هذا الامر يقوم بوضع اسم حسابك للعديد من الكلايش مثل امر الفحص والسورس .. الخ

**- الاستخـدام :**
بالـرد على اسمك بالامر   `تغيير اسمي`""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"pmvars")))
@check_owner
async def _(event):
    await event.edit(
        "[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر فــارات حمايـة الخــاص 🛄](t.me/YamenThon) .\n\n**「❖╎اليك عـزيـزي شـࢪوحـات اوامـر فــارات حمايـة الخــاص :**\n\n",
        buttons=[
            [
                Button.inline("صورة الحماية", data="picpmvar"),
                Button.inline("كليشة الحماية", data="pmvarkish"),
            ],
            [
                Button.inline("عدد التحذيرات", data="warnvars"),
            ],
            [Button.inline("رجوع", data="varszed")],
            [Button.inline("رجــوع", data="ZEDHELP")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"warnvars")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الفــارات](t.me/YamenThon) .
**- الامـر :**
**⪼** `.اضف عدد التحذيرات`

**- الوصـف :**
لـ تغييـر عدد تحذيرات امـر حماية الخاص التي يقوم البوت باعطائها للشخص الذي يراسلك خاص قبل حظـره

**- الاستخـدام :**
**بالـرد على عدد بالامـر**   `.اضف عدد التحذيرات`""",
        buttons=[
            [Button.inline("رجوع", data="pmvars")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"pmvarkish")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الفــارات](t.me/YamenThon) .
**- الامـر :**
**⪼** `.اضف كليشة الحماية`

**- الوصـف :**
لـ تغيير الكليشة التي يرد فيهـا البـوت عندما يكون امر الحماية شغال
حيث تعتبـر هاي الكليشـه بمثابـة الـرد الآلـي من البـوت لكـل شخـص يراسلك بالخـاص

**- الاستخـدام :**
**بالـرد على الكليشـه بالامـر**   `.اضف كليشة الحماية`""",
        buttons=[
            [Button.inline("رجوع", data="pmvars")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"picpmvar")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الفــارات](t.me/YamenThon) .
**- الامـر :**
**⪼** `.اضف صورة الحماية`

**- الوصـف :**
لوضع صورة لـ الكليشة التي تظهر عندما يكون امر الحماية شغال ويراسلك احد بالخاص

**- الاستخـدام :**
**بالـرد على صورة بالامـر**   `.اضف صورة الحماية`""",
        buttons=[
            [Button.inline("رجوع", data="pmvars")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"alivevar")))
@check_owner
async def _(event):
    await event.edit(
        "[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر فــارات الفحـص 🏮](t.me/YamenThon) .\n\n**「❖╎اليك عـزيـزي شـࢪوحـات اوامـر فــارات الفحـص :**\n\n",
        buttons=[
            [
                Button.inline("كليشة الفحص", data="kleshalive"),
                Button.inline("رمز الفحص", data="rmzalive"),
            ],
            [Button.inline("صورة الفحص", data="picvars")],
            [Button.inline("رجوع", data="varszed")],
            [Button.inline("رجــوع", data="ZEDHELP")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"picvars")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الفــارات](t.me/YamenThon) .
**- الامـر :**
**⪼** `.اضف صورة الفحص`

**- الوصـف :**
لوضع صورة لـ الكليشة التي تظهر عندما ترسل امر (.فحص) 

**- الاستخـدام :**
بالـرد على صورة بالامـر   `.اضف صورة الفحص`""",
        buttons=[
            [Button.inline("رجوع", data="alivevar")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"kleshalive")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الفــارات](t.me/YamenThon) .
**- الامـر :**
**⪼** `.اضف كليشة الفحص`

**- الوصـف :**
لـ تغيير الكليشة (الكلام) التي تظهر عندما ترسل امر (.فحص)

**- الاستخـدام :**
بالـرد على الكليشـه بالامـر   `.اضف كليشة الفحص`""",
        buttons=[
            [Button.inline("رجوع", data="alivevar")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"rmzalive")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الفــارات](t.me/YamenThon) .
**- الامـر :**
**⪼** `.اضف رمز الفحص`

**- الوصـف :**
لـ تغيير الرمز الذي يظهر عند ارسال الامـر (.فحص)

**- الاستخـدام :**
بالـرد على اي رمز بالامـر   `.اضف رمز الفحص`""",
        buttons=[
            [Button.inline("رجوع", data="alivevar")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"katmvar")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الفــارات](t.me/YamenThon) .
**- الامـر :**
**⪼** `.اضف صورة الكتم`

**- الوصـف :**
لوضع صورة لـ كليشـة الكتم التي تظهر عندما تقوم بكتم احد

**- الاستخـدام :**
بالـرد على صورة بالامـر   `.اضف صورة الكتم`""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    link_preview=False)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"startbotvar")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الفــارات](t.me/YamenThon) .
**- الامـر :**
**⪼** `.اضف صورة البوت`

**- الوصـف :**
لوضع صورة لـ كليشـة الستارت التي تظهر عندما يقوم احد بالدخول للبوت المساعد الخاص بك

**- الاستخـدام :**
بالـرد على صورة بالامـر   `.اضف صورة البوت`""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    link_preview=False)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"rmsavar")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الفــارات](t.me/YamenThon) .
**- الامـر :**
**⪼** `.اضف رمز ايدي`

**- الوصـف :**
لـ تغيير الرمز الذي يظهر بكليشة الايدي عندما تقوم بارسال (.ايدي)

**- الاستخـدام :**
بالـرد على اي رمز بالامـر   `.اضف رمز ايدي`""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    link_preview=False)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"enoanvar")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الفــارات](t.me/YamenThon) .
**- الامـر :**
**⪼** `.اضف عنوان ايدي`

**- الوصـف :**
لـ تغيير العنوان الذي يظهر اعلى كليشة الايدي عندما تقوم بارسال (.ايدي)

**- الاستخـدام :**
بالـرد على اي نص بالامـر   `.اضف عنوان ايدي`""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    link_preview=False)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"katvar")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الفــارات](t.me/YamenThon) .
**- الامـر :**
**⪼** `.اضف خط ايدي`

**- الوصـف :**
لـ تغيير الخط الذي يظهر بكليشة الايدي عندما تقوم بارسال (.ايدي)

**- الاستخـدام :**
بالـرد على اي خط ------ بالامـر   `.اضف خط ايدي`""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"msrvar")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الفــارات](t.me/YamenThon) .
**- الامـر :**
**⪼** `.ضع وقت مصر`

**- الوصـف :**
لـ تغيير المنطقه الزمنيه للاسم والبروفايل الوقتي عندما يكون مفعل بحيث يكون الوقت هو وقت دولة مصـر الحبيبـه توقيت القاهـرة 🇪🇬

**- الاستخـدام :**
فقط ارسـل الامـر   `.ضع وقت مصر`""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"yemenvar")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الفــارات](t.me/YamenThon) .
**- الامـر :**
**⪼** `.ضع وقت اليمن`

**- الوصـف :**
لـ تغيير المنطقه الزمنيه للاسم والبروفايل الوقتي عندما يكون مفعل بحيث يكون الوقت هو وقت دولة اليمن الحبيبـه توقيت صنعاء 🇾🇪

**- الاستخـدام :**
فقط ارسـل الامـر   `.ضع وقت اليمن`""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"kyamio")))
@check_owner
async def _(event):
    await event.edit(
        """   𓆩 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗧𝗶𝗺𝗲 **🝢 المنطقة الزمنية** 𓆪
    **⋆┄─┄─┄─┄─┄─┄─┄─┄⋆**
    **✧ قائمـة اوامر تغييـر المنطقـة الزمنيـة لـ ضبط الوقت ع يـــمنثون حسب توقيت دولتك 🌐:** 
    
    **⪼** `.ضع وقت فلسطين`
    **⪼** `.ضع وقت اليمن`
    **⪼** `.ضع وقت العراق`
    **⪼** `.ضع وقت السعودية`
    **⪼** `.ضع وقت سوريا`
    **⪼** `.ضع وقت الامارات`
    **⪼** `.ضع وقت قطر`
    **⪼** `.ضع وقت الكويت`
    **⪼** `.ضع وقت البحرين`
    **⪼** `.ضع وقت سلطنة عمان`
    **⪼** `.ضع وقت الاردن`
    **⪼** `.ضع وقت لبنان`
    **⪼** `.ضع وقت مصر`
    **⪼** `.ضع وقت السودان`
    **⪼** `.ضع وقت ليبيا`
    **⪼** `.ضع وقت الجزائر`
    **⪼** `.ضع وقت المغرب`
    **⪼** `.ضع وقت تونس`
    **⪼** `.ضع وقت موريتانيا`
    **⪼** `.ضع وقت ايران`
    **⪼** `.ضع وقت تركيا`
    **⪼** `.ضع وقت امريكا`
    **⪼** `.ضع وقت روسيا`
    **⪼** `.ضع وقت ايطاليا`
    **⪼** `.ضع وقت المانيا`
    **⪼** `.ضع وقت فرنسا`
    **⪼** `.ضع وقت اسبانيا`
    **⪼** `.ضع وقت بريطانيا`
    **⪼** `.ضع وقت بلجيكا`
    **⪼** `.ضع وقت النرويج`
    **⪼** `.ضع وقت الصين`
    **⪼** `.ضع وقت اليابان`
    **⪼** `.ضع وقت الهند`
    **⪼** `.ضع وقت اندنوسيا`
    **⪼** `.ضع وقت ماليزيا`
    
    "**🛃 اذا لم تجد دولتك .. قم بالبحث عن اقرب دوله لها**
    "𓆩 [𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗩𝗮𝗿𝘀 - قنـاة الفـارات](t.me/YamenThon_vars) 𓆪""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"syriavar")))
@check_owner
async def _(event):
  await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الفــارات](t.me/YamenThon) .
**- الامـر :**
**⪼** `.ضع وقت سوريا`

**- الوصـف :**
لـ تغيير المنطقه الزمنيه للاسم والبروفايل الوقتي عندما يكون مفعل بحيث يكون الوقت هو وقت دولة سوريا الحبيبـه توقيت دمشق 

**- الاستخـدام :**
فقط ارسـل الامـر   `.ضع وقت سوريا`""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"timavar")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الفــارات](t.me/YamenThon) .
**- الامـر :**

**⪼** `.وقتيه 1`
**⪼** `.وقتيه 2`
**⪼** `.وقتيه 3`
**⪼** `.وقتيه 4`
**⪼** `.وقتيه 5`
**⪼** `.وقتيه 6`
**⪼** `.وقتيه 7`
**⪼** `.وقتيه 8`
**⪼** `.وقتيه 9`
**⪼** `.وقتيه 10`
**⪼** `.وقتيه 11`
**⪼** `.وقتيه 12`
**⪼** `.وقتيه 13`
**⪼** `.وقتيه 14`
**⪼** `.وقتيه 15`
**⪼** `.وقتيه 16`
**⪼** `.وقتيه 17`

**- الوصـف :**
لـ تغييـر زخرفـة ارقام الوقت الذي يظهر على البروفايل الوقتي اثناء تفعيلها للعديد من الزخارف حسب اختيارك للامر

**- الاستخـدام :**
فقط ارسـل اي امر من الاوامر اعلاه

**- ملاحظـه :**
لرؤية زخارف الصورة الوقتيه بالترتيب ع حسب الرقم 
https://t.me/YamenThon_vars/20""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"pointvar")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الفــارات](t.me/YamenThon) .
**- الامـر :**
**⪼** `.اضف نقطة الاوامر`

**- الوصـف :**
لـ تغيير النقطه التي ترسلها بداية اي امر لتنفيذه الى اي رمز اخر تريده

**- الاستخـدام :**
بالـرد على اي رمز بالامـر   `.اضف نقطة الاوامر`""",
        buttons=[
            [Button.inline("رجوع", data="namevar")],
        ],
    link_preview=False)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"zdownload")))
@check_owner
async def zed_help(event):
    zelzal = "⤶ عـذراً عـزيـزي 🤷🏻‍♀\n⤶ هـذه اللوحه لا تشتغل في الخاص\n⤶ لـ إظهـار لوحـة المسـاعـدة 👇\n\n⤶ ارســل (.مساعده) في اي مجمـوعـه"
    try:
        await event.edit(
            "[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البحـث والتحميــل 🛰](t.me/YamenThon) .\n\n**「❖╎اليك عـزيـزي شـࢪوحـات اوامـر البحث والتحميـل من جميـع مواقـع الـ سوشـل ميديـا :**\n\n",
            buttons=[
                [
                    Button.inline("بحث اوقـات الصـلاة 🕋", data="aseqalsamt"),
                ],
                [
                    Button.inline("فيديو", data="vedzed"),
                    Button.inline("ستوري تلي💖", data="yyamm"),
                    Button.inline("بحث", data="songzed"),
                ],
                [
                    Button.inline("بحث انلايـن", data="youini"),
                ],
                [
                    Button.inline("تحميل صوت", data="downsou"),
                    Button.inline("تحميل فيديو", data="downved"),
                ],
                [
                    Button.inline("بحث بـ الصوت", data="shazam"),
                ],
                [
                    Button.inline("متحركات", data="giff"),
                    Button.inline("ملصقات", data="stickkers"),
                    Button.inline("صور", data="pictures"),
                ],
                [
                    Button.inline("يوتيوب", data="youtubb"),
                    Button.inline("ساوند كلود", data="soundcloud"),
                ],
                [
                    Button.inline("انستا", data="insta"),
                    Button.inline("بنترست", data="pentrist"),
                ],
                [
                    Button.inline("لايكي", data="likee"),
                    Button.inline("تيك توك", data="tiktok"),
                ],
                [
                    Button.inline("فيس بوك", data="facebook"),
                    Button.inline("تويتر", data="tweter"),
                ],
                [Button.inline("سناب شات", data="snapchat")],
                [Button.inline("رجوع", data="ZEDHELP")],
            ],
        link_preview=False)
    except Exception:
        await event.answer(zelzal, cache_time=0, alert=True)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"songzed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البحـث والتحميــل 🛰](t.me/YamenThon) .
**- الامـر :**
**⪼** `.بحث`
**⪼** `.اغنيه`

**- الوصـف :**
لـ البحث وتحميـل الاغاني والمقاطـع الصوتيـه من يوتيـوب

**- الاستخـدام :**
`.بحث` + اسـم الاغنيـه

**- مثـال :**
`.بحث Lonley Slowd+Reverb`""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"aseqalsamt")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البحـث اوقـات الصـلاة 🛰](t.me/YamenThon) .
**- اوقـات الصـلاة لـ عواصـم الـدول العـربيـة🕋 :**

**⪼** الامـر -

**⪼** `.صلاة`  + العاصمـه

**- الوصـف :**
لـ البحث عن اوقـات الصـلاة 🕋

**- الاستخـدام :**
`.صلاة` + اسـم العاصمـه 

**- مثـال :**
`.صلاة صنعاء`""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"yyamm")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البحـث والتحميــل 🛰](t.me/YamenThon) .
**- الامـر :**
**⪼** `.ستوري`

**⪼** الاستخـدام برد على الشخص الذي تريد تحميل الاستوري الخاص به
او ارسال الامر معا يوزر الشخص  مثـال `.ستوري @T_A_Tl` 💌💯 خاص بتحميل ستوريات التلي فقط""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"vedzed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البحـث والتحميــل 🛰](t.me/YamenThon) .
**- الامـر :**
**⪼** `.فيديو`

**- الوصـف :**
لـ البحث وتحميـل مقاطـع الفيديـو مـن اليوتيـوب

**- الاستخـدام :**
`.فيديو` + اسـم المقطـع

**- مثـال :**
`.فيديو حسين الجسمي احبك`""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"youini")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البحـث والتحميــل 🛰](t.me/YamenThon) .
**- الامـر :**
**⪼** `.يوت`

**- الوصـف :**
لـ البحث وتحميـل مقاطـع الصـوت والفيديـو
والافـلام والمسلسلات مـن يوتيـوب
بعـدة صيـغ عبـر لوحـة انلايـن شفافـه

هذا الامر يدعم تحميل مقاطع صوت وفيديو عالية الدقه
تصـل الى 5 جيجابايت وبسرعه تحميـل عاليـه

**- ملاحظـه :**
اللوحـه تشتغل فقط في المجموعات وليس في الخاص ⚠️
للبحث عن الاغاني في الخاص
استخدم امر (.بحث) او (.فيديو)

**- الاستخـدام :**
`.يوت` + اسـم المقطع او الاغنيه
`.يوت` بالـرد على رابـط

**- مثـال :**
`.يوت Lonely Slowd+Reverb`""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"downsou")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البحـث والتحميــل 🛰](t.me/YamenThon) .
**- الامـر :**
**⪼** `.تحميل صوت`

**- الوصـف :**
لـ تحميـل المقـاطع الصـوتيه من يوتيـوب عبر الرابـط

**- الاستخـدام :**
`.تحميل صوت` + رابـط
`.تحميل صوت` بالـرد ع رابـط""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"downved")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البحـث والتحميــل 🛰](t.me/YamenThon) .
**- الامـر :**
**⪼** `.تحميل فيديو`

**- الوصـف :**
لـ تحميـل مقـاطع الفيديـو من يوتيـوب عبر الرابـط

**- الاستخـدام :**
`.تحميل فيديو` + رابـط
`.تحميل فيديو` بالـرد ع رابـط""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"shazam")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البحـث والتحميــل 🛰](t.me/YamenThon) .
**- الامـر :**
**⪼** `.ابحث`

**- الوصـف :**
لـ البحث بالصوت عبر Shazam عن مصـادر الاغـاني والمقاطـع الصوتيـه
حيث يقوم بجلب اسم الفنلن وصورته ورابـط المقطـع
هذا الامر يفيدك اذا كنت تبحث عن اغنيه او موسيقى لا تعرف اسمهـا

**- الاستخـدام :**
`.ابحث` **بالـرد ع بصمـه او تسجيل صوتي**""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"giff")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البحـث والتحميــل 🛰](t.me/YamenThon) .
**- الامـر :**
**⪼** `.متحركه`

**- الوصـف :**
لـ تحميـل صـور متحركـه من جـوجـل ..

**- الاستخـدام :**
`.متحركه` + كلمـه""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"stickkers")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البحـث والتحميــل 🛰](t.me/YamenThon) .
**- الامـر :**
**⪼** `.ملصقات`

**- الوصـف :**
لـ البحث عـن حـزم الملصقـات علـى تيليجـرام ..

**- ملاحظـه :**
الامـر يقبـل بحث عـربي + انكلـش

**- الاستخـدام :**
`.ملصقات` + كلمـه

**- مثــال :**
`.ملصقات احمد البشير`""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"pictures")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البحـث والتحميــل 🛰](t.me/YamenThon) .
**- الامـر :**
**⪼** `.صور`

**- الوصـف :**
لـ البحث وتحميـل الصـور والخلفيـات من جـوجـل بدقـه HD ..

**- ملاحظـه :**
هـذا الامـر حصـري فقط وخاص بـ سـورس يـــمنثون بقية السورسات ماتحمـل دقـة HD ؟!

**- الاستخـدام :**
`.صور` + كلمـه

**- مثــال :**
`.صور حسن نصرالله`""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"youtubb")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البحـث والتحميــل 🛰](t.me/YamenThon) .
**- الامـر :**
**⪼** `.يوتيوب`

**- الوصـف :**
لـ البحـث عـن روابــط بالكلمــه المحــدده علـى يـوتيــوب

**- ملاحظـه :**
هذا الامر فقط يجلب لك نتائج بحث عن كلمـه على يوتيوب ولا يقم بتحميل المطلوب

**- الاستخـدام :**
`.يوتيوب` + كلمـه
`.يوتيوب` + عـدد + كلمـه""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"soundcloud")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البحـث والتحميــل 🛰](t.me/YamenThon) .
**- الامـر :**
**⪼** `.ساوند`

**- الوصـف :**
لـ تحميـل الاغـاني مـن سـاونـد كـلـود عـبر الرابـط

**- الاستخـدام :**
`.ساوند` + رابـط
`.ساوند` بالـرد ع رابـط""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"insta")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البحـث والتحميــل 🛰](t.me/YamenThon) .
**- الامـر :**
**⪼** `.انستا`
`.تحميل صوت`
`.تحميل فيديو`

**- الوصـف :**
لـ تحميـل الصـور ومقاطـع الصـوت والفيديـو والستوريـات مـن انستجـرام عبر الرابـط

**- الاستخـدام :**
`.انستا` + رابـط
`.انستا` بالـرد ع رابـط""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"pentrist")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البحـث والتحميــل 🛰](t.me/YamenThon) .
**- الامـر :**
**⪼** `.بنترست`

**- الوصـف :**
لـ تحميـل الصــور ومقـاطـع الفيـديـو مـن بنتـرسـت عـبر الرابـط

**- الاستخـدام :**
`.بنترست` + رابـط""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"likee")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البحـث والتحميــل 🛰](t.me/YamenThon) .
**- الامـر :**
**⪼** `.لايكي`

**- الوصـف :**
لـ تحميـل مقـاطـع الفيـديــو مـن لايكـي عـبر الرابـط

**- الاستخـدام :**
`.لايكي` + رابـط
`.لايكي` + بالـرد ع رابـط""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"tiktok")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البحـث والتحميــل 🛰](t.me/YamenThon) .
**- الامـر :**
**⪼** `.تيك`

**- الوصـف :**
لـ تحميـل مقـاطـع الفيـديــو مـن تيـك تـوك عـبر الرابـط

**- الاستخـدام :**
`.تيك` + رابـط
`.تيك` + بالـرد ع رابـط""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"facebook")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البحـث والتحميــل 🛰](t.me/YamenThon) .
**- الامـر :**
**⪼** `.فيس`

**- الوصـف :**
لـ تحميـل مقـاطـع الفيـديــو مـن فيس بـوك عـبر الرابـط

**- الاستخـدام :**
`.فيس` **+ رابـط او بالـرد ع رابـط**""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"tweter")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البحـث والتحميــل 🛰](t.me/YamenThon) .
**- الامـر :**
**⪼** `.تويتر`

**- الوصـف :**
لـ تحميـل مقاطـع الفيديـو من تويتـر عبـر الرابـط

**- الاستخـدام :**
`.تويتر` + رابـط
`.تويتر` + بالـرد ع رابـط""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"snapchat")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر البحـث والتحميــل 🛰](t.me/YamenThon) .
**- الامـر :**
**⪼** `.سناب`

**- الوصـف :**
لـ تحميـل مقاطـع الفيديـو من سنـاب شـات عبـر الرابـط

**- الاستخـدام :**
`.سناب` + رابـط
`.سناب` + بالـرد ع رابـط""",
        buttons=[
            [Button.inline("رجوع", data="zdownload")],
        ],
    link_preview=False)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"funzed")))
@check_owner
async def _(event):
    zelzal = "⤶ عـذراً عـزيـزي 🤷🏻‍♀\n⤶ هـذه اللوحه لا تشتغل في الخاص\n⤶ لـ إظهـار لوحـة المسـاعـدة 👇\n\n⤶ ارســل (.مساعده) في اي مجمـوعـه"
    try:
        await event.edit(
            "[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر التسليـه والتحشيش 🏂🎃](t.me/YamenThon) .\n\n**「❖╎اليك عـزيـزي شـࢪوحـات اوامـر التسليـه والتحشيش :**\n\n",
            buttons=[
                [
                    Button.inline("اوامــر تسليـه متحركـه", data="fun1zed"),
                ],
                [
                    Button.inline("اوامــر تسليـه جديـدة", data="fun2zed"),
                ],
                [
                    Button.inline("اوامــر التحـشيش", data="fun3zed"),
                ],
                [
                    Button.inline("اوامــر الالعــاب", data="fun4zed"),
                ],
                [Button.inline("رجــوع", data="ZEDHELP")],
            ],
        link_preview=False)
    except Exception:
        await event.answer(zelzal, cache_time=0, alert=True)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"fun1zed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر التسليـه 🏂](t.me/YamenThon) .
**⪼** `.تسليه1`
**⪼** `.تسليه2`
**⪼** `.تسليه3`
**⪼** `.تسليه4`
**⪼** `.تسليه5`
**⪼** `.تسليه6`
**⪼** `.تسليه7`
**⪼** `.تسليه8`
**⪼** `.تسليه9`
**⪼** `.تسليه10`
**⪼** `.تهكير`

**- الوصـف :**
اكثـر من 70 امـر تسليـه متحركـه للترفيـه والمـرح فقـط

**- الاستخـدام :**
فقط ارسـل اي امـر من الاوامـر اعـلاه وانسـخ الامـر

**- ملاحظـه :**
لا تقم بتكرار هذه الاوامـر او استخدامهـا بكثـره حتى لا يحدث تعليق لحسابك""",
        buttons=[
            [Button.inline("رجوع", data="funzed")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"fun2zed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر التسليـه ⛹🏻‍♀](t.me/YamenThon) .
**- الامـر :**
**⪼** `.حيوان`
**⪼** `.زاحف`
**⪼** `.مشهور`
**⪼** `.مشهوره`
**⪼** `.معاني`
**⪼** `.كت`
**⪼** `.اوصف`
**⪼** `.هينه`
**⪼** `.نسبه الحب`
**⪼** `.نسبه الانوثه`
**⪼** `.نسبه الغباء`
**⪼** `.نسبه الانحراف`
**⪼** `.نسبه المثليه`
**⪼** `.نسبه النجاح`
**⪼** `.نسبه الكراهيه`


**- الوصـف :**
اوامـر تسليـه جديـدة ممطـروقـه للترفيـه والمـرح فقـط

**- الاستخـدام :**
فقط ارسـل اي امـر من الاوامـر اعـلاه كالتالي :

.الامر بالـرد ع الشخـص
.الامر +معـرف او ايـدي الشخـص

او بالنسبه للنسب ارسـل :
الامر + اسم + اسم

**- ملاحظـه :**
يتم اضافة المزيد من اوامـر التسليه بالتحديثات الجايه""",
        buttons=[
            [Button.inline("رجوع", data="funzed")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"fun3zed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر التحشيش 🎃](t.me/YamenThon) .
**- الامـر :**
**⪼** `.رفع تاج`
**⪼** `.رفع بقلبي`
**⪼** `.رفع مرتي`
**⪼** `.رفع صاك`
**⪼** `.رفع صاكه`
**⪼** `.رفع حات`
**⪼** `.رفع حاته`
**⪼** `.رفع ورع`
**⪼** `.رفع مزه`
**⪼** `.رفع مرتبط`
**⪼** `.رفع مرتبطه`
**⪼** `.رفع حبيبي`
**⪼** `.رفع خطيبتي`
**⪼** `.رفع جلب`
**⪼** `.رفع جريذي`
**⪼** `.رفع فرخ`
**⪼** `.رفع مطي`
**⪼** `.رفع حمار`
**⪼** `.رفع خروف`
**⪼** `.رفع حيوان`
**⪼** `.رفع بزون`
**⪼** `.رفع زباله`
**⪼** `.رفع منشئ`
**⪼** `.رفع مدير`
**⪼** `.رفع كواد`

**- الوصـف :**
اوامـر تحشيش للترفيـه والمـرح فقـط

**- الاستخـدام :**
فقط ارسـل اي امـر من الاوامـر اعـلاه كالتالي :

.الامر بالـرد ع الشخـص
.الامر +معـرف او ايـدي الشخـص

**- ملاحظـه :**
يتم اضافة المزيد من اوامـر التحشيش بالتحديثات الجايه""",
        buttons=[
            [Button.inline("رجوع", data="funzed")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"fun4zed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الالـعــاب 🎮🎳](t.me/YamenThon) .
**- الامـر :**
**⪼** `.بلاي`
**العــاب الانـلايـن لســورس يـــمنثون 🕹**
**⪼** `.كت`
**اسئلـة كـت تـويت ⁉️**
**⪼** `.احكام`
**لعبــة احكــام الشهيــرة ⚖👩🏻‍⚖**
**⪼** `.عقاب`
**لعبــة عقــاب ⛓**
**⪼** `.اكس او`
**لعبــة اكـس او 🧩**
**⪼** `.نرد`
**لعبــة رمـي النــرد 🎲**
**⪼** `.سهم`
**لعبــة رمـي السهــم 🎯**
**⪼** `.سله`
**لعبــة كــرة السلــة 🏀**
**⪼** `.كرة`
**- لعبــة كــرة القــدم ⚽️**
**⪼** `.حظ`
**لعبــة الحــظ 🎰**
**⪼** `.اكينوتر`
**لعبــة اسئلـه انلايـن ⁉️**
**⪼** `.خيرني`
**لعبــة لـو خيـروك بالصـور ⁉️🌉**
**⪼** `.تويت`
**- لعبــة كـت تـويت بالصـور ⁉️🌁**


**- الوصـف :**
العـاب سـورس يـــمنثون ممطـروقـه 🥳💞

**- ملاحظـه :**
سيتـم اضـافــة المـزيــد من الالعــاب بالتحديثــات الجــايـه 🎭

**- الاستخـدام :**
فقط ارسـل اي امـر من الاوامـر اعـلاه""",
        buttons=[
            [Button.inline("رجوع", data="funzed")],
        ],
    link_preview=False)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"acccount")))
@check_owner
async def zed_help(event):
    zelzal = "⤶ عـذراً عـزيـزي 🤷🏻‍♀\n⤶ هـذه اللوحه لا تشتغل في الخاص\n⤶ لـ إظهـار لوحـة المسـاعـدة 👇\n\n⤶ ارســل (.مساعده) في اي مجمـوعـه"
    try:
        await event.edit(
            "[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الحســاب 🚹](t.me/YamenThon) .\n\n**「❖╎اليك عـزيـزي شـࢪوحـات الاوامـر المتعلقـه بالحسـاب :**\n\n",
            buttons=[
                [
                    Button.inline("البايو الوقتي", data="biome"),
                    Button.inline("الاسم الوقتي", data="namme"),
                ],
                [
                    Button.inline("الصورة الوقتيه", data="picme"),
                ],
                [
                    Button.inline("قنواتي", data="channelme"),
                    Button.inline("كروباتي", data="groubme"),
                ],
                [
                    Button.inline("حماية الخاص", data="pmme"),
                ],
                [
                    Button.inline("رجـوع", data="ZEDHELP"),
                    Button.inline("التالـي", data="nextacc"),
                ],
            ],
        link_preview=False)
    except Exception:
        await event.answer(zelzal, cache_time=0, alert=True)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"nextacc")))
@check_owner
async def zed_help(event):
    await event.edit(
        "[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الحســاب 🚹](t.me/YamenThon) .\n\n**「❖╎اليك عـزيـزي شـࢪوحـات الاوامـر المتعلقـه بالحسـاب :**\n\n",
        buttons=[
            [
                Button.inline("احصائياتي", data="infome"),
                Button.inline("الكشف", data="whome"),
            ],
            [
                Button.inline("التخزين", data="logme"),
            ],
            [
                Button.inline("الكتم", data="mutme"),
                Button.inline("الحظر", data="banme"),
            ],
            [Button.inline("سجل الاسماء", data="whonam")],
            [
                Button.inline("رجـوع", data="ZEDHELP"),
                Button.inline("التالـي", data="next2acc"),
            ],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"next2acc")))
@check_owner
async def zed_help(event):
    await event.edit(
        "[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الحســاب 🚹](t.me/YamenThon) .\n\n**「❖╎اليك عـزيـزي شـࢪوحـات الاوامـر المتعلقـه بالحسـاب :**\n\n",
        buttons=[
            [
                Button.inline("الازعاج", data="echozed"),
                Button.inline("الانتحال", data="enthalzed"),
            ],
            [
                Button.inline("الاذاعــة", data="gozzz"),
            ],
            [
                Button.inline("الحاظرهم", data="banzzz"),
                Button.inline("حذف دردشة", data="delzzz"),
            ],
            [
                Button.inline("رجـوع", data="ZEDHELP"),
            ],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"echozed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الحســاب 🚹](t.me/YamenThon) .
**- الامـر :**
**⪼** `.ازعاج`
**⪼** `.الغاء ازعاج`
**⪼** `.تقليد`
**⪼** `.الغاء تقليد`
**⪼** `.المقلدهم`
**⪼** `.حذف المقلدهم`

**- الوصـف :**
لـ ازعاج شخص حيث يظل حسابك يكرر نفس كلام الشخص تماماً كالببغاء 🦜😹

**- الاستخـدام :**
`.ازعاج` **بالـرد ع شخـص**
`.الغاء ازعاج` **بالـرد ع شخـص**

بقيـة الاوامـر في الاعلـى""",
        buttons=[
            [Button.inline("رجوع", data="next2acc")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"enthalzed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الحســاب 🚹](t.me/YamenThon) .
**- الامـر :**
**⪼** `.انتحال`
**⪼** `.اعاده`

**- الوصـف :**
لـ انتحـال حساب شخص حيث يصبح حسابك منتحل الشخص من حيث الاسم والبروفايل والبايو
يستخدم للتمويه فقط🥷😹

**- الاستخـدام :**
`.انتحال` **بالـرد ع شخـص لـ انتحالـه**
`.اعاده` **بالـرد ع شخـص لـ الغـاء انتحالـه**""",
        buttons=[
            [Button.inline("رجوع", data="next2acc")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"gozzz")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الحســاب 🚹](t.me/YamenThon) .
**- الامـر :**
**⪼** `.للكروبات`
**⪼** `.للخاص`
**⪼** `.خاص`

**- الوصـف :**
(.للكروبات) لـ اذاعة رسـالتك لجميـع المجموعات التي في حسابك

(.للخاص) لـ اذاعة رسـالتك لجميـع الاشخـاص الذين لديك خاص معهم

(.خاص) لـ ارسـال رسـالة لشخـص بدون الدخول للخاص

**- الاستخـدام :**
`.للكروبات` **بالـرد ع رسـاله**
`.للخاص` **بالـرد ع رسـاله**
`.خاص` **+ معـرف الشخص + الرسـاله**""",
        buttons=[
            [Button.inline("رجوع", data="next2acc")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"banzzz")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الحســاب 🚹](t.me/YamenThon) .
**- الامـر :**
**⪼** `.الحاظرهم`

**- الوصـف :**
لـ جلب قائمـة بجميـع الاشخـاص الذين قمت بحظرهم من خاصك

**- الاستخـدام :**
`.الحاظرهم`""",
        buttons=[
            [Button.inline("رجوع", data="next2acc")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"delzzz")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الحســاب 🚹](t.me/YamenThon) .
**- الامـر :**
**⪼** `.احذف`

**- الوصـف :**
لـ حذف الدردشـة مع اي شخص من الطـرفين بالخـاص

**- الاستخـدام :**
`.احذف` **+معـرف الشخـص**""",
        buttons=[
            [Button.inline("رجوع", data="next2acc")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"biome")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الحســاب 🚹](t.me/YamenThon) .
**- الامـر :**
**⪼** `.بايو وقتي`

**- الوصـف :**
لـ إضافة وقت او ساعة رقميه على نبذتك الخاصه

**- الاستخـدام :**
**اولاً قم باضافة فار البايو عبر الامر :**
`.اضف البايو` بالـرد ع النص الذي تريده نبذه لك

**ثانياً قم بتشغيل النبذه الوقتيه عبر الامر :**
`.بايو وقتي`

**- ملاحظـه :**
**لـ ايقاف البايو الوقتي قم بارسال الامر التالي :**
`.انهاء البايو`""",
        buttons=[
            [Button.inline("رجوع", data="acccount")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"namme")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الحســاب 🚹](t.me/YamenThon) .
**- الامـر :**
**⪼** `.اسم وقتي`

**- الوصـف :**
لـ إضافة وقت او ساعة رقميه بجانب اسم حسابك تيليجرام

**- الاستخـدام :**
**اولاً قم بتشغيل الاسم الوقتي عبر الامر :**
`.اسم وقتي`

**ثانياً قم بالذهاب ل اعدادات حسابك تيليجرام
سوف تلاحظ الوقت بالخانه الاولى للاسم
قم بادراج اسمك بالخانه الثانيه ليظهر بجانب الوقت**

**- ملاحظـه :**
**لـ ايقاف الاسم الوقتي قم بارسال الامر التالي :**
`.انهاء الاسم`""",
        buttons=[
            [Button.inline("رجوع", data="acccount")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"picme")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الحســاب 🚹](t.me/YamenThon) .
**- الامـر :**
**⪼** `.صوره وقتيه`

**- الوصـف :**
لـ إضافة وقت او ساعة رقميه على صورة حسابك تيليجرام

**- الاستخـدام :**
**اولاً قم باضافة فار الصورة عبر الامر :**
`.اضف صورة الوقتي` بالـرد ع الصورة التي تريدها صورة لحسابك

**ثانياً قم بتشغيل الصورة الوقتيه عبر الامر :**
`.صوره وقتيه`

**- ملاحظـه :**
**لـ ايقاف الصورة الوقتيه قم بارسال الامر التالي :**
`.انهاء البروفايل`""",
        buttons=[
            [Button.inline("رجوع", data="acccount")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"channelme")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الحســاب 🚹](t.me/YamenThon) .
**- الامـر :**
**⪼** `.قنواتي ادمن`
**⪼** `.قنواتي مالك`
**⪼** `.قنواتي الكل`

**➼➼➼➼➼➼➼➼➼➼**
**⪼** `.مغادره القنوات`
🔮**الوصـف لمغادرة جميع القنوات التي في حسابك و تبقى فقط القنوات التي انت مالكها او مشرف بها**
**➼➼➼➼➼➼➼➼➼➼**

**- الوصـف :**
لـ جلب قائمـه فيها كل القنوات التي انت مشترك فيها على حسب الامر
كمثال الامر (.قنواتي ادمن) يقوم بجلب قائمه فيها كل اسماء القنوات التي انت ادمن فيها فقط وهكـذا لبقية الاوامر

**- الاستخـدام :**
**ارسـل احد الاوامـر ادناه**
`.قنواتي ادمن`
`.قنواتي مالك`
`.قنواتي الكل`""",
        buttons=[
            [Button.inline("رجوع", data="acccount")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"groubme")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الحســاب 🚹](t.me/YamenThon) .
**- الامـر :**
**⪼** `.كروباتي ادمن`
**⪼** `.كروباتي مالك`
**⪼** `.كروباتي الكل`

**➼➼➼➼➼➼➼➼➼➼**
**⪼** `.مغادره المجموعات`
🔮**الوصـف لمغادرة جميع المجموعات التي في حسابك و تبقى فقط المجموعات التي انت مالكها او مشرف بها**
**➼➼➼➼➼➼➼➼➼➼**

**- الوصـف :**
لـ جلب قائمـه فيها كل المجموعات التي انت مشترك فيها على حسب الامر
كمثال الامر (.كروباتي ادمن) يقوم بجلب قائمه فيها كل اسماء المجموعات التي انت ادمن فيها فقط وهكـذا لبقية الاوامر

**- الاستخـدام :**
**ارسـل احد الاوامـر ادناه**
`.كروباتي ادمن`
`.كروباتي مالك`
`.كروباتي الكل`""",
        buttons=[
            [Button.inline("رجوع", data="acccount")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"pmme")))
@check_owner
async def _(event):
    await event.edit(
        "[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الحســاب 🚹](t.me/YamenThon) .\n\n**「❖╎اليك عـزيـزي شـࢪوحـات اوامـر البحث والتحميـل من جميـع مواقـع الـ سوشـل ميديـا :**\n\n",
        buttons=[
            [
                Button.inline("اوامر حماية الخاص", data="pmcmd"),
            ],
            [
                Button.inline("فارات حماية الخاص", data="pmvar"),
            ],
            [Button.inline("رجوع", data="acccount")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"pmcmd")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر حمـايــة الخــاص 🛡](t.me/YamenThon) .
**⪼** `.الحمايه تفعيل`
**لـ تفعيـل حمايـة الخـاص لـ حسـابك**

**⪼** `.الحمايه تعطيل`
**لـ تعطيـل حمايـة الخـاص لـ حسـابك**

**⪼** `.قبول`
**لـ السمـاح لـ الشخـص بـ ارسـال رسـائل الخـاص اثنـاء تفعيـل حمـاية الخـاص بحسـابك بـدون تحـذير**

**⪼** `.رفض`
**لـ رفـض الشخـص من ارسـال رسـائل الخـاص اثنـاء تفعيـل حمـاية الخـاص بحسـابك**

**⪼** `.مرفوض`
**لـ حظـر الشخـص من الخـاص دون تحـذير**

**⪼** `.المقبولين`
**لـ عـرض قائمـة بالاشخـاص المقبـولين**

**⪼** `.بلوك`
**لـ حظـر شخـص من التكلم معـاك خـاص**

**⪼** `.الغاء بلوك`
**لـ الغـاء حظـر شخـص محظـور من الخـاص**


**- الوصـف :**
 حماية الخـاص هي عبـارة عن رد آلي تلقائي من البوت
لكل شخص يراسلك خاص في حال غيابك او انشغـالك لعـدم الـرد
عنـدما تكون حمايـة الخـاص مفعلـه عبـر الامـر (`.الحمايه تفعيل`) ..
حيث يقوم البوت بالرد الآلي ع الاشخاص اليراسلونك خاص
واعطائهم تحذيرات بعدم تكرار الرسائل والانتظار لك
والا يتم حظرهم اذا تجاوزو عدد التحذيرات

**- الاستخـدام :**
ارسـل اولاً
`.الحمايه تفعيل`
لتفعيـل الحمايـة والـرد الآلـي للبـوت بالخـاص

بقية الاوامـر مع شـرح كل أمـر في الاعلـى""",
        buttons=[
            [Button.inline("رجوع", data="acccount")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"pmvar")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - فــارات حمـايــة الخــاص 🛡](t.me/YamenThon) .
**⪼** `.اضف عدد التحذيرات`
**لـ تغييـر عدد تحذيرات امـر حماية الخاص التي يقوم البوت باعطائها للشخص الذي يراسلك خاص قبل حظـره**

**⪼** `.اضف كليشة الحماية`
**لـ تغيير الكليشة التي يرد فيهـا البـوت عندما يكون امر الحماية شغال
حيث تعتبـر هاي الكليشـه بمثابـة الـرد الآلـي من البـوت لكـل شخـص يراسلك بالخـاص**

**⪼** `.اضف صورة الحماية`
**لـ وضع صورة لـ الكليشة التي تظهر عندما يكون امر حماية الخاص شغال
حيث تظهـر هذه الصورة وتحتهـا كليشة الكلام عندما يراسلك احد بالخاص**


**- الوصـف :**
لـ تخصيص وتغييـر ملحقـات حماية الخاص من عدد تحذيرات وكليشـه وصـورة على حسب اختيارك انت ..

**- الاستخـدام :**
**بالـرد على عدد بالامـر**   `.اضف عدد التحذيرات`

**بالـرد على الكليشـه بالامـر**   `.اضف كليشة الحماية`

**بالـرد على صورة بالامـر**   `.اضف صورة الحماية`""",
        buttons=[
            [Button.inline("رجوع", data="acccount")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"infome")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الحســاب 🚹](t.me/YamenThon) .
**- الامـر :**
**⪼** `.احصائياتي`

**- الوصـف :**
لـ جلب قائمـه بـ احصائيات دردشـات حسابك من قنوات ومجموعات وبوتات .. الخ

**- الاستخـدام :**
**ارسـل** `.احصائياتي`""",
        buttons=[
            [Button.inline("رجوع", data="nextacc")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"whome")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الحســاب 🚹](t.me/YamenThon) .
**- الامـر :**
**⪼** `.ايدي`
**⪼** `.ا`
**⪼** `.ايديي`
**⪼** `.الايدي`
**⪼** `.اسمه`
**⪼** `.صورته`
**⪼** `.صورته الكل`

**- الوصـف :**
لـ عرض معلومات حسابك او حساب احد غيرك من ايدي وصورة ومعـرف وبايو ورتبـه
يشبه تمام امر (ايدي) في بوتات الحماية

**- الاستخـدام :**
**لجلب معلومات حسابك ارسـل فقط** 
`.ايدي`

**لجلب او الكشف عن شخص آخر ارسـل**
`.ايدي` **بالـرد ع الشخـص**
`.ايدي` **+ معـرف او ايـدي الشخص**

**لجلب ايديك فقـط ارسـل**
`.ايديي`

**لجلب اسـم شخص ارسـل**
`.اسمه` **بالـرد ع الشخـص**

**لجلب بروفايـلات شخص ارسـل**
`.صورته` **بالـرد ع الشخـص**
`.صورته الكل` **بالـرد ع الشخـص لجلب جميع برفايلاته**

**لجلب ايدي شخص او مجموعة او قناة ارسـل**
`.الايدي` **بالـرد ع الشخـص**
`.الايدي` **داخـل المجموعـة او القنـاة**""",
        buttons=[
            [Button.inline("رجوع", data="nextacc")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"logme")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الحســاب 🚹](t.me/YamenThon) .
**- الامـر :**
**⪼** `.تخزين الخاص تعطيل`
**⪼** `.تخزين الخاص تفعيل`
**⪼** `.تخزين الكروبات تعطيل`
**⪼** `.تخزين الكروبات تفعيل`

**- الوصـف :**
**اولاً تخزين الخاص :**
لـ تفعيل او تعطيل تخـزين جميـع رسـائل الخـاص بـ كـروب التخـزين
هذا الامر يحتاجه الكثيرين مثلا عندما يأتي شخص لمراسلتك خاص وانت مو موجود ثم يقوم بحذف المحادثه البوت يكون قد اخذ توجيهات من هذه الرسائل لتخزينها بكروب التخزين الخاص بك
طبعا هذا الامر بعد التنصيب يكون مفعل تلقائياً
**ثانياً تخزين الكروبات :**
لـ تفعيل او تعطيل تخـزين جميـع تاكـات الكـروبات بـ كـروب التخـزين
هذا الامر يحتاجه الكثيرين مثلا عندما يقوم شخص باحد المجموعات التي انت موجود فيها بالرد ع رسائلك في المجموعه وانت مو موجود يقوم البوت بمعل اشعار لك بالرساله او الرسائل وتخزينها بكروب التخزين الخاص بك
طبعا هذا الامر بعد التنصيب يكون مفعل تلقائياً

**- الاستخـدام :**
قم بـ ارسـال احد الاوامـر اعـلاه""",
        buttons=[
            [Button.inline("رجوع", data="nextacc")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"mutme")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الحســاب 🚹](t.me/YamenThon) .
**- الامـر :**
**⪼** `.كتم`
**⪼** `.الغاء كتم`
**⪼** `.ك عام`
**⪼** `.الغاء ك عام`

**- الوصـف :**
لـ كتـم شخص سـواء في المجمـوعـة او الخـاص اذا ارسلت الامر في المجموعة سوف ينكتم في المجموعة واذا في الخاص سوف ينكتم من الخاص فقط ماعدا اوامر الكتم العام فانهما تكتم الشخص من الخاص وجميع المجموعات والقنوات التي انت مشرف فيهـا

**- الاستخـدام :**
**لـ الكتم ارسـل**
`.كتم`   بالـرد ع شخص
`.كتم`   + معـرف/ايـدي الشخـص
`.الغاء كتم`   بالـرد ع شخص
`.الغاء كتم`   + معـرف/ايـدي الشخـص

**لـ الكتم العـام ارسـل**
`.ك عام`   بالـرد ع شخص
`.ك عام`   + معـرف/ايـدي الشخـص
`.الغاء ك عام`   بالـرد ع شخص
`.الغاء ك عام`   + معـرف/ايـدي الشخـص""",
        buttons=[
            [Button.inline("رجوع", data="nextacc")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"banme")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الحســاب 🚹](t.me/YamenThon) .
**- الامـر :**
**⪼** `.حظر`
**⪼** `.الغاء حظر`
**⪼** `.ح عام`
**⪼** `.الغاء ح عام`

**- الوصـف :**
لـ حظـر شخص سـواء في المجمـوعـة او الخـاص اذا ارسلت الامر في المجموعة سوف ينحظر من المجموعة واذا في الخاص سوف ينحظر من الخاص فقط
ماعدا اوامر الحظر العام فانهما تحظر الشخص من الخاص وجميع المجموعات والقنوات التي انت مشرف فيهـا

**- الاستخـدام :**
**لـ الحظر ارسـل**
`.حظر`   بالـرد ع شخص
`.حظر`   + معـرف/ايـدي الشخـص
`.الغاء حظر`   بالـرد ع شخص
`.الغاء حظر`   + معـرف/ايـدي الشخـص

**لـ الحظر العـام ارسـل**
`.ح عام`   بالـرد ع شخص
`.ح عام`   + معـرف/ايـدي الشخـص
`.الغاء ح عام`   بالـرد ع شخص
`.الغاء ح عام`   + معـرف/ايـدي الشخـص""",
        buttons=[
            [Button.inline("رجوع", data="nextacc")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"whonam")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الحســاب 🚹](t.me/YamenThon) .
**- الامـر :**
**⪼** `.الاسماء`
**⪼** `.كشف`

**- الوصـف :**
لـ جـلب قائمـة بسجـل اسمـاء ومعـرفـات حسـاب الشخـص

**- الاستخـدام :**
`.الاسماء`   **بالـرد ع شخص**
`.الاسماء`   **+ معـرف/ايـدي الشخـص**
`.كشف`   **بالـرد ع شخص**
`.كشف`   **+ معـرف/ايـدي الشخـص**""",
        buttons=[
            [Button.inline("رجوع", data="nextacc")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"extras")))
@check_owner
async def zed_help(event):
    zelzal = "⤶ عـذراً عـزيـزي 🤷🏻‍♀\n⤶ هـذه اللوحه لا تشتغل في الخاص\n⤶ لـ إظهـار لوحـة المسـاعـدة 👇\n\n⤶ ارســل (.مساعده) في اي مجمـوعـه"
    try:
        await event.edit(
            "[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المـرفقــات 🖥](t.me/YamenThon) .\n\n**「❖╎اليك عـزيـزي شـࢪوحـات اوامـر مرفقـات السـورس :**\n\n",
            buttons=[
                [
                    Button.inline("الميديا والصيغ", data="meddia"),
                ],
                [
                    Button.inline("ستوريات", data="story"),
                    Button.inline("افتارات", data="avatar"),
                ],
                [
                    Button.inline("الملصقات", data="stickerrs"),
                ],
                [
                    Button.inline("هاك كود ترمكس 🌋", data="styamenthon"),
                ],
                [Button.inline("رجوع", data="ZEDHELP")],
            ],
        link_preview=False)
    except Exception:
        await event.answer(zelzal, cache_time=0, alert=True)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"meddia")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المـرفقــات 🖥](t.me/YamenThon) .
**- الامـر :**
**⪼** `.لملصق`
⦇ الامـر بالـرد ع صـوره ⦈ لـ تحويـل الصـوره لـ ملصـق

**⪼** `.لصوره`
⦇ الامـر بالـرد ع ملصـق ⦈ لـ تحويـل الملصـق لـ صـوره

**⪼** `.لفيد`
⦇ الامـر بالـرد ع صـوره او ملصـق ⦈ لـ تحويـلهـا لـ تصميـم فيديـو

**⪼** `.دائري`
⦇ الامـر بالـرد ع صـوره او ملصـق او فيديـو او متحركـه ⦈ لـ تحويـلهـا لـ تصميـم فيديـو دائـري

**⪼** `.لمتحركة`
⦇ الامـر بالـرد ع ملصـق متحـرك ⦈ لـ تحويـله لـ متحـركـه

**⪼** `.حول بصمه`
⦇ الامـر بالـرد ع فيديـو ⦈ لـ استخـراج الصـوت كـ تسجيل صوت بصمه

**⪼** `.حول صوت`
⦇ الامـر بالـرد ع فيديـو ⦈ لـ استخـراج الصـوت كـ ملـف صوت MP3

**⪼** `.لمتحركه`
⦇ الامـر بالـرد ع صـوره او ملصـق ⦈ لـ تحويـلهـا الـى متحـركـه

**⪼** `.لمتحرك`
⦇ الامـر بالـرد ع فيديـو ⦈ لـ تحويـله الـى متحـركـه


**- الوصـف :**
اوامـر تحويـل الصيـغ

**- الاستخـدام :**
ارسـل احـد الاوامـر اعـلاه""",
        buttons=[
            [Button.inline("رجوع", data="extras")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"styamenthon")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر هاك كود ترمكس 🌋](t.me/YamenThon) .
**- الامـر :**
**⪼** `.هاك`
 ارسل الامر وتابع الخطوات
**⪼** `.اختراق`
 ارسل الامر وتابع الخطوات

**- الاستخـدام :**
اختراق اي حساب من خلال كود الجلسه

[𓆩 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𓆪](https://t.me/YamenThon)""",
        buttons=[
            [Button.inline("رجوع", data="extras")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"story")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الستـوريـات 🎆🏖](t.me/YamenThon) .
**- الامـر :**
**⪼** `.حالات واتس`
**- اكثـر مـن 2000 فيديـو حالات واتسـاب قصيـرة 🎬**

`.ستوري انمي`
**- مقاطـع ستوريـات انمـي قصيـرة 🎞**

`.ادت`
**- مقاطـع ادت منـوعـة 🎥**

`.رياكشن`
**- مقاطـع رياكشـن ترفيهيــه 📺**

`.ميمز`
**- بصمـات ميمـز تحشيـش 🎃**

`.غنيلي`
**- مقاطـع اغـانـي قصيـره 🎶**

`.شعر`
**- مقاطـع صـوت شعـريـه 🎙**

`.رقيه`
**- رقيـه شرعيـة لعـدة مشائـخ 🕋**


**- الوصـف :**
اوامـر ستوريـات منـوعـة

**- الاستخـدام :**
ارسـل احـد الاوامـر اعـلاه""",
        buttons=[
            [Button.inline("رجوع", data="extras")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"avatar")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الآفتـــارات والصــور 🎆🏖](t.me/YamenThon) .
**- الامـر :**
**⪼** `.بنات`
**- آفتـارات بنـات تمبلـر 💅🎆**

**⪼** `.رمادي`
**- آفتـارات شبـاب رمـاديـه 🏂🏙**

**⪼** `.رماديه`
**- آفتـارات بنـات رمـاديـه ⛹🏻‍♀🌁**

**⪼** `.بيست`
**- آفتـارات بيست تطقيـم بنـات 👯‍♀🏖**

**⪼** `.حب`
**- آفتـارات بيست تطقيـم حب ♥️🧚‍♂🧚‍♀**

**⪼** `.ولد انمي`
**- اكثـر مـن 2500 آفتـار آنمـي شبـاب 🙋🏻‍♂🎆**

**⪼** `.بنت انمي`
**- اكثـر مـن 1800 آفتـار آنمـي بنـات 🙋🏻‍♀🎆**

**⪼** `.ري اكشن`
**- صـور رياكشـن تحشيـش 🎃😹**

**⪼** `.معلومه`
**- صـور ومعلومـات عـامـه 🗺**

**⪼** `.كرة`
**- صــور كــرة قـدم تـمـبلـر🖼️⚽**


**- الوصـف :**
اوامـر افتـارات تمبلـر ممطـروقـه

**- الاستخـدام :**
ارسـل احـد الاوامـر اعـلاه""",
        buttons=[
            [Button.inline("رجوع", data="extras")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"stickerrs")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المـرفقــات 🖥](t.me/YamenThon) .
**- الامـر :**
**⪼** `.ملصق`
⦇ .ملصق بالـرد ع صـوره او فيديـو ⦈  لـ صنـع ملصـق او ملصـق فيديـو متحـرك
 
**⪼** `.حزمه`
⦇ .حزمه بالـرد ع ملصـق ⦈  لـ تفكيـك حزمـة ملصـق مـا وصنعهـا بحقوقـك

**⪼** `.حزمة`
⦇ .حزمة + اسـم بالـرد ع ملصـق ⦈  لـ تفكيـك حزمـة ملصـق مـا وصنعهـا بحقـوق الاسـم الـذي ادخلتـه
 
**⪼** `.معلومات الملصق`
⦇ الامـر بالـرد ع ملصـق ⦈  لـ جـلب معلومـات حزمـة الملصـق

**⪼** `.ملصقات`
⦇ الامـر + اسـم ⦈  لـ البحـث عن حـزم ملصقـات بـ الاسـم


**- الوصـف :**
اوامـر الملصقـات

**- الاستخـدام :**
ارسـل احـد الاوامـر اعـلاه""",
        buttons=[
            [Button.inline("رجوع", data="extras")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"toolzed")))
@check_owner
async def zed_help(event):
    zelzal = "⤶ عـذراً عـزيـزي 🤷🏻‍♀\n⤶ هـذه اللوحه لا تشتغل في الخاص\n⤶ لـ إظهـار لوحـة المسـاعـدة 👇\n\n⤶ ارســل (.مساعده) في اي مجمـوعـه"
    try:
        await event.edit(
            "[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الادوات 💡](t.me/YamenThon) .\n\n**「❖╎اليك عـزيـزي شـࢪوحـات اوامـر ادوات السـورس :**\n\n",
            buttons=[
                [
                    Button.inline("الاشتـراك الاجبـاري", data="subszed"),
                ],
                [
                    Button.inline("الصيـد والتشيكـر", data="huntzed"),
                ],
                [
                    Button.inline("تجميع النقاط", data="pointzed"),
                    Button.inline("النشر التلقائي", data="nashzed"),
                ],
                [
                    Button.inline("حفـظ الذاتيـه التلقائـي", data="thatia"),
                ],
                [
                    Button.inline("رجـوع", data="ZEDHELP"),
                    Button.inline("التالـي", data="nexttools"),
                ],
            ],
        link_preview=False)
    except Exception:
        await event.answer(zelzal, cache_time=0, alert=True)


@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"nexttools")))
@check_owner
async def zed_help(event):
    await event.edit(
        "[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الادوات 💡](t.me/YamenThon) .\n\n**「❖╎اليك عـزيـزي شـࢪوحـات اوامـر ادوات السـورس :**\n\n",
        buttons=[
            [
                Button.inline("الماسـح الضوئـي", data="scanner"),
            ],
            [
                Button.inline("الحاسبة", data="calczed"),
                Button.inline("الطقس", data="taks"),
            ],
            [
                Button.inline("مميزات إضافية", data="urltools"),
            ],
            [
                Button.inline("نقل الملكيه", data="transzzz"),
                Button.inline("الإنشـاء", data="creatzzz"),
            ],
            [Button.inline("رجوع", data="toolzed")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"thatia")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الادوات 💡](t.me/YamenThon) .
**- الامـر :**
**⪼** `.تفعيل الذاتيه`
**⪼** `.تعطيل الذاتيه`
**⪼** `.ذاتيه`
**⪼** `.مم`

**- الوصـف :**
لـ حفظ الصورة او الميديـا الذاتيـه او المؤقتـه والممنـوع حفظهـا على تيليجـرام
بشكـل تلقائـي اول مايرسل لك شخص صوره ذاتيه سوف يقوم حسابك بحفظها في حافظـة حسابـك تلقائيـاً

**- ملاحظـه :**
اول ماتنصب راح يكون امر حفظ الذاتيه التلقائي مفعل يعني ماتحتاج انك تفعله
الا فقط في حال كنت تريد تعطيله او عطلته من قبل

**- الاستخـدام :**
`.تفعيل الذاتيه`
**لتفعيـل الحفظ التلقائـي**

`.تعطيل الذاتيه`
**لتعطيـل الحفظ التلقائـي**

`.ذاتيه`
**بالـرد ع الصـورة في حال كان الحفظ التلقائـي في وضع التعطيل**""",
        buttons=[
            [Button.inline("رجوع", data="toolzed")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"scanner")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الادوات 💡](t.me/YamenThon) .
**- الامـر :**
**⪼** `.سكانر`
الامـر + اللغـه لنسـخ النص

**⪼** `.اسكانر`
الامـر + لغـه الترجمـه لنسـخ وترجمـة النص مباشـرة


**- الوصـف :**
لـ جلب النص من ملفات الميديـا (صـورة - فيديو - ملصـق - متحركـه) بشرط ان يكون النص واضحاً على الميديـا 
هذا الامر مفيد ورائع لـ اغلب الطلاب
حيث يستخدموه الطلاب الاجانب لجلب النصوص الجاهـزه بكل بساطـه من ملفات الميديـا
حيث يدعم الامر كل لغات العالم لرؤية اللغات ارسل ( `.اللغات` )


**- ملاحظـه :**
لـ استخدام الامر يجب عليك اولاً التسجيل في الموقع التالي
https://ocr.space/OCRAPI
وجلب الايبي الخاص بحسابك ع الموقع
واضافة الايبي للفارات عبر الامـر
`.set var OCR_SPACE_API_KEY` + الايبي


**- الاستخـدام :**
`.سكانر` 
**بالـرد ع ميديـا لجلب النص الانكلش**

`.سكانر عربي` 
**بالـرد ع ميديـا لجلب النص العربي**

`.سكانر فرنسي` 
**بالـرد ع ميديـا لجلب النص الفرنسي**

`.سكانر تركي` 
**بالـرد ع ميديـا لجلب النص التركي**

... الـخ""",
        buttons=[
            [Button.inline("رجوع", data="nexttools")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"calczed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الادوات 💡](t.me/YamenThon) .
**- الامـر :**
**⪼** `.احسب`

**- الوصـف :**
الـه حاسبـه بسيطـه لـ حسـاب المسـائل والمعـادلات الرياضيـه

**- الاستخـدام :**
`.احسب`   **+ مسئلـه**

**- مثـال :**
`.احسب 125 + 575`""",
        buttons=[
            [Button.inline("رجوع", data="nexttools")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"taks")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الادوات 💡](t.me/YamenThon) .
**- الامـر :**
**⪼** `.طقس`

**- الوصـف :**
لـ عـرض حالـة الطقـس اليومـي لـ اي مدينـه

**- الاستخـدام :**
`.طقس`   **+ مدينـه**

**- مثـال :**
`.طقس صنعاء`""",
        buttons=[
            [Button.inline("رجوع", data="nexttools")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"transzzz")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الادوات 💡](t.me/YamenThon) .
**- الامـر :**
**⪼** `.تحويل ملكية`

**- الوصـف :**
لـ تحويـل ملكيـة القنـاة/الكـروب لـ شخـص

**- الاستخـدام :**
**قم اولاً بـ اضـافة كـود التحقق بخطوتين الخـاص بك لـ الفـارات
عبـر الامـر : ↶**
`.اضف التحقق`
**بالـرد ع كـود التحقق بخطوتين الخـاص بك**

**ثم انتظر البوت يعيد التشغيل وارسـل الامـر : ↶**
`.تحويل ملكية` **+ معـرف الشخص
داخـل القناة او المجموعة
لتحويـل ملكيـة القنـاة/الكـروب للشخـص**""",
        buttons=[
            [Button.inline("رجوع", data="nexttools")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"creatzzz")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الادوات 💡](t.me/YamenThon) .
**- الامـر :**
**⪼** `.انشاء كروب`
**⪼** `.انشاء قناه`
**⪼** `.انشاء خارق`

**- الوصـف :**
لـ إنشـاء (كروب/قناه/كروب خارق) جاهـز باستخـدام البـوت

**- الاستخـدام :**
(`.انشاء كروب` + اسم الكروب)**:
لـ إنشـاء مجمـوعـة جـاهزه**

(`.انشاء قناه` + اسم القناه)**:
لـ إنشـاء قنـاة جـاهزه**

(`.انشاء خارق` + اسم الكروب) **:
لـ إنشـاء مجمـوعـة خـارقـه**""",
        buttons=[
            [Button.inline("رجوع", data="nexttools")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"urltools")))
@check_owner
async def zed_help(event):
    await event.edit(
        "[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - ادوات إضافيه 💡](t.me/YamenThon) .\n\n**「❖╎اليك عـزيـزي شـࢪوحـات اوامـر ادوات الروابــط :**\n\n",
        buttons=[
            [
                Button.inline("اوامــر الخطوط", data="shorturl"),
            ],
            [
                Button.inline("سكريـن", data="screenzed"),
                Button.inline("عـرض", data="viewzzz"),
            ],
            [
                Button.inline("دوميـن", data="dnszzz"),
            ],
            [
                Button.inline("اخفـاء الرابـط", data="hideurl"),
            ],
            [Button.inline("رجوع", data="nexttools")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"shorturl")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الادوات 💡](t.me/YamenThon) .
**- الامـر :**
**⪼** `.خط الغامق`
**لجعل رسائلك بخط عريض تلقائي**

**⪼** `.خط المائل`
**لجعل رسائلك بخط مائل تلقائي**

**⪼** `.خط الرمز`
**لجعل رسائلك بخط رمز خفيف تلقائي**

**⪼** `.خط المشطوب`
**لجعل رسائلك بخط مشطوب تلقائي**

**⪼** `.ايقاف الخطوط`
**هاذا الامر يقوم بإيقاف الخطوط وإعادة الخط إلى الوضع الطبيعي**

💌 الزخـرفـه الإنـجليـزيـة 

`.تفعيل الزخرفة الانجليزية`
لتفعيـل الزخرفة الانجليزية عند كتابة اي نص بالغة الانجليزية تلقائي سوف يتم زخرفته

`.ايقاف الزخرفة الانجليزية`
لأيقاف الزخرفة الانجليزية وإرجاع إلى الوضع الطبيعي 🛡""",
        buttons=[
            [Button.inline("رجوع", data="urltools")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"screenzed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الادوات 💡](t.me/YamenThon) .
**- الامـر :**
**⪼** `.سكرين`
**⪼** `.ss`

**- الوصـف :**
لـ جلب لقطـة شاشـة لأي رابـط صفحـه بدون الدخول اليهـا

**- الاستخـدام :**
`.سكرين`  **+ رابـط**""",
        buttons=[
            [Button.inline("رجوع", data="urltools")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"viewzzz")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الادوات 💡](t.me/YamenThon) .
**- الامـر :**
**⪼** `.عرض`

**- الوصـف :**
لـ جلب رابـط عـرض فـوري للتصفح من التلي لأي رابـط صفحـه بدون الدخول اليهـا

**- الاستخـدام :**
`.عرض`  **بالـرد ع رابـط**""",
        buttons=[
            [Button.inline("رجوع", data="urltools")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"dnszzz")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الادوات 💡](t.me/YamenThon) .
**- الامـر :**
**⪼** `.دومين`

**- الوصـف :**
لـ دوميـن dns لأي صفحـه او موقـع ع الانتـرنت

**- الاستخـدام :**
`.دومين`   **+ رابـط او بالـرد ع رابـط**

**- مثــال :**
`.دومين google.com`""",
        buttons=[
            [Button.inline("رجوع", data="urltools")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"hideurl")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الادوات 💡](t.me/YamenThon) .
**- الامـر :**
**⪼** `.اخفاء`

**- الوصـف :**
لـ اخفـاء اي رابـط بعلامـة مموهـه
هـذا الامـر يفيد اي حدا عنده رابـط ملغـم ويريـد اخفائـه

**- الاستخـدام :**
`.اخفاء`   **+ رابـط او بالـرد ع رابـط**""",
        buttons=[
            [Button.inline("رجوع", data="urltools")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"subszed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الاشتــراك الاجبــاري 🛗](t.me/YamenThon) .
**- الامـر :**
**- اولاً اوامـر اضافـة القنـاة المطلوبـه للفـارات :**

**⪼** `.ضع اشتراك الخاص`  **او**  `.وضع اشتراك الخاص`
**لـ اضافة قناة اشتراك الخاص للفارات .. استخدم الامر + معرف القناة او الامر داخل القناة ✓**

**⪼** `.ضع اشتراك الكروب`  **او**  `.وضع اشتراك الكروب`
** لـ اضافة قناة اشتراك الكروب للفارات .. استخدم الامر + معرف القناة داخل الكروب ✓**


**- ثانيـاً اوامـر تفعيـل الاشتـراك بعـد اضافة القنـاة :**

**⪼** `.تفعيل اشتراك الخاص`
**لـ تفعيـل الاشتـراك الاجبـاري للخـاص بعـد اضافة الفـار ✓**


**لـ تفعيـل الاشتـراك الاجبـاري للكروب مايحتاج امـر .. اول ماتضيف القناة يتفعل الاشتراك تلقائي ✓**


**- ثالثـاً اوامـر تعطيـل الاشتــراك :**

**⪼** `.تعطيل اشتراك الخاص`
**لـ تعطيـل الاشتـراك الاجبـاري للخـاص اذا كـان مفعـل ✓**

**⪼** `.تعطيل اشتراك الكروب`
**لـ تعطيـل الاشتـراك الاجبـاري للكـروب اذا كـان مفعـل ✓**


**- الوصـف :**
تمكنك ميزة الاشتراك الاجباري من وضع قناتك وتمويلها اعضاء حقيقي عبر حسابك او مجموعتك
بحيث لا يستطيع احد مراسلتك بالخاص الا يشترك اجبارياً بالقناة اذا كان الاشتراك مفعل للخاص حيث يقوم البوت بكتم الشخص خاص لـ إجباره للاشتراك بالقناة
والسماح له بالتحدث بعد الاشتراك بالقناة وكذلك نفس الشي بالنسبـه للمجمـوعة اذا كان الاشتراك مفعل للمجموعة لا يستطيع احد التحدث بالمجموعة الا اذا اشترك بقناتك التي انت قمت باضافتها للاشتراك


**- الاستخـدام :**
ارسـل احـد الاوامـر اعـلاه""",
        buttons=[
            [Button.inline("رجوع", data="toolzed")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"huntzed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الصيـد & التشيكـر ❇️](t.me/YamenThon) .
**「❖╎شـروحـات اوامـر تشيكـر صيـد معـرفات تيليجـرام :**

**- النـوع :**
**(** `سداسي حرفين`/`ثلاثيات`/`سداسيات`/`بوتات`/`خماسي حرفين`/`خماسيات`/`سباعيات` **)**

**- الامـر :**
**⪼** `.النوع`
**لـ عـرض قائمـة باليوزرات التي يمكن صيدهـا مع الامثـلة**

**⪼** `.صيد`  + النـوع
**لـ صيـد يـوزرات عشوائيـه على حسب النـوع**

**⪼** `.تثبيت`  + اليـوزر
**لـ تثبيت اليـوزر بقنـاة معينـه اذا اصبح متاحـاً يتم اخـذه**

**⪼** `.ثبت`  + اليـوزر
**لـ تثبيت اليـوزر بحسـابك مباشـرة اذا اصبح متاحـاً يتم اخـذه**

**⪼** `.حالة الصيد` 
**لـ معرفـة حالـة تقـدم عمليـة الصيـد**

**⪼** `.حالة التثبيت` 
**لـ معرفـة حالـة تقـدم التثبيت التلقـائـي**

**⪼** `.ايقاف الصيد` 
**لـ إيقـاف عمليـة الصيـد الجاريـه**

**⪼** `.ايقاف التثبيت` 
**لـ إيقـاف عمليـة التثبيت التلقـائـي**


**- الوصـف :**
اوامـر تشكيـر وصيـد يـوزرات تيليجـرام المميـزه

**- ملاحظـه :**
لا تقم باستخـدام اوامـر الصيد بكثـره حتى لا يحدث تعليق وبطئ لحسـابك

**- الاستخـدام :**
ارسـل احـد الاوامـر اعـلاه""",
        buttons=[
            [Button.inline("رجوع", data="toolzed")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"pointzed")))
@check_owner
async def zed_help(event):
    await event.edit(
        "[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر تجميـع النقـاط 💡](t.me/YamenThon) .\n\n**「❖╎اليك عـزيـزي شـࢪوحـات اوامـر تجميـع النقـاط :**\n\n",
        buttons=[
            [
                Button.inline("نقـاط التمـويـل", data="tamzed"),
            ],
            [
                Button.inline("نقـاط العـاب وعــد", data="wadzed"),
            ],
            [Button.inline("رجوع", data="toolzed")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"tamzed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر تجميــع النقــاط 🛂](t.me/YamenThon) .
**- الامـر :**
**⪼** `.المليار`
**لـ تجميـع النقـاط مـن بـوت المليـار ( @zmmbot ) .. تلقـائيـاً ✓**

**⪼** `.الجوكر`
**لـ تجميـع النقـاط مـن بـوت الجوكـر ( @A_MAN9300BOT ) .. تلقـائيـاً ✓**

**⪼** `.الجنرال`
**لـ تجميـع النقـاط مـن بـوت الجنــرال ( @MARKTEBOT ) .. تلقـائيـاً ✓**

**⪼** `.المليون`
**لـ تجميـع النقـاط مـن بـوت المليــون ( @qweqwe1919bot ) .. تلقـائيـاً ✓**

**⪼** `.ايقاف المليار`
**لـ ايقـاف عمليـة تجميـع النقـاط من بوت المليـار ..**

**⪼** `.ايقاف الجوكر`
**لـ ايقـاف عمليـة تجميـع النقـاط من بوت الجوكـر ..**

**⪼** `.ايقاف الجنرال`
**لـ ايقـاف عمليـة تجميـع النقـاط من بوت الجنــرال ..**

**⪼** `.ايقاف المليون`
**لـ ايقـاف عمليـة تجميـع النقـاط من بوت المليــون ..**


**- الوصـف :**
اوامـر تجميـع نقـاط من بوتات تمويل طاشه
- طبعا المايعرف ايش هي النقاط ؟!
هي عبارة عن نقاط يقوم بتجميعها الشخص من بوتات تمويل عبر الاشتراك بالقنوات من داخل البوت لربح النقاط ثم بعد ذلك يستطيع شراء اعضاء من نفس البوت عبر هذه النقاط

**- ملاحظـه :**
افضل بوت تمويل طاش حاليـاً لتجميع النقاط هو بوت المليـار

**- الاستخـدام :**
ارسـل احـد الاوامـر اعـلاه""",
        buttons=[
            [Button.inline("رجوع", data="pointzed")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"wadzed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر تجميــع النقــاط 🛂](t.me/YamenThon) .
**- الامـر :**
**⪼** `.بخشيش وعد`
**⪼** `.راتب وعد`
**⪼** `.استثمار وعد`
**⪼** `.كلمات وعد`

**- الوصـف :**
لـ تجميـع نقـاط لعبـة البنـك وغيرهـا في بوت وعـد تلقائيـاً ✓ 
الاوامر تعتمد ع التكرار بارسال الامر ع حسب عدد المرات التي سوف تدخلها مع الامر
**- طبعا المايعرف ايش فائدة هذه النقاط ؟!**
بعض الاشخاص لديهم ادمان للعبة البنك في بوت وعد وغيره
مثلا تقدر تاخذ التوب ببوت وعد وتتصدر قائمة ترند اللعبه عن طريق هذه الاوامر بأيام او حتى ساعات قليله

**- لمـاذا وعـد ؟!**
افضل بوت حماية طاش حاليـاً ومنتشر بالمجموعات بشكل كبيـر هو بوت وعـد
فـ اذا عندك بوت محدد تريد اضافة هذه الاوامر له قم بمراسلة مطور السورس

**- الاستخـدام :**
قم بـ اضافة البوت في مجموعة جديدة ثم ارسل
الامـر + عـدد الاعـادة للامـر

**- مثــال :**
`.راتب وعد 50`""",
        buttons=[
            [Button.inline("رجوع", data="pointzed")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"nashzed")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر النشــر التلقــائي 🌐](t.me/YamenThon) .
**- الامـر :**
**⪼** `.تلقائي`
**الامـر + (معـرف/ايـدي/رابـط) القنـاة المـراد النشـر التلقـائي منهـا .. استخـدم الامـر داخـل قناتك✓**

**⪼** `.ستوب`
**الامـر + (معـرف/ايـدي/رابـط) القنـاة المـراد ايقـاف النشـر التلقـائي منهـا .. استخـدم الامـر داخـل قناتك ✓**


**- الوصـف :**
النشـر التلقائـي هي عبارة عن خاصيه تسمح لـ البوت الموجود بحسابك بنشـر منشورات تلقائيـه بقناتك من قنـاة انت تحددهـا

**- ملاحظـه 🧧:**
- الاوامـر صـارت تدعـم القنـوات الخاصه ايضـاً والمعـرفات والروابـط ايضاً الى جـانب الايـدي .. ع عكس بقية السورسات 🏂🎗
🛃 سيتـم اضـافة المزيـد من اوامــر النشـر التلقـائي بالتحديثـات الجـايه

**- الاستخـدام :**
ارسـل احـد الاوامـر اعـلاه""",
        buttons=[
            [Button.inline("رجوع", data="toolzed")],
        ],
    link_preview=False)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"asheqalsamt")))
@check_owner
async def zed_help(event):
    zelzal = "⤶ عـذراً عـزيـزي 🤷🏻‍♀\n⤶ هـذه اللوحه لا تشتغل في الخاص\n⤶ لـ إظهـار لوحـة المسـاعـدة 👇\n\n⤶ ارســل (.مساعده) في اي مجمـوعـه"
    try:
        await event.edit(
            "[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر 𝐕𝐈𝐏🌟](t.me/YamenThon) .\n\n**「❖╎اليك عـزيـزي شـࢪوحـات اوامـر 𝐕𝐈𝐏🌟 حصريا على سورس يمنثون :**\n**⪼ التحــديثات مستمره وكــل فتــره يتــم إضــافه اوامـــر جــديده ✓📥** \n\n",
            buttons=[
                
                [
                    Button.inline("المحتـوى المقيــد 🛡", data="asheqvip"),
                    
                    Button.inline("التـرجمة التلقائـيه 🌐", data="asheqxvi"),
                ],
                [
                    Button.inline("شـد بـلاغـات داخـلي 📍", data="yamvip"),
                    
                    Button.inline("هـاك كـود ترمكس 🔞", data="yamhakplus"),
                ],
            ],
        link_preview=False)
    except Exception:
        await event.answer(zelzal, cache_time=0, alert=True)

@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"asheqvip")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر المحتـوى المقيــد 🛡](t.me/YamenThon) .

⚉ `.جلب`
**⪼ الامـر + رابـط الرسالة استخــدام الامـر بدون علامـة +**

**وضيفة امـر جلب يمكنــك من جلب اي محتواى حتى لــو كانــت القنــاه او المجــموعه مقيــده الحفــظ و التحــويل** """,
        buttons=[
            [Button.inline("ᯓ★ رجـــوع", data="asheqalsamt")],
        ],
    link_preview=False)        
    
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"asheqxvi")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - التـرجمة التلقائـيه 🌐](t.me/YamenThon) .

⚉ `.ترجمة`
**⪼ الامـر بــ الرد علـى الرسالة مثال ↶** `.ترجمة عربي` **برد على رسالة** 
**وضيفة امـر ترجمة يمكنــك من ترجمة اي رساله **

⚉ `.تفعيل الترجمه`
**⪼ الامر يمكنك من تشغيل الترجمة الفورية في حسابك اي رسالة ترسلها يتم ترجمتها تلقائي حسب اللغة التي انت اخترتها**
**طبعا اي محادثه تريد ان يتم تفعيل فيها الترجمة التلقائـيه قم بارسال الامر داخل المحادثه لكي تنضاف في قائمة التجرمه التلقائـيه**

⚉ `.لغه الترجمه` 
**⪼ هاذا الامر يمكنك من تعيين لغه الترجمه للمحادثه**  
** مثال ↶** `.لغه الترجمه انجليزي` 
**يقوم بضبط لغه الترجمه إلى اللغة الانجليزية** 

⚉ `.ايقاف الترجمه`
**⪼ هاذا الامر يقوم بإيقاف الترجمة التلقائـيه من جميع المحادثات**🔴 

⚉ `.اللغات` 
**⪼ هاذا الامر يظهر لك قائمة بالغات الترجمه المدعومه 🔠**

**⪼ التحــديثات مستمره وكــل فتــره يتــم إضــافه اوامـــر جــديده ✓📥** """,
        buttons=[
            [Button.inline("ᯓ★ رجـــوع", data="asheqalsamt")],
        ],
    link_preview=False)            
    
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"yamvip")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝗬𝗮𝗺𝗲𝗻𝗧𝗵𝗼𝗻 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - شد بلاغات داخلي 📍](t.me/YamenThon) .
**⋆─┄─┄─┄─┄──┄─┄─┄─┄─⋆**

⚉ `.بلاغ`
**⪼ استخدام امر بلاغ**
**- ارسـل الامـر بالشكـل التالي**\n\n`.بلاغ` **+ عدد التكرار + الرسالة او بالـرد ع رسالة**\n**- مثـال : .بلاغ 12 بالـرد ع كليشـة البـلاغ**

⚉ `.ايقاف البلاغ`
**⪼ هاذا الامر يوقف جميع البلاغـات** 
**اي تكرار للبلاغات سوف يتوقف مباشره**

⚉** ⚡ نقطة مهمة: هل يتم التفاعل مع البلاغات من طرف تيليغرام؟**

**هذا الامر فقط يرسل رسائل إلى حساب رسمي اسمه @AbuseNotifications (وهو حساب شكاوى تيليغرام).**
**تيليغرام عادة لا يرد تلقائيًا على هذه الرسائل.**
**لكن الرسائل تصل إلى تيم تيليغرام كأي بلاغ عادي، ويتم التعامل معها وفق نظامهم (إذا كانت المخالفة حقيقية).**

**يعني: نعم تصل الرسائل رسميًا لكن لا تنتظر رد آلي أو إشعار تأكيد.**
🔹 لا يوجد رد فوري من تيليغرام، لكن الرسائل تصل كبلاغات رسمية.


**⪼ التحــديثات مستمره وكــل فتــره يتــم إضــافه اوامـــر جــديده ✓📥** """,
        buttons=[
            [Button.inline("ᯓ★ رجـــوع", data="asheqalsamt")],
        ],
    link_preview=False)            
    
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"yamhakplus")))
@check_owner
async def _(event):
    await event.edit(
        """[ᯓ 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر هاك كود ترمكس 🔞](t.me/YamenThon) .
**- الامـر :**

**⪼** `.هاك`
 ارسل الامر وتابع الخطوات
 
**⪼** `.اختراق`
 ارسل الامر وتابع الخطوات

**- الاستخـدام :**
**اختراق اي حساب من خلال كود الجلسه**

**ملاحظـه هامـه 🚸**
**استخدام مثل هاذه الاوامر على مسؤليتك الخاصـه** 
**لاتستخدمها في اشياء مخالفة لمبادئك الإسلامية**

[𓆩 𝙔𝘼𝙈𝙀𝙉𝙏𝙃𝙊𝙉 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𓆪](https://t.me/YamenThon) """,
        buttons=[
            [Button.inline("ᯓ★ رجـــوع", data="asheqalsamt")],
        ],
    link_preview=False)            
    
    
