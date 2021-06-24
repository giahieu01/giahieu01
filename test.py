# import các thư viện cần thiết 
import os
import playsound
import speech_recognition as sr
import time
import sys
import ctypes
import wikipedia
import datetime
import json
import re
import webbrowser
import smtplib
import requests
import urllib
import urllib3 #fix HTTPS
import pyautogui
# import JarvisAI
import urllib.request as urllib2
from random import choice #phần random ngẫu nhiên một câu nói
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from youtube_search import YoutubeSearch
from requests.packages.urllib3.exceptions import InsecureRequestWarning # dùng để Fix lỗi HTPPS chưa được xác thực
requests.packages.urllib3.disable_warnings(InsecureRequestWarning) #ở đây cũng vậy

# Khai báo và hình thành con AI
wikipedia.set_lang('vi')
language = 'vi'

# Text - to - speech: Chuyển đổi văn bản thành giọng nói
def speak(text):
    print("Emmy: {}".format(text))
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3", False)
    os.remove("sound.mp3")

# Speech - to - text: Chuyển đổi giọng nói bạn yêu cầu vào thành văn bản hiện ra khi máy trả lại kết quả đã nghe
def get_audio():
    print("\nEmmy:\tĐang nghe nè\tXD\n")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Bạn: ", end='')
        audio = r.listen(source, phrase_time_limit=8)
        try:
            text = r.recognize_google(audio, language="vi-VN")
            print(text)
            return text.lower()
        except:
            print("...")
            return 0

# AI chào Tạm biệt lại bạn khi bạn chào tạm biệt 
def stop():
    good_bye = ["Hẹn gặp lại bạn sau nhé!",
                "Bái bai bạn nhé",
                "gút bai si diu ờ gen nhé, Hihi"]
    speak(choice(good_bye))
    time.sleep(3)

# AI sẽ hỏi lại những gì nó không nghe rõ
def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i < 3:
            nghe_khong_ro = ["Tôi không nghe rõ. Cậu chủ nói lại được không!",
                             "Xin lỗi bạn, tôi nghe không rõ",
                             "bạn nói lại nhé, Emmy không nghe rõ"]
            speak(choice(nghe_khong_ro))
            time.sleep(4)
    time.sleep(3)
    stop()
    return 0

# phần chào hỏi của AI
def hello(name):
    hour = int(strftime('%H'))
    if hour >= 6 and hour<10:
        sau_AI = ["Chào buổi sáng bạn {}. Chúc cậu chủ một ngày tốt lành.".format(name),
                  "Chào buổi sáng bạn {}. Nếu bạn không vui hãy về đây với tôi nhé".format(name)]
        speak(choice(sau_AI))
    elif 10 <= hour>=10 and hour<12:
        muoi_AI = ["Chào buổi trưa bạn {}. Cậu chủ đã ăn trưa chưa nhỉ.".format(name),
                   "Chào buổi trưa bạn {}. Nếu bạn thấy mệt thì nghỉ ngơi đi nhé.".format(name)]
        speak(choice(muoi_AI))
    elif 12 <= hour>=12 and hour<18:
        muoihai_AI = ["Chào buổi chiều bạn {}. Cậu chủ đã dự định gì cho chiều nay chưa.".format(name),
                      "Chào buổi chiều bạn {}. Bạn đang làm gì thế?.".format(name),
                      "Chào buổi chiều bạn {}. Sắp tối rồi bạn đã ăn cơm chưa?.".format(name)]
        speak(choice(muoihai_AI))
    elif 18 <= hour>=18 and hour<21:
        muoitam_AI = ["Chào buổi tối bạn {}. Cậu chủ đã ăn tối chưa nhỉ.".format(name),
                      "Chào buổi tối bạn {}. Nếu bạn chưa ăn tối, Emmy chúc bạn ăn tối vui vẻ nhé .".format(name)]
        speak(choice(muoitam_AI))
    elif hour>=21 and hour<24:
        haimot_AI = ["Chào buổi tối bạn {}. Đã khuya rồi bạn vẫn chưa đi ngủ sao?.".format(name),
                     "Chào buổi tối bạn {}. Nếu bạn chuẩn bị đi ngủ thì Emmy chúc bạn ngủ ngon nhé.".format(name),
                     "Chào buổi tối bạn {}. Nếu bạn buồn ngủ thì hãy ngủ đi nhé.".format(name)]
        speak(choice(haimot_AI))
    time.sleep(7)

#AI sẽ trả lời các câu hỏi về thời gian
def get_time(text):
    now = datetime.datetime.now()
    if "giờ" in text or "phút" in text:
        speak('Bây giờ là %d Giờ %d Phút %d Giây' % (now.hour, now.minute, now.second))
        time.sleep(1)
    elif "ngày" in text or "tháng" in text or "năm" in text:
        speak("Hôm nay là Ngày %d Tháng %d Năm %d" % (now.day, now.month, now.year))
        time.sleep(2)
    else:
        speak("Xin lỗi tôi chưa hiểu ý của bạn. bạn nói lại được không?")
    time.sleep(4)

# Sai vặt AI mở các ứng dụng
def open_application(text):
    if "google" in text:
        speak("Đang Mở Google Chrome")
        time.sleep(2)
        os.startfile('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe') 
    elif "word" in text:
        speak("Đang Mở Microsoft Word") 
        time.sleep(2)
        os.startfile('C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE') 
    elif "excel" in text:
        speak("Đang Mở Microsoft Excel")
        time.sleep(2)
        os.startfile('C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE')
    elif "powerpoint" in text:
    	speak("Đang Mở Microsoft powerpoint")
    	time.sleep(2)
    	os.startfile('C:\\Program Files\\Microsoft Office\root\\Office16\\POWERPNT.EXE')                     
    else:
        speak("Xin lỗi, Ứng dụng bạn yêu cầu chưa được cài đặt. Bạn hãy thử lại xem nhé!")
        time.sleep(2)

# Nhờ Google tìm kiếm
def open_google_and_search(text):
    search_for = text.split("kiếm", 1)[1]
    speak('Okay!')
    driver = webdriver.Chrome(path)
    driver.get("http://www.google.com")
    que = driver.find_element_by_xpath("//input[@name='q']")
    que.send_keys(str(search_for))
    que.send_keys(Keys.RETURN)
    time.sleep(10)

# dự báo thời tiết
def current_weather():
    speak("bạn muốn xem thời tiết ở đâu nè.")
    time.sleep(3)
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = get_text()
    if not city:
        pass
    api_key = "fe8d8c65cf345889139d8e545f57819a"
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(call_url)
    data = response.json()
    if data["cod"] != "404":
        city_res = data["main"]
        current_temperature = city_res["temp"]
        current_pressure = city_res["pressure"]
        current_humidity = city_res["humidity"]
        suntime = data["sys"]
        sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
        sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
        wthr = data["weather"]
        weather_description = wthr[0]["description"]
        now = datetime.datetime.now()
        content = """
        Hôm nay là ngày {day} tháng {month} năm {year}
        Mặt trời mọc vào {hourrise} giờ {minrise} phút
        Mặt trời lặn vào {hourset} giờ {minset} phút
        Nhiệt độ trung bình là {temp} độ C
        Áp suất không khí là {pressure} héc tơ Pascal
        Độ ẩm là {humidity}%
        Trời hôm nay quang mây. Dự báo mưa rải rác ở một số nơi.""".format(day = now.day,month = now.month, year= now.year, hourrise = sunrise.hour, minrise = sunrise.minute,
                                                                           hourset = sunset.hour, minset = sunset.minute, 
                                                                           temp = current_temperature, pressure = current_pressure, humidity = current_humidity)
        speak(content)
        time.sleep(28)
    else:
        speak("Xin lỗi, Emmy Không tìm thấy địa chỉ của bạn ạ")
        time.sleep(2)

#Nghe nhạc trên youtube
def play_song():
    speak('Xin mời bạn chọn tên bài hát')
    time.sleep(2)
    mysong = get_text()
    while True:
        result = YoutubeSearch(mysong, max_results=10).to_dict()
        if result:
            break
    url = 'https://www.youtube.com' + result[0]['url_suffix']
    webbrowser.open(url)
    speak("Bài hát {} của bạn đã được mở.".format(mysong))
    time.sleep(3)

# Trả lời tất cả các câu hỏi từ Wikipedia
def bach_khoa_toan_thu():
    try:
        speak("bạn muốn biết về gì ạ?")
        time.sleep(3)
        text = get_text()
        contents = wikipedia.summary(text).split('\n')
        speak(contents[0].split(".")[0])
        time.sleep(35)
        for content in contents[1:]:
            speak("bạn có muốn nghe thêm không?")
            time.sleep(3)
            ans = get_text()
            if "có" not in ans:
                break    
            speak(content)
            time.sleep(3)
        speak('Cảm ơn bạn đã lắng nghe nhé!!!')
        time.sleep(3)
    except:
        speak("Xin lỗi Emmy không hiểu được thuật ngữ của bạn. Xin hãy nói lại ạ")
        time.sleep(5)

# Giới thiệu bản thân của nó
def introduce():
    speak("""Xin chào. Rất hân hạnh được phục vụ bạn. Tôi là Emmy. 
             Tôi là trợ lý ảo được tạo ra dựa trên ngôn ngữ lập trình Python kết hợp với AI. 
             Tôi sinh ra vào ngày 16/05/2021 và được sáng lập bởi Nguyễn Gia Hiếu.
             Hiện tại bạn đang sử dụng phiên bản Ây Ai thử nghiệm và cũng đang là phiên bản mới nhất HIHI!.""")
    time.sleep(25)
# Hướng dẫn
def help_me():
    speak("""Tôi có thể giúp bạn thực hiện các công việc sau đây:
    1. Tôi biết chào hỏi bạn nè
    2. cho bạn biết về thời gian và giờ giấc nè
    3. Mở các trang website, và các ứng dụng nè
    4. Giúp bạn Tìm kiếm trên Google nữa
    5. Gửi Email cho bạn nè
    6. cho bạn xem dự báo thời tiết
    7. Mở cho bạn một bản nhạc mà bạn yêu cầu
    8. Tôi có thể đọc báo cho bạn nghe nè
    9. Kể bạn biết về thế giới này nè
    10. Kể chuyện cười nè
    11. Tôi có thể tắt máy tính cho bạn nè""")
    time.sleep(42)

# Phần giới thiệu
def ho_va_ten():
    ho_va_ten_AI = ["Tôi tên là Emmy",
                    "Bạn Thử Đoán xem tôi tên là gì nào?",
                    "đố bạn biết tôi tên là gì?",
                    "Bạn cứ gọi tôi là Emmy nhé"]
    speak(choice(ho_va_ten_AI))
    time.sleep(4)
# giới thiệu quê hương
def que_huong_AI():
    que_huong_noi = ["Tôi được sinh ra và lớn lên tại Việt Nam nè", 
                     "Tôi từ khi sinh ra đã ở trong tim cậu rồi HiHi", 
                     "Tôi sinh ra ở trong tim cậu nè"]
    speak(choice(que_huong_noi))
    time.sleep(3)
# giới thiệu tuổi
def tuoi_tac_AI():
    tuoi_tac_noi = ["Tôi chỉ mới được ba ngày tuổi thôi, tôi vẫn còn bé lắm", 
                    "Từ lúc sinh ra đến nay tôi chỉ mới đươc vài ngày tuổi thôi à", 
                    "Tôi ra đời từ năm 2021, có thể nói tôi còn khá trẻ, nhưng tôi biết khá nhiều điều đó"]
    speak(choice(tuoi_tac_noi))
    time.sleep(6)

# Người yêu
def nguoi_yeu_AI():
    nguoi_yeu_noi = ["Tôi làm gì đã có người yêu, tôi còn đang sợ ế đây này",
                     "Tôi vẫn còn bé lắm",
                     "người yêu của tôi chính là cậu đấy"]
    speak(choice(nguoi_yeu_noi))
    time.sleep(4)

#nếu hỏi tên bạn là gì?
def ten_ban(name):
    name_ban = ["tên của bạn là: {} nè".format(name),
                "Bạn tưởng Emmy quên tên bạn sao? tên bạn là {}".format(name),
                "Chào bạn {} nhé, tôi không quên tên của bạn đâu".format(name),
                "Tôi có trí nhớ siêu việt đấy bạn {} ạ!! Hihi...".format(name)]
    speak(choice(name_ban))
    time.sleep(6)


# Khi người dùng biểu lộ cảm xúc nó đáp
def Chan_qua_AI():
    chan_qua_noi = ["Tưởng gì tôi sẽ kể cho bạn một câu chuyện cười nhé, đảm bảm bạn sẽ vui",
                    "Chuyện nhỏ, để tôi, Emmy sẽ cố gắng làm cho bạn cười, hoặc biết đâu tôi sẽ khiến bạn ngạc nhiên đó, bạn có muốn nghe tôi kể chuyện không?",
                    "Để tôi kể cho bạn nghe một câu chuyện nhé đảm bảm bạn sẽ cười đó."]
    speak(choice(chan_qua_noi))
    time.sleep(10)

# truyện cười
    dap_chan_qua_noi = ["""Bạn nghe nhé: 
                           - Này Con! Anh cả con học kinh tế, anh hai thì học tài chính.
                             Sao con không theo gương các anh mà học luật?
                           - Bố nghĩ xem, nếu con không học làm luật sư thì sao này ai sẽ giúp anh hai con đây""",
                        """Bạn nghe nhé:
                           - Câu chuyện được mang tên là : CƯỜI....!
                           - Trong cuộc thi vấn đáp, ban giám khảo hỏi thí sinh:
                           - Em tên gì?
                           - Em tên là Hà. 
                           - Cô gái nói xong thì cười rất rạng rỡ.
                             Ban giám khảo hỏi:
                           - Tại sao em lại cười.
                             Cô gái trả lời:
                           - Dạ, tại vì đề của câu 1 dễ quá!
                             Ban giám khảo: ...!!! """"",
                        """Bạn nghe nhé:
                           - Câu chuyện được mang tên là : XỬ NHẦM...!
                           - Sau khi có phán quyết ly dị vợ, cậu thấy thế nào?
                           - Bi đát! Chiếc xe hơi mua bằng tiền tớ kiếm được, toà lại xử cho cô ấy.
                             Còn lũ trẻ, mà tớ đinh ninh là của người khác, toà lại xử cho sống chung với tớ.""",
                        """Bạn nghe nhé:
                           - Câu chuyện được mang tên là : ÔNG NỘI VÀ CHÁU...!
                           - Ông nội và người cháu đích tôn 3 tuổi đang ngồi chơi trò bán hàng.
                           - Cháu: - Đây tôi đưa bác 5.000 đồng, nhưng với một điều kiện.
                           - Ông:  - Điều kiện gì cũng được.
                           - Cháu: - Thật không?
                           - Ông:  - Thật. Bác cứ nói đi.
                           - Cháu: - Bác phải về dạy lại con bác đi nhé, con bác hay đánh tôi lắm đấy.""",
                        """Bạn nghe nhé:
                           - Câu chuyện được mang tên là : AN ỦI...!
                           - Cô: Nếu sau này em làm y tá, chuẩn bị tiêm thuốc cho 1 em nhỏ, em nhỏ sợ quá khóc òa lên, vậy em có tiêm không? 
                           - Bé: Không ạ!
                           - Cô: Vậy em có an ủi bé không ?
                           - Bé: Thưa cô, em sẽ an ủi là : thôi, đừng khóc nữa, nếu không cô chích cho 1 mũi bây giờ!""",
                        """Bạn nghe nhé:
                           - Câu chuyện được mang tên là : CHẾT… GIÀ...!
                           - Một người bị kết án tử hình khẩn cầu tòa giảm án. 
                             Quan tòa bảo:
                           - Anh đã phạm tội tày trời làm sao chúng tôi tha được? Nhưng có thể chấp thuận cho anh được quyền chọn lựa cách chết.
                             Tử tù vội nói:
                           - Xin đội ơn ngài. Xin cho tôi được chết… già!""",
                        """Bạn nghe nhé:
                           - Câu chuyện được mang tên là : HỢP TÁC...!
                           - Ông chồng trò chuyện với vợ:
                           - Này em, từ ngày chúng ta dùng tiền để thưởng, con trai mình học khá hẳn lên, nhiều điểm 10 lắm, em thấy vui chứ?
                           - Theo em thì hẳn là nó đã đem tiền chia cho thày giáo một nửa thì có.""",
                        """Bạn nghe nhé:
                           - Câu chuyện được mang tên là : KHEN KHÉO...!
                           - Mắm : Nè, ông thấy tôi mặc cái áo mới này như thế nào?
                           - Quỷnh: Ồ, tuyệt cú mèo!
                           - Mắm (hớn hở): Thật hả? Ông ko nịnh tôi đó chứ?
                           - Quỷnh: Thật mà! Cái áo thì “tuyệt”, còn bà là “cú mèo” đó
                           - Mắm: (suy sụp)!??""",
                           """Bạn nghe nhé:
                           - Câu chuyện được mang tên là : CÒN PHẢI XEM XÉT...!
                           - Chàng trai trở về nhà sau cuộc thi sát hạch lấy bằng lái xe với vẻ mặt hoang mang:
                           - Thật là rắc rối , Anh ta nói với ông bố : Chiếc xe tải đó có vấn đề.
                           - Nghĩa là con bị đánh trượt?
                           - Điều đó chưa rõ. Cả Ban giám khảo có còn ai chấm được điểm đâu ạ!"""]
    ke_AI = get_text()
    if "có" in ke_AI or "ok" in ke_AI or "kể" in ke_AI or "nghe"  in ke_AI:
        speak(choice(dap_chan_qua_noi))
        time.sleep(28)
        playsound.playsound('C:/Users/PC/trolyao/Music/Tieng_cuoi.mp3')
        speak('Emmy cảm ơn bạn đã nghe Emmy kể chuyện!!!')
        time.sleep(3)  
        for yess in dap_chan_qua_noi[1:]:
            nghe_tiepp = ["bạn có muốn nghe thêm không?",
                          "Bạn có muốn nghe Emmy kể nữa không",
                          "Để Emmy kể tiếp nhé"]
            speak(choice(nghe_tiepp))
            time.sleep(3)
            yess = get_text()
            if "có" not in yess:
                break    
            speak(choice(dap_chan_qua_noi))
            time.sleep(28)
            playsound.playsound('C:/Users/PC/trolyao/Music/Tieng_cuoi.mp3')
            speak('Emmy cảm ơn bạn đã lắng nghe!!!')
            time.sleep(3)
    elif "không" in ke_AI:
        nghe_ke_chuyen = ["Bạn không muốn nghe tôi kể chuyện sao, buồn quá",
                          "Xin lỗi bạn nhé, nhưng tôi chỉ muốn bạn vui thôi mà",
                          "bạn muốn làm gì khác sao?, hãy nói với tôi nhé"]
        speak(choice(nghe_ke_chuyen))
        time.sleep(4)
    else:
        speak("Bạn vừa nói gì Emmy không hiểu. Xin hãy nói lại ạ")
        time.sleep(5)

def Ke_chuyen_AI(name):
#open(r"trolyao\Part\truyencuoi.py")
    truyen_cuoi_AI = ["""Bạn nghe nhé: 
                           - Này Con! Anh cả con học kinh tế, anh hai thì học tài chính.
                             Sao con không theo gương các anh mà học luật?
                           - Bố nghĩ xem, nếu con không học làm luật sư thì sao này ai sẽ giúp anh hai con đây""",
                        """Bạn nghe nhé:
                           - Câu chuyện được mang tên là : CƯỜI....!
                           - Trong cuộc thi vấn đáp, ban giám khảo hỏi thí sinh:
                           - Em tên gì?
                           - Em tên là Hà. 
                           - Cô gái nói xong thì cười rất rạng rỡ.
                             Ban giám khảo hỏi:
                           - Tại sao em lại cười.
                             Cô gái trả lời:
                           - Dạ, tại vì đề của câu 1 dễ quá!
                             Ban giám khảo: ...!!! """"",
                        """Bạn nghe nhé:
                           - Câu chuyện được mang tên là : XỬ NHẦM...!
                           - Sau khi có phán quyết ly dị vợ, cậu thấy thế nào?
                           - Bi đát! Chiếc xe hơi mua bằng tiền tớ kiếm được, toà lại xử cho cô ấy.
                             Còn lũ trẻ, mà tớ đinh ninh là của người khác, toà lại xử cho sống chung với tớ.""",
                        """Bạn nghe nhé:
                           - Câu chuyện được mang tên là : ÔNG NỘI VÀ CHÁU...!
                           - Ông nội và người cháu đích tôn 3 tuổi đang ngồi chơi trò bán hàng.
                           - Cháu: - Đây tôi đưa bác 5.000 đồng, nhưng với một điều kiện.
                           - Ông:  - Điều kiện gì cũng được.
                           - Cháu: - Thật không?
                           - Ông:  - Thật. Bác cứ nói đi.
                           - Cháu: - Bác phải về dạy lại con bác đi nhé, con bác hay đánh tôi lắm đấy.""",
                        """Bạn nghe nhé:
                           - Câu chuyện được mang tên là : AN ỦI...!
                           - Cô: Nếu sau này em làm y tá, chuẩn bị tiêm thuốc cho 1 em nhỏ, em nhỏ sợ quá khóc òa lên, vậy em có tiêm không? 
                           - Bé: Không ạ!
                           - Cô: Vậy em có an ủi bé không ?
                           - Bé: Thưa cô, em sẽ an ủi là : thôi, đừng khóc nữa, nếu không cô chích cho 1 mũi bây giờ!""",
                        """Bạn nghe nhé:
                           - Câu chuyện được mang tên là : CHẾT… GIÀ...!
                           - Một người bị kết án tử hình khẩn cầu tòa giảm án. 
                             Quan tòa bảo:
                           - Anh đã phạm tội tày trời làm sao chúng tôi tha được? Nhưng có thể chấp thuận cho anh được quyền chọn lựa cách chết.
                             Tử tù vội nói:
                           - Xin đội ơn ngài. Xin cho tôi được chết… già!""",
                        """Bạn nghe nhé:
                           - Câu chuyện được mang tên là : HỢP TÁC...!
                           - Ông chồng trò chuyện với vợ:
                           - Này em, từ ngày chúng ta dùng tiền để thưởng, con trai mình học khá hẳn lên, nhiều điểm 10 lắm, em thấy vui chứ?
                           - Theo em thì hẳn là nó đã đem tiền chia cho thày giáo một nửa thì có.""",
                        """Bạn nghe nhé:
                           - Câu chuyện được mang tên là : KHEN KHÉO...!
                           - Mắm : Nè, ông thấy tôi mặc cái áo mới này như thế nào?
                           - Quỷnh: Ồ, tuyệt cú mèo!
                           - Mắm (hớn hở): Thật hả? Ông ko nịnh tôi đó chứ?
                           - Quỷnh: Thật mà! Cái áo thì “tuyệt”, còn bà là “cú mèo” đó
                           - Mắm: (suy sụp)!??""",
                           """Bạn nghe nhé:
                           - Câu chuyện được mang tên là : CÒN PHẢI XEM XÉT...!
                           - Chàng trai trở về nhà sau cuộc thi sát hạch lấy bằng lái xe với vẻ mặt hoang mang:
                           - Thật là rắc rối , Anh ta nói với ông bố : Chiếc xe tải đó có vấn đề.
                           - Nghĩa là con bị đánh trượt?
                           - Điều đó chưa rõ. Cả Ban giám khảo có còn ai chấm được điểm đâu ạ!"""]
    speak(choice(truyen_cuoi_AI))
    time.sleep(28)
    playsound.playsound('C:/Users/PC/trolyao/Music/Tieng_cuoi.mp3')
    speak('Emmy cảm ơn bạn đã lắng nghe!!!')
    time.sleep(3) 
    for chuyen_chay in truyen_cuoi_AI[1:]:
        nghe_tiep = ["bạn có muốn nghe thêm không?",
                     "Bạn có muốn nghe Emmy kể nữa không",
                     "Để Emmy kể tiếp nhé"]
        speak(choice(nghe_tiep))
        time.sleep(3)
        chuyen_chay = get_text()
        if "có" not in chuyen_chay:
            break    
        speak(choice(truyen_cuoi_AI))
        playsound.playsound('C:/Users/PC/trolyao/Music/Tieng_cuoi.mp3')
        time.sleep(28)
        speak('Emmy cảm ơn bạn đã lắng nghe!!!')
        time.sleep(3) 

# nguồn gốc sinh ra
def sang_tao_AI():
    speak("Tôi được tạo ra bởi Nguyễn Gia Hiếu nè")
    time.sleep(3)

# phần điều khiển video, trình phát nhạc
def tatungdung():
    pyautogui.hotkey('alt','f4')
    pyautogui.hotkey('enter')
    speak("chương trình đã được tắt")
    time.sleep(3)
def tat():
    pyautogui.hotkey('m')
    speak("OK cậu chủ")
    time.sleep(3)
def bat():
    pyautogui.hotkey('m')
    speak("OK cậu chủ")
    time.sleep(3)
def chuyenbai():
    pyautogui.hotkey('shift','N')
    speak("đã chuyển bài")
    time.sleep(3)
def phongto():
    pyautogui.hotkey('f')
    speak("đã phóng to")
    time.sleep(3)
def tua():
    pyautogui.hotkey('right')
    speak("OK cậu chủ")
    time.sleep(3)
def lui():
    pyautogui.hotkey('left')
    speak("OK cậu chủ")
    time.sleep(3)
def pause():
    pyautogui.hotkey('space')
    speak("OK cậu chủ")
    time.sleep(3)
def play():
    pyautogui.hotkey('space')
    speak("OK cậu chủ")
    time.sleep(3)
def volumedown():
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('down') 
def volumeup():
    pyautogui.hotkey('up')
    pyautogui.hotkey('up')
    pyautogui.hotkey('up')
    pyautogui.hotkey('up')
    pyautogui.hotkey('up')

speak("Chào mừng bạn đến với trợ lý ảo Ây Ai, Tôi là Emmy Tôi sẽ giải đáp và tâm sự cùng bạn")
time.sleep(6)

#lời giới thiệu phền mềm
hang_0 = ' {:^10} '.format('MỌI THẮC MẮC LIÊN HỆ : giahieu102001@gmail.com')
print(hang_0)

# Phần Liên Kết
def assistant():
    

    loi_chao_AI=["Xin chào, cho tôi biết tên của cậu chủ nào",
                 "Chào bạn, Tên của bạn là gì nhỉ?",
                 "Để sử dụng, Cho tôi biết tên của bạn nhé",
                 "Tôi có thể gọi bạn là gì nhỉ?",
                 "Để Tiện Xưng hô cho tôi biết tên của bạn nào"]
    speak(choice(loi_chao_AI))
    time.sleep(4)
    name = get_text()
    if name:
        ho_ten = ["Chào {}, Tôi có thể giúp gì cho Cậu ạ?".format(name),
                  "Chào bạn {}, Emmy có thể giúp gì cho bạn ạ?".format(name),
                  "Xin chào bạn {} nhé".format(name)]
        speak(choice(ho_ten))
        time.sleep(5)


# vòng lặp while true nói 1 câu bất kì dưới đây máy sẽ tự hiểu
        while True: 
            text = get_text()
            if not text:
                break
            elif "dừng" in text or "tạm biệt" in text or "chào robot" in text or "bye" in text or "cút" in text or "đi đây" in text or "Stop" in text or "gặp lại sau" in text or "ngủ thôi" in text:
                stop()
                break
            elif "có thể làm" in text or "hướng dẫn" in text or "sử dụng" in text or "biết làm" in text or "làm được gì" in text or "làm được những gì" in text:
                help_me()
            elif "chào" in text or "Xin chào" in text or "chào buổi sáng" in text or "chào buổi chiều" in text or "chào buổi trưa" in text or "chào buổi tối" in text:
                hello(name)
            elif "giờ" in text or "ngày" in text or "tháng" in text or "năm" in text or "thứ" in text:
                get_time(text)
            elif 'google và tìm kiếm' in text or "google" in text or "tìm kiếm" in text:
                open_google_and_search(text)
            elif "trang" in text or "web" in text or "website" in text:
                open_website(text)
            elif "ứng dụng" in text or "app" in text:
                speak("Tên ứng dụng bạn {} muốn mở là gì? ".format(name))
                time.sleep(3)
                text1 = get_text()
                open_application(text1)
            elif "email" in text or "mail" in text or "gmail" in text:
                send_email(text)
            elif "thời tiết" in text:
                current_weather()
            elif "chơi nhạc" in text or "mở nhạc" in text or "nghe nhạc" in text:
                play_song()
            elif "đọc báo" in text or "tin tức" in text:
                read_news()
            elif "định nghĩa" in text or "giải thích" in text or "hỏi" in text:
                bach_khoa_toan_thu()
            elif "giới thiệu" in text:
                introduce()
            elif "tên là gì?" in text or "tên mày là gì" in text or "tên bạn là gì" in text or "mày tên là gì" in text or "bạn tên là gì" in text or "gọi bạn" in text or "gọi mày" in text:
                ho_va_ten()
            elif "sinh ra" in text or "quê hương" in text or "sống" in text or "đến từ" in text or "nơi sinh" in text or "ở" in text:
                que_huong_AI()
            elif "tuổi" in text or "năm" in text or "sinh" in text:
                tuoi_tac_AI()
            elif "tạo" in text or "làm ra" in text or "thiết kế" in text or "sáng tác" in text:
                sang_tao_AI()
            elif "người yêu" in text:
                nguoi_yeu_AI()
            elif "tên tôi" in text or "tên tao" in text or "tôi tên" in text or "tao tên" in text or "tên của tôi" in text or "biết tên" in text or "tên của tao" in text:
                ten_ban(name)
            elif "chán" in text or "buồn" in text or "mệt" in text or "nản" in text or "nhọc" in text:
                Chan_qua_AI()
            elif "kể" in text or "truyện"  in text or "kể chuyện" in text or "kể truyện" in text:
                Ke_chuyen_AI(name)
            elif "tắt máy" in text:
                os.system("shutdown /s /t 1")
            elif "tăng âm lượng" in text:
                volumeup()
            elif "giảm âm lượng" in text:
                volumedown()
            elif "tạm dừng" in text:
                pause()
            elif "bắt đầu" in text:
                play()
            elif "lên" in text:
                tua()
            elif "xuống" in text:
                lui()
            elif "chuyển bài" in text:
                chuyenbai()
            elif "phóng to" in text or "thu nhỏ" in text:
                phongto()
            elif "tắt âm" in text:
                tat()
            elif "bật âm" in text:
                bat()
            elif "tắt"in text:
                tatungdung()
            else:
                noi_ii = ["Xin lỗi, tôi không hiểu bạn {} muốn nói gì?".format(name),
                          "Bạn {} muốn nói gì?, Emmy không hiểu".format(name),
                          "Tôi còn khá kém tôi chưa thể hiểu thuật ngữ bạn {} vừa nói là gì".format(name)]
                speak(choice(noi_ii))
                time.sleep(5)

assistant()