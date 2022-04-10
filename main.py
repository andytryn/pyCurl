from function.curl import *

appGetUrl = "https://httpbin.org/get"
appPostUrl = "https://httpbin.org/post"
appHeader = [
    "Accept: application/json",
    "Content-type: application/json",
    "User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Mobile/15E148 Snapchat/10.77.5.59 (like Safari/604.1)"
]
appBody = {'field': 'value'}

# Example: GET Method
getOutput = cURLGet(appGetUrl, appHeader)
print(getOutput)

# Example: POST Method
# json = json post 
# url = url post
postOutput = cURLPost(appPostUrl, appHeader, appBody, 'json')
print(postOutput)