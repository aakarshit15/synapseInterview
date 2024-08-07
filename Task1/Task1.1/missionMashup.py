from itertools import combinations as com;

Kevin = {
    "Halsey", "Taylor Swift", "Mitski", "Joji", "Shawn Mendes", "Sabrina Carpenter", "Nicky Minaj", "Conan Gray", "One Direction", "Justin Bieber"
}

Stuart = {
    "Kendrick Lamar", "Steve Lacy", "Tyler the Creator", "Joji", "TheWeekend", "Coldplay", "Kanye West", "Travis Scott", "Frank Ocean", "Brent Faiyaz"
}

Bob = {
    "Conan Gray", "Joji", "Dove Cameron", "Mitski", "Arctic Monkeys", "Steve Lacy", "Kendrick Lamar", "Isabel LaRosa", "Shawn Mendes", "Coldplay"
}

Edith = {
    "Metallica", "Billie Eilish", "TheWeekend", "Mitski", "NF", "Conan Gray", "Kendrick Lamar", "Nicky Minaj", "Kanye West", "Coldplay"
}

djs = {"Kevin": Kevin, "Stuart": Stuart, "Bob": Bob, "Edith": Edith}

djsList = djs.keys()

pairObj = com(djsList, 2)

pairList = [pair for pair in pairObj]

eligiblePairs = []

for pair in pairList:
    comArtist = djs[pair[0]].intersection(djs[pair[1]])
    intersectPercent = (len(comArtist) * 100) / len(djs[pair[0]])
    if intersectPercent >= 30:
        eligiblePairs.append({"pair": pair, "intersectPercent": intersectPercent})

eligiblePairs.sort(key=(lambda pairObj: pairObj["intersectPercent"]), reverse=True)

for pair in eligiblePairs:
    print(pair)