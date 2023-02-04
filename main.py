import requests,time,random,json,os,string
def Randstr(count):
    return ''.join(random.choices(string.ascii_letters + string.digits, k = count))
def GenerateParma(roomid):
    random.seed(time.time())
    anid=Randstr(32)
    ssad=str(random.randint(10**37,10**38-1));
    deviceModel="unknown_"+Randstr(3)+"-"+Randstr(3);
    params={"std_nplat":"1","std_rid":str(roomid),"network":"1","streamType":"1-2-7-8","std_bid":"0","sign":"3623e97cefa447e8","ua":"fx-alone-android","ssad":ssad,"appid":"1131","version":"57000","std_anid":anid,"channel":"1503","freeType":"0","platform":"5","std_plat":"1","deviceModel":deviceModel,"std_dev":anid}
    return params;
def DoTheRequest(roomid):
    urls={}
    UrlType= ["hls","rtmp","flv","httpsflv","httpshls","httpsQuicFlv","webrtc"];
    reqheaders ={
        "Accept-Encoding":"gzip, deflate" ,"KG-RC":"1","x-router": "service1.fanxing.kugou.com",
        "Host":"m1fanxing.kugou.com","Connection":"Keep-Alive"
    }
    r = requests.get("http://m1fanxing.kugou.com/video/mo/live/pull/mutiline/streamaddr/v2.json",params=GenerateParma(roomid),headers=reqheaders)
    try:lines=json.loads(r.text)["data"]["roomStreams"][0]["lines"]
    except:return ""
    for x in lines:
        for y in x["streamProfiles"]:
            for z in UrlType:
                try:
                    for i in y[z]:
                        urls[i]=z
                except:pass
    for i in urls.keys():
        print(urls[i],":",i)
#You can find the id in the url.
DoTheRequest(input("ID="))





