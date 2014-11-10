import urllib, urllib2, httplib, base64
import json



headers = { 
    # Basic Authorization Sample 
    # 'Authorization': 'Basic %s' % base64.encodestring('{username}:{password}'), 
} 

params = urllib.urlencode({'key': 'BB75E8A7-F767-47B0-B17F-BD16E94E3D8B'}) 

conn = httplib.HTTPConnection('api.nfldata.apiphany.com') 

team = "NYJ"
conn.request("GET", "/trial/json/Players/"+team+"?%s" % params, "", headers) 

response = conn.getresponse() 
data = response.read() 

d = json.loads(data)






for player in d:
        print player["Name"]
        try:
                print player["PlayerSeason"]["FantasyPoints"]
        except:
                print 0
conn.close() 


        
        
