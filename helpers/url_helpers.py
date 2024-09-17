import re

def is_valid_url(url):
    """
    URL'nin geçerli olup olmadığını kontrol eder.
    
    :param url: URL adresi
    :return: URL geçerli ise True, değilse False
    """
    pattern = re.compile(
        r'^(?:https?:\/\/)?'  # Başlangıç (isteğe bağlı http:// veya https://)
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}|[A-Z0-9-]{2,}))'  # Alan adı
        r'(?:\/[^\s]*)?$'  # Yol (isteğe bağlı)
        , re.IGNORECASE)

    return re.match(pattern, url) is not None

def ensure_secure_url(url, secure=True):
    """
    URL'yi güvenli hale getirir (http -> https).
    
    :param url: URL adresi
    :param secure: Eğer True ise, URL'yi 'https' yapar. Eğer False ise, 'http' olarak bırakır.
    :return: Güvenli URL
    """
    if not url:
        return url
    
    # URL'nin başında 'http://' veya 'https://' varsa, çıkar
    url = remove_http_https(url)
    
    # URL'nin başına 'https://' ekle
    if secure:
        return f"https://{url}"
    else:
        return f"http://{url}"

def remove_http_https(url):
    """
    URL'den 'http://' veya 'https://' kısımlarını çıkarır.
    
    :param url: URL adresi
    :return: Protokol kısmı çıkarılmış URL
    """
    if url.startswith("https://"):
        return url[len("https://"):]
    elif url.startswith("http://"):
        return url[len("http://"):]
    return url
