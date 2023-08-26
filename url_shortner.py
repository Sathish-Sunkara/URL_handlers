import hashlib
#--------------------------------------------------------
class URL:
    def __init__(self):
        self.hashh = hashlib.sha256()
        self.dic = {}
        
    def short(self,long_url):
        self.hashh.update(long_url.encode())
        url = self.hashh.hexdigest()[:8]
        self.dic[url] = long_url
        return url
    
    def long(self,short_url):
        return self.dic[short_url]
        
       # ---------------------------------------------------------------------------------

shortner = URL()       
while True:
    print("1. short \n 2. long")
    n= int(input())
    if n == 1:
        url = input("enter your url")
        print("shrt url : ")
        print(shortner.short(url))
    else:
        url = input("enter your url")
        print("long url : ")
        print(shortner.long(url))
    print("do you want to continue")
    ch = int(input())
    if ch:
        continue
    else:
        break
        

