from controllers.crawler import WebCrawler
from config import ConfigManager
from helpers.url_helpers import is_valid_url, remove_http_https

def main():
    # Kullanıcıdan geçerli URL'yi al
    while True:
        target_url = input("Geçerli bir URL girin: ").strip()
        if is_valid_url(target_url):
            # HTTP/HTTPS kısımlarını temizle
            target_url = remove_http_https(target_url)
            break
        else:
            print("Geçersiz URL. Lütfen geçerli bir URL girin.")

    # Kullanıcıdan geçerli proje adını al
    project_name = input("Proje adını girin: ").strip()
    while not project_name:
        print("Proje adı belirtilmedi. Lütfen geçerli bir proje adı girin.")
        project_name = input("Proje adını girin: ").strip()

    # ConfigManager ile konfigürasyonları ayarla
    ConfigManager(target_url, project_name)

    # Crawler'ı başlat ve linkleri topla
    crawler = WebCrawler()
    links = crawler.get_links_and_save_html()

    # İşlemler tamamlandıktan sonra kullanıcıya geri dönüş
    print(f"Tarama tamamlandı. Toplam {len(links)} link bulundu.")
    input("Kapatmak için Enter'a basın...")

if __name__ == "__main__":
    main()
