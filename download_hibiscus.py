import urllib.request
import json

url = "https://en.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&piprop=original&titles=Roselle_(plant)"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
resp = json.loads(urllib.request.urlopen(req).read().decode())
pages = resp['query']['pages']
for page_id in pages:
    if 'original' in pages[page_id]:
        img_url = pages[page_id]['original']['source']
        print(img_url)
        img_req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(img_req) as img_resp, open('public/images/hibiscus.jpg', 'wb') as out:
            out.write(img_resp.read())
        print("Downloaded hibiscus.jpg")
