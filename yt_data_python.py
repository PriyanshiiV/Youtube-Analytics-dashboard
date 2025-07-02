from googleapiclient.discovery import build
import pandas as pd

api_key = "AIzaSyAF393nCflyXQ2WiICehnrHPUdciAcHaz0"

youtube = build('youtube', 'v3', developerKey=api_key)

def get_channel_stats(youtube, channel_ids):
    all_data = []

    for channel_id in channel_ids:
        request = youtube.channels().list(
            part='snippet,contentDetails,statistics',
            id=channel_id
        )
        response = request.execute()
        
        for item in response['items']:
            data = {
                "channelName": item['snippet']['title'],
                "subscribers": int(item['statistics']['subscriberCount']),
                "views": int(item['statistics']['viewCount']),
                "totalVideos": int(item['statistics']['videoCount']),
                "channelId": item['id']
            }
            all_data.append(data)
    
    return pd.DataFrame(all_data)

# List of channel IDs
channel_ids = [
    "UC_x5XG1OV2P6uZZ5FSM9Ttw",  # Google Developers
    "UCsT0YIqwnpJCM-mx7-gSA4Q",  # TEDx Talks
    "UCWOA1ZGywLbqmigxE4Qlvuw",  # Netflix
    "UC295-Dw_tDNtZXFeAPAW6Aw",  # 5-Minute Crafts
    "UCqwUrj10mAEsqezcItqvwEw"   # BB Ki Vines
]

df = get_channel_stats(youtube, channel_ids)
df.to_csv("multi_channel_stats.csv", index=False)
print(df)
