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
