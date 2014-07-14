# -*- coding: utf-8 -*-

## 实现一个批处理行
## 基本上嫩实现一个计数功能了
f = open('1')

di = {}
line = f.readline()
while line != "" :
    token = line.split(' ')
    if len(token) <= 11:
        print line
        continue
    ip = token[11]
    print ip 
    if di.has_key(ip) :
        nu = di.get(ip) + 1
        di[ip] = nu
    else :
        di[ip] = 1
    line = f.readline()
f.close()
print di


# str = r"'2014-07-12 00:00:00,799', 'INFO', 'WebContainer : 5', 'webservice.interceptor.IpInterceptor', 'IP拦截器开始  IP : 101.101.101.101 请求接口 :HELO'"
# token = str.split(' ')
# print token[11]
# ip = token[11]
# if di.has_key(ip) :
#     nu = di.get(ip) + 1
#     di[ip] = nu
# else :
#     di[ip] = 1
# print di

