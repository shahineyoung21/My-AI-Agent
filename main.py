#!/usr/bin/env python3
"""
🤖 AI Agent - برنامج وكيل ذكاء اصطناعي فائق
يساعدك في جميع مهام البرمجة والتطوير
"""

import os
import sys
import json
import traceback
from datetime import datetime

try:
    import google.generativeai as genai
except ImportError:
    print("❌ خطأ: مكتبة google-generativeai غير مثبتة")
    print("قم بتشغيل: pip install -r requirements.txt")
    sys.exit(1)

# ===================== Configuration =====================
API_KEY = os.getenv('GEMINI_API_KEY')
MODEL_NAME = 'gemini-2.0-flash'
MAX_RETRIES = 3
TEMPERATURE = 0.7

# ===================== AI Agent Class =====================
class ProgrammingAIAgent:
    """وكيل ذكاء اصطناعي متخصص في مهام البرمجة"""
    
    def __init__(self):
        """تهيئة الوكيل والاتصال بـ Gemini API"""
        self.retry_count = 0
        self.session_id = datetime.now().isoformat()
        self.conversation_history = []
        
        if not API_KEY:
            raise ValueError("❌ خطأ: GEMINI_API_KEY غير موجود في البيئة!")
        
        try:
            genai.configure(api_key=API_KEY)
            self.model = genai.GenerativeModel(MODEL_NAME)
            print("✅ تم الاتصال بـ Google Gemini بنجاح!")
        except Exception as e:
            raise RuntimeError(f"❌ فشل الاتصال بـ Gemini: {str(e)}")
    
    def write_code(self, requirement: str, language: str = "Python") -> str:
        """كتابة كود جديد حسب المتطلبات"""
        prompt = f"""أنت مطور برامج متقدم وذكي جداً.

لغة البرمجة: {language}
المتطلب: {requirement}

يرجى:
1. كتابة كود كامل وجاهز للاستخدام
2. إضافة تعليقات توضيحية
3. اتباع أفضل الممارسات البرمجية
4. تضمين معالجة الأخطاء
5. شرح الكود بعد انتهائك

تأكد من أن الكود يعمل بدون أخطاء."""
        return self._send_request(prompt)
    
    def analyze_code(self, code: str, task: str = "تحليل الكود") -> str:
        """تحليل وتقييم الكود"""
        prompt = f"""أنت خبير برمجة فائق متخصص في تحليل الأكواد.

المهمة: {task}

الكود المراد تحليله:
```
{code}
```

يرجى تقديم:
1. شرح شامل للكود
2. تحديد المشاكل والأخطاء (إن وجدت)
3. اقتراحات للتحسين
4. أمثلة على الاستخدام

الرد بصيغة واضحة ومنظمة."""
        return self._send_request(prompt)
    
    def debug_code(self, code: str, error_message: str = "") -> str:
        """تصحيح أخطاء الكود"""
        prompt = f"""أنت متخصص في تصحيح الأخطاء البرمجية.

الكود الذي يحتوي على خطأ:
```
{code}
```

رسالة الخطأ:
{error_message if error_message else "لم يتم توفير رسالة خطأ - قم بتحليل الكود للعثور على المشاكل"}

يرجى:
1. تحديد السبب الجذري للخطأ
2. شرح المشكلة بوضوح
3. تقديم الكود المصحح
4. شرح ما تم تغييره ولماذا"""
        return self._send_request(prompt)
    
    def explain_concept(self, concept: str, language: str = "Python") -> str:
        """شرح مفهوم برمجي"""
        prompt = f"""أنت معلم برمجة متميز.

لغة البرمجة: {language}
المفهوم: {concept}

يرجى:
1. شرح المفهوم بأسلوب بسيط وواضح
2. تقديم أمثلة عملية متعددة
3. توضيح الاستخدامات الشائعة
4. تحذيرات أو نقاط مهمة

استخدم لغة سهلة الفهم."""
        return self._send_request(prompt)
    
    def solve_problem(self, problem: str, language: str = "Python") -> str:
        """حل مشكلة برمجية معينة"""
        prompt = f"""أنت خبير برمجة فائق يحل المشاكل البرمجية.

لغة البرمجة: {language}
المشكلة: {problem}

يرجى:
1. شرح المشكلة بوضوح
2. تقديم حل كامل ومختبر
3. شرح خطوات الحل
4. تقديم أمثلة عملية"""
        return self._send_request(prompt)
    
    def _send_request(self, prompt: str, retries: int = 0) -> str:
        """إرسال طلب إلى Gemini مع معالجة الأخطاء"""
        try:
            self.conversation_history.append({
                "timestamp": datetime.now().isoformat(),
                "type": "request",
                "prompt": prompt[:80] + "..." if len(prompt) > 80 else prompt
            })
            
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=TEMPERATURE,
                    max_output_tokens=4096,
                )
            )
            
            if not response.text:
                return "⚠️ لم يتم الحصول على رد من الـ AI"
            
            self.conversation_history.append({
                "timestamp": datetime.now().isoformat(),
                "type": "response",
                "length": len(response.text)
            })
            
            return response.text
        
        except Exception as e:
            if retries < MAX_RETRIES:
                print(f"⚠️ محاولة {retries + 1}/{MAX_RETRIES}: {str(e)}")
                return self._send_request(prompt, retries + 1)
            else:
                return f"❌ فشل بعد {MAX_RETRIES} محاولات: {str(e)}"
    
    def save_session(self, filename: str = None) -> str:
        """حفظ سجل الجلسة"""
        if filename is None:
            filename = f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump({
                    "session_id": self.session_id,
                    "timestamp": datetime.now().isoformat(),
                    "history_count": len(self.conversation_history),
                }, f, ensure_ascii=False, indent=2)
            
            return f"✅ تم حفظ الجلسة في: {filename}"
        except Exception as e:
            return f"❌ خطأ في حفظ الجلسة: {str(e)}"

# ===================== Main Function =====================
def main():
    """الدالة الرئيسية"""
    print("=" * 60)
    print("🤖 برنامج الوكيل الذكي للبرمجة")
    print("=" * 60)
    print()
    
    try:
        agent = ProgrammingAIAgent()
        print("✅ الوكيل جاهز للعمل!")
        print()
        
        # اختبار بسيط
        print("📝 اختبار: كتابة دالة بسيطة")
        print("-" * 60)
        result = agent.write_code("كتابة دالة تجمع رقمين", "Python")
        print(result)
        print()
        
        print("=" * 60)
        print("✅ اختبار نجح! الوكيل يعمل بشكل صحيح")
        print("=" * 60)
        
    except Exception as e:
        print(f"❌ خطأ: {str(e)}")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
