from flask import Flask, render_template, request
import os

app = Flask(__name__)

# بيانات المحاضرات
ENT_LECTURES = [
    {
        "id": 1,
        "title": "Anatomy & physiology of ear",
        "doctor": "د.فؤاد شمسان",
        "resources": [
            {"type": "report", "label": "التقرير", "url": "https://t.me/september216thbatchENT/58"},
            {"type": "recording", "label": "التسجيل", "url": "https://t.me/september216thbatchENT/56"},
            {"type": "slides", "label": "الملزمة", "url": "https://t.me/september216thbatchENT/55"},
        ]
    },
    {
        "id": 2,
        "title": "Symptomatology & examination & Assessment of Ear",
        "doctor": "د.فؤاد شمسان",
        "resources": [
            {"type": "report", "label": "التقرير", "url": "https://t.me/september216thbatchENT/59"},
            {"type": "recording", "label": "التسجيل", "url": "https://t.me/september216thbatchENT/57"},
            {"type": "slides", "label": "الملزمة", "url": "https://t.me/september216thbatchENT/55"},
        ]
    },
    {
        "id": 3,
        "title": "Otosclerosis, Otitic Barotrauma and Facial nerve",
        "doctor": "د.حنان داؤود",
        "resources": [
            {"type": "report", "label": "التقرير", "url": "https://t.me/september216thbatchENT/75"},
            {"type": "recording", "label": "التسجيل", "url": "https://t.me/september216thbatchENT/60"},
            {"type": "slides", "label": "الملزمة", "url": "https://t.me/september216thbatchENT/73"},
        ]
    },
    # ... يمكن إضافة بقية المحاضرات هنا بنفس التنسيق
    {
        "id": 16,
        "title": "DNS, Allergic & non-allergic Rhinitis, Neck Mass & ENT Tumors",
        "doctor": "د.خالد الطهيف",
        "resources": [
            {"type": "extra", "label": "التقرير والتسجيل والملازم", "url": "https://t.me/september216thbatchENT/137"},
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html', lectures=ENT_LECTURES)

if __name__ == "__main__":
    # Render يستخدم المتغير البيئي PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)