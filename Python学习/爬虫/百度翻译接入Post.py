#!/usr/bin/env python2
# -*- coding:utf-8 -*-
# Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习


import urllib
import urllib2

# 组拼一个post 请求
# 头信息
# url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
url = "http://fanyi.baidu.com/v2transapi"
headers = {
    "User-Agent":"User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "Cookie": "BIDUPSID=A6F06C8E0D8E5C5586BB1663E10D250B; PSTM=1489211070; BAIDUID=82103FDCB2BB469EE3D56E9699DDAFFF:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDRCVFR[mkUqnUt8juD]=mk3SLVN4HKm; H_PS_PSSID=25631_1465_21087_18559_17001_20930; PSINO=2; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[feWj1Vr5u3D]=mk3SLVN4HKm; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1516175867; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1516175867; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D"
      }
# 提交的字段信息
formdata ={
    'from':'en','to':'zh','query':'love',
               'transtype':'translang',
               'simple_means_flag':'3',
                "sign":"244250.481579",
                "token":"6929bf07d3ecaafda9561bc9b5a1d036"
}

formdatas = urllib.urlencode(formdata)
request = urllib2.Request(url,data=formdatas,headers=headers)
print(urllib2.urlopen(request).read())