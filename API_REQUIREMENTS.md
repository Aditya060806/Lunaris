# 🔑 API & Requirements Summary

## Required APIs

### 1. Google Gemini API Key ⭐ REQUIRED

**Purpose:** Facial emotion recognition and mood detection

**Where to get it:**
- Website: https://aistudio.google.com/app/apikey
- Sign in with Google account
- Click "Create API Key"
- Copy the key (format: `AIzaSyC...`)

**Where to configure:**
- File: `fastapi-backend/.env`
- Format: `GEMINI_API_KEY=your_actual_key_here`

**Cost:** Free tier with generous limits

**Used in:**
- `fastapi-backend/main.py` (line 22)

---

## Optional APIs

### YouTube API (NOT REQUIRED)

**Current Status:** Not used - YouTube IFrame API works without key

**If you want advanced features:**
- YouTube Data API v3 from Google Cloud Console
- For video search, metadata, etc.
- **Not needed for current functionality**

---

## Software Requirements

### Required:

1. **Java Development Kit (JDK)**
   - Version: 17 or higher
   - Download: https://adoptium.net/ or https://www.oracle.com/java/
   - Verify: `java -version`

2. **Python**
   - Version: 3.9 or higher
   - Download: https://www.python.org/downloads/
   - Verify: `python --version`

3. **Maven** (Optional - project includes wrapper)
   - Version: 3.6+
   - Download: https://maven.apache.org/download.cgi
   - Or use included `mvnw` / `mvnw.cmd`

### Optional:

- **Docker** - For containerized deployment
- **Git** - For version control
- **Node.js** - Only if using npm/http-server for frontend

---

## Environment Variables

### FastAPI Backend

**File:** `fastapi-backend/.env`

```env
GEMINI_API_KEY=AIzaSyC_your_actual_api_key_here
```

**How to create:**
```bash
cd fastapi-backend
echo "GEMINI_API_KEY=your_key" > .env
# Then edit .env and paste your actual key
```

### Spring Boot Backend

**File:** `moodify/src/main/resources/application.properties`

```properties
spring.application.name=Moodify
server.port=${PORT:8080}
spring.servlet.multipart.max-file-size=10MB
spring.servlet.multipart.max-request-size=12MB
```

**Note:** `PORT` environment variable is optional (defaults to 8080)

---

## Configuration Checklist

- [ ] Google Gemini API key obtained
- [ ] `.env` file created in `fastapi-backend/` directory
- [ ] API key added to `.env` file
- [ ] Java 17+ installed and verified
- [ ] Python 3.9+ installed and verified
- [ ] Maven installed OR using `mvnw` wrapper
- [ ] FastAPI dependencies installed (`pip install -r requirements.txt`)
- [ ] Spring Boot can build (`mvnw clean package`)
- [ ] Frontend API URL configured (if using localhost)

---

## Port Configuration

| Service | Default Port | Environment Variable |
|---------|-------------|---------------------|
| FastAPI | 8000 | None (hardcoded) |
| Spring Boot | 8080 | `PORT` (optional) |
| Frontend | 3000 | None (if using server) |

---

## Quick Verification

```bash
# Check Java
java -version
# Should show: openjdk version "17" or higher

# Check Python
python --version
# Should show: Python 3.9.x or higher

# Check Maven (if installed)
mvn -version
# Or use wrapper: ./mvnw --version
```

---

## Summary

**You ONLY need:**
1. ✅ **Google Gemini API Key** (get from https://aistudio.google.com/app/apikey)
2. ✅ **Java 17+**
3. ✅ **Python 3.9+**

**That's it!** Everything else is optional or included in the project.

---

For detailed setup instructions, see [SETUP.md](SETUP.md)
For quick start, see [QUICK_START.md](QUICK_START.md)

