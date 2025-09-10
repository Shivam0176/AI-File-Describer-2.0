import os
from googleapiclient.discovery import build
from dotenv import dotenv_values
env_vars = dotenv_values(".env")

API_KEY = env_vars.get("Google_Search_Engine_API_key")
CX = env_vars.get("Engine_ID")

def google_search(keywords, api_key=API_KEY, cx=CX, num_results=10):

    query_string = " ".join(keywords)

    service = build("customsearch","v1",developerKey=api_key)

    try:

        res = service.cse().list(
            q=query_string,
            cx=cx,
            num = num_results
        ).execute()

        search_results = res.get('items',[])
        return search_results
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    
if __name__ == '__main__':
    keywords = ['thedigital marketing landscape includes various platforms', '• search engine marketing done either', 'yahoo !, india times', 'page views per month', 'follow anyone without seeking', 'thus getting higher ctr', 'user even without following', 'digital marketing strategy helps', 'hence marketing objectives must', 'different parts like seo']
    results = google_search(keywords,API_KEY,CX)

    if results:
        # print(f"Search results for '{search_query}: ")
        print("="*30)

        for i, item in enumerate(results):
            print(f"{i+1}. {item.get("title")}")
            print(f"     Link: {item.get('link')}")
            print(f"     Snippet:{item.get('snippet')}\n")

    else:
        print("No results found or an error occurred")