import streamlit as st
import requests

# Set your NewsAPI key here
API_KEY = "3adb597335b3456b896666fa9a244786"

# Base URL for NewsAPI
BASE_URL = "https://newsapi.org/v2/top-headlines"

# Supported countries
COUNTRIES = {
    "USA": "us",
    "India": "in",
    "United Kingdom": "gb",
    "Canada": "ca",
    "Australia": "au"
}

def get_news(country, category):
    params = {
        "apiKey": API_KEY,
        "country": country,
        "category": category,
        "pageSize": 10  # Number of articles
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

def main():
    st.set_page_config(page_title="NewsApp", page_icon="📰")
    st.title("🗞️ Live News with NewsAPI")

    country_name = st.selectbox("Choose Country", list(COUNTRIES.keys()))
    category = st.selectbox("Choose Category", [
        "general", "business", "entertainment", "health", "science", "sports", "technology"
    ])

    if st.button("Get News"):
        country_code = COUNTRIES[country_name]
        news_data = get_news(country_code, category)

        if news_data["status"] == "ok":
            articles = news_data.get("articles", [])
            if articles:
                for article in articles:
                    st.subheader(article["title"])
                    if article.get("urlToImage"):
                        st.image(article["urlToImage"], use_column_width=True)
                    st.write(article["description"] or "No description provided.")
                    st.markdown(f"[Read more]({article['url']})")
                    st.markdown("---")
            else:
                st.warning("No articles found for the selected category.")
        else:
            st.error("Failed to fetch news. Please check your API key or try again later.")

if __name__ == "__main__":
    main()
