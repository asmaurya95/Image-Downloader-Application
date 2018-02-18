import random
import urllib.request

def image_download(url):
    name=random.randrange(1,1000)
    saveas=(str)(name)+".jpg"
    urllib.request.urlretrieve(url,saveas)


