#!/usr/bin/env python
# coding=utf-8
import web
import urllib
import sys
import StringIO
import gzip
import os

reload(sys)
sys.setdefaultencoding('utf-8')

urls = (
        '/ios/(.*)','ios',
        '/(.*)','index'
)
class index:
    def GET(self,name):
        return urllib.urlopen('https://raw.github.com/superior2008/dist/master/index.html').read()

class ios:
    def GET(self,name):
        ext=name.split(".")[-1]
        ctype={
            "ipa":"application/octet-stream",
            "plist":"application/x-plist"
        }
        if name in os.listdir("ios"):
            web.header("Content-Type",ctype[ext])
            return open("ios/%s"%name,"rb")
        else:
            raise web.notfound()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()