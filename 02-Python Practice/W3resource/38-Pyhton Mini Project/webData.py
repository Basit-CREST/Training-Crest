from urllib.request import urlopen
import json

class WebData():
   
    def __init__(self, url):
       
        
        self._url   = url
        self._data  = None
        self._readData()
        
    def _readData(self):
        
        webUrl = urlopen(self._url)
        if (webUrl.getcode() == 200):
            self._data = webUrl.read().decode('utf-8')
        else:
            raise ConnectionError("Received an error {} from server, cannot retrieve results ".format(str(webUrl.getcode())))
        return self
    
    def getData(self):
       
        return self._data
    
    def parseJson(self):
        
        return json.loads(self.getData())
