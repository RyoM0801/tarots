import os
import time
import pixabay.core
import urllib.parse

# Pixabay APIキーを設定
PIXABAY_API_KEY = "38825882-45accb416eabc6d382e66cafb"

# init pixabay API
px = pixabay.core(PIXABAY_API_KEY)

# search for notebook, category: computers, color: black, minWidth 100px with safeSearch (more in https://pixabay.com/api/docs/)
notebooks = px.query(
    query = "タロット",
    lang = "ja",
    safeSearch = True
)

# get len of hits len(notebooks)
print("{} hits".format(len(notebooks)))

i = 0
for i in range(len(notebooks)):
    # get image id
    url = notebooks[i].getPageURL()
    title = urllib.parse.unquote(url.split("/")[-2])
    title = title.split("-")[0:-1]
    title = "_".join(title)
    notebooks[i].download("img/"+title+".jpg", "largeImage")
    time.sleep(1)
