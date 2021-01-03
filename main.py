from apiclient.discovery import build

YOUTUBE_API_KEY = "AIzaSyC9_Qh0h12dyM45XkOwI5uez-rbMJYnPvc"


youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

search_response = youtube.search().list(part="snippet",q="ホロライブ",order="videoCount", regionCode="JP" ,type="video").execute()
