import os
import requests
import xml.etree.ElementTree as ET

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

RSS_URL = "https://rss.app/feeds/D83sSRekfJBBDRPo.xml"

LAST_POST_FILE = "last_post.txt"

rss = requests.get(RSS_URL)

root = ET.fromstring(rss.content)

item = root.find("./channel/item")

title = item.find("title").text
link = item.find("link").text

current_post = link

old_post = ""

if os.path.exists(LAST_POST_FILE):
with open(LAST_POST_FILE, "r") as f:
old_post = f.read().strip()

if current_post != old_post:

```
message = f"""🚨 Nueva publicación de @fedesturze
```

{title}

{link}
"""

```
requests.get(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    params={
        "chat_id": CHAT_ID,
        "text": message
    }
)

with open(LAST_POST_FILE, "w") as f:
    f.write(current_post)

print("Nueva publicación enviada")
```

else:
print("Sin novedades")
