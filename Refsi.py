#fna = 'LTBI_contacts_manuscript.txt'
#fna = 'ApaginProtUTF8.txt'
#fna = 'Liu-461-6.txt'
#fi = open (fna, 'r')
#line = fi.read()
#fi.close()
#rl = line.split('. ')
rl = []
SE = {}
Refsi = {}

UN = []
Ol = []

post_points = [';',',', ':', ')', ']']
ant_points = ['(', '[']
JunkSi = post_points + ant_points + ['a', 'the', 'of', 'and', 'in', 'to']


def replace__points(ls):

    for point in post_points:
        if point in ls:
            ls = ls.replace(point, ' '+point)
    
    for point in ant_points:
        if point in ls:
            ls = ls.replace(point, point+' ')
            
    return ls

def GetRefsi():
    for y in range(len(rl)):
        ls = rl[y]
        ls = ls.strip()
        if len(ls) > 2:
            ls = ls.lower()
            UN.append(ls)
            
    for y in range(len(UN)):
        ls = UN[y]
        ls = replace__points(ls)
        SE[y] = {'ls':ls}
        SE[y]['ss'] = ls.split()
        
        
    for y in range(len(SE)):
        seinx = y
        ss = SE[seinx]['ss']
        for si in ss:
            if si in Refsi:
                Refsi[si] += 1
            else:
                Refsi[si] = 1

    for k, v in Refsi.items():
        si, inci = k, v
        if si not in JunkSi:
            oline = [inci, si]
            Ol.append(oline)

    Ol.sort()
    Ol.reverse()
    print 'GetRefsi: done'

def PrintoutOl():
    for ol in Ol[:20]:
        if ol[0]  == 2:
            break
        print ol[0], ol[1]


    
    
            
    












    

