import netflix

print 'start'

api = netflix.NetflixAPI(api_key='y56g4wvr49qkecdkw6uev66p',
               api_secret='FKA3C3Zcjv')

d = api.get("catalog/titles/autocomplete", {"term" : "spider"})

for title_info in d['autocomplete']['autocomplete_item']:
	print title_info['title']['short']

print 'finish'