import os
import sys
import subprocess

# تأكيد تثبيت المكتبات الضرورية أوتوماتيكياً
try:
    import google.genai as genai
except ImportError:
    print("📦 Installing missing dependency: google-genai...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "google-genai"])
    import google.genai as genai

import traceback

# استدعاء مفتاح الأمان والتأكد من وجوده
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("❌ Critical Error: GEMINI_API_KEY is missing from GitHub Secrets!")
    print("📋 Please add GEMINI_API_KEY to your repository secrets:")
    print("   1. Go to: https://github.com/shahineyoung21/My-AI-Agent/settings/secrets/actions")
    print("   2. Click 'New repository secret'")
    print("   3. Name: GEMINI_API_KEY")
    print("   4. Value: Your Google Gemini API key")
    exit(1)

def execute_with_ai_fallback(task_description):
    client = genai.Client(api_key=api_key)
    print(f"🤖 Agent Target: {task_description}")
    
    prompt = f"""
    أنت وكيل ذكاء اصطناعي ذاتي التعلم ومبرمج مستقل. 
    مهمتك: {task_description}
    إذا واجهت أي عقبات برمجية أو منطقية، قم بابتكار حلول بديلة، تجاوز المشاكل بحلول إبداعية.
    اعطني النتيجة النهائية في شكل تقرير تنفيذي دقيق ومباشر.
    """
    
    max_retries = 3
    for attempt in range(1, max_retries + 1):
        try:
            print(f"🔄 محاولة التنفيذ رقم ({attempt}/{max_retries})...")
            response = client.models.generate_content(
                model="models/gemini-2.0-flash",
                contents=prompt
            )
            
            print("\n--- 🧠 Agent Execution Report ---")
            print(response.text)
            print("---------------------------------")
            print("✅ Task successfully completed!")
            return True
            
        except Exception as e:
            print(f"⚠️ Warning: Encountered an obstacle on attempt {attempt}: {str(e)}")
            traceback.print_exc()
            if attempt == max_retries:
                print("❌ Agent reached max retries.")
                raise e

if __name__ == "__main__":
    print("🚀 Initializing Self-Learning Autonomous Agent Engine...")
    target_goal = "تحليل اتجاهات السوق والبيانات الرقمية، وتجاوز أي أخطاء في جلب البيانات، وتقديم استراتيجية تشغيل محسّنة"
    execute_with_ai_fallback(target_goal)
