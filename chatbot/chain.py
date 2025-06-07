import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage, SystemMessage
from chatbot.company_profile import get_formatted_info
from chatbot.prompts import project_clarification_prompt

# ✅ Load environment variables
load_dotenv()

# ✅ Initialize the Gemini model via LangChain
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # You can also try "gemini-1.5-pro" if needed
    temperature=0.5,
    convert_system_message_to_human=True  # Makes Gemini treat system message like user message
)

# ✅ System-level assistant setup
SYSTEM_INSTRUCTION = (
    "You are Arvitai Assistant, representing Arvitai Technology, a software service company. "
    "Your job is to explain Arvitai’s services and capabilities, and help clients by suggesting the "
    "right technologies based on their requirements. Ask clarifying questions when needed."
)

def generate_response(user_input: str) -> str:
    normalized = user_input.lower()

    # Direct company info queries
    if any(keyword in normalized for keyword in [
        "about your company", "arvitai", "who are you", "owner", "contact",
        "location", "email", "phone", "services", "what do you offer"
    ]):
        return get_formatted_info()

    # Dynamic response for project-related questions
    try:
        system_msg = SystemMessage(content=SYSTEM_INSTRUCTION)
        user_msg = HumanMessage(content=project_clarification_prompt(user_input))
        
        response = llm.invoke([system_msg, user_msg])
        return response.content.strip()

    except Exception as e:
        return f"❌ Error generating response: {str(e)}"
