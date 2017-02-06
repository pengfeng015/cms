#/usr/bin/env python
#coding=utf8
 
import httplib
import md5
import urllib
import random
import json

appid = '20170206000038641'
secretKey = 'AvtF0UjkaL3lS63pZO5U'
myurl = '/api/trans/vip/translate'
 
# httpClient = None
#
# q = '百度翻译API通过HTTP\\n接口对外提供多语种互译服务'
# fromLang = 'zh'
# toLang = 'en'
# salt = random.randint(32768, 65536)
# print 'salt:',salt
# sign = appid+q+str(salt)+secretKey
# print 'Sign:',sign
# m1 = md5.new()
# m1.update(sign)
# sign = m1.hexdigest()
# myurl = myurl+'?appid='+appid+'&q='+urllib.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
#
# try:
#     httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
#     httpClient.request('GET', myurl)
#
#     #response是HTTPResponse对象
#     response = httpClient.getresponse()
#     resut = response.read()
#     jsonresult = json.loads(resut)
#     print jsonresult
#     print jsonresult['trans_result'][0]['dst']
#     print type(jsonresult['trans_result'][0])
# except Exception, e:
#     print e
# finally:
#     if httpClient:
#         httpClient.close()


def baidu_translate (query,fromLang,toLang) :
    httpClient = None
    salt = random.randint(32768, 65536)
    sign = appid + query + str(salt) + secretKey
    m1 = md5.new()
    m1.update(sign)
    sign = m1.hexdigest()
    myurl = '/api/trans/vip/translate' + '?appid=' + appid + '&q=' + urllib.quote(query) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
    print myurl
    try:
        httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        resut = response.read()
        jsonresult = json.loads(resut)
        print jsonresult
        print jsonresult['trans_result'][0]['dst']
        print type(jsonresult['trans_result'][0])
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()

baidu_translate('新加坡','zh','en')