
import requests
import re
from bs4 import BeautifulSoup

def get_video(url):
    
    print("processing....")

    lst=url.split('/')
    filename=lst[-1]

    res= requests.get(url)
    soup= BeautifulSoup(res.content, "html5lib")
    for data in soup.find_all("script"):
        if re.search(r"props",str(data)):
            tmp= re.search(r'file\\(.*\.mp4)',str(data))
            #print(tmp.group(0))
            tmp1= re.search(r':\\.(.*)',tmp.group(0))
            mp4_file= tmp1.group(1)

    print('downloading '+filename+'....')

    r= requests.get(mp4_file)
    with open("videos/"+filename+".mp4", 'wb') as mp4:
        mp4.write(r.content)
    
    print(filename+" downloaded !")
        


if __name__ == "__main__":
    
    #url="https://www.ted.com/talks/anees_bahji_why_are_eating_disorders_so_hard_to_treat"
    url="https://www.ted.com/talks/katherine_maher_wikipedia_s_enduring_nuanced_perspective_on_truth"

    url=str(input("enter teded video url : "))

    try:
        get_video(url)
    except:
        print("check readme.md")