# ⚡ Lunaris - Quick Start Guide

## 🎯 What You Need

### APIs Required:
- **Google Gemini API Key** (REQUIRED)
  - Get it: https://aistudio.google.com/app/apikey
  - Free tier available

### Software Required:
- Java 17+
- Python 3.9+
- Maven (or use included `mvnw` wrapper)

---

## 🚀 5-Minute Setup

### 1. Get Gemini API Key
```
1. Go to: https://aistudio.google.com/app/apikey
2. Sign in with Google
3. Create new API key
4. Copy the key (starts with AIza...)
```

### 2. Setup FastAPI (Terminal 1)
```bash
cd fastapi-backend
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate    # macOS/Linux
pip install -r requirements.txt

# Create .env file
echo "GEMINI_API_KEY=YOUR_KEY_HERE" > .env
# Edit .env and paste your actual API key

uvicorn main:app --reload --port 8000
```

### 3. Setup Spring Boot (Terminal 2)
```bash
cd moodify
$env:JAVA_HOME = "C:\Program Files\Eclipse Adoptium\jdk-17.0.17.10-hotspot"

.\mvnw.cmd spring-boot:run    # Windows
# ./mvnw spring-boot:run      # macOS/Linux
```

### 4. Open Frontend
```bash
cd frontend
# Option 1: Open index.html directly in browser
# Option 2: Use local server
python -m http.server 3000
# Then open: http://localhost:3000
```

---

## ✅ Verify Setup

1. **FastAPI:** http://localhost:8000/docs
2. **Spring Boot:** http://localhost:8080/api/health
3. **Frontend:** Upload image → Analyze → Should work!

---

## 🔧 Configuration Files

| File | What to Configure |
|------|------------------|
| `fastapi-backend/.env` | `GEMINI_API_KEY=your_key` |
| `frontend/script.js` | `API_URL = 'http://localhost:8080/api/analyse'` |
| `moodify/.../AIServiceClient.java` | `FASTAPI_URL = "http://localhost:8000/mood-analysis"` |

---

## 📞 Need Help?

See [SETUP.md](SETUP.md) for detailed instructions.

