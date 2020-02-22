# dic={"2key":1,"1key":1}
# inpt = "I am a little happy face 1key"
# for val in inpt.split():
#     dic[val] = dic.get(val, 0)+1
# print(dic)



# for exp in range(1,8):
#     print(pow(3, exp))
# import re
# print(re.findall(r'\b\d+\b',"he33llo 42 I\'m a 32 string 30"))


# x=35
# for i in range(0, (x+1)):
#     c=i
#     r=x-i
#     if ((c*2)+(r*4)) == 94:
#         print("Chicken :"+str(c)+"  Rabbit :"+str(r))

# a=list(range(100))
# print(a[0:int((len(a)/2)+1):2])

# from urllib.parse import urlparse
# 
# url = 'http://www.mydomain.com:8080/path;params?query=arg#fragments'
# parsed = urlparse(url)
# print('scheme  :', parsed.scheme)
# print('netloc  :', parsed.netloc)
# print('path    :', parsed.path)
# print('params  :', parsed.params)
# print('query   :', parsed.query)
# print('fragment:', parsed.fragment)
# print('username:', parsed.username)
# print('password:', parsed.password)
# print('hostname:', parsed.hostname)
# print('port    :', parsed.port)

# Validate every entity based on our requirement using regular expression

# from urllib.request import Request, urlopen
# 
# url = 'https://www.google.com/search?q=python'
# try:
#     urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}))
#     print("Valid URL")
# except Exception as e:
#     print("Invalid URL ",e)

# a=123123.1
# b=123123.1
# print(type(a))
# print(type(b))
# print(id(a))
# print(id(b))
# print(a is b)
# c=123123.1
# print(id(c))
s={1,2,3,4,5}
fs=frozenset(s)
s.add(6)
print(s.add(7))
print(fs)



