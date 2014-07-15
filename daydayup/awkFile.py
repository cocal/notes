# -*- coding: utf-8 -*-

## 实现一个批处理行
## 基本上嫩实现一个计数功能了


di = {}
ip2io = {}
def findIp2Io(token):
    ip = token[11]
    io = []
    if ip2io.has_key(ip):
        ios = ip2io.get(ip);
        ios.append(token[13])
        ibs = set(ios)
        ip2io[ip] = list(ibs)
    else :
        io.append(token[13])
        ip2io[ip] = io

io2ip = {}#统计每个接口调用的ip
def findio2ip(token):
    ip = []
    io = token[13]
    if io2ip.has_key(io):
        ips = io2ip.get(io)
        ips.append(token[11])
        io2ip[io] = list(set(ips))
    else :
        ip.append(token[11])
        io2ip[io] = ip


def readData(filename):
    print '---------',filename
    f = open(filename)
    line = '-1'
    while line != '':
        line = f.readline()
        token = line.split(' ')
        if len(token) <= 11:
            print line
            continue
        findIp2Io(token)
        findio2ip(token)
        ip = token[11]
#        print ip 
        if di.has_key(ip) :
            nu = di.get(ip) + 1
            di[ip] = nu
        else :
            di[ip] = 1
    f.close()

filenames = [13,15,16,2] #需要处理的文件名
for x in filenames:
      readData(str(x))      
        
print di
print ip2io
print io2ip
for x in io2ip.iterkeys():
     print x , io2ip[x]


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

