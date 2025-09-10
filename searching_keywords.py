import os
from googleapiclient.discovery import build

API_KEY = "AIzaSyDxupUzs-hnj9Y7mgVyhz5jVEzfYxm1BDA"
CX = "f4d165e8248234d5a"

def google_search(query, api_key, cx, num_results=10):
    service = build("customsearch","v1",developerKey=api_key)

    try:

        res = service.cse().list(
            q=query,
            cx=cx,
            num = num_results
        ).execute()

        search_results = res.get('items',[])
        return search_results
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    
if __name__ == '__main__':
    search_query = "Python programming"
    results = google_search(search_query,API_KEY,CX)

    if results:
        print(f"Search results for '{search_query}: ")
        print("="*30)

        for i, item in enumerate(results):
            print(f"{i+1}. {item.get("title")}")
            print(f"     Link: {item.get('link')}")
            print(f"     Snippet:{item.get('snippet')}\n")

    else:
        print("No results found or an error occurred")