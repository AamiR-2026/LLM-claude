print("🔄 Starting connection test...")

import os
print("✅ OS module imported")



from dotenv import load_dotenv
print("✅ dotenv imported")

import anthropic
print("✅ anthropic imported")

# Load environment variables
print("🔄 Loading .env file...")
load_dotenv()
print("✅ .env file loaded")


try:
    # Test API key
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("API key not found in .env file")
        exit(1)
    
    print("✅ API key loaded successfully")
    
    

    client = anthropic.Anthropic(
        api_key=api_key,
       
        default_headers={"User-Agent": "test-client"}
    )
    
    print("🔄 Testing connection to Claude...")
    
   
    message = client.messages.create(
        model="claude-3-5-sonnet-latest",
        max_tokens=50,
        messages=[
            {"role": "user", "content": "Say hello"}
        ]
    )
    
    print("✅ Connection successful!")
    print(f"Claude says: {message.content[0].text}")
    
except Exception as e:
    print(f" Error: {e}")
    