# https://github.com/baptisteCanac/urlShortener/
import urllib.request

def tiny_url(url):
    apiurl = "https://tinyurl.com/api-create.php?url="
    tinyurl = urllib.request.urlopen(apiurl + url).read()
    return tinyurl.decode("utf-8")

url = input("Enter your url to shorten : ")
print("Voici votre nouvel url : ", tiny_url(url))
