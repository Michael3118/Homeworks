import asyncio
import aiohttp
import json

async def fetch_comments(session, url):
    async with session.get(url) as response:
        return await response.json()

async def download_comments(subreddit, start_date, end_date):
    base_url = "https://api.pushshift.io/reddit/comment/search/"
    params = {
        "subreddit": subreddit,
        "after": start_date,
        "before": end_date,
        "sort": "asc",
        "size": 100,
    }

    async with aiohttp.ClientSession() as session:
        comments = []
        while True:
            params["before"] = params["after"]
            response = await fetch_comments(session, base_url + "?" + "&".join(f"{k}={v}" for k, v in params.items()))
            data = response.get("data", [])
            if not data:
                break
            comments.extend(data)
            params["after"] = data[-1]["created_utc"]

        return comments

async def main():
    subreddit = "python"  # Replace with your desired subreddit
    start_date = "1609459200"  # Replace with your desired start date in Unix timestamp
    end_date = "1633084799"  # Replace with your desired end date in Unix timestamp

    comments = await download_comments(subreddit, start_date, end_date)

    with open("reddit_comments.json", "w", encoding="utf-8") as file:
        json.dump(comments, file, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    asyncio.run(main())
