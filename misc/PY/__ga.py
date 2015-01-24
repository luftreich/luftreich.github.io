#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
VISITOR = str(randint(0, 0x7fffffff))
                    
VERSION = "1.7.7"
PATH = "LUFTREICH"            
UATRACK="UA-58829288-1" 

class Track:

    def __init__( self ):

        self.GA("None","Atrix")
        # self.GA("Atrix","7SS-MXB")

        # notify user
        print "All is Over !"

    def send_request_to_google_analytics(self, utm_url):
##        ua='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
        ua='Mozilla/5.0 (Linux; U; Android 2.2.2; de-de; MB860 Build/OLYFR_U4_1.8.3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'

        # print (ua)
        import urllib2
        try:
            print (utm_url)
            req = urllib2.Request(utm_url, None,
                                        {'User-Agent':ua}
                                         )
            response = urllib2.urlopen(req).read()
            print (response)

        except:
            print ("GA fail: %s" % utm_url)         
        return response
           
    def GA(self, group, name):
            try:
                try:
                    from hashlib import md5
                except:
                    from md5 import md5
                from random import randint
                import time
                from urllib import unquote, quote
                from os import environ
                from hashlib import sha1
                utm_gif_location = "http://www.google-analytics.com/__utm.gif"
                if not group=="None":
                        utm_track = utm_gif_location + "?" + \
                                "utmwv=" + VERSION + \
                                "&utmn=" + str(randint(0, 0x7fffffff)) + \
                                "&utmsr=" + "540x960" + \
                                "&utmul=" + "zh-cn" + \
                                "&utmdt=" + "思想的天空" + \
                                "&utmt=" + "event" + \
                                "&utme="+ quote("5("+PATH+"*"+group+"*"+name+")")+\
                                "&utmp=" + quote(PATH) + \
                                "&utmac=" + UATRACK + \
                                "&utmcc=__utma=%s" % ".".join(["1", VISITOR, VISITOR, VISITOR,VISITOR,"2"])
                        try:
                            print "============================ POSTING TRACK EVENT ============================"
                            self.send_request_to_google_analytics(utm_track)
                        except:
                            print "=========================  CANNOT POST TRACK EVENT ==========================" 
                if name=="None":
                        utm_url = utm_gif_location + "?" + \
                                "utmwv=" + VERSION + \
                                "&utmn=" + str(randint(0, 0x7fffffff)) + \
                                "&utmsr=" + "540x960" + \
                                "&utmul=" + "zh-cn" + \
                                "&utmdt=" + "思想的天空" + \
                                "&utmp=" + quote(PATH) + \
                                "&utmac=" + UATRACK + \
                                "&utmcc=__utma=%s" % ".".join(["1", VISITOR, VISITOR, VISITOR, VISITOR,"2"])
                else:
                    if group=="None":
                           # print "group -> None"
                           utm_url = utm_gif_location + "?" + \
                                    "utmwv=" + VERSION + \
                                    "&utmn=" + str(randint(0, 0x7fffffff)) + \
                                    "&utmsr=" + "540x960" + \
                                    "&utmul=" + "de-de" + \
                                    "&utmdt=" + "Wir_aber_besitzen_im_Luftreich_des_Traums" + \
                                    "&utmp=" + quote(PATH+"/"+name) + \
                                    "&utmac=" + UATRACK + \
                                    "&utmcc=__utma=%s" % ".".join(["1", VISITOR, VISITOR, VISITOR, VISITOR,"2"])
                    else:
                           utm_url = utm_gif_location + "?" + \
                                    "utmwv=" + VERSION + \
                                    "&utmn=" + str(randint(0, 0x7fffffff)) + \
                                    "&utmsr=" + "540x960" + \
                                    "&utmul=" + "zh-cn" + \
                                    "&utmdt=" + "思想的天空" + \
                                    "&utmp=" + quote(PATH+"/"+group+"/"+name) + \
                                    "&utmac=" + UATRACK + \
                                    "&utmcc=__utma=%s" % ".".join(["1", VISITOR, VISITOR, VISITOR, VISITOR,"2"])
                                    
                print "============================ POSTING ANALYTICS ============================"
                self.send_request_to_google_analytics(utm_url)
                
            except:
                print "================  CANNOT POST TO ANALYTICS  ================" 



if ( __name__ == "__main__" ):
    Track()

