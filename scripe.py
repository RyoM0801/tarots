
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_images_from_blog(url, save_folder):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')  # <img> タグを含む要素を抽出
        
        for img_tag in img_tags:
            img_url = img_tag.get('src')  # 画像のURLを取得
            if img_url:
                img_url = urljoin(url, img_url)  # 相対URLを絶対URLに変換
                
                # 画像のダウンロード
                img_name = img_url.split("/")[-1]
                img_save_path = os.path.join(save_folder, img_name)
                
                response_img = requests.get(img_url)
                if response_img.status_code == 200:
                    with open(img_save_path, 'wb') as f:
                        f.write(response_img.content)
                    print(f"Image '{img_name}' downloaded successfully.")
                else:
                    print(f"Failed to download image '{img_name}'.")
    else:
        print("Failed to fetch page.")

blog_url = "https://happy-fleama.com/tarot-minor-arcana-wand/"  # ブログ記事のURLを指定
save_folder = "img"  # 画像を保存するフォルダを指定

os.makedirs(save_folder, exist_ok=True)
download_images_from_blog(blog_url, save_folder)
