# My AI Agent 🤖

برنامج وكيل ذكاء اصطناعي ذاتي التعلم يستخدم Google Gemini AI لتحليل البيانات والمهام المعقدة.

## المميزات ✨

- 🧠 وكيل ذكاء اصطناعي مستقل
- 🔄 إعادة محاولة تلقائية عند الفشل (3 محاولات)
- 📊 تحليل البيانات والاتجاهات
- ⚡ تثبيت تلقائي للمتطلبات
- 🚀 التشغيل التلقائي عبر GitHub Actions

## المتطلبات 📋

- Python 3.10+
- مفتاح API من Google Gemini

## التثبيت 🔧

```bash
# تثبيت المتطلبات
pip install -r requirements.txt
```

## الإعداد 🔐

### 1. احصل على مفتاح API
1. انتقل إلى [Google AI Studio](https://aistudio.google.com/app/apikey)
2. أنشئ مفتاح API جديد

### 2. أضف المفتاح إلى GitHub Secrets
1. اذهب إلى Settings → Secrets and variables → Actions
2. أنشئ secret جديد باسم `GEMINI_API_KEY`
3. الصق مفتاح API الخاص بك

### 3. تشغيل محلي
```bash
export GEMINI_API_KEY="your-api-key-here"
python main.py
```

## الاستخدام 💻

البرنامج يقوم بالمهام التالية تلقائيًا:
- تحليل اتجاهات السوق والبيانات الرقمية
- حل المشاكل البرمجية والمنطقية
- تقديم تقارير تنفيذية

عند كل push إلى main/master، سيتم تشغيل الـ Agent تلقائيًا عبر GitHub Actions.

## البنية 📁

```
.
├── main.py                    # البرنامج الرئيسي
├── requirements.txt           # المتطلبات
├── .github/workflows/agent.yml # تكوين GitHub Actions
└── README.md                  # التوثيق
```

## استكشاف الأخطاء 🐛

### خطأ: GEMINI_API_KEY is missing
- تأكد من إضافة `GEMINI_API_KEY` إلى GitHub Secrets
- تحقق من أن الـ workflow يستخدم `secrets.GEMINI_API_KEY`

### خطأ: ModuleNotFoundError
- تأكد من تشغيل `pip install -r requirements.txt`

## الترخيص 📄

هذا المشروع مفتوح المصدر.

---

**ملاحظة**: تأكد من أن مفتاح API آمن ولا تشاركه مع أي شخص! 🔒
