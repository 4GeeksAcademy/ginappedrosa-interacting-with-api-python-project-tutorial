import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import numpy as np

# load the .env file variables
load_dotenv()

# Get credential values
# client_id = 'b57d070520064b218ca246119cd2a5be'
# client_secret = 'e6fe12efd09a437f919ff17997aa5e2e'

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

# spotipy.Spotify()
ml_uri = 'spotify:artist:3muH0fOWJZ2SaxK3agdOMD'
sp = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret))

#Get the tracks Top 10 and Filter

results = sp.artist_top_tracks(ml_uri)

# for track in results['tracks'][:10]:
    # print('track    : ' + track['name'])
    # print('cover art: ' + track['album']['images'][0]['url'])
    # print()

# for track in results['tracks'][:10]:
    # print(track['name'])
    # print(track['duration_ms'])
    # print(track['popularity'])

songs = []

for track in results['tracks'][:10]:
    song_info = {
        'name': track['name'],
        'duration_ms': track['duration_ms'],
        'popularity': track['popularity']
    }

    songs.append(song_info)
df = pd.DataFrame(songs)

print(df)

df_sorted = df.sort_values(by="popularity", ascending=False)
top_3 = df_sorted.head(3)

print(top_3)


plt.scatter(df['duration_ms'], df['popularity'])
plt.xlabel('Duración (ms)')
plt.ylabel('Popularidad')
plt.title('Popularidad vs duración')
plt.show()


print("COMENTARIO: Vemos error en el top 10 por popularidad ya que el número 3 debería ser el 2")
print("No se observa relación directa entre la popularidad y la duración de la canción, de hecho las canciones más populares suelen ser las más cortas a nivel de duración")
# print(os.getenv('VARIABLE_NAME'))