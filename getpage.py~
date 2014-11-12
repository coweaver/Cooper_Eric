import urllib, urllib2, httplib, base64
import json



headers = {} 
params = urllib.urlencode({'key': 'BB75E8A7-F767-47B0-B17F-BD16E94E3D8B'}) 
conn = httplib.HTTPConnection('api.nfldata.apiphany.com') 

def getInfo(team):
	conn.request("GET", "/trial/json/Players/"+team+"?%s" % params, "",headers) 
	
	response = conn.getresponse() 
	data = response.read() 
	
	d = json.loads(data)
	return d


	

def getTop(d):
	top5 = []

	for player in d:
#		print player
		if(len(top5) == 0):
			top5.append(player)
		
		else:
			top5 = insert(player, top5)
	return top5
		

def insert(player,top5):
	i = 0
	while(i < len(top5)):
                if player["PlayerSeason"] != None:
                        print "success"
                        if player["PlayerSeason"]["FantasyPoints"] > top5[i]["PlayerSeason"]["FantasyPoints"]:
                                print player["Name"]
				x = len(top5) - 1
                                top5.append(player)
                                while(x >= i):
                                        top5[x+1] = top5[x]
                                        x -= 1
				
                                top5[i] = player
				
                                if(len(top5) > 5):
                                        top5 = top5[0:5]
                                        #print top5	
				return top5
                i += 1
	return top5
				
#for player in d:
 #       print player["Name"]
  #      try:
   #             print player["PlayerSeason"]["FantasyPoints"]
    #    except:
     #           print 0


conn.close() 


        
        
