try:
	import json,sys,requests,re,os
	from requests import post,get
	from time import time
	from secrets import token_hex
	from random import choice
	from threading import Lock
	from time import sleep
except Exception as Joker:
	input(Joker);sys.exit()
def slow(J):
	for qTr in J + '\n':
		sys.stdout.write(qTr)
		sys.stdout.flush()
		sleep(1. / 80)
class RSP:
	def Login():
		return 'logged_in_user'
	def BDpes():
		return '"error_type":"bad_password"'
	def BDusr():
		return '"exception_name":"UserInvalidCredentials"'
	def BadLog():
		return '"Please wait a few minutes before you try again."'
class REQUESTS:
	def UUID():
		lst='QAZ123WSX456EDC789RFV012TGV345YHBUJN678IKLPO0'
		return str(str(''.join((choice(lst) for i in range(8))))+'-'+str(''.join((choice(lst) for i in range(4))))+'-'+str(''.join((choice(lst) for i in range(4))))+'-'+str(''.join((choice(lst) for i in range(4))))+'-'+str(''.join((choice(lst) for i in range(12)))))
	def HEADERS(uuids):
		return {"X-FB-Client-IP" : "True","X-IG-Connection-Type" : "WiFi","Accept-Language" : "en-EN;q=1.0","x-fb-rmd" : "state=URL_ELIGIBLE","Host" : "i.instagram.com","X-IG-Capabilities" : "36r/F/8=","X-Bloks-Version-Id" : str(token_hex(8)*4),"X-IG-App-Locale" : "en","X-IG-ABR-Connection-Speed-KBPS" : "130","X-IG-Timezone-Offset" : "10800","X-IG-Mapped-Locale" : "en_EN","Connection" : "keep-alive","X-IG-App-ID" : "124024574287414","X-FB-Friendly-Name" : "api","X-IG-Bandwidth-Speed-KBPS" : "303.000","X-Bloks-Is-Panorama-Enabled" : "true","Priority" : "u=2, i","X-Pigeon-Rawclienttime" : str(time()),"User-Agent" : "Instagram 275.0.0.17.100 (iPhone8,1; iOS 13_5; en_JO; en-JO; scale=2.00; 750x1334; 457382757) AppleWebKit/420+","X-IG-Family-Device-ID" : uuids,"X-MID" : "ZK0F5gAAAAFe8doHU5fRFe4Tx8Qa","X-Tigon-Is-Retry" : "False","Content-Length" : "860","X-FB-Connection-Type" : "wifi","X-IG-Device-ID" : uuids,"Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8","X-FB-Server-Cluster" : "True","X-IG-Connection-Speed" : "0kbps","IG-INTENDED-USER-ID" : "0","X-IG-Device-Locale" : "en-JO","X-FB-HTTP-Engine" : "Liger"}
	def DATA(uuids,username,password):
		return {"phone_id":uuids,"reg_login":"0","device_id":uuids,"has_seen_aart_on":"0","username": username,"adid":REQUESTS.UUID(),"login_attempt_count":"0","enc_password":f"#PWD_INSTAGRAM:0:&:{password}"}
Notes = [
   "لا إِلَهَ إِلا أَنتَ سُبْحَانَكَ إِنِّي كُنتُ مِنَ الظَّالِمِينَ🌸",
   "اللَّهُمَّ أَعِنِّي عَلَى ذِكْرِكَ , وَشُكْرِكَ , وَحُسْنِ عِبَادَتِكَ🎈💞",
   "استغفر الله العظيم وأتوبُ إليه 🌹",
   "حَسْبِيَ اللَّهُ لا إِلَـهَ إِلاَّ هُوَ عَلَيْهِ تَوَكَّلْتُ وَهُوَ رَبُّ الْعَرْشِ الْعَظِيم"
   "ِ سبع مرات، كفاه الله تعالى ما أهمه من أمور الدنيا والآخرة🌹🌸",
   "ربنا اغفر لنا ذنوبنا وإسرافنا فِي أمرنا وثبت أقدامنا وانصرنا على القوم الكافرين🌸",
   "أشهد أنْ لا إله إلا الله وحده لا شريك له، وأشهد أن محمدًا عبده ورسوله🌺",
   "سبحان الله وبحمده سبحان الله العظيم🌸",
   "أشهد أنْ لا إله إلا الله وحده لا شريك له، وأشهد أن محمدًا عبده ورسوله🌺",
   "اللهم إنك عفو تُحب العفو فاعفُ عنّا 🌿🌹",
   "استغفر الله العظيم وأتوبُ إليه 🌹",
   "لا تقطع صلاتك، إن كنت قادراً على الصلاة في الوقت فصلِي و أكثر من الدعاء لتحقيق ما تتمنى💙",
   "قال صلى الله عليه وسلم : ”حَيْثُمَا كُنْتُمْ فَصَلُّوا عَلَيَّ، فَإِنَّ صَلَاتَكُمْ تَبْلُغُنِي“.",
   "﴿ رَبِّ اشْرَحْ لِي صَدْرِي وَيَسِّرْ لِي أَمْرِي ﴾",
   "‏{ تَوَفَّنِي مُسْلِمًا وَأَلْحِقْنِي بِالصَّالِحِينَ }",
   "‏اللهّم لطفك بقلوبنا وأحوالنا وأيامنا ،‏اللهّم تولنا بسعتك وعظيم فضلك ",
   "‏إن الله لا يبتليك بشيء إلا وبه خيرٌ لك فقل الحمدلله.",
   "اللهم اشفي كل مريض يتألم ولا يعلم بحاله إلا أنت",
   "استغفر الله العظيم وأتوبُ إليه.",
   "‏لَم تعرف الدنيا عظيماً مِثله صلّوا عليه وسلموا تسليم",
   " أنتَ اللّطيف وأنا عبدُك الضّعيف اغفرلي وارحمني وتجاوز عنّي.",
   "- اللهُم صبراً ، اللهم جبراً ، اللهم قوّة",
   "أصبحنا وأصبح الملك لله ولا اله الا الله.",
   "‏إنَّ اللهَ يُحِبُ المُلحِينَ فِي الدُّعَاء.",
   "‏إن الله لا يخذل يداً رُفعت إليه أبداً.",
   "يارب دُعاء القلب انت تسمعه فأستجب لهُ.",
   "- اللهم القبول الذي لا يزول ❤️🍀.",
   "- اللهُم خذ بقلبّي حيث نورك الذي لا ينطفِئ.",
   "سبحان الله وبحمده ،سبحان الله العظيم.",
   "لا تعودوا أنفسكم على الصمت، اذكرو الله، استغفروه، سبّحوه، احمدوه،"
   " عودوا السنتكم على الذكر فإنها إن اعتادت لن تصمت أبدًا.",
   "بسم الله الذي لا يضر مع اسمه شيء في الأرض ولا في السماء وهو السميع العلي- ثلاث مرات -",
   "- اللهم احرمني لذة معصيتك وارزقني لذة طاعتك 🌿💜.",
   "- اللهُم إن في صوتي دُعاء وفي قلبِي أمنية اللهُم يسر لي الخير حيث كان.",
   "‏اللهم أرني عجائب قدرتك في تيسير أموري 💜.",
   "يغفر لمن يشاء إجعلني ممن تشاء يا الله.*",
   "صلوا على من قال في خطبة الوداع  ‏و إني مُباهٍ بكم الأمم يوم القيامة♥️⛅️",
   "اللهـم إجعلنا ممن تشهد أصابعهم بذكـر الشهادة قبل الموت 🌿💜.",
   "- وبك أصبحنا يا عظيم الشأن 🍃❤️.",
   "اللهُم الجنة ونعيَّم الجنة مع من نحب💫❤️🌹",
   "‏اللهم قلبًا سليمًا عفيفًا تقيًا نقيًا يخشاك سرًا وعلانية🤍🌱",
   "اشهد ان لا اله الا الله وان محمدا عبده ورسوله",
   "لا اله الا الله سيدنا محمد رسول الله🌿💜",
   "قول معايا - استغفر الله استفر الله استغفر الله -",
   "مُجرد ثانية تنفعِك : أستغفُرالله العظيِم وأتوب إليّه.",
   "أدعُ دُعاء الواثِق فالله لايُجرّبُ معه‌‏",
   "صلي على اشرف الخلق سيدنا محمد صلاةً الله عليه وسلم تسليما كثيرا ❤️",
   "ربي اجعلني مقيم الصلاة ومن ذريتي ربنا وتقبل دعاءنا . ربنا تقبل منا إنك أنت السميع العليم وتب علينا إنك أنت التواب الرحيم",
   "اللهم إني أعوذ بك من عذاب النار، وأعوذ بك من عذاب القبر، وأعوذ بك من الفتن ما ظهر منها وما بطن، وأعوذ بك من فتنة الدجال",
   "اللهم إني أعوذ بك من علم لا ينفع وعمل لا يرفع وقلب لا يخشع وقول لا يسمع",
   "رَبَّنَا اغفِر لي وَلِوالِدَيَّ وَلِلمُؤمِنينَ يَومَ يَقومُ الحِسابُ",
   "رَّبِّ اغْفِرْ لِي وَلِوَالِدَيَّ وَلِمَن دَخَلَ بَيْتِيَ مُؤْمِنًا وَلِلْمُؤْمِنِينَ وَالْمُؤْمِنَاتِ وَلَا تَزِدِ الظَّالِمِينَ إِلَّا تَبَارًا",
   "يا حيّ يا قيّوم برحمتك أستغيث أصلح لي شأني كله ولا تكلني إلى نفسي طرفة عينٍ أبداً ...",
   "‏﴿ وَاذْكُر ربّكَ إِذَا نَسِيتَ ﴾ ",
   "- اللهم صلِ وسلم على نبينآ محمد ❥⇣",
   "((اللَّهُمَّ صَلِّ وَسَلِّمْ عَلَى نَبَيِّنَا مُحَمَّدٍ)) (عشرَ مرَّاتٍ).",
   "((لاَ إِلَهَ إِلاَّ اللَّهُ، وَحْدَهُ لاَ شَرِيكَ لَهُ، لَهُ الْمُلْكُ وَلَهُ الْحَمْدُ وَهُوَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ)) (مائةَ مرَّةٍ).",
   "اللهم اكفني بحلالك عن حرامك، وأغنني بفضلك عمن سواك",
   "(بِسْمِ اللَّهِ، تَوَكَّلْتُ عَلَى اللَّهِ، وَلَاَ حَوْلَ وَلَا قُوَّةَ إِلاَّ بِاللَّهِ)",
   "((أَسْتَغْفِرُ اللَّهَ وَأَتُوبُ إِلَيْهِ)) (مِائَةَ مَرَّةٍ فِي الْيَوْمِ).",
   "مَنْ كَانَ آخِرُ كَلاَمِهِ لاَ إِلَهَ إِلاَّ اللَّهُ دَخَلَ الْجَنَّة",
]
def HI_BEB():
	print(""" -By Joker @vv1ck @TweakPY
────(♥)(♥)(♥)────(♥)(♥)(♥) __ 
──(♥)██████(♥)(♥)██████(♥) 
─(♥)████████(♥)████████(♥) 
─(♥)██████████████████(♥) 
──(♥)████████████████(♥) 
────(♥)████████████(♥)always thanks God
──────(♥)████████(♥) 
────────(♥)████(♥)Did you thank God today?
─────────(♥)██(♥) 
───────────(♥)""")
class INSTAGRAM_API:
	def __init__(self):
		self.DN,self.ER,self.slp=0,0,0
		self.PRNT=Lock()
		self.uuids=REQUESTS.UUID()
		self.hed=REQUESTS.HEADERS(self.uuids)
		self.username=input('[$] Enter username: ')
		self.password=input('[$] Enter password: ')
		self.CheckLogins()
	def New_Note(self,TIMNG):
		while True:
			NOTE=post('https://i.instagram.com/api/v1/notes/create_note/',headers=self.hed,data={"audience" : "0","text" : str(choice(Notes)),"_uuid" : str(REQUESTS.UUID())})
			if ('"status":"ok"' in NOTE.text):
				self.DN+=1
			elif ('Note text too large' in NOTE.text):self.ER+=1
			elif NOTE.status_code==404:self.ER+=1
			else:
				print(NOTE.text)
				print('\n      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
			print(f'\r\t\t New Note: {self.DN}, Errors: {self.ER}\r',end="")
			sleep(int(TIMNG))
	def CheckLogins(self):
		try:
			CHEACK=post('https://i.instagram.com/api/v1/accounts/login/',headers=self.hed,data=REQUESTS.DATA(self.uuids,self.username,self.password))
			
			if (RSP.Login() in CHEACK.text ):
				print('[+] Logged in successfully..\n')
				self.hed['Authorization']=str(CHEACK.headers['ig-set-authorization'])
				self.hed['IG-INTENDED-USER-ID']=str(CHEACK.headers['ig-set-ig-u-ds-user-id'])
				slow('      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
				try:print(f'\t\t[+] Logged in successfully [$]')
				except TypeError:pass
				slow('      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
				TIMS=input('[*] Enter the time between each new note:\n -0) Every 5 minutes a new note\n -1) Every 15 minutes a new note\n -2) Every half hour a new note\n -3) Every hour a new note\n -4) Every two hours a new note\n\n[?] Choose when to switch: ')
				if (TIMS == '0'):TIMNG=300
				elif (TIMS == '1'):TIMNG=800
				elif (TIMS == '2'):TIMNG=1800
				elif (TIMS == '3'):TIMNG=3300
				elif (TIMS == '4'):TIMNG=6300
				else:TIMNG=1800
				os.system("cls" if os.name=='nt' else "clear")
				HI_BEB()
				slow('      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
				self.New_Note(TIMNG)
			
			elif (RSP.BDusr() in CHEACK.text):
				input('[-] Username is incorrect')
					
			elif (RSP.BDpes() in CHEACK.text):
				input('[-] Password is incorrect')
			elif (RSP.BadLog() in CHEACK.text):
				input('[-] Too many login attempts, please try again later or use vpn')
			elif ('two_factor_required' in CHEACK.text):
				input("[!] The account contains verification, enter your account now and verify the login by pressing the ( Approve ) button, If that doesn't work, de-verify your account. ")
			elif ('challenge_required' in CHEACK.text):
				input("[!] The account contains verification, enter your account now and verify the login by pressing the ( Approve ) button, If that doesn't work, de-verify your account. ")
			else:input(CHEACK.text)
		except requests.exceptions.ConnectionError:
			input('error log')
INSTAGRAM_API()
