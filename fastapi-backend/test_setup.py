"""
Quick test script to verify .env configuration
Run this before starting the server to ensure everything is set up correctly
"""
import os
from dotenv import load_dotenv

print("🔍 Testing FastAPI Setup...\n")

# Load .env file
load_dotenv()

# Check if .env file exists
env_file = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(env_file):
    print(f"✅ .env file found at: {env_file}")
else:
    print(f"❌ .env file NOT found at: {env_file}")
    print("   Please create .env file with: GEMINI_API_KEY=your_key")
    exit(1)

# Check API key
api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    # Mask the key for security (show first 7 and last 4 chars)
    masked_key = f"{api_key[:7]}...{api_key[-4:]}" if len(api_key) > 11 else "***"
    print(f"✅ GEMINI_API_KEY found: {masked_key}")
    
    # Check if it looks like a valid Gemini key
    if api_key.startswith("AIza"):
        print("✅ API key format looks correct (starts with AIza)")
    else:
        print("⚠️  Warning: API key doesn't start with 'AIza' - make sure it's correct")
    
    # Test Gemini API connection
    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.5-flash")
        print("✅ Google Generative AI imported successfully")
        print("✅ Model 'gemini-2.5-flash' configured")
    except Exception as e:
        print(f"❌ Error configuring Gemini API: {e}")
        exit(1)
    
    print("\n✅ All checks passed! You're ready to run the server.")
    print("\n📝 Next steps:")
    print("   1. Run: uvicorn main:app --reload --port 8000")
    print("   2. Test: http://localhost:8000/docs")
    print("   3. Test health: http://localhost:8000/start-server")
    
else:
    print("❌ GEMINI_API_KEY not found in .env file")
    print("\n📝 Please add to .env file:")
    print("   GEMINI_API_KEY=your_actual_api_key_here")
    exit(1)

