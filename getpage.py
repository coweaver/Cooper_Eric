import urllib, urllib2, httplib, base64
import json


headers = { 
    # Basic Authorization Sample 
    # 'Authorization': 'Basic %s' % base64.encodestring('{username}:{password}'), 
} 

params = urllib.urlencode({'key': 'BB75E8A7-F767-47B0-B17F-BD16E94E3D8B'}) 

try:
        conn = httplib.HTTPConnection('api.nfldata.apiphany.com')
        # Specify values for path parameters (shown as {...}) and request body if needed 

        team = "NYJ"
        conn.request("GET", "/trial/json/Players/"+team+"?%s" % params, "", headers)
        response = conn.getresponse()
        conn.request("GET", "/trial/json/Player/732?%s" % params, "", headers) 
       
        data = response.read()
        
        print(data) 
        conn.close()
except ValueError:
        print "Oops! didn't work"


