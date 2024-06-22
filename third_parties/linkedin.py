# Scrape linkedin for profile information
import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str) -> str:
    """
    Scrape information from LinkedIn profiles using the Proxycurl API.

    Args:
        linkedin_profile_url (str): The URL of the LinkedIn profile to scrape.

    Returns:
        str: The scraped information from the LinkedIn profile.

    """
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": f'Bearer {os.getenv("PROXYCURL_API_KEY")}'}
    response = requests.get(
        api_endpoint,
        params={"url": linkedin_profile_url},
        headers=header_dic,
        timeout=10,
    )
    # Process the response, e.g., return response.text or response.json()
    data = response.json()
    # snipped to remove empty returned values
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k
        not in ["people_also_viewed", "certifications", "similarly_named_profiles"]
    }
    if data.get("groups"):
        for group in data["groups"]:
            group.pop("profile_pic_url")
    return data


# Test the function
if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/jayozer"
        )
    )
