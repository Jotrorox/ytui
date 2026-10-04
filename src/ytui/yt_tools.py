from yt_dlp import YoutubeDL

def search_youtube(query: str, limit: int = 10) -> list[dict]:
    options = {
        "quiet": True,
        "extract_flat": True,
    }

    with YoutubeDL(options) as ydl:
        results = ydl.extract_info(f"ytsearch{limit}:{query}", download = False)

    videos = []

    for video in results.get("entries", []):
        if video:
            videos.append({
                "title": video["title"],
                "channel": video.get("channel"),
                "url": f"https://www.youtube.com/watch?v={video['id']}",
            })

    return videos