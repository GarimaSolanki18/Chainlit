import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI


#from langchain_core.messages import HumanMessage, SystemMessage

#from src.config import instruction

load_dotenv()

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

def ask_bot(message):
    
   llm = ChatGoogleGenerativeAI(model="gemini-pro") 
    
   responses = llm.invoke(message)

    #respones=model(
    #[
    #    SystemMessage(content=instruction),
     #   HumanMessage(content=user_message),
    #]
   return responses.content

if __name__== "__main__":
    
    mess=ask_bot("What is capital of India")
    print(mess)