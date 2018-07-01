# Write a module webget.py that exposes a function to download a file from the web in case it does not exist locally already. 
# The function shall have the following signature download(url, to=None) 
#  where the keyword argument  to specifies where to save a file locally and with which name.
#  If to == None then the file shall be saved in the current working directory ./ with the same name as it has at its origin.
#  For example, calling your program as in the following.

# url = 'http://data.kk.dk/dataset/76ecf368-bf2d-46a2-bcf8-adaf37662528/resource/9286af17-f74e-46c9-a428-9fb707542189/download/befkbhalderstatkode.csv'
# webget.download(url)
# will download the remote file to ./befkbhalderstatkode.csv.
# Likely, you will need functions from the standard library modules os, and urllib. For example, read the doc strings for the following functions and implement the given function stub with help of them.


import os
import urllib.request as req
from urllib.parse import urlparse

def download(url, to=None):
    """Download a remote file specified by a URL to a
          local directory.
          :param url: str
              URL pointing to a remote file.
          :param to: str
              Local path, absolute or relative, with a filename
              to the file storing the contents of the remote file.
          """

    # TODO: Implement me!
    filename = os.path.basename(urlparse(url).path)
    if to:
        path = os.path.join(to, filename)
    else:
        path = os.path.join(".", filename)

    if not os.path.isfile(path):
        try:
            req.urlretrieve(url, path)
        except:
            opener = req.build_opener()
            opener.addheaders = [
            ('User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0')]
            req.install_opener(opener)
            req.urlretrieve(url, path)
    return filename