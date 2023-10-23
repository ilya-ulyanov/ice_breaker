from typing import Tuple

from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from agents.linkedin_lookup_agent import lookup
from output_parsers import person_intel_parser, PersonIntel
from third_parties.linkedin import scrape_linkedin_profile


def ice_break(name: str) -> Tuple[PersonIntel, str]:
    summary_template = """
            Given the LinkedIn information {information} about a person I want you to create:
            1. A short summary
            2. Two interesting facts about them
            \n{format_instructions}
        """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": person_intel_parser.get_format_instructions()
        },
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    profile_url = lookup(name)
    linkedin_data = scrape_linkedin_profile(profile_url=profile_url)
    response = chain.run(information=linkedin_data)
    return person_intel_parser.parse(response), linkedin_data.get("profile_pic_url")


if __name__ == "__main__":
    print("Hello LangChain!")
    result = ice_break("Eden Marco")
    print(result)
