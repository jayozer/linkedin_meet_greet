# Agent erform actions on my behalf and interact with an LLM. Make API calls to make complex applications. 
# Agent uses tools. Tool connects langchain parties with external parties. Agent uses LLM to do a list of tasks
# Agent is build with a REACT framework. Agent will get a name as an input, search linkedin and get the link of that person's linkedin page. 

from dotenv import load_dotenv

from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
# from langchain.chains import LLMChain

# Add the helper functions to the agent
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

def ice_break_with(name:str) -> str:
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username)

    summary_template = """
        given the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
            """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    
    # chain = LLMChain(llm=llm, prompt=summary_prompt_template)  # this is depreciated.
    chain = summary_prompt_template | llm
    
    res = chain.invoke(input={"information": linkedin_data})
    
    print(res)

if __name__ == "__main__":
    load_dotenv()

    print("Ice Breaker Enter")

    ice_break_with(name="Jay Ozer")


#LLMChain is depreciated. Commented out. 