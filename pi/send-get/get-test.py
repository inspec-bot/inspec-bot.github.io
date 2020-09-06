import requests 
  
# api-endpoint 

urlMain = "http://192.168.137.100/ac"

tempData = 20
tempText = str(tempData)

URL = urlMain + tempText

# sending get request and saving the response as response object 
r = requests.get(url = URL) 
