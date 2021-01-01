import facebook
graph = facebook.GraphAPI(access_token="<insert access token here>", version="8.0")
stream_url = graph.put_object(parent_object='me',connection_name='live_videos',status='LIVE_NOW')['stream_url']
print(stream_url)
stream_url_key = stream_url.split(':443/rtmp/')[1]
print(stream_url_key)
