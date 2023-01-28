import json
import requests

# Substitua <video_id> pelo ID do vídeo da transmissão ao vivo
url = "https://www.youtube.com/live_chat/get_live_chat?video_id=<video_id>"

# Substitua <access_token> pelo seu token de acesso à API do YouTube
headers = {'Authorization': 'Bearer <access_token>'}

response = requests.get(url, headers=headers)
data = json.loads(response.txt)

# Abra o arquivo para escrita
with open('chat.txt', 'w') as f:
    for message in data['items']:
        # Escreva a mensagem e o nome do autor no arquivo
        f.write(message['snippet']['displayMessage'] + ' - ' + message['authorDetails']['displayName'] + '\n')
