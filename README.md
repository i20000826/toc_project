# Line聊天機器人

## 環境
* windows
* anaconda
* Python 3.6
* ngrok/Heroku

## 設定

### 安裝相關套件

#### anaconda
```
conda install -c conda-forge pygraphviz

pip install flask python-dotenv line-bot-sdk transitions pygraphviz
```

#### ngrok
下載ngrok <br>
在ngrok輸入: `ngrok http 8000` <br>
在terminal執行: `python app.py` <br>

#### Heroku
下載Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli <br>
註冊Heroku帳號: https://signup.heroku.com <br>
在Heroku網站Create new app <br>
在terminal登入Heroku CLI: `heroku login` <br>
如果無法辨識heroku: `set PATH=%PATH%;C:\Program Files\heroku\bin`(heroku路徑) <br>
設定line環境
```
heroku config:set LINE_CHANNEL_SECRET=[YOUR_LINE_CHANNEL_SECRET]

heroku config:set LINE_CHANNEL_ACCESS_TOKEN=[YOUR_LINE_CHANNEL_ACCESS_TOKEN]
```
放上Heroku
```
heroku git:remote -a [HEROKU_APP_NAME]

git add .

git commit -m "Add code"

git push -f heroku master
```
如果push時顯示pygraphviz安裝失敗
```
heroku buildpacks:set heroku/python

heroku buildpacks:add --index 1 heroku-community/apt
```
在line的webhook url輸入: `[HEROKU_APP_NAME].herokuapp.com/webhook` <br>
debug輸入: `heroku logs --tail --app [HEROKU_APP_NAME]` <br>

## Finite State Machine
![fsm](./fsm.png)

## 實作
The initial state is set to `user`.

Every time `user` state is triggered to `advance` to another state, it will `go_back` to `user` state after the bot replies corresponding message.

* user
	* Input: "go to state1"
		* Reply: "I'm entering state1"

	* Input: "go to state2"
		* Reply: "I'm entering state2"


