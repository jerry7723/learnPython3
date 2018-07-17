#!/usr/bin/python3
# -*- coding : utf-8 -*-

# https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=8&nc=1531815954317&pid=hp

import urllib
import urllib.request
import ssl
import time
import json
import os.path


class BingBgdownLoader(object):
    _bing_interface = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=%d&nc=%d&pid=hp'
    _bing_url = 'https://cn.bing.com'
    _img_name = '[%s%s][%s].%s'

    def __init__(self):
        super(BingBgdownLoader, self).__init__()
        # self.arg = arg
        ssl._create_default_https_context = ssl._create_unverified_context

    def download(self, num=1, local_path='./'):
        if num < 1:
            num = 1
        url = self._bing_interface % (num, int(time.time()))
        img_infos = self._get_img_infos(url)
        for info in img_infos:
            print(self._get_img_url(info))
            self._down_img(self._get_img_url(info), local_path+self._get_img_filename(info))

    #         请求接口获取图片信息
    def _get_img_infos(self, url):
        request = urllib.request.urlopen(url).read()
        bgObj = json.loads(bytes.decode(request))
        return bgObj['images']

    #     下载图片
    def _down_img(self, url, pathname):
        data = urllib.request.urlopen(url).read()
        f = open(pathname, 'wb')
        f.write(data)
        f.close()
        print('success saved img:', url)

    #     根据info获取文件url
    def _get_img_url(self, info):
        return self._bing_url+info['url']

    #     根据info获取文件名
    def _get_img_filename(self, info):
        zh_name = ''
        pos = info['copyright'].index('(')
        if pos < 0:
            zh_name = info['copyright']
        else:
            zh_name = info['copyright'][0:pos]
        entmp = info['url']
        en_name = entmp[entmp.rindex('/') + 1:entmp.rindex('_ZH')]
        ex_name = entmp[entmp.rindex('.') + 1:len(entmp)]
        pix = entmp[entmp.rindex('_') + 1:entmp.rindex('.')]
        return self._img_name % (zh_name, en_name, pix, ex_name)


if __name__ == '__main__':
    dl = BingBgdownLoader()
    dl.download(8)
