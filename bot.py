from modules import *
from twitter import tweets
from chat import master_chat,driver
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from PIL import Image


# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")
# driver = webdriver.Chrome("drivers/chromedriver",options=chrome_options)
if not os.path.exists("./audio"):
    os.mkdir("./audio")
if not os.path.exists("./images"):
    os.mkdir("./images")

path, dirs, files = next(os.walk("./images"))
image_count = len(files)

def image_conversion():
    root = tk.Tk()
    def my_function():
        current_id = variable.get()
        output_format =str(current_id)
        inside=root.filename
        for i in range(len(inside)):
            if inside[i]=='/':
                index=i
            if inside[i]=='.':
                index2=i
        output=inside[:index]
        outside=inside[:index2]
        outside+=output_format
        inside = r"{}".format(inside)
        outside = r"{}".format(outside)
        img = Image.open(inside)
        new_i = img.convert('RGB')
        new_i.save(outside)
        root.destroy()
        os.startfile(output)

    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    root.filename = filedialog.askopenfilename(initialdir=desktop, title="Select A File")
    print(root.filename)
    my_label = tk.Label(root, text = "Select output image format")
    my_label.config(width=25,font=('Helvetica,12'))
    my_label.grid(row = 0, column = 0)

    OptionList = [".jpg",".png",".tiff",".bmp",".eps"]
    variable = tk.StringVar(root)
    variable.set(OptionList[0])
    opt = tk.OptionMenu(root, variable, *OptionList)
    opt.config(width=50, font=('Helvetica', 12))
    opt.grid(row = 2, column = 0)

    my_button = tk.Button(root, text = "Submit", command = my_function)
    my_button.config(width=10,font=('Helvetica,12'))
    my_button.grid(row = 4, column = 0)

    root.mainloop()

os.system('cls')
while 1:
    # r = sr.Recognizer()
    # with sr.Microphone() as source:
    #     print("Say something")
    #     audio = r.listen(source, timeout=10)
    #     print("Time over")
    try:
        # text = r.recognize_google(audio)
        text=input()
    except:
        continue
    print("Text :"+text)
    if "where to watch" in text:
        text=text.replace("where to watch","")
        text2="https://www.justwatch.com/in/search?q="
        text=text.replace(" ","%20")
        text2+=text
        webbrowser.open_new_tab(text2)
        os.system('cls')
    elif "suggest movie" in text:
        speech=gTTS("What genre do you want?",lang='en',slow=False)
        speech.save("speech_default.mp3")
        playsound.playsound("speech_default.mp3",True)
        s=sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak")
            audio=s.listen(source)
            print("Over")
        text=s.recognize_google(audio)
        # text=input()
        text2="agoodmovietowatch.com"
        text=text+" movie "+text2
        for j in search(text, tld="co.in", num=10,stop=10,pause=2):
            if "agoodmovietowatch.com" in j:
                webbrowser.open_new_tab(j)
                os.system('cls')
                break
    elif "stock price" in text:
        flag=True
        for j in search(text, tld="co.in", num=10, stop=10, pause=2):
            if "moneycontrol.com" in j:
                webbrowser.open_new_tab(j)
                flag=False
                os.system('cls')
                break
        if flag:
            URL = f"https://google.com/search?q={text}"
            webbrowser.open_new_tab(URL)
            os.system('cls')
    elif "translate" in text:
        text=text.replace("translate",'')
        speech=gTTS("What language should I translate to?",lang='en',slow=False)
        os.remove("speech_default.mp3")
        speech.save("speech_default.mp3")
        playsound.playsound("speech_default.mp3",True)
        language=input()
        # s=sr.Recognizer()
        # with sr.Microphone() as source:
        #     print("Say something")
        #     audio=s.listen(source)
        # print("Time over")
        # language=s.recognize_google(audio)
        language=language[0].lower()+language[1:]
        print(language)
        if language=="chinese" or language=="chinese simplified":
            language="chinese (simplified)"
        elif language=="chinese traditional":
            language="chinese (traditional)"
        trans=Translator()                                  #translator object
        res=trans.translate(text,language)
        print(res.text)
        language=googletrans.LANGCODES[language]
        speech=gTTS(text=res.text,lang=language,slow=False)
        os.remove("speech.mp3")
        speech.save("speech.mp3")
        playsound.playsound("speech.mp3")
        print("")
        print("")
    elif "repeat after me" in text:
        text=text[16:]
        speak=gTTS(text=text,lang='en',slow=False)
        speak.save("speech.mp3")
        playsound.playsound("speech.mp3",True)
        print("")
        print("")
    elif "convert" in text:
        print("What would you like to convert?")
        print("1. doc to pdf")
        print("2. Image format conversion")
        choice=int(input())
        if choice==1:
            print("1. Convert docx file")
            print("2. Convert all docx files in a folder")
            ch=int(input())
            if ch==1:
                Tk().withdraw()
                inside= askopenfilename()
                outside=inside[:len(inside)-4]
                outside+="pdf"
                convert(inside,outside)
                for i in range(len(inside)):
                    if inside[i]=='/':
                        index=i
                os.startfile(inside[:index])
            else:
                root = Tk()
                root.withdraw()
                inside = filedialog.askdirectory()
                convert(inside)
                os.startfile(inside)
        elif choice==2:
                image_conversion()
        os.system('cls')
    elif "compress file" in text:
        print("Select compression format:")
        print("1. .tar.gz")
        print("2. .zip")
        choice=int(input())
        if choice==1:
            Tk().withdraw()
            inside= askopenfilename()
            for i in range(len(inside)):
                if inside[i]=='.':
                    index=i
                if inside[i]=='/':
                    index2=i
            output=inside[:index2]
            output+='//'
            name=inside[index2+1:index]
            inside=inside[index2+1:]
            shutil.make_archive(output+name,'tar',output,inside)
            os.startfile(output)
        elif choice==2:
            Tk().withdraw()
            inside= askopenfilename()
            for i in range(len(inside)):
                if inside[i]=='.':
                    index=i
                if inside[i]=='/':
                    index2=i
            output=inside[:index2]
            output+='//'
            name=inside[index2+1:index]
            inside=inside[index2+1:]
            shutil.make_archive(output+name,'zip',output,inside)
            os.startfile(output)
        os.system('cls')
    elif "compress folder" in text:
        print("Select compression format:")
        print("1. .tar.gz")
        print("2. .zip")
        choice=int(input())
        if choice==1:
            root = Tk()
            root.withdraw()
            inside = filedialog.askdirectory()
            for i in range(len(inside)):
                if inside[i]=='/':
                    index2=i
            outside=inside
            inside = r"{}".format(inside)
            shutil.make_archive(outside, 'tar',inside)
            os.startfile(inside[:index2])
        elif choice==2:
            root = Tk()
            root.withdraw()
            inside = filedialog.askdirectory()
            for i in range(len(inside)):
                if inside[i]=='/':
                    index2=i
            outside=inside
            inside = r"{}".format(inside)
            shutil.make_archive(outside, 'zip',inside)
            os.startfile(inside[:index2])
        os.system('cls')
    elif "wikipedia" in text:
        flag=False
        text=text.replace("search on wikipedia","")
        text=text.replace("on wikipedia","")
        text=text.replace("wikipedia","")
        for j in search(text, tld="co.in", num=10,stop=10,pause=2):
            print(j)
            if "en.wikipedia.org" in j:
                webbrowser.open_new_tab(j)
                flag=True
                break
        if flag==False:
            text = text.replace(' ', '+')
            URL = f"https://google.com/search?q={text}"
            webbrowser.open_new_tab(URL)
        os.system('cls')
    elif "chat mode" in text:
        # system("clear")
        master_chat()
    elif "news" in text:
        print("Fetching News....Please Wait")
        data = tweets(1, "EconomicTimes")
        speak = ""
        for i in data:
            speak += i.text
        speak = speak.replace("#", "")
        speak = gTTS(text=speak, lang='en', slow=False)
        speak.save("./audio/news.mp3")
        os.chdir("./audio/")
        os.system("news.mp3")
        os.chdir("../")
        continue
    elif text=="go to sleep":
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    elif "camera" in text:
        cam = cv2.VideoCapture(0)
        cv2.namedWindow("test")
        while True:
            ret, frame = cam.read()
            cv2.imshow("test", frame)
            if not ret:
                break
            k = cv2.waitKey(1)
            if k % 256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k % 256 == 32:
                # SPACE pressed
                img_name = "./images/opencv_frame_{}.png".format(image_count)
                cv2.imwrite(img_name, frame)
                print("{} saved!".format(img_name))
                image_count += 1
        cam.release()
        cv2.destroyAllWindows()
    elif "exit" in text:
        print("GoodBye")
        break
    else:
        text = text.replace('+', '%2B')
        text = text.replace(' ', '+')
        URL = f"https://google.com/search?q={text}"
        data=[]
        driver.get(URL)
        content=driver.page_source
        soup=BeautifulSoup(content,features='html.parser')
        try:
            # webbrowser.open_new_tab(URL)
            data=soup.find('div', attrs={'class':'ayqGOc kno-fb-ctx KBXm4e'})
            os.system('cls')
            print(data.text)
            continue
        except:
            pass
        try:
            data=soup.findAll('div', attrs={'class':'thODed Uekwlc XpoqFe'})
            # res=(data.text).split(" ")
            count=0
            os.system('cls')
            for i in data:
                if count>2:
                    break
                for j in range(2,len(i.text)):
                    if i.text[j]=='.':
                        break
                if i.text[0] not in ['1','2','3']:
                    print((count+1),end="")
                    print(". ",end="")
                if i.text[:j+1] != "":
                    print(i.text[:j+1])
                    flag=False
                else:
                    flag=True
                count+=1
                # print(i.text)
            if flag==False:
                continue
            else:
                pass
        except:
            pass
        try:
            data=soup.find('div', attrs={'class':'z7BZJb XSNERd'})
            res=(data.text).split(" ")
            os.system('cls')
            print(res[1])
            continue
        except:
            pass
        try:
            data=soup.find('div', attrs={'class':'Z0LcW XcVN5d'})
            os.system('cls')
            print(data.text)
            continue
        except:
            pass
        try:
            data=soup.find('div', attrs={'class':'Z0LcW XcVN5d AZCkJd'})
            os.system('cls')
            print(data.text)
            continue
        except:
            pass
        try:
            print("reached me")
            os.system('cls')
            webbrowser.open_new_tab(URL)
            continue
        except:
            pass
