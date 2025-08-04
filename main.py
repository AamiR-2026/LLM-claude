import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain.schema import HumanMessage, SystemMessage

# Load environment variables
load_dotenv()

def main():
    # Initialize Claude model
    llm = ChatAnthropic(
        model="claude-3-sonnet-20240229",  # or claude-3-opus-20240229
        anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"),
        max_tokens=1000,
        temperature=0.7
    )
    
    # Simple chat example
    messages = [
        SystemMessage(content="You are a helpful AI assistant."),
        HumanMessage(content="Explain quantum computing in simple terms.")
    ]
    
    # Get response
    response = llm.invoke(messages)
    print("Claude's Response:")
    print(response.content)
    
    # Interactive chat loop
    print("\n" + "="*50)
    print("Interactive Chat (type 'quit' to exit)")
    print("="*50)
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'quit':
            break
            
        messages = [
            SystemMessage(content="You are a helpful AI assistant."),
            HumanMessage(content=user_input)
        ]
        
        try:
            response = llm.invoke(messages)
            print(f"Claude: {response.content}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()