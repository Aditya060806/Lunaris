# 🚀 Lunaris Deployment Guide

## 🌐 Deployment Architecture

**Frontend** → **Spring Boot Backend** → **FastAPI Backend**

---

## 📋 Deployment Steps

### 1. Deploy FastAPI Backend (Render)

1. **Go to**: https://render.com
2. **Sign up/Login** with GitHub
3. **New Web Service** → Connect GitHub → Select `Lunaris` repo
4. **Configure**:
   - **Name**: `lunaris-fastapi-backend`
   - **Root Directory**: `fastapi-backend`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. **Environment Variables**:
   - `GEMINI_API_KEY` = `your_actual_api_key`
6. **Deploy** → Copy the URL (e.g., `https://lunaris-fastapi-backend.onrender.com`)

---

### 2. Deploy Spring Boot Backend (Render)

1. **New Web Service** → Connect GitHub → Select `Lunaris` repo
2. **Configure**:
   - **Name**: `lunaris-springboot-backend`
   - **Root Directory**: `moodify`
   - **Runtime**: `Docker`
   - **Build Command**: (leave empty - uses Dockerfile)
   - **Start Command**: (leave empty - uses Dockerfile)
3. **Environment Variables**:
   - `PORT` = `8080`
   - `FASTAPI_URL` = `https://lunaris-fastapi-backend.onrender.com/mood-analysis`
4. **Deploy** → Copy the URL (e.g., `https://lunaris-springboot-backend.onrender.com`)

---

### 3. Deploy Frontend (Vercel)

1. **Go to**: https://vercel.com
2. **Sign up/Login** with GitHub
3. **New Project** → Import `Lunaris` repo
4. **Configure**:
   - **Framework Preset**: `Other`
   - **Root Directory**: `frontend`
   - **Build Command**: (leave empty)
   - **Output Directory**: (leave empty)
5. **Deploy** → Copy the URL (e.g., `https://lunaris.vercel.app`)

---

## 🔧 Configuration Updates Needed

After deployment, update these files with your actual URLs:

### Frontend (`frontend/script.js`)
```javascript
const API_URL = 'https://lunaris-springboot-backend.onrender.com/api/analyse';
```

### Spring Boot (`moodify/src/main/java/.../AIServiceClient.java`)
```java
private static final String FASTAPI_URL = "https://lunaris-fastapi-backend.onrender.com/mood-analysis";
```

---

## 🌟 Alternative Deployment Options

### Option 1: All on Render
- **FastAPI**: Render Web Service
- **Spring Boot**: Render Web Service  
- **Frontend**: Render Static Site

### Option 2: Mixed Platforms
- **FastAPI**: Railway/Heroku
- **Spring Boot**: Railway/Heroku
- **Frontend**: Netlify/Vercel

---

## ✅ Post-Deployment Checklist

- [ ] FastAPI backend responding at `/start-server`
- [ ] Spring Boot backend responding at `/api/health`
- [ ] Frontend loads without errors
- [ ] Image upload works
- [ ] Mood analysis returns results
- [ ] YouTube player works
- [ ] All CORS configured properly

---

## 🔑 Environment Variables Summary

### FastAPI (Render)
```
GEMINI_API_KEY=your_actual_gemini_api_key
```

### Spring Boot (Render)
```
PORT=8080
FASTAPI_URL=https://your-fastapi-url.onrender.com/mood-analysis
```

---

## 🚨 Important Notes

1. **Cold Starts**: Free tier services sleep after inactivity
2. **CORS**: Already configured in both backends
3. **File Size**: 10MB limit for image uploads
4. **API Keys**: Never commit API keys to git

---

## 📞 Need Help?

- Check service logs in Render/Vercel dashboards
- Verify environment variables are set
- Test each service individually
- Check CORS and network connectivity