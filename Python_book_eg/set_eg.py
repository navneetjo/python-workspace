# example of set
bri = set(['brazil', 'russia', 'india'])
print("case 1:"+ 'india' in bri)

print("usa is present :" + 'usa' in bri)
bric = bri.copy()
bric.add('china')
print("bric :" + str(bric))
print("Bric is super set of bric :" + str(bric.issuperset(bri)))
bri.remove('russia')
print("Bric :" + str(bric))
print("Bri :" + str(bri))