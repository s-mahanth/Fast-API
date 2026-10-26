import requests

# Sample public API endpoint (returns JSON data)
API_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_posts():
    """
    Fetch posts from the sample API.
    Includes error handling for network issues and invalid responses.
    """
    try:
        response = requests.get(API_URL, timeout=5)  # timeout prevents hanging
        response.raise_for_status()  # raises HTTPError for bad status codes

        # Parse JSON safely
        try:
            data = response.json()
        except ValueError:
            print("Error: Response is not valid JSON.")
            return None

        return data

    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        return None

def main():
    posts = fetch_posts()
    if posts:
        print(f"Fetched {len(posts)} posts successfully.\n")
        # Display first 3 posts for training/demo
        for post in posts[:3]:
            print(f"Post ID: {post['id']}")
            print(f"Title: {post['title']}")
            print(f"Body: {post['body']}\n")
    else:
        print("No data retrieved.")

if __name__ == "__main__":
    main()