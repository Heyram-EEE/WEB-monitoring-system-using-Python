import requests
import notifier


class getstat:
    def send_error(self,errortext,site,notids):
        notifier.notify(errortext,site,notids)
    def __init__(self,url,txt,notids):
        try:
            res = requests.get(url)
            rcode=res.status_code
            print(rcode)
            if(rcode > 400):
                if(rcode not in [401,403]):
                    self.send_error("Site Not working Error",url,notids)
            elif(txt!=""):
                if txt not in res.text:
                    self.send_error("Text Not Found Error",url,notids)
        except:
            self.send_error("Site Not working Error",url,notids)
