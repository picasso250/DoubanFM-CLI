import time, json, urllib2
import os.path
import douban

def download_song(n):
    d = {}
    for i in range(user.liked * 4):
        songlist = user.playlist()
        for s in songlist:
            print s['title'],s['artist']
            fid = str(s['aid'])+'-'+str(s['sid'])
            if fid in d:
                continue
            d[fid] = s['title']
            if len(d) == user.liked:
                print 'All', user.liked, 'songs download complete'
                return
            jf = 'songs/'+fid+'.json'
            print 'write info to', jf
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
        print len(d), 'songs complete, sleep 10 s to avoid douban anti robot'
        time.sleep(10)


user = douban.PrivateFM(-3, False, False, True)
print user.liked
download_song(user.liked)
