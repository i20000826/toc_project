from transitions.extensions import GraphMachine
from linebot.models import MessageTemplateAction
from utils import send_text_message, send_image_message, send_button_message

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model = self, **machine_configs)

    # 神秘成就

    def is_going_to_achievement(self, event):
        text = event.message.text
        if (text == "神秘成就"):
            return True
        return False

    def on_enter_achievement(self, event):
        send_text_message(event.reply_token, "神秘成就\n"
            "自強不息: 單人通關5星以上紫色禁忌森林\n"
            "福來再現: 一張圖書證中學習三張傳說咒語\n"
            "不幸成真: 連續五次觸發借閱保底\n"
            "無期徒刑: PVP戰鬥中使用不赦咒300次(啊哇呾喀呾啦 咒咒虐)\n"
            "夜遊之神: 去四院交誼廳(需要隱形藥水)\n"
            "魔法史先驅: 社團問答中唯一答對\n"
            "魁地奇之星: 在一場魁地奇比賽中投進10個球\n"
            "巨蛛殺手: 15分鐘內通關巨蛛領地五星難度\n\n"
            "輸入「主選單」返回主選單"
        )

    # 大世界收集

    def is_going_to_furniture(self, event):
        text = event.message.text
        if (text == "大世界收集"):
            return True
        return False

    def on_enter_furniture(self, event):
        title = "請選擇想查詢的家具"
        text = "限定款好看 隱藏款特別"
        btn = [
            MessageTemplateAction(
                label = "常駐款",
                text = "常駐款"
            ),
            MessageTemplateAction(
                label = "限定款",
                text = "限定款"
            ),
            MessageTemplateAction(
                label = "隱藏款",
                text = "隱藏款"
            ),
            MessageTemplateAction(
                label = "主選單",
                text = "主選單"
            ),
        ]
        url = "https://i.imgur.com/eGCwVab.jpg"
        send_button_message(event.reply_token, title, text, btn, url)

    def is_going_to_always(self, event):
        text = event.message.text
        if (text == "常駐款"):
            return True
        return False

    def on_enter_always(self, event):
        send_text_message(event.reply_token, "大世界收集 常駐款\n"
            "學院: 送的\n經典: 完成初級成就\n糖果主題: 完成進階成就\n禁忌森林主題: 解鎖禁森手記"
        )
        self.go_back()

    def is_going_to_limited(self, event):
        text = event.message.text
        if (text == "限定款"):
            return True
        return False

    def on_enter_limited(self, event):
        send_text_message(event.reply_token, "大世界收集 限定款\n"
            "魔藥狂熱: 第一期轉盤(2021.09)\n"
            "兩腳蛇迷蹤: 第二期轉盤(2021.10)\n"
            "萬聖節主題: 第三期轉盤(2021.11)\n"
            "冰雪主題: 第四期轉盤(2021.12)\n"
            "聖誕主題: 限時禮包獲得(2021聖誕節)\n"
            "煙火主題: 第五期轉盤(2022.01)"
        )
        self.go_back()

    def is_going_to_hidden(self, event):
        text = event.message.text
        if (text == "隱藏款"):
            return True
        return False

    def on_enter_hidden(self, event):
        send_text_message(event.reply_token, "大世界收集 隱藏款\n"
            "藍紫色線索8~10星機率掉落，紅色線索4~5星機率掉落\n"
            "帷幔 碧藍深海: 尋犬啟示 追尋獨角獸\n"
            "櫃飾 釀造榮譽: 加隆竊賊\n"
            "擺件 魔法時鐘: 尋訪人馬 魔藥事故\n\t 龍蛋標本: 丹尼爾的抉擇\n\t 水晶球: 跟隨閃電\n\t 飛天掃帚: 追尋搜捕手\n\t 結網蜘蛛:紫紅線索\n"
            "地毯 紫角獸地毯: 紫角獸之災"
        )
        self.go_back()
    
    # 占卜學圖鑑

    def is_going_to_divination_1(self, event):
        text = event.message.text
        if (text == "占卜學圖鑑" or text == "上一輪"):
            return True
        return False

    def on_enter_divination_1(self, event):
        title = "請選擇想查詢的難度"
        text = "繼續選擇難度查詢或輸入「主選單」返回主選單"
        btn = [
            MessageTemplateAction(
                label = "難度1",
                text = "難度1"
            ),
            MessageTemplateAction(
                label = "難度2",
                text = "難度2"
            ),
            MessageTemplateAction(
                label = "難度3",
                text = "難度3"
            ),
            MessageTemplateAction(
                label = "下一輪",
                text = "下一輪"
            ),
        ]
        url = "https://i.imgur.com/946WarB.jpg"
        send_button_message(event.reply_token, title, text, btn, url)

    def is_going_to_level_1(self, event):
        text = event.message.text
        if (text == "難度1"):
            return True
        return False

    def on_enter_level_1(self, event):
        send_image_message(event.reply_token, "https://i.imgur.com/hs0vkYK.jpg")
        self.go_back()

    def is_going_to_level_2(self, event):
        text = event.message.text
        if (text == "難度2"):
            return True
        return False

    def on_enter_level_2(self, event):
        send_image_message(event.reply_token, "https://i.imgur.com/GNr8MFL.jpg")
        self.go_back()

    def is_going_to_level_3(self, event):
        text = event.message.text
        if (text == "難度3"):
            return True
        return False

    def on_enter_level_3(self, event):
        send_image_message(event.reply_token, "https://i.imgur.com/VpnqOCY.jpg")
        self.go_back()

    def is_going_to_divination_2(self, event):
        text = event.message.text
        if (text == "下一輪"):
            return True
        return False

    def on_enter_divination_2(self, event):
        title = "請選擇想查詢的難度"
        text = "繼續選擇難度查詢或輸入「主選單」返回主選單"
        btn = [
            MessageTemplateAction(
                label = "難度4",
                text = "難度4"
            ),
            MessageTemplateAction(
                label = "難度5",
                text = "難度5"
            ),
            MessageTemplateAction(
                label = "上一輪",
                text = "上一輪"
            ),
        ]
        url = "https://i.imgur.com/946WarB.jpg"
        send_button_message(event.reply_token, title, text, btn, url)

    def is_going_to_level_4(self, event):
        text = event.message.text
        if (text == "難度4"):
            return True
        return False

    def on_enter_level_4(self, event):
        send_image_message(event.reply_token, "https://i.imgur.com/NoltEN8.jpg")
        self.go_back()

    def is_going_to_level_5(self, event):
        text = event.message.text
        if (text == "難度5"):
            return True
        return False

    def on_enter_level_5(self, event):
        send_image_message(event.reply_token, "https://i.imgur.com/llUEvYn.jpg")
        self.go_back()

    #禁忌森林

    def is_going_to_forbidden_forest_1(self, event):
        text = event.message.text
        if (text == "禁忌森林" or text == "第一批線索"):
            return True
        return False

    def on_enter_forbidden_forest_1(self, event):
        title = "請選擇想查詢的線索 此為第一批"
        text = "繼續選擇線索查詢或輸入「主選單」返回主選單"
        btn = [
            MessageTemplateAction(
                label = "尋訪人馬",
                text = "尋訪人馬"
            ),
            MessageTemplateAction(
                label = "魔藥事故",
                text = "魔藥事故"
            ),
            MessageTemplateAction(
                label = "追尋獨角獸",
                text = "追尋獨角獸"
            ),
            MessageTemplateAction(
                label = "第二批線索",
                text = "第二批線索"
            ),
        ]
        url = "https://i.imgur.com/WQ79nr8.jpg"
        send_button_message(event.reply_token, title, text, btn, url)

    def is_going_to_forbidden_forest_2(self, event):
        text = event.message.text
        if (text == "第二批線索"):
            return True
        return False

    def on_enter_forbidden_forest_2(self, event):
        title = "請選擇想查詢的線索 此為第二批"
        text = "繼續選擇線索查詢或輸入「主選單」返回主選單"
        btn = [
            MessageTemplateAction(
                label = "尋犬啟示",
                text = "尋犬啟示"
            ),
            MessageTemplateAction(
                label = "丹尼爾的抉擇",
                text = "丹尼爾的抉擇"
            ),
            MessageTemplateAction(
                label = "加隆竊賊",
                text = "加隆竊賊"
            ),
            MessageTemplateAction(
                label = "第三批線索",
                text = "第三批線索"
            ),
        ]
        url = "https://i.imgur.com/WQ79nr8.jpg"
        send_button_message(event.reply_token, title, text, btn, url)

    def is_going_to_forbidden_forest_3(self, event):
        text = event.message.text
        if (text == "第三批線索"):
            return True
        return False

    def on_enter_forbidden_forest_3(self, event):
        title = "請選擇想查詢的線索 此為第三批"
        text = "繼續選擇線索查詢或輸入「主選單」返回主選單"
        btn = [
            MessageTemplateAction(
                label = "紫角獸之災",
                text = "紫角獸之災"
            ),
            MessageTemplateAction(
                label = "跟隨閃電",
                text = "跟隨閃電"
            ),
            MessageTemplateAction(
                label = "搜尋搜捕手",
                text = "搜尋搜捕手"
            ),
            MessageTemplateAction(
                label = "第一批線索",
                text = "第一批線索"
            ),
        ]
        url = "https://i.imgur.com/WQ79nr8.jpg"
        send_button_message(event.reply_token, title, text, btn, url)

    def is_going_to_centaur(self, event):
        text = event.message.text
        if (text == "尋訪人馬"):
            return True
        return False

    def on_enter_centaur(self, event):
        send_text_message(event.reply_token, "尋訪人馬11\n以下適用2~10星\n\n"
            "0/7\n_<戰鬥>挪威脊背龍(動畫): 一進禁忌森林就碰上一條會噴火的龍?!看情形，她還不是一般生氣。\n\n"
            "1/7\n_<對話>海格: 聽海格說，有人重傷了那條龍，還偷走了她的龍蛋……今晚註定是個不寧夜。\n\n"
            "2/7\n_不要打擾她，偷偷溜走: 不要隨意叫醒一條沉睡中的龍，這是避免一場惡戰的最佳方式。\n"
                 "_幫她治療一下(白鮮液8級): 雖然不知道白鮮液會不會對龍起作用，但我還是冒著\"生命危險\"幫她治療了一下。 *2~10星獨有\n\n"
            "4/7\n_接受歡樂靈藥: 看來丹尼爾是禁忌森林的常客。因為聽我說完龍和黑巫師在附近活動後，他相當冷靜。\n"
                 "_接受巧克力: 聽說我要幫助海格在禁忌森林中尋找龍蛋，魔藥天才丹尼爾送我了一些歡樂靈藥。對於他的魔藥手藝，我一向很信任。\n\n"
            "5/7\n_湊近一點聽他們的對話 <戰鬥>黑巫師 撿起樹下的龍蛋: 有時直面恐懼，堅持心中認為正確的選擇，最後就能戰勝恐懼!真幸運，我找回了龍蛋!\n"
                 "_悄悄地……溜走 <戰鬥>黑巫師: 那一刻我遲疑了……實話實說，我確實有點害怕，畢竟要面對兩個成年黑巫師。\n\n"
            "6/7\n_她看上去十分憤怒，恐怕只能作戰了 <戰鬥>首領(A結局): 母龍的突然降臨，攪亂了戰場……最終我和海格不得不同時對付兩個黑巫師和一頭發怒的母龍。\n"
                 "_將龍蛋放下，示意自己沒有敵意 <戰鬥>首領(B結局): 希望找回龍蛋後，她心中的憤怒可以平息。畢竟不管哪種生物，母親這個角色做起來都不輕鬆。\n\n"
            "*1星獨有: 0/7向人馬的方向跑去+1/7向人馬問路+3/7選左調查\n"
                 "_謝謝，我會幫你留意材料的: 在禁忌森林深處遇到了人馬，他上半身與人無異，下半身則是馬的模樣。他為我的前路作出了預言，但我不太明白……\n\n"
            "結局路線\n"
                 "A結局: 什麼都不觸發\n"
                 "B結局: 5/7湊近一點聽他們的對話+撿起樹下的龍蛋"
        )
        self.go_back()

    def is_going_to_potion(self, event):
        text = event.message.text
        if (text == "魔藥事故"):
            return True
        return False

    def on_enter_potion(self, event):
        send_text_message(event.reply_token, "魔藥事故8\n\n"
            "1/7\n_安靜地偷聽他們在吵什麼: 多虧弗雷兄弟，我得知了卡珊卓的計畫……我一定要阻止她的瘋狂行為。\n"
                 "_走上前詢問發生了什麼: 多虧弗雷兄弟，我得知了卡珊卓的計畫……我一定要阻止她的瘋狂行為。\n\n"
            "3/7\n_調查空地: 卡珊卓調配製了一種藥水，但那肯定不是縮骨藥水，因為她沒有收集到全部的材料!\n"
                 "_朝著閃光走去: 我跟隨奇怪的閃光進入了禁忌森林的深處，最後我發現了一些爆尾釘蝦的蹤跡……但它們看上去比平常更大，更有攻擊性!\n\n"
            "5/7\n_和弗雷兄弟說話: 弗雷兄弟根本不是我的對手!這樣的幫手確定不是來拖後腿的嗎?\n"
                 "_無視弗雷兄弟，追蹤蹤跡: 我跟隨奇怪的閃光進入了禁忌森林的深處，最後我發現了一些爆尾釘蝦的蹤跡……但牠們看上去比平常更大，更有攻擊性!\n"
                 "_告訴弗雷兄弟關於卡珊卓的大釜的事(3/7調查空地): 我把卡珊卓和大釜的事情告訴了弗雷兄弟，他們沒有攻擊我，並準備去尋找她。看來他們認為這件事更重要。\n\n"
            "6/7\n_<戰鬥>首領(A結局): 梅林的鬍子，禁忌森林裡竟然有這麼多異變的爆尾釘蝦!我能活著回來真是個奇蹟。\n"
                 "_<戰鬥>首領(B結局): 我從來都沒有想過我會和卡珊卓並肩作戰，但不這樣做，我們可能就沒命了。當然，事後她沒有感謝我。\n"
                 "_<戰鬥>首領(C結局): 禁忌森林裡真是太瘋狂了……好在卡珊卓的縮骨藥水沒有配置成功，她瘋狂得就像是一隻爆尾釘蝦。\n\n"
            "結局路線\n"
                "A結局: 什麼都不觸發\n"
                "B結局: 5/7和弗雷兄弟說話或無視弗雷兄弟，追蹤蹤跡\n"
                "C結局: 1/7安靜地偷聽他們在吵什麼+3/7調查空地+5/7告訴弗雷兄弟關於卡珊卓的大釜的事+6/7卡珊卓存活"
        )
        self.go_back()

    def is_going_to_unicorn(self, event):
        text = event.message.text
        if (text == "追尋獨角獸"):
            return True
        return False

    def on_enter_unicorn(self, event):
        send_text_message(event.reply_token, "追尋獨角獸15\n\n"
            "0/7\n_詢問獨角獸的資訊: \"步態似人的狼\"，還是\"步態似狼的人\"?不管這位人馬想表達什麼，他指的一定就是狼人了。\n"
                 "_詢問洛蒂的去向: \"步態似人的狼\"，還是\"步態似狼的人\"?不管這位人馬想表達什麼，他指的一定就是狼人了。\n\n"
            "2/7\n_調查灌木叢(0/7詢問獨角獸的資訊+1/7選右): 我在禁忌森林中找到了一根銀白色的毛髮，這一定是獨角獸的毛髮。\n"
                 "_調查樹椿(0/7詢問獨角獸的資訊+1/7選右)\n"
                 "_撿起草藥(0/7詢問獨角獸的資訊+1/7選右+2/7調查樹樁): 我找到了一些罕見的草藥和金幣，彌補了沒找到獨角獸的遺憾。蜂蜜公爵糖果店，我來啦!\n"
                 "_還是不拔草藥了(0/7詢問獨角獸的資訊+1/7選右+2/7調查樹樁): 我在禁忌森林中找到了獨角獸的蹤跡，同時還發現一些我從沒見過的草藥。我敢打賭，丹尼爾一定會對它們感興趣。\n"
                 "_調查石頭(0/7詢問洛蒂的去向+1/7選右)\n"
                 "_調查木樁(0/7詢問洛蒂的去向+1/7選右)\n"
                 "_撿起草藥(0/7詢問洛蒂的去向+1/7選右+2/7調查石頭): 我在禁忌森林中找到了一些草藥──但我沒有看到洛蒂!希望她沒事。\n"
                 "_還是不拔草藥了(0/7詢問洛蒂的去向+1/7選右+2/7調查石頭)\n"
                 "_拾取畫筆(0/7詢問洛蒂的去向+1/7選右+2/7調查木樁): 好消息!我找到了洛蒂的畫筆，壞消息……沒有看到洛蒂!希望她沒事。\n"
                 "_不拾取畫筆(0/7詢問洛蒂的去向+1/7選右+2/7調查木樁)\n\n"
            "4/7\n_繼續尋找洛蒂(0/7詢問獨角獸的資訊+1/7選右+2/7調查灌木叢): 找到洛蒂才是最重要的任務，我無暇顧及這隻髒兮兮的獨角獸，希望下次還能遇到它。\n"
                 "_停下來撫摸獨角獸(0/7詢問獨角獸的資訊+1/7選右+2/7調查灌木叢): 我找到了一隻髒兮兮的獨角獸，並用\"水水噴\"咒為它洗了個澡。它看起來棒極了，光彩照人。\n"
                 "_使用「水水噴」沖洗獨角獸(水水噴10級)(0/7詢問獨角獸的資訊+1/7選右+2/7調查灌木叢): 這隻獨角獸髒得讓人難以忍受，我不得不用\"水水噴\"清潔一下它，它看起來好像很享受。\n"
                 "_和洛蒂打招呼(0/7詢問洛蒂的去向): 找到洛蒂了!原來她正在禁忌森林裡尋找畫筆。我讓她打消了繼續尋找的念頭，因為禁忌森林裡不安全。\n"
                 "_嚇洛蒂一跳(0/7詢問洛蒂的去向): 我本以為嚇洛蒂一跳會很有趣的……這真是個糟糕的主意，希望她能原諒我。\n"
                 "_把畫筆給洛蒂(0/7詢問洛蒂的去向+1/7選右+2/7調查木樁+拾取畫筆): 我終於找到了洛蒂，還把她遺失的畫筆還給她了。我從未見過她如此高興!\n\n"
            "6/7\n_<戰鬥>首領(A結局): 我希望我這輩子都不要再和狼人戰鬥——事實上，我連見都不想再見到它們。它們真是太可怕了!\n"
                 "_<戰鬥>首領(B結局)\n"
                 "_<戰鬥>首領(C結局): 洛蒂和我真是黃金搭檔。我們共同擊敗了狼人!可惜的是她的畫筆永遠遺失在了禁忌森林裡。\n"
                 "_<戰鬥>首領(D結局): 洛蒂的施咒水準和她的繪畫技巧一樣出色，我們共同擊敗了狼人，並找回了她的畫筆，這對她來說比擊敗狼人還重要。\n\n"
            "結局路線\n"
                 "A結局: 什麼都不觸發\n"
                 "B結局: 0/7詢問獨角獸的資訊+1/7選右+2/7調查灌木叢+3/7選中+4/7停下來撫摸獨角獸\n"
                 "C結局: 0/7詢問洛蒂的去向+6/7洛蒂存活\n"
                 "D結局: 0/7詢問洛蒂+1/7選右+2/7調查木樁+拾取畫筆+4/7把畫筆給洛蒂+6/7洛蒂死亡"

        )
        self.go_back()

    def is_going_to_dog(self, event):
        text = event.message.text
        if (text == "尋犬啟示"):
            return True
        return False

    def on_enter_dog(self, event):
        send_text_message(event.reply_token, "尋犬啟示12\n\n"
            "0/6\n_追牙牙──你可不想把它跟丟了: 誰能想到遛牙牙會遇到麻煩?我們才走了五分鐘，它就跑丟了!\n"
                 "_去找海格──他知道該怎麼做: 雖然海格沒有責怪我們弄丟牙牙，但我們還是非常內疚。\n\n"
            "1/6\n_調查水漥(0/6追牙牙): 我在禁忌森林裡發現了一灘……血跡，我總忍不住往最壞的方面想，希望不是牙牙留下的。\n"
                 "_忽略水漥(0/6追牙牙): 我好像看到了一灘液體，但我無心停下來觀察，找到牙牙更加重要。\n"
                 "_調查水漥(0/6去找海格): 就連海格看到那灘血之後都憂心忡忡的，他也從來沒遇見過這種情況。\n"
                 "_忽略水漥(0/6去找海格): 海格和我在禁忌森林中找到了一灘奇怪的液體，但我們沒有看見牙牙，希望它沒事。\n\n"
            "3/6\n_遇到黑巫師(0/6追牙牙+1/6選放大鏡+2/6選右): 卑鄙的黑巫師在我毫無防備的時候偷襲我!雖然我打敗了他，但仍然沒有牙牙的蹤跡。\n"
                 "_靜靜地跟著黑巫師(0/6找海格+1/6選放大鏡+2/6選右): 我在禁忌森林中撿到了一把口琴，那時候我們就意識到附近有三頭巨犬在遊蕩。海格對此一點都不感到驚訝!\n"
                 "_繞開黑巫師(0/6找海格+1/6選放大鏡+2/6選右): 拿著小粉傘的海格是最可靠的夥伴，我隨時都願意和他並肩作戰。\n\n"
            "5/6\n_<戰鬥>首領(A結局): 三頭巨犬又兇猛又可怕，但它的口水才是最糟糕的部分，希望夥伴們明天不要嫌棄我。\n"
                 "_<戰鬥>首領(B結局): 三頭巨犬太可怕了，但是它們在口琴面前卻毫無抵抗力。\n"
                 "_<戰鬥>首領(C結局): 謝天謝地，還好有海格與我並肩作戰，你永遠可以信賴海格。\n\n"
            "結局路線\n"
                 "A結局: 什麼都不觸發\n"
                 "B結局: 0/6去找海格+1/6調查水漥+2/6選右+3/6靜靜地跟著黑巫師\n"
                 "C結局: 0/6去找海格+1/6選放大鏡+2/6選右+3/6繞開黑巫師"
        )
        self.go_back()

    def is_going_to_daniel(self, event):
        text = event.message.text
        if (text == "丹尼爾的抉擇"):
            return True
        return False

    def on_enter_daniel(self, event):
        send_text_message(event.reply_token, "丹尼爾的抉擇13\n\n"
            "0/7\n_查看岩石\n"
                 "_忘記岩石……你必須找到丹尼爾: 我還沒找到丹尼爾，但我卻找到了一堆石頭。說實話，我有點失望!\n"
                 "_仔細觀察(0/7查看岩石): 我還沒找到丹尼爾，但我卻找到了一些龍蛋。其中一顆蛋已經孵化了，牠們散發著白鮮的氣味。\n"
                 "_不管蛋了，你必須找到丹尼爾(0/7查看岩石): 林間的空地上有一些龍蛋，他們比丹尼爾更早出現在我的視線裡。\n\n"
            "2/7\n_小心地接近龍寶寶(0/7查看岩石+仔細觀察): 一隻龍寶寶，它看上去很友好，我覺得它能帶我找到丹尼爾。\n"
                 "_偷偷地跟著龍寶寶(0/7放大鏡): 我找到了一隻龍寶寶。我決定先別靠近，以免打擾到它。還是先尋找丹尼爾吧。\n"
                 "_開始對戰(0/7查看岩石+不管蛋了，你必須找到丹尼爾+2/7小心地接近龍寶寶)或(0/7忘記岩石……你必須找到丹尼爾+2/7小心地接近龍寶寶): 這隻龍寶寶看起來很傷心，是因為和媽媽走丟了嗎?我決定留在原地保護它。\n"
                 "_不理會龍寶寶(0/7查看岩石+不管蛋了，你必須找到丹尼爾+2/7小心地接近龍寶寶)或(0/7忘記岩石……你必須找到丹尼爾+2/7小心地接近龍寶寶): 在尋找丹尼爾的路上，我找到了一隻龍寶寶。它看起來不太高興，我最好還是不要招惹它。\n\n"
            "4/7\n_把龍寶寶安置在一個中空的樹幹中(0/7查看岩石+仔細觀察+2/7小心地接近龍寶寶+3/7選右)或(0/7忘記岩石……你必須找到丹尼爾+2/7偷偷地跟著龍寶寶+3/7選右): 我對受傷的龍寶寶無能為力，我並不擅長治療，所以我把它留在了原地。\n"
                 "_溫柔地拿起龍寶寶並把它帶在身邊(0/7查看岩石+仔細觀察+2/7小心地接近龍寶寶+3/7選右)或(0/7忘記岩石……你必須找到丹尼爾+2/7偷偷地跟著龍寶寶+3/7選右): 可憐的龍寶寶受傷了──它被咬傷了!我對治療不太在行，但是丹尼爾或許有辦法，他很擅長療傷。\n\n"
            "6/7\n_<戰鬥>首領(A結局): 我沒有找到丹尼爾，但找到了一隻成年的紐澳彩眼!那真是一場驚心動魄的戰鬥!\n"
                 "_<戰鬥>首領(B結局): 我終於找到了丹尼爾──和一隻成年的紐澳彩眼!那是一場艱難的戰鬥，但是我成功趕走了這個大傢伙。\n"
                 "_<戰鬥>首領(C結局): 我終於找到了龍寶寶的媽媽──一隻成年的紐澳彩眼!是丹尼爾讓這對母子重聚了，真是太好了!\n"
                 "_<戰鬥>首領(D結局): 一隻成年的紐澳彩眼幾乎就要對我發動攻擊了!好在龍寶寶醒來了，真是有驚無險!\n\n"
            "結局路線\n"
                 "A結局: 什麼都不觸發\n"
                 "B結局: 0/7查看岩石+仔細觀察+2/7小心地接近龍寶寶+3/7選右+4/7把龍寶寶安置在一個中空的樹幹中\n"
                 "B結局: 0/7查看岩石+不管蛋了，你必須找到丹尼爾+2/7小心地接近龍寶寶+不理會龍寶寶+3/7選右+4/7溫柔地拿起龍寶寶並把它帶在身邊\n"
                 "C結局: 0/7查看岩石+仔細觀察+2/7小心地接近龍寶寶+3/7選右+4/7溫柔地拿起龍寶寶並把它帶在身邊\n"
                 "D結局: 0/7忘記岩石……你必須找到丹尼爾+2/7偷偷地跟著龍寶寶+3/7選右+4/7溫柔地拿起龍寶寶並把它帶在身邊"
        )
        self.go_back()

    def is_going_to_galleon(self, event):
        text = event.message.text
        if (text == "加隆竊賊"):
            return True
        return False

    def on_enter_galleon(self, event):
        send_text_message(event.reply_token, "加隆竊賊12\n\n"
            "1/8\n_試著和玻璃獸說話\n"
                 "_抓住玻璃獸，並把金幣從它的口袋搖出來: 成功!我找到了玻璃獸和一部份遺失的加隆。不過我是不是該讓龐芮夫人看一看我被玻璃獸咬出來的傷口?\n"
                 "_試著再次和玻璃獸說話(1/8試著和玻璃獸說話)\n"
                 "_不管玻璃獸，繼續前行(1/8試著再次和玻璃獸說話): 看來教授說的沒錯──一隻玻璃獸偷走了加隆，而且藏在了禁忌森林裡。玻璃獸，別跑!我盯上你了!\n"
                 "_用加隆吸引玻璃獸的注意力(1/8試著再次和玻璃獸說話): 我居然找到了玻璃獸和遺失的加隆……可惜我讓它逃走了。我真想歸還那些加隆來換取一些獎勵，比如為學院加上十分之類的!\n\n"
            "3/8\n_屏住呼吸偷聽他們說話(1/8選放大鏡+2/8選中)\n"
                 "_先發制人──施咄咄失(需要掌握咄咄失)(1/8選放大鏡+2/8選中): 主動攻擊那些巫師可能不是一個好主意，但他們看上去就不是什麼好東西。總的來說，那是一場不錯的決鬥練習!\n"
                 "_偷偷離開現場(1/8選放大鏡+2/8選中+3/8屏住呼吸偷聽他們說話): 我聽到兩個巫師說他們正在追捕那隻可憐的玻璃獸，因為它偷走了他們主人的金子。我很慶幸他們沒有發現我在偷聽。\n"
                 "_保護玻璃獸——對黑巫師施咄咄失(需要掌握咄咄失)(1/8選放大鏡+2/8選中+3/8屏住呼吸偷聽他們說話): 那些巫師正要對付手無寸鐵的玻璃獸，我得做些什麼。和他們對戰或許不是明智之舉，但我必須這麼做!\n\n"
            "5/8\n_用治療咒為玻璃獸療傷(白鮮液10級)(1/8抓住玻璃獸，並把金幣從它的口袋搖出來+2/8選中+3/8屏住呼吸偷聽他們說話+保護玻璃獸+4/8選中): 我又見到了那隻玻璃獸，它看上去好像受傷了。但不久它就恢復了體力並開始跟著我!\n"
                 "_接近玻璃獸並試著安慰它(1/8抓住玻璃獸，並把金幣從它的口袋搖出來+2/8選中+3/8屏住呼吸偷聽他們說話+保護玻璃獸+4/8選中): 受傷的玻璃獸對我好像並不信任，它休息了一會就跑掉了。\n\n"
            "7/8\n_<戰鬥>首領(A結局): 這是目前最奇怪的一次禁忌森林之旅了!玻璃獸，黑巫師，還有決鬥，我能夠毫髮無損地回到城堡裡真是幸運。\n"
                 "_<戰鬥>首領(B結局): 真不敢相信那些壞巫師帶著玻璃獸逃走了!我沒能救下它，我感到很遺憾。\n"
                 "_<戰鬥>首領(C結局): 打敗了巫師並救出玻璃獸之後，我得到了一個驚喜……一隻金色的懷錶!可能是玻璃獸丟下的，但這只是我的猜測……\n"
                 "_<戰鬥>首領(D結局): 我為了玻璃獸與兩個黑巫師進行了決鬥，贏得勝利的同時還拿回了丟失的加隆。\n\n"
            "結局路線\n"
                 "A結局: 什麼都不觸發\n"
                 "B結局: 1/8用加隆吸引玻璃獸的注意力+2/8選中+3/8屏住呼吸偷聽他們說話+保護玻璃獸+4/8選中+5/8接近玻璃獸並試著安慰它+7/8玻璃獸死亡\n"
                 "C結局: 1/8抓住玻璃獸，並把金幣從它的口袋搖出來+2/8選中+3/8先發制人+4/8選中+5/8選放大鏡+7/8玻璃獸存活\n"
                 "D結局: 1/8不管玻璃獸，繼續前行+2/8選中+3/8屏住呼吸偷聽他們說話+偷偷離開現場+4/8選中+5/8接近玻璃獸並試著安慰它+7/8玻璃獸存活"
        )
        self.go_back()

    def is_going_to_graphorn(self, event):
        text = event.message.text
        if (text == "紫角獸之災"):
            return True
        return False

    def on_enter_graphorn(self, event):
        send_text_message(event.reply_token, "紫角獸之災12\n\n"
            "2/9\n_施展颶風咒(颶風咒達到12級): 有人說禁忌森林裡有隻紫角獸，我的確找到了一些四個腳趾的腳印，不過更奇怪的是，我在樹上找到了一個快浮。\n"
                 "_搖樹: 樹上的隆隆果和地上的四趾腳印會有什麼聯繫呢?\n\n"
            "4/9\n_什麼快浮?(2/9施展颶風咒): 艾略特口中的消息值得相信嗎？禁忌森林裡有龐然大物跑過的聲音，會是什麼呢?\n"
                 "_把快浮交給艾略特(2/9施展颶風咒): 艾略特‧艾弗斯說禁忌森林裡有一個帶著兜帽的高個子在遊蕩，但我不太瞭解艾略特，我可以相信他嗎?\n\n"
            "6/9\n_應該只是一些在禁忌森林遊蕩的生物吧。這裡到處都是這樣的生物(2/9施展颶風咒+4/9選放大鏡): 我們還沒找到禁忌森林中騷動的源頭，海格說可能是某個動物鬧出的動靜……而且是本不該出現在這裡的生物!\n"
                 "_可能有人不懷好意。禁忌森林是個做壞事的好地方(2/9施展颶風咒+4/9選放大鏡): 海格說可能是一名走私者和他的綠仙……我很好奇他們為什麼會弄出這些響動。\n\n"
            "8/9\n_紫角獸一定是這一切騷亂的源頭，攻擊吧! <戰鬥>首領(A結局): 騷動原來是一隻紫角獸造成的——我和它進行了一番激烈的搏鬥並制服了它!\n"
                 "_你不想惹麻煩，於是你藏在了一棵樹後面(2/9施展颶風咒、4/9選放大鏡、6/9選放大鏡)\n"
                 "_這就是海格所說的那個走私者(2/9施展颶風咒+4/9什麼快浮?+6/9選放大鏡+8/9你不想惹麻煩，於是你藏在了一棵樹後面): 我遇到了一位商人，雖然他憤怒地矢口否認，但我覺得他就是海格口中的走私者，這就能解釋紫角獸造成的所有破壞了。\n"
                 "_他不是海格告訴我的走私者(2/9施展颶風咒+4/9把快浮交給艾略特+6/9選放大鏡+8/9你不想惹麻煩，於是你藏在了一棵樹後面): 這位商人幫了我一把，我最終制服了紫角獸，我很感謝他。但仍對他的意圖有所疑慮……。\n"
                 "_走上前偷聽對話 <戰鬥>首領(B結局): 我早就知道我會在禁忌森林中遇到奇怪的事情，但是有巫師想用壞掉的港口鑰走私紫角獸?這真是太不可思議了!\n"
                 "_在他們看到你之前發起攻擊 <戰鬥>首領(C結局): 我還是沒法把巫師、綠仙、港口鑰和紫角獸聯繫在一起?也許我再也不會遇到這樣奇怪的事了。\n"
                 "_走上前偷聽對話 <戰鬥>首領(D結局): 如果沒有海格的幫助，這個巫師就會成功地用壞掉的港口鑰走私紫角獸\n\n"
            "結局路線\n"
                 "A結局: 什麼都不觸發\n"
                 "B結局: 2/9施展颶風咒+4/9什麼快浮?+6/9選放大鏡+8/9你不想惹麻煩，於是你藏在了一棵樹後面+這就是海格所說的那個走私者+走上前偷聽對話\n"
                 "C結局: 2/9施展颶風咒+4/9什麼快浮?+6/9選放大鏡+8/9你不想惹麻煩，於是你藏在了一棵樹後面+這就是海格所說的那個走私者+在他們看到你之前發起攻擊\n"
                 "C結局: 2/9施展颶風咒+4/9把快浮交給艾略特+6/9選放大鏡+8/9你不想惹麻煩，於是你藏在了一棵樹後面+他不是海格告訴我的走私者+在他們看到你之前發起攻擊\n"
                 "D結局: 2/9施展颶風咒+4/9把快浮交給艾略特+6/9可能有人不懷好意。禁忌森林是個做壞事的好地方+8/9你不想惹麻煩，於是你藏在了一棵樹後面+他不是海格告訴我的走私者+走上前偷聽對話"
        )
        self.go_back()

    def is_going_to_thunder(self, event):
        text = event.message.text
        if (text == "跟隨閃電"):
            return True
        return False

    def on_enter_thunder(self, event):
        send_text_message(event.reply_token, "跟隨閃電11\n\n"
            "0/8\n_跟隨艾薇: 艾薇像以前一樣毫不猶豫地開始冒險，但我認為應該在原地等待海格，所以我們兵分兩路。\n"
                 "_在原地等待海格: 艾薇像以前一樣毫不猶豫地開始冒險，但我認為應該在原地等待海格，所以我們兵分兩路。\n\n"
            "2/8\n_調查這片區域(0/8跟隨艾薇): 我們到底還要為多管閒事付出多少次代價。探索八眼巨蛛的巢穴真是大錯特錯。\n"
                 "_說服艾薇離開(0/8跟隨艾薇): 艾薇和我路過了一個巨大的八眼巨蛛巢穴，我們決定不多管閒事，現在看來這個決定是正確的。\n"
                 "_施放路摸思(0/8等待海格)\n"
                 "_繼續前行(0/8等待海格): 我就知道不等海格的話，我們一定會遇到麻煩的!我看到艾薇的訊號，跑進了禁忌森林，卻沒找到她。\n"
                 "_調查這片區域(0/8等待海格+2/8施放路摸思): 一看到艾薇的紅色火光，我就知道她又惹麻煩了。我擊退了一大群蜘蛛，從蛛網中救出了她。\n"
                 "_熄滅魔杖，繼續前行(0/8等待海格+2/8施放路摸思): 我看到了艾薇的紅色火光，跑進了禁忌森林，但是我沒有找到她。蜘蛛!除了蜘蛛還是蜘蛛。\n\n"
            "6/8\n_調查樹叢(0/8跟隨艾薇+2/8說服艾薇+3/8選右+4/8選右+5/8選左): 那個奇怪的羽毛，還有\"跟隨閃電\"的指示，原來海格的客人是雷鳥!\n"
                 "_跟隨閃電!(0/8跟隨艾薇+2/8說服艾薇+3/8選右+4/8選右+5/8選左): 海格的客人一定是雷鳥!難怪他留給我們的指示是\"跟隨閃電\"。\n\n"
            "7/8\n_<戰鬥>首領(A結局): 海格讓我們自己先去見他的神秘客人。他說只要\"跟隨閃電\"就可以了，不過我們多少還是有些不放心。\n"
                 "_<戰鬥>首領(B結局): 好在海格阻止了我們和雷鳥大動干戈，我們的目標應該是那個趁亂溜掉的商人才對!\n"
                 "_<戰鬥>首領(C結局): 海格的客人原來是一隻雷鳥——我揍了它一頓……下手有點重。好在艾薇阻止了我，還把事情的經過告訴了我……那個貪婪的商人支開了海格，想利用雷鳥獲得閃電!\n\n"
            "結局路線\n"
                 "A結局: 什麼都不觸發\n"
                 "B結局: 0/8跟隨艾薇+2/8說服艾薇離開+3/8選右+4/8選右+5/8選左+6/8選放大鏡\n"
                 "C結局: 0/8等待海格+2/8施放路摸思+熄滅魔杖，繼續前行"
        )
        self.go_back()

    def is_going_to_seeker(self, event):
        text = event.message.text
        if (text == "搜尋搜捕手"):
            return True
        return False

    def on_enter_seeker(self, event):
        send_text_message(event.reply_token, "搜尋搜捕手9\n\n"
            "0/9\n_尋找凱文: 太糟了，凱文獨自去尋找羅賓了，我需要在凱文迷失在禁忌森林裡之前找到他!\n"
                 "_在此處等待凱文: 太糟了，凱文獨自去尋找羅賓了，我需要在凱文迷失在禁忌森林裡之前找到他!\n\n"
            "3/9\n_使用修復咒(當前魔力大於5): 我沒有找到凱文，但找到了羅賓四分五裂的掃帚，並修好了它。\n"
                 "_忽略飛天掃帚: 還是沒有找到凱文的蹤影，但羅賓的掃帚已經面目全非，我不敢想像她看到會有多傷心。\n\n"
            "6/9\n_使用咄咄失: 我終於找到被大黑貓纏上的凱文並把他救了出來，但願他不要患上恐貓症。讓他休息會吧，我去找羅賓。\n"
                 "_使用繩繩禁(繩繩禁11級): 打敗黑貓魔救出凱文並不算什麼，不過我們還有更重要的任務──找到羅賓。\n\n"
            "8/9\n_<戰鬥>首領(A結局): 凱文獨自去尋找羅賓了，這可真是個\"明智\"的決定。要知道他連在城堡裡都會迷路!\n"
                 "_<戰鬥>首領(B結局): 我們剛剛逃過一劫，可凱文和羅賓現在卻有心情懷念魁地奇球場上的往事。聽起來有點古怪，不過還是很甜蜜的。\n"
                 "_<戰鬥>首領(C結局): 凱文雖然不一定能保護得了自己，但羅賓遇到危險時，他會毫不猶豫地站出來。不過凱文說得沒錯──她總是自找麻煩。\n"
                 "_<戰鬥>首領(D結局): 凱文和羅賓居然在討論如何保養飛天掃帚，拜託，你們可剛剛死裡逃生。\n\n"
            "結局路線\n"
                 "A結局: 什麼都不觸發\n"
                 "B結局: 0/9尋找凱文+3/9使用修復咒+6/9使用繩繩禁+8/9凱文存活\n"
                 "C結局: 0/9尋找凱文+3/9使用修復咒+6/9使用繩繩禁+8/9凱文死亡\n"
                 "D結局: 0/9尋找凱文+3/9忽略飛天掃帚+6/9使用繩繩禁"
        )
        self.go_back()

    # 主選單

    def is_going_to_menu(self, event):
        text = event.message.text
        if (text == "主選單"):
            return True
        return False

    def on_enter_menu(self, event):
        send_text_message(event.reply_token, "霍格華茲的學生你好!\n"
            "輸入「神秘成就」取得成就解鎖方式\n輸入「大世界收集」取得家具獲取方式\n輸入「占卜學圖鑑」查看圖鑑\n"
            "輸入「禁忌森林」取得禁森手記攻略\n隨時輸入「fsm」取得fsm狀態圖"
        )
        self.go_back()
