import requests
import json
import concurrent.futures
from multiprocessing import Process, Queue

# Function to download comments from a subreddit
def download_comments(subreddit, queue):
    url = f"https://api.pushshift.io/reddit/comment/search/?subreddit={subreddit}&size=100"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        comments = data['data']
        queue.put(comments)
    else:
        print(f"Failed to fetch comments from subreddit: {subreddit}")

# Function to write comments to a file
def write_to_file(comments, file_path):
    with open(file_path, 'w') as file:
        json.dump(comments, file, indent=4)
    print(f"Comments saved to {file_path}")

if __name__ == "__main__":
    subreddit = "python"  # Choose your subreddit here
    file_path = "comments.json"  # Specify file path to save comments

    # Using multiprocessing to download comments concurrently
    queue = Queue()
    processes = []
    for _ in range(5):  # Adjust number of processes as needed
        process = Process(target=download_comments, args=(subreddit, queue))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    # Collect comments from the queue
    all_comments = []
    while not queue.empty():
        all_comments.extend(queue.get())

    # Write comments to file
    write_to_file(all_comments, file_path)
