import re
import json
import os
from telethon import events
from deep_translator import GoogleTranslator

from . import zedub
from ..core.managers import edit_or_reply
from . import mention 
# ملف تخزين بيانات الترجمة
TRANSLATE_FILE = "translate_settings.json"

# تحميل البيانات أو إنشاؤها إذا غير موجودة
if os.path.exists(TRANSLATE_FILE):
    try:
        with open(TRANSLATE_FILE, "r", encoding="utf-8") as f:
            translate_data = json.load(f)
    except Exception:
        translate_data = {"chats": {}, "enabled": []}
else:
    translate_data = {"chats": {}, "enabled": []}


def save_data():
    with open(TRANSLATE_FILE, "w", encoding="utf-8") as f:
        json.dump(translate_data, f, ensure_ascii=False, indent=2)


# قاموس أسماء اللغات بالعربي -> رمز اللغة
LANG_MAP = {
    "انجليزي": "en", "انجليزية": "en", "انكليزي": "en",
    "عربي": "ar", "عربية": "ar",
    "فرنسي": "fr", "فرنسية": "fr", "فرنسيه": "fr",
    "روسي": "ru", "روسية": "ru",
    "هندي": "hi", "هندية": "hi",
    "فارسي": "fa", "فارسية": "fa",
    "اسباني": "es", "اسبانية": "es",
    "تركي": "tr", "تركية": "tr",
    "الماني": "de", "المانية": "de",
    "صيني": "zh-cn", "ياباني": "ja", "كوري": "ko",
    "برتغالي": "pt", "ايطالي": "it"
}

# اسم اللغة للعرض حسب رمزها (لجعل الرد أكثر ودّية)
CODE_TO_NAME = {
    "en": "انجليزي", "ar": "عربي", "fr": "فرنسي", "ru": "روسي",
    "hi": "هندي", "fa": "فارسي", "es": "اسباني", "tr": "تركي",
    "de": "الماني", "zh-cn": "صيني", "ja": "ياباني", "ko": "كوري",
    "pt": "برتغالي", "it": "ايطالي"
}


# أمر ضبط اللغة: يقبل اسم اللغة بالعربي أو رمز اللغة مباشرة
@zedub.zed_cmd(pattern="لغه الترجمه(?:\\s+(.+))?")
async def set_lang(event):
    lang_input = event.pattern_match.group(1)
    chat_id = str(event.chat_id)
    lang = translate_data["chats"].get(chat_id)
    

    if not lang_input:
        langs = "، ".join(sorted(LANG_MAP.keys()))
        return await edit_or_reply(
            event,
            f"✧ أرسل اسم اللغة التي تريد ضبطها.\nمثال:\n`.لغه الترجمه انجليزي`\nاللغات المدعومة:\n\n{langs}"
        )

    key = lang_input.strip().lower()

    # قبول الاسم بالعربي أو رمز اللغة
    if key in LANG_MAP:
        lang_code = LANG_MAP[key]
    elif key in CODE_TO_NAME:
        lang_code = key
    else:
        langs = "، ".join(sorted(LANG_MAP.keys()))
        return await edit_or_reply(
            event,
            f"⚠️ لم أتعرف على اللغة **{lang_input}**.\nاللغات المدعومة:\n\n{langs}"
        )

    translate_data["chats"][chat_id] = lang_code
    save_data()
    friendly = CODE_TO_NAME.get(lang_code, lang_code)
    friendly = CODE_TO_NAME.get(lang, lang)
    await edit_or_reply(event, f"**🫂┊ عــزيــزي المــالك** {mention}\n\n**✧ تم ضبط لغة الترجمة**\n**✧ اللغة الحالية:** **{friendly} ({lang})**\n✧ ارسل الان امر ↶ `.تفعيل الترجمه` \n\n[𓆩 𝗦𝗼𝘂𝗿𝗰𝗲 𝗬𝗮𝗺𝗲𝗻𝗧𝗵𝗼𝗻 𓆪](https://t.me/YamenThon)\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n")


# أمر تفعيل الترجمة — الآن يتحقق إذا كانت مفعلة مسبقًا
@zedub.zed_cmd(pattern="(تفعيل الترجمه|تفعيل الترجمة)")
async def enable_translate(event):
    chat_id = str(event.chat_id)
    lang = translate_data["chats"].get(chat_id)

    if not lang:
        return await edit_or_reply(
            event,
            "✧ يجب أولاً ضبط لغة الترجمة في هذه الدردشة باستخدام:\n`.لغه الترجمه <اسم_اللغة>`"
        )

    # تحقق إن كانت مفعلّة بالفعل في نفس الدردشة
    if chat_id in translate_data.get("enabled", []):
        friendly = CODE_TO_NAME.get(lang, lang)
        return await edit_or_reply(
            event,
            f"[𓆩 𝗦𝗼𝘂𝗿𝗰𝗲 𝗬𝗮𝗺𝗲𝗻𝗧𝗵𝗼𝗻 𓆪](https://t.me/YamenThon)\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n\n**🫂┊ عــزيــزي المــالك** {mention}\n\n**✧┊  الترجمة الفورية مفعّلة مسبقًا في هذه الدردشة.⚠️**\n**✧┊ اللغة الحالية:** **{friendly} ({lang})**\n**✧┊ حـالـة التـرجمة ← مــفعله 🟢**"
        )

    # تفعيل للدردشة الحالية فقط
    translate_data.setdefault("enabled", []).append(chat_id)
    save_data()
    friendly = CODE_TO_NAME.get(lang, lang)
    await edit_or_reply(event, f"[𓆩 𝗦𝗼𝘂𝗿𝗰𝗲 𝗬𝗮𝗺𝗲𝗻𝗧𝗵𝗼𝗻 𓆪](https://t.me/YamenThon)\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n\n**✧ تم تفعيل الترجمة الفورية ✓**\n**✧ لغــه الترجمه ← {friendly} ({lang})**\n**✧ حـالـة التـرجمة ← مــفعله 🟢**")


# أمر إيقاف الترجمة (يعطل لكل الدردشات كما طلبت سابقًا)
@zedub.zed_cmd(pattern="(ايقاف الترجمه|ايقاف الترجمة)")
async def disable_translate(event):
    chat_id = str(event.chat_id)
    lang = translate_data["chats"].get(chat_id)
    if not translate_data.get("enabled"):
        return await edit_or_reply(event, "✧ الترجمة الفورية متوقفة بالفعل ❌")

    translate_data["enabled"].clear()
    save_data()
    friendly = CODE_TO_NAME.get(lang, lang)
    await edit_or_reply(event, f"[𓆩 𝗦𝗼𝘂𝗿𝗰𝗲 𝗬𝗮𝗺𝗲𝗻𝗧𝗵𝗼𝗻 𓆪](https://t.me/YamenThon)\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n\n**✧ تم إيقاف الترجمة الفورية ✓**\n**✧ لغــه الترجمه ← {friendly} ({lang})**\n**✧ حـالـة التـرجمة ← معــطله 🔴**")


# فلتر للرسائل العادية — يترجم رسائل صاحب السورس فقط ويعدلها بدل إرسال رد
@zedub.on(events.NewMessage)
async def auto_translate(event):
    chat_id = str(event.chat_id)

    # التأكد أن الترجمة مفعلة في هذه الدردشة
    if chat_id not in translate_data.get("enabled", []):
        return

    # الترجمة فقط لرسائل صاحب البوت/السورس
    if event.sender_id != getattr(zedub, "uid", None):
        return

    # استثناء الأوامر والرسائل الفارغة
    if not event.message.message or event.message.message.startswith("."):
        return

    text = event.message.message

    # استثناء الرسائل التي تتكون من رموز/إيموجي فقط
    if re.fullmatch(r"[\W_]+", text):
        return

    lang = translate_data["chats"].get(chat_id, "en")

    try:
        translated = GoogleTranslator(source="auto", target=lang).translate(text)
        if translated and translated.strip() != text.strip():
            # تعديل الرسالة الأصلية نفسها إلى النص المترجم
            await event.edit(f"{translated}")
    except Exception as e:
        # لو فشلت الترجمة نخلي رسالة خطأ بسيطة (نعدل بدل أن نرد)
        await event.reply(f"⚠️ خطأ في الترجمة: ")
 


AsheqMusic_cmd = (
"[ᯓ 𝗬𝗮𝗺𝗲𝗻𝗧𝗵𝗼𝗻 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - اوامــر الترجــمة 🌐 ](t.me/YamenThon) ."
"**⋆─┄─┄─┄─┄──┄─┄─┄─┄─⋆**\n"
"⚉ `.ترجمة`\n"
"**⪼ الامـر بــ الرد علـى الرسالة مثال ↶** `.ترجمة عربي` **برد على رسالة** \n\n**وضيفة امـر ترجمة يمكنــك من ترجمة اي رساله ** \n\n"
"⚉ `.تفعيل الترجمه`\n"
"**⪼ الامر يمكنك من تشغيل الترجمة الفورية في حسابك اي رسالة ترسلها يتم ترجمتها تلقائي حسب اللغة التي انت اخترتها** \n"
"**طبعا اي محادثه تريد ان يتم تفعيل فيها الترجمة التلقائـيه قم بارسال الامر داخل المحادثه لكي تنضاف في قائمة التجرمه التلقائـيه**\n\n"
"⚉ .لغه الترجمه`\n"
"**⪼ هاذا الامر يمكنك من تعيين لغه الترجمه للمحادثه** \n ** مثال ↶** `.لغه الترجمه انجليزي` \n"
"**يقوم بضبط لغه الترجمه إلى اللغة الانجليزية** \n\n"
"⚉ `.ايقاف الترجمه`\n"
"**⪼ هاذا الامر يقوم بإيقاف الترجمة التلقائـيه من جميع المحادثات** 🔴 \n\n"
"⚉ `.اللغات` \n"
"**⪼ هاذا الامر يظهر لك قائمة بالغات الترجمه المدعومه 🔠**\n\n"
"**⪼ التحــديثات مستمره وكــل فتــره يتــم إضــافه اوامـــر جــديده ✓📥**\n\n"
) 

@zedub.zed_cmd(pattern="الترجمه")
async def cmd(asheqqqq):
    await edit_or_reply(asheqqqq, AsheqMusic_cmd)    
    
Asheqlan_cmd = ("[ᯓ 𝗬𝗮𝗺𝗲𝗻𝗧𝗵𝗼𝗻 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - لغات الترجــمة 🌐](t.me/YamenThon) .\n"
"**⋆─┄─┄─┄─┄──┄─┄─┄─┄─⋆**\n\n"

"⚉ `.لغه الترجمه عربي` \n"
"⚉ `.لغه الترجمه انجليزي` \n"
"⚉ `.لغه الترجمه روسي` \n"
"⚉ `.لغه الترجمه فرنسي` \n"
"⚉ `.لغه الترجمه هندي` \n"
"⚉ `.لغه الترجمه فارسي` \n"
"⚉ `.لغه الترجمه تركي` \n"
"⚉ `.لغه الترجمه اسباني` \n"
"⚉ `.لغه الترجمه الماني` \n"
"⚉ `.لغه الترجمه صيني` \n"
"⚉ `.لغه الترجمه برتغالي` \n\n"

"**⪼ سيتم إضـافة لغات جديـدة في التحديثـات القادمـه لمواكبـة كل ماهـو جديـد** 📥\n"
)               

@zedub.zed_cmd(pattern="اللغات")
async def cmd(asheqqqx):
    await edit_or_reply(asheqqqx, Asheqlan_cmd)            
