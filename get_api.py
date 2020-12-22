from bs4 import BeautifulSoup
import requests 

# replace testurl.com with the url you want to use.
# requests.get downloads the webpage and stores it as a variable
url = 'http://10.10.24.3:8000/api/'
for i in range(100):
	if i%2==1:
		test_url = url+str(i)
		http = requests.get(test_url)
		if http.status_code != 404:
			print(http.content)