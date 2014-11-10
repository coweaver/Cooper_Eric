import urllib2
import json


url = """
http://fantasysports.yahooapis.com/fantasy/v2/users;use_login=1/games;game_keys=nfl/teams
"""

consumer_data = 
consumer_data['test']['key'] = 'dj0yJmk9YTRxSTlkWG5heHBhJmQ9WVdrOWMwWlFNazFZTkdFbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD04Mg--' 
consumer_data['test']['secret'] = '8295393164313926944a1b7209ed6c996d74828d'



scope = 'test'

rlist = d['responseData']['results']

request = urllib2.urlopen(url)
result = request.read()
d = json.loads(result)

for r in rlist:
	print r['titleNoFormatting']
	print r['url']







