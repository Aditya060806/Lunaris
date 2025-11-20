# ✅ Next Steps After Adding .env File

Great! You've added the `.env` file with your Gemini API key. Now let's get everything running!

## 🔍 Step 1: Verify .env File Setup

First, let's make sure your `.env` file is correctly configured:

```bash
cd fastapi-backend
python test_setup.py
```

This will check:
- ✅ .env file exists
- ✅ API key is loaded
- ✅ Key format is correct
- ✅ Gemini API can be configured

**Expected output:**
```
✅ .env file found
✅ GEMINI_API_KEY found: AIzaSy...xyz
✅ API key format looks correct
✅ Google Generative AI imported successfully
✅ Model 'gemini-2.5-flash' configured
✅ All checks passed!
```

---

## 🚀 Step 2: Start FastAPI Backend

Open Terminal 1:

```bash
cd fastapi-backend

# Activate virtual environment (if you created one)
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

# Install dependencies (if not done already)
pip install -r requirements.txt

# Start the server
uvicorn main:app --reload --port 8000
```

**Expected output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

**Test the server:**
- Open browser: http://localhost:8000/docs (API documentation)
- Or test: http://localhost:8000/start-server (should return `{"status":"success"}`)

---

## ☕ Step 3: Start Spring Boot Backend

Open Terminal 2 (keep FastAPI running in Terminal 1):

```bash
cd moodify

# Using Maven Wrapper (Windows)
.\mvnw.cmd spring-boot:run

# Using Maven Wrapper (macOS/Linux)
./mvnw spring-boot:run
```

**Expected output:**
```
Started MoodifyApplication in X.XXX seconds
Tomcat started on port(s): 8080 (http)
```

**Test the server:**
- Open browser: http://localhost:8080/api/health
- Should return: `"Healthy"`

---

## 🌐 Step 4: Update Frontend API URL (For Local Development)

If you want to test locally, update the frontend:

**File:** `frontend/script.js`
**Line 2:** Change from:
```javascript
const API_URL = 'http://127.0.0.1:8080/api/analyse';
```
To:
```javascript
const API_URL = 'http://localhost:8080/api/analyse';
```
(Already correct, but verify)

**Also check Spring Boot can reach FastAPI:**

**File:** `moodify/src/main/java/com/moodify/moodify/service/AIServiceClient.java`
**Line 22:** Should be:
```java
private static final String FASTAPI_URL = "http://localhost:8000/mood-analysis";
```
(Already correct for localhost)

---

## 🎨 Step 5: Run Frontend

**Option 1: Direct Browser**
```bash
cd frontend
# Simply open index.html in your browser
```

**Option 2: Local Server (Recommended)**
```bash
cd frontend

# Using Python
python -m http.server 3000

# Or using Node.js (if installed)
npx http-server -p 3000
```

Then open: http://localhost:3000

---

## ✅ Step 6: Test Full Application

1. **Open frontend** (http://localhost:3000 or open index.html)
2. **Upload an image** or use camera
3. **Click "Analyze Mood"**
4. **Check results:**
   - Mood detected (HAPPY, SAD, ENERGETIC, or LOVE)
   - AI comment displayed
   - Song recommendation shown
   - YouTube player should load

---

## 🐛 Troubleshooting

### Issue: "GEMINI_API_KEY not found"
**Solution:**
- Check `.env` file is in `fastapi-backend/` directory
- Verify format: `GEMINI_API_KEY=AIzaSy...` (no spaces around `=`)
- Run `python test_setup.py` to verify

### Issue: FastAPI can't start
**Solution:**
- Ensure virtual environment is activated
- Install dependencies: `pip install -r requirements.txt`
- Check port 8000 is not in use

### Issue: Spring Boot can't connect to FastAPI
**Solution:**
- Ensure FastAPI is running on port 8000
- Check `AIServiceClient.java` has correct URL
- Test: http://localhost:8000/start-server should work

### Issue: Frontend can't connect to backend
**Solution:**
- Ensure Spring Boot is running on port 8080
- Check browser console for CORS errors
- Verify `script.js` has correct `API_URL`

---

## 📊 Service Status Check

| Service | URL | Status Check |
|---------|-----|--------------|
| FastAPI | http://localhost:8000 | http://localhost:8000/start-server |
| Spring Boot | http://localhost:8080 | http://localhost:8080/api/health |
| Frontend | http://localhost:3000 | Open in browser |

---

## 🎯 Quick Command Summary

```bash
# Terminal 1: FastAPI
cd fastapi-backend
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python test_setup.py  # Verify setup
uvicorn main:app --reload --port 8000

# Terminal 2: Spring Boot
cd moodify
.\mvnw.cmd spring-boot:run  # Windows

# Terminal 3: Frontend (optional)
cd frontend
python -m http.server 3000
```

---

## 🎉 You're All Set!

Once all three services are running, your Moodify application should be fully functional!

**Next:** Test it by uploading an image and analyzing the mood! 🎵😊

