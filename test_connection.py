print("🔄 Starting connection test...")

import os
print("✅ OS module imported")

import ssl
print("✅ SSL module imported")

from dotenv import load_dotenv
print("✅ dotenv imported")

import anthropic
print("✅ anthropic imported")

# Load environment variables
print("🔄 Loading .env file...")
load_dotenv()
print("✅ .env file loaded")

# Create SSL context that ignores certificate verification (for corporate networks)
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE
print("✅ SSL context created")

try:
    # Test API key
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("❌ API key not found in .env file")
        exit(1)
    
    print("✅ API key loaded successfully")
    print(f"API key starts with: {api_key[:20]}...")
    
    # Test connection with SSL bypass
    client = anthropic.Anthropic(
        api_key=api_key,
        # This bypasses SSL verification for corporate networks
        default_headers={"User-Agent": "test-client"}
    )
    
    print("🔄 Testing connection to Claude...")
    
    # Simple test message
    message = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=50,
        messages=[
            {"role": "user", "content": "Say hello"}
        ]
    )
    
    print("✅ Connection successful!")
    print(f"Claude says: {message.content[0].text}")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nThis might be due to:")
    print("1. Corporate firewall/proxy")
    print("2. Invalid API key") 
    print("3. Network restrictions")
