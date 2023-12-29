# GeminiLineBot

### 1.Set parameters in the configuration file(.env)
```
GEMINI_API_KEY = xxx
LINE_ACCESS_TOKEN = xxx
LINE_CHANNEL_SECRET = xxx
NGROK_AUTHTOKEN = xxx
```

### 2.Run Gemini LineBot
**docker build** 
```
docker build . -t geminilinebot
```
**docker run** 
```
docker run -itd  geminilinebot
```

or. 

**python run** 

```
python3 gemini_linebot.py
```


  ![mole](https://github.com/bowwowxx/GeminiLineBot/blob/main/01.jpg)  

### 3.Check ngrok tunnels URL

 ```
docker logs -t containername
 ```

  ![mole](https://github.com/bowwowxx/GeminiLineBot/blob/main/05.jpg)  

### 4.Verify line bot webhook

  ![mole](https://github.com/bowwowxx/ChatGPTLineBot/blob/main/linebot-webhook.jpg)  

### 5.enjoy it !
  ![mole](https://github.com/bowwowxx/GeminiLineBot/blob/main/02.jpg)  
