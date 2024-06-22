# take output and use lanchain output parsers and transform it a list of strings. 

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
from output_parsers import summary_parser


def ice_break_with(name: str) -> str:
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username)

# we add {format_instructions} to use the pydantic schema to represent the output we want the LLM to return us
    summary_template = """
        given the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
        \n{format_instructions}    
            """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template,
        partial_variables={"format_instructions": summary_parser.get_format_instructions()}
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = summary_prompt_template | llm | summary_parser  #LCEL - synthatic sugar for chaining

    res = chain.invoke(input={"information": linkedin_data})

    print(res)


if __name__ == "__main__":
    load_dotenv()

    print("Ice Breaker Enter")

    ice_break_with(name="Jay Ozer")


"""Now with pydantic formatting we get a summary object. get_format_instructions is a method or attribute associated with the LangChain framework.

• get_format_instructions is a function or attribute within the LangChain framework that likely provides instructions or guidelines on how to format input data or interact with certain components of the LangChain system [0,1,5].
• This function or attribute may be used to retrieve formatting instructions for specific tasks or actions within the LangChain environment, helping users understand the expected format for input data or the structure of interactions with LangChain components [0,1,5].
• By calling get_format_instructions, users can access detailed guidance on how to structure their input, queries, or commands to effectively utilize the features and functionalities offered by LangChain agents or tools [0,1,5].

In essence, get_format_instructions serves as a resource within LangChain that provides users with clear instructions on how to format their input data or interactions to make the most of the LangChain framework.
"""