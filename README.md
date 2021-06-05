# 2021/06/05 
## 功能 :
+ 點餐用 
  點餐
  點@{你是誰@餐點內容@金額}
  收單
  
+ 抽飲料
+ 菜單@{要查詢的店家}
+ 熱量@{要查詢的食物}
+ 食記@{要查詢的店家}
+ 遊記@{要查詢的地點}
+ 影評@{要查詢的電影}
+ 提問@{要問的事情}
+ Wiki@{要在Wiki上查的事情}

## 說明
### SQLite
+ 食物熱量資料庫
+ 菜單圖片網址資料庫
### API
+ 利用IMGUR api做為圖片資料庫
+ 利用Wiki api實作在Line上的wiki查詢功能
### 其他
+ Config.ing儲存所需Token
+ DrinkShop.txt儲存飲料店清單
+ 藉由Pixnet之網頁查詢功能實作在LineBot上的食記與遊記查詢
+ test.py用來在功能設計初期測試是否可以正常運行
+ Selffunction.py為細節功能處理 
+ app.py負責處理接收到的資訊後丟到Selffunction.py進行處理，並輸出處理結果給Lin
