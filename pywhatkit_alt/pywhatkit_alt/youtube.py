import yt_dlp


def search_youtube(query):
    """
    Search YouTube and return top 5 video results.

    Args:
        query (str): The search query.

    Returns:
        list: A list of dictionaries with video title and URL.
    """
    ydl_opts = {
        "quiet": True,
        "default_search": "ytsearch5",  # Get top 5 results
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(query, download=False)
        return [
            {"title": vid["title"], "url": vid["webpage_url"]}
            for vid in info["entries"]
        ]


# Example usage
# if __name__ == "__main__":
#     results = search_youtube("Python tutorial")
#     for vid in results:
#         print(f"{vid['title']} - {vid['url']}")
