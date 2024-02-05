import requests
import threading
import json

def fetch_comments(url, params, results):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        comments = response.json().get('data', [])
        results.extend(comments)
    else:
        print(f"Error fetching comments: {response.status_code}")

def download_comments(subreddit, num_threads=5):
    base_url = "https://api.pushshift.io/reddit/comment/search/"
    params = {"subreddit": subreddit, "sort": "desc", "size": 100}

    # List to store all comments
    all_comments = []

    # Create threads
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=fetch_comments, args=(base_url, params, all_comments))
        threads.append(thread)

    # Start threads
    for thread in threads:
        thread.start()

    # Join threads
    for thread in threads:
        thread.join()

    # Sort comments by created_utc in chronological order
    all_comments.sort(key=lambda x: x.get('created_utc', 0))

    # Save comments to a JSON file
    with open(f"{subreddit}_comments.json", "w") as json_file:
        json.dump(all_comments, json_file, indent=2)

if __name__ == "__main__":
    subreddit_name = "your_subreddit_here"  # Replace with the desired subreddit
    download_comments(subreddit_name)
