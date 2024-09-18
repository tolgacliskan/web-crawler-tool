from controllers.crawler import WebCrawler
from config import ConfigManager
from helpers.url_helpers import is_valid_url, remove_http_https
from urllib.parse import urlparse, parse_qs
from url_parser import parse_url, get_url, get_base_url
import json

def main():

    target_url = input("Geçerli bir URL girin: ").strip()
    while not is_valid_url(target_url):
        print("Geçersiz URL. Lütfen geçerli bir URL girin.")
        target_url = input("Geçerli bir URL girin: ").strip()
    
    project_name = input("Proje adını girin: ").strip()
    while not project_name:
        print("Proje adı belirtilmedi. Lütfen geçerli bir proje adı girin.")
        project_name = input("Proje adını girin: ").strip()

    # parsed = json.dumps(parse_url(target_url), indent=4)
    ConfigManager(target_url, project_name)

    crawler = WebCrawler()
    links = crawler.start()

if __name__ == "__main__":
    main()
