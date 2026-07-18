from .library import *

admin_user_id = 6642473599 #<--- آیدی ادمین
api_id = 32652890 #<--- آی پی آی آیدی
api_hash = 'd643d86f2a2f379addc4c4aa46e81d6c' #<--- ای پی آی هش
helper_username = 'Salselfbot' #<--- یوزر ربات هلپر بدون @
bot_token = '8814285772:AAHc4E_3ixlNeSI7jftK6rJO5aYgGao057U' #<--- توکن ربات هلپر

client_id = '01e7dc6b41c3471b94efe87abeb05919'
client_secret = '4f5f93af1ced4b0d9ba8440606803639'

client = TelegramClient('TRself-MT', api_id, api_hash)
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
