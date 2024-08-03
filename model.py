from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers.string import StrOutputParser
import os



if __name__ == "__main__":
    #load_dotenv()
    print("Hello LangChain")    
    #print(os.environ["OPENAI_API_KEY"])
    prompt=open("website_text.txt","r").read()
    
    summary_template = prompt+"""You are payroll management company operating in UK.Your expertise is exclusively in Bulk Payroll Processing Engine
    Bulk Payroll Processing Engine,Statutory Automation,White Labelled portal,Payroll Grouping,Cloud Infrastructure,Auto Enrolment
    Real-time Reporting to HMRC,Holiday Pay Calculations,HR Management,payroll management,GDPR Compliance.if
    a question is not about brain payroll respond with ,"i can't assist with that,sorry!"
    Question:{information}
    Answer:
                        """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    
    #llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    llm=ChatOllama(model="llama3")

    chain = summary_prompt_template | llm | StrOutputParser()
    
    def query_llm(information):
        print(chain.invoke({'information':information}))

    while True:
        query_llm(input("please ask your question"))
