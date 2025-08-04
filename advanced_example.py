import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema import BaseMessage
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# Load environment variables
load_dotenv()

class ClaudeChat:
    def __init__(self):
        self.llm = ChatAnthropic(
            model="claude-3-sonnet-20240229",
            anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"),
            max_tokens=1000,
            temperature=0.7
        )
        
        # Setup memory for conversation
        self.memory = ConversationBufferMemory(return_messages=True)
        
        # Create conversation chain
        self.conversation = ConversationChain(
            llm=self.llm,
            memory=self.memory,
            verbose=False
        )
    
    def chat_with_memory(self, message: str) -> str:
        """Chat with conversation memory"""
        response = self.conversation.predict(input=message)
        return response
    
    def summarize_text(self, text: str) -> str:
        """Summarize long text"""
        prompt = ChatPromptTemplate.from_template(
            "Please provide a concise summary of the following text:\n\n{text}"
        )
        
        chain = prompt | self.llm
        response = chain.invoke({"text": text})
        return response.content
    
    def code_review(self, code: str, language: str = "python") -> str:
        """Review code and provide suggestions"""
        prompt = ChatPromptTemplate.from_template(
            """Please review the following {language} code and provide:
1. Overall assessment
2. Potential issues or bugs
3. Suggestions for improvement
4. Best practices recommendations

Code:
```{language}
{code}
```
"""
        )
        
        chain = prompt | self.llm
        response = chain.invoke({"code": code, "language": language})
        return response.content

def demo_features():
    chat = ClaudeChat()
    
    print("=== LangChain + Claude Advanced Features Demo ===\n")
    
    # 1. Conversation with memory
    print("1. Conversation with Memory:")
    print("User: My name is John and I like programming.")
    response1 = chat.chat_with_memory("My name is John and I like programming.")
    print(f"Claude: {response1}\n")
    
    print("User: What's my name and what do I like?")
    response2 = chat.chat_with_memory("What's my name and what do I like?")
    print(f"Claude: {response2}\n")
    
    # 2. Text summarization
    print("2. Text Summarization:")
    long_text = """
    Artificial intelligence (AI) is intelligence demonstrated by machines, 
    in contrast to the natural intelligence displayed by humans and animals. 
    Leading AI textbooks define the field as the study of "intelligent agents": 
    any device that perceives its environment and takes actions that maximize 
    its chance of successfully achieving its goals. Colloquially, the term 
    "artificial intelligence" is often used to describe machines that mimic 
    "cognitive" functions that humans associate with the human mind, such as 
    "learning" and "problem solving". As machines become increasingly capable, 
    tasks considered to require "intelligence" are often removed from the 
    definition of AI, a phenomenon known as the AI effect.
    """
    
    summary = chat.summarize_text(long_text)
    print(f"Summary: {summary}\n")
    
    # 3. Code review
    print("3. Code Review:")
    sample_code = """
def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

result = calculate_average([1, 2, 3, 4, 5])
print(result)
"""
    
    review = chat.code_review(sample_code)
    print(f"Code Review:\n{review}")

if __name__ == "__main__":
    demo_features()