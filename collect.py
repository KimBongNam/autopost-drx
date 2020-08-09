from riotwatcher import LolWatcher, ApiError

member = ['모찌피치모찌피치', 'DRX 홍창현', '요붕스1', 'DRX Deft', 'DRX Keria']
api_key = 'RGAPI-1e751ed8-a379-41d7-8d2d-e6e4ca9aca6a'
watcher = LolWatcher(api_key)
my_region = 'kr'

rank = [0,0,0,0,0]
point = [0,0,0,0,0]

for i, name in enumerate(member):
    me = watcher.summoner.by_name(my_region, name)
    result = watcher.league.by_summoner(my_region, me['id'])
    rank[i] = result[0]['tier']
    point[i] = result[0]['leaguePoints']

for i in range(5):
    print(member[i],rank[i], point[i])