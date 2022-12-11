#C:\Users\1\source\repos
import urllib.request, urllib.error, urllib.parse
import re

url = str (input ("Enter url:"))

#url = 'https://rgsu.net/for-students/tsentralizovannyy-dekanat-1/'

response = urllib.request.urlopen(url)
webContent = response.read().decode('UTF-8')
result = re.findall(r'[\w\.-]+@[\w\.-]+(?:\.[\w]+)+', webContent)
print(result[0])
print(result)