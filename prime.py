#really basic prime number counter
#input integer, tells you how many primes lead up to that

#input
while True:
    target = input('Please enter an integer above 1: ')
    try:
        int(target)
    except:
        continue
    target = int(target)
    if target > 10000:
        print('Ok, slow down there buckaroo...')
        continue
    elif target < 2:
        continue
    else:
        break

#make list 0-input (for loops take too much processing power?)
#is a list the best?
plist = list()
lindex = 2
while (lindex < target + 1):
    plist.append(lindex)
    lindex += 1
#print(plist)

def getmultiples(v):
    #returns a list of multiples for plist specifically, takes argument as index
    mlist = list() #list of multiples
    m0 = plist[v] #m0 is our target we want multiples of
    m = m0 * 2 #first multiple
    while m < target + 1:
        mlist.append(m) 
        m = m + m0
    return mlist #should return empty list when no multiples between v and target

#loop to take multiples out of our plist
#doesn't take multiples of things already taken out (eg no multilist for 4 or 10), effecient!
index = 0
while True:
    if index >= len(plist):
        break
    multilist = getmultiples(index)
    #is it better to skip this subtraction if multilist is empty?
    #I stole this line from the internet, I don't actually get it
    plist = [y for y in plist if y not in multilist]
    index += 1

print(plist)
print(index)
