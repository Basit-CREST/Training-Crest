from urllib import request
import threading


def concurrent_downloader(url,fname):
    print(fname)
    request.urlretrieve(url,fname)
    print("Download succesfully" + str(fname))
downn = r"D:\Python Course\02-Python Practice\W3resource\30-Multi Threading and concurrency\\"
files_to_download = [
    {"url": "https://en.wikipedia.org/wiki/British_logistics_in_the_Normandy_campaign", "filename": downn + "1.html"},
    {"url": "https://en.wikipedia.org/wiki/Graph_(abstract_data_type)", "filename": downn + "2.html"},
    {"url": "https://example.com/", "filename": downn + "3.html"}
]

threads = []

def downloader(info):
    for i in info:
        thread = threading.Thread(target=concurrent_downloader,args=(i["url"],i["filename"]))
        thread.start()
        threads.append(thread)


for i in threads:
    i.join()



downloader(files_to_download)