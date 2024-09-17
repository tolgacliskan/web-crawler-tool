import requests
from bs4 import BeautifulSoup
from config import ConfigManager
from helpers.url_helpers import remove_http_https, ensure_secure_url

class WebCrawler:
    def __init__(self):
        # ConfigManager'dan base URL ve proje adını al
        self.base_url = remove_http_https(ConfigManager.get_target_url())
        self.project_name = ConfigManager.get_project_name()
        
        # Base URL'yi güvenli hale getir
        self.secure_url = ensure_secure_url(self.base_url)

    def get_links_and_save_html(self):
        """
        Verilen base URL'deki tüm linkleri toplar ve konsola yazdırır.
        """
        links = set()
        
        try:
            # Base URL'ye istek gönder
            response = requests.get(self.secure_url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            # Tüm linkleri topla
            for link in soup.find_all('a', href=True):
                href = link['href']
                # Linklerin tam URL olup olmadığını kontrol et ve gerekli protokolü ekle
                href = ensure_secure_url(href)
                links.add(href)
            
            # Toplanan linkleri konsola yaz
            for link in links:
                print(link)
                
            return links

        except requests.RequestException as e:
            print(f"HTTP isteği sırasında bir hata oluştu: {e}")
            return set()
        except Exception as e:
            print(f"Beklenmeyen bir hata oluştu: {e}")
            return set()


from bs4 import BeautifulSoup
import requests
from config import ConfigManager  # ConfigManager import edilmelidir

class WebCrawler:
    def __init__(self):
        self.base_url = ConfigManager.get_target_url()
        self.project_name = ConfigManager.get_project_name()

    def get_links_and_save_html(self):
        # Taranacak URL'yi istek yaparak içeriği alın
        response = requests.get(self.base_url)
        if response.status_code != 200:
            print(f"Error: Unable to fetch the URL. Status code: {response.status_code}")
            return set()

        # HTML içeriği BeautifulSoup ile parse edin
        soup = BeautifulSoup(response.text, 'html.parser')

        # Linkleri toplamak için bir set oluşturun
        links = set()

        # Tüm linkleri topla
        for link in soup.find_all('a', href=True):
            href = link['href']
            # Linkleri olduğu gibi al
            links.add(href)

        # Toplanan linkleri konsola yazdır
        for link in links:
            print(link)

        return links
