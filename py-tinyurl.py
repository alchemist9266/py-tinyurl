#!/usr/bin/python3
import urllib.request

#gay
print("#====================================#")
print("[+]py-tinyurl by Leak#5749")
print("[+]Github : https://github.com/leak37")
print("#====================================#")
linkurl = input("[>] URL Link : ")

def tiny_url(url):
    apiurl = "http://tinyurl.com/api-create.php?url="
    tinyurl = urllib.request.urlopen(apiurl + url).read()
    return tinyurl.decode("utf-8")

print(tiny_url(linkurl))