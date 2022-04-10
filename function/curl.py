import pycurl
import json
from io import BytesIO
from urllib.parse import urlencode

def cURLGet(setURL, setHeader):
    c = pycurl.Curl()
    data = BytesIO()

    c.setopt(c.URL, setURL)
    c.setopt(c.HTTPHEADER, setHeader)
    c.setopt(c.WRITEFUNCTION, data.write)
    c.perform()
    c.close()

    if len(data.getvalue()) > 0:
        getData = json.loads(data.getvalue())
        return(getData)
    else:
        getData = "No response data output"
        return(getData)

def cURLPost(setURL, setHeader, setBody, setPost):
    c = pycurl.Curl()
    data = BytesIO()

    c.setopt(c.URL, setURL)
    c.setopt(c.HTTPHEADER, setHeader)
    c.setopt(c.POST, 1)

    if setPost == 'json':
        applyBody = json.dumps(setBody)
        c.setopt(c.POSTFIELDS, applyBody)
    elif setPost == 'url':
        applyBody = urlencode(setBody)
        c.setopt(c.POSTFIELDS, applyBody)

    c.setopt(c.WRITEFUNCTION, data.write)
    c.perform()
    c.close()

    if len(data.getvalue()) > 0:
        getData = json.loads(data.getvalue())
        return(getData)
    else:
        getData = "No response data output"
        return(getData)