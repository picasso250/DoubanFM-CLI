import time, json, urllib2
import os.path
import douban

user = douban.PrivateFM(-3, False, False)
user.login()
print user.liked
d = {}
for i in range(user.liked):
    print i+1
    songlist = user.playlist()
    for s in songlist:
        print s['title'],s['artist']
        for k in s:
            print k, s[k]
        d[s['url']] = s['title']
        fid = str(s['aid'])+'-'+str(s['sid'])
        jf = 'songs/'+fid+'.json'
        print 'write info to', jf
        print json.dumps(s)
        with open(jf, 'w') as f:
            json.dump(s, f)
        mf = 'songs/'+fid+'.'+s['file_ext']
        if os.path.exists(mf):
            print mf, 'downloaded, skip'
            continue
        print 'download from', s['url'], 'to', mf
        f = urllib2.urlopen(s['url'])
        data = f.read()
        with open(mf, "wb") as f:
            f.write(data)
    print 'sleep 10 s to avoid douban anti robot'
    time.sleep(10)

print len(d)


