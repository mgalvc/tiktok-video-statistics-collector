from TikTokApi import TikTokApi
import sys

try:
  video_url = sys.argv[1]
  video_id = video_url.split('/')[-1]
except IndexError:
  print('Error: Please provide the video URL')
  exit()

with TikTokApi() as api:
  try:
    print(f'Info: Collecting stats for video of ID {video_id}')
    video_stats = api.video(id=video_id).info()['stats']
  except Exception as e:
    print(f'Error: An error occurred when trying to fetch the video -- {e}')
    exit()
  
  print(f"Views: {video_stats['playCount']}")
  print(f"Comments: {video_stats['commentCount']}")
  print(f"Likes: {video_stats['diggCount']}")
  print(f"Shares: {video_stats['shareCount']}")