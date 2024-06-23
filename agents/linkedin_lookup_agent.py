from dotenv import load_dotenv

load_dotenv()
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.tools import Tool  # Import tool for langchain agent.
from langchain.agents import (
    create_react_agent,  # receive a react prompt and return us an agent based on the react algorithm
    AgentExecutor,  # runtime of agent. obj receives our prompts and instructions and finish tasks
)
from langchain import hub  # premade prompts from the community
from tools.tools import get_profile_url_tavily




def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """Given the full name {name_of_person} I want you to get it me a link to their linkedin profile page.
                Your answer should only contain a URL"""
    # template = """Given the business name {name_of_person} I want you to get it me a link to their business webpage.
    #             Your answer should only contain a URL"""

    prompt_template = PromptTemplate(
        input_variables=["name_of_person"], template=template
    )

    tools_for_agent = [
        Tool(
            name="Crawl Google for Linkedin profile page",
            # name="Crawl Google for a business webpage",
            func=get_profile_url_tavily,
            description="Useful for when you need to get the Linkedin page URL",  # must be consice and clear so it is not ambigous
            # description="Useful for when you need to get the business webpage URL",
        )
    ]

    react_prompt = hub.pull(
        "hwchase17/react"
    )  # https://smith.langchain.com/hub/hwchase17/react
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    linkedin_profile_url = result["output"]
    return linkedin_profile_url


if __name__ == "__main__":
    # linkedin_url = lookup(name="Andrea Aduna Poppy")
    # # linkedin_url = lookup(name="Poppy Kids Pediatric Dentistry")
    # print(linkedin_url)
    print(lookup(name="Eden Marco Udemy"))


# I had issues with function -> func. And I did not install all teh required packages such as langchainhub
# the blue text in result is the actual answer returned.
# does not work for Andrea Aduna. - returns somebody else. However Poppy Kids solidies the search.
