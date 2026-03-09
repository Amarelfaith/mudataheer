import urllib.request
import json
import os

images = {
    "Soybean": "public/images/soybeans.jpg",
    "Ginger": "public/images/ginger.jpg",
    "Hibiscus_tea": "public/images/hibiscus.jpg",
    "Cassava": "public/images/cassava.jpg"
}

os.makedirs('public/images', exist_ok=True)

for title, filename in images.items():
    url = f"https://en.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&piprop=original&titles={title}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
        
        pages = data['query']['pages']
        for page_id, page_data in pages.items():
            if 'original' in page_data:
                img_url = page_data['original']['source']
                print(f"Downloading {title} from {img_url} to {filename}")
                img_req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(img_req) as img_resp, open(filename, 'wb') as out:
                    out.write(img_resp.read())
            else:
                print(f"No original image for {title}")
    except Exception as e:
        print(f"Failed to fetch {title}: {e}")
