import requests


def scrape_linkedin_profile(profile_url: str):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""
    api_endpoint = "https://gist.githubusercontent.com/ilya-ulyanov/a7072ec29a6415bb3ad9a3b01c6ed023/raw/11d97e0f6f336a027eef407afa6506cf4e7529b9/linkedin-profile.json"
    # header_dict = {"Authorization": f'Bearer {os.environ["PROXYCURL_API_KEY"]}'}
    response = requests.get(api_endpoint)

    data = response.json()

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
