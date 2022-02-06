# speak function 
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == '__main__':
    import requests
    import json
    r=requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=4818d9ee6a0640efa8efb6fc93a93e63')
    resJson = json.loads(r.text)
    print(resJson)
    number = 1
    for item in resJson['articles']:
        speak(f"{number} the source of this news is {item['source']['name']}")
        speak(f"title {item['title']}")
        number += 1