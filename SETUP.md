# 🚀 Moodify Setup Guide

## 📋 Prerequisites & Requirements

### Required Software

1. **Java Development Kit (JDK)**
   - Version: **17 or higher**
   - Download: [Oracle JDK](https://www.oracle.com/java/technologies/downloads/) or [OpenJDK](https://adoptium.net/)
   - Verify: `java -version`

2. **Maven**
   - Version: **3.6+**
   - Download: [Maven Download](https://maven.apache.org/download.cgi)
   - Verify: `mvn -version`
   - Note: The project includes `mvnw` (Maven Wrapper), so Maven installation is optional

3. **Python**
   - Version: **3.9 or higher**
   - Download: [Python Downloads](https://www.python.org/downloads/)
   - Verify: `python --version` or `python3 --version`

4. **Git** (Optional, for cloning)
   - Download: [Git Downloads](https://git-scm.com/downloads)

5. **Docker** (Optional, for containerized deployment)
   - Download: [Docker Desktop](https://www.docker.com/products/docker-desktop/)

---

## 🔑 Required APIs & Keys

### 1. **Google Gemini API Key** (REQUIRED)

**What it's used for:**
- Facial emotion recognition and mood detection
- AI-powered image analysis

**How to get it:**
1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Click "Get API Key" or go to [API Keys Page](https://aistudio.google.com/app/apikey)
4. Create a new API key
5. Copy the API key (starts with `AIza...`)

**Where to use it:**
- FastAPI backend: `.env` file in `fastapi-backend/` directory
- Environment variable: `GEMINI_API_KEY`

**Cost:** Free tier available with generous limits

---

### 2. **YouTube API** (OPTIONAL - Not Required)

**What it's used for:**
- Currently NOT used - the app uses YouTube video URLs directly
- YouTube IFrame API is loaded from CDN (no key needed)
- Video playback works without API key

**Note:** If you want to use YouTube Data API v3 for advanced features (search, metadata), you would need:
- YouTube Data API v3 key from [Google Cloud Console](https://console.cloud.google.com/)
- But this is **NOT required** for current functionality

---

## 📦 Installation Steps

### Step 1: Clone/Download the Project

```bash
# If using Git
git clone <repository-url>
cd Moodify-1.0

# Or download and extract the ZIP file
```

---

### Step 2: Setup FastAPI Backend (Python)

```bash
# Navigate to FastAPI directory
cd fastapi-backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
# On Windows (PowerShell):
echo "GEMINI_API_KEY=your_api_key_here" > .env
# On Windows (CMD):
echo GEMINI_API_KEY=your_api_key_here > .env
# On macOS/Linux:
echo "GEMINI_API_KEY=your_api_key_here" > .env

# Edit .env file and replace 'your_api_key_here' with your actual Gemini API key
```

**Or manually create `.env` file:**
```env
GEMINI_API_KEY=AIzaSyC_your_actual_api_key_here
```

**Run FastAPI server:**
```bash
uvicorn main:app --reload --port 8000
```

**Verify:** Open http://localhost:8000/docs to see API documentation

---

### Step 3: Setup Spring Boot Backend (Java)

```bash
# Navigate to Spring Boot directory
cd moodify

# Using Maven Wrapper (recommended - no Maven installation needed)
# On Windows:
.\mvnw.cmd clean package
.\mvnw.cmd spring-boot:run

# On macOS/Linux:
./mvnw clean package
./mvnw spring-boot:run

# Or if you have Maven installed:
mvn clean package
mvn spring-boot:run
```

**Verify:** Open http://localhost:8080/api/health (should return "Healthy")

**Update FastAPI URL (if needed):**
- Edit `src/main/java/com/moodify/moodify/service/AIServiceClient.java`
- Change line 22: `private static final String FASTAPI_URL = "http://localhost:8000/mood-analysis";`
- Or use environment variable for production

---

### Step 4: Setup Frontend

```bash
# Navigate to frontend directory
cd frontend

# For local development, you can:
# Option 1: Open directly in browser
# Just open index.html in your browser

# Option 2: Use a local server (recommended)
# Using Python:
python -m http.server 3000
# Or using Node.js (if you have it):
npx http-server -p 3000
```

**Update API URL for local development:**
- Edit `frontend/script.js`
- Line 2: Change `API_URL` to `'http://localhost:8080/api/analyse'`

**Verify:** Open http://localhost:3000 (or the port you chose)

---

## 🔧 Configuration Files

### 1. FastAPI `.env` file
**Location:** `fastapi-backend/.env`
```env
GEMINI_API_KEY=your_actual_api_key_here
```

### 2. Spring Boot `application.properties`
**Location:** `moodify/src/main/resources/application.properties`
```properties
spring.application.name=Moodify
server.port=${PORT:8080}
spring.servlet.multipart.max-file-size=10MB
spring.servlet.multipart.max-request-size=12MB
```

### 3. Frontend API Configuration
**Location:** `frontend/script.js`
```javascript
// For local development:
const API_URL = 'http://localhost:8080/api/analyse';

// For production (already configured):
// const API_URL = 'https://moodify-springboot-backend.onrender.com/api/analyse';
```

### 4. Spring Boot FastAPI Client
**Location:** `moodify/src/main/java/com/moodify/moodify/service/AIServiceClient.java`
```java
// For local development:
private static final String FASTAPI_URL = "http://localhost:8000/mood-analysis";

// For production:
// private static final String FASTAPI_URL = "https://moodify-fastapi-backend.onrender.com/mood-analysis";
```

---

## 🐳 Docker Setup (Optional)

### Build and Run Spring Boot with Docker

```bash
cd moodify

# Build Docker image
docker build -t moodify-backend .

# Run container
docker run -p 8080:8080 moodify-backend
```

### Create Dockerfile for FastAPI (if needed)

Create `fastapi-backend/Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## ✅ Verification Checklist

- [ ] Java 17+ installed (`java -version`)
- [ ] Python 3.9+ installed (`python --version`)
- [ ] Maven installed or using `mvnw` wrapper
- [ ] Google Gemini API key obtained
- [ ] `.env` file created in `fastapi-backend/` with API key
- [ ] FastAPI server running on port 8000
- [ ] Spring Boot server running on port 8080
- [ ] Frontend accessible (localhost:3000 or opened directly)
- [ ] API endpoints responding correctly

---

## 🧪 Testing the Setup

### 1. Test FastAPI Backend
```bash
# Health check
curl http://localhost:8000/start-server

# Should return: {"status":"success"}
```

### 2. Test Spring Boot Backend
```bash
# Health check
curl http://localhost:8080/api/health

# Should return: "Healthy"
```

### 3. Test Full Flow
1. Open frontend in browser
2. Upload an image or use camera
3. Click "Analyze Mood"
4. Should see mood detection and song recommendation

---

## 🚨 Troubleshooting

### FastAPI Issues

**Problem:** `ModuleNotFoundError: No module named 'fastapi'`
- **Solution:** Activate virtual environment and install dependencies:
  ```bash
  source venv/bin/activate  # or venv\Scripts\activate on Windows
  pip install -r requirements.txt
  ```

**Problem:** `GEMINI_API_KEY not found`
- **Solution:** Create `.env` file in `fastapi-backend/` directory with your API key

**Problem:** Port 8000 already in use
- **Solution:** Change port: `uvicorn main:app --reload --port 8001`

### Spring Boot Issues

**Problem:** `JAVA_HOME not set`
- **Solution:** Set JAVA_HOME environment variable to your JDK installation path

**Problem:** Port 8080 already in use
- **Solution:** Change port in `application.properties`: `server.port=8081`

**Problem:** Cannot connect to FastAPI
- **Solution:** Ensure FastAPI is running on port 8000, or update `AIServiceClient.java` with correct URL

### Frontend Issues

**Problem:** CORS errors
- **Solution:** Both backends have CORS enabled, but ensure they're running

**Problem:** API calls failing
- **Solution:** Check browser console for errors, verify API URLs are correct

---

## 📊 Port Summary

| Service | Default Port | URL |
|---------|-------------|-----|
| FastAPI Backend | 8000 | http://localhost:8000 |
| Spring Boot Backend | 8080 | http://localhost:8080 |
| Frontend | 3000 (or direct) | http://localhost:3000 |

---

## 🎯 Quick Start Commands

```bash
# Terminal 1: FastAPI
cd fastapi-backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
# Create .env with GEMINI_API_KEY
uvicorn main:app --reload --port 8000

# Terminal 2: Spring Boot
cd moodify
.\mvnw.cmd spring-boot:run  # Windows
# or ./mvnw spring-boot:run  # macOS/Linux

# Terminal 3: Frontend (optional server)
cd frontend
python -m http.server 3000
```

---

## 📝 Summary

**Required APIs:**
- ✅ **Google Gemini API Key** (REQUIRED) - Get from [Google AI Studio](https://aistudio.google.com/)

**Required Software:**
- ✅ Java 17+
- ✅ Python 3.9+
- ✅ Maven 3.6+ (or use mvnw wrapper)

**Optional:**
- Docker (for containerization)
- YouTube API (not needed for current functionality)

**Key Configuration:**
- `.env` file in `fastapi-backend/` with `GEMINI_API_KEY`
- Update API URLs in `script.js` and `AIServiceClient.java` for local development

---

**Need Help?** Check the main [README.md](README.md) for more details.

