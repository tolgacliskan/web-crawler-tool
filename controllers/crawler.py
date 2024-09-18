import requests
from bs4 import BeautifulSoup
from config import ConfigManager
from urllib.parse import urlparse, urljoin

class WebCrawler:
    def __init__(self):
        self.base_url = ConfigManager.get_base_url()
        self.secure_url = ConfigManager.get_secure_url()
        
    def is_internal_link(self, link):
        parsed_link = urlparse(link)
        if parsed_link.netloc == '' or parsed_link.netloc == self.base_url:
            return True
        return False

    def is_unwanted_protocol(self, href):
        unwanted_protocols = ['mailto:', 'tel:', 'javascript:']
        return any(href.startswith(proto) for proto in unwanted_protocols)
    
    def start(self):
        links = set()
        
        try:
            response = requests.get(self.secure_url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

           # Tüm linkleri topla
            for link in soup.find_all('a', href=True):
                href = link['href'].strip()

                if href.startswith('#') or self.is_unwanted_protocol(href):
                    continue

                if self.is_internal_link(href):
                    if href.startswith('/'):
                        full_url = urljoin(self.secure_url, href)
                    elif not urlparse(href).scheme:
                        full_url = urljoin(response.url, href)
                    else:
                        full_url = href
                    links.add(full_url)
            
            for link in links:
                print(link)
                
            return links

        except requests.RequestException as e:
            print(f"HTTP isteği sırasında bir hata oluştu: {e}")
            return set()
        except Exception as e:
            print(f"Beklenmeyen bir hata oluştu: {e}")
            return set()
