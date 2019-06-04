from urllib import request, parse

#resp = request.urlopen("https://www.wikipedia.org")
#print(resp.peek())

#data = resp.read()
#print("data type: ", type(data))
#html = data.decode("UTF-8")
#print("html type: ", type(html))
#print(html)

params = {"v": "EuC-yVzHhMI", "t": "5m56s"}
querystring = parse.urlencode(params)
print(querystring)
url = "https://www.youtube.com/watch" + "?" + querystring
print(url)
resp = request.urlopen(url)
print(resp.isclosed())
print(resp.code)
html = resp.read().decode("utf-8")
print(html[:500])
print(resp.isclosed())