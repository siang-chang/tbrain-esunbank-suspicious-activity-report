# Data Description

| 表格       | 欄位名稱         | 欄位說明             | 格式        | 備註                                                                       |
| :--------- | :--------------- | :------------------- | :---------- | :------------------------------------------------------------------------- |
| custinfo   | 顧客資料         |                      |             |                                                                            |
|            | cust_id          | 顧客編號             |             |                                                                            |
|            | alert_key        | alert 主鍵           |             |                                                                            |
|            | risk_rank        | 風險等級             | Categorical |                                                                            |
|            | occupation_code  | 職業                 | Categorical |                                                                            |
|            | total_asset      | 行內總資產           | Numerical   | 經過神秘轉換                                                               |
|            | AGE              | 年齡                 | Categorical |                                                                            |
| ccba       | 信用卡帳單       |                      |             | 月總結                                                                     |
|            | cust_id          | 顧客編號             |             |                                                                            |
|            | lupay            | 上月繳款總額         | Numerical   | 經過神秘轉換                                                               |
|            | byymm            | 帳務年月             | Categorical | 經過神秘轉換，數字序列有前後順序意義                                       |
|            | cycam            | 信用額度             | Numerical   | 經過神秘轉換                                                               |
|            | usgam            | 已使用額度           | Numerical   | 經過神秘轉換                                                               |
|            | clamt            | 本月分期預借現金金額 | Numerical   | 經過神秘轉換                                                               |
|            | csamt            | 本月預借現金金額     | Numerical   | 經過神秘轉換                                                               |
|            | inamt            | 本月分期消費金額     | Numerical   | 經過神秘轉換                                                               |
|            | cucsm            | 本月消費金額         | Numerical   | 經過神秘轉換                                                               |
|            | cucah            | 本月借現金額         | Numerical   | 經過神秘轉換                                                               |
| cdtx       | 信用卡交易資料   |                      |             | 僅有出項，單筆紀錄                                                         |
|            | cust_id          | 顧客編號             |             |                                                                            |
|            | date             | 消費日期             | Categorical | 經過神秘轉換，數字序列有前後順序意義                                       |
|            | country          | 消費地國別           | Categorical | 經過神秘轉換 （130 = 台灣）                                                |
|            | cur_type         | 消費地幣別           | Categorical | 經過神秘轉換 （47 = 台幣）                                                 |
|            | amt              | 交易金額（台幣）     | Numerical   | 經過神秘轉換                                                               |
| dp         | 借貸資料         |                      |             | 單筆紀錄                                                                   |
|            | cust_id          | 顧客編號             |             |                                                                            |
|            | debit_credit     | 借貸別               | Categorical |                                                                            |
|            | tx_date          | 交易日期             | Categorical | 經過神秘轉換，數字序列有前後順序意義                                       |
|            | tx_time          | 交易時間             | Categorical | 經過神秘轉換，數字序列有前後順序意義                                       |
|            | tx_type          | 交易類別             | Categorical |                                                                            |
|            | tx_amt           | 交易金額             | Numerical   | 經過神秘轉換                                                               |
|            | exchg_rate       | 匯率                 | Numerical   | tx_amt \* exchg_rate = NTD                                                 |
|            | info_asset_code  | 資訊資產代號         | Categorical | 經過神秘轉換，tx_type = 1 且 info_asset_code = 12 時，該交易為臨櫃現金交易 |
|            | fiscTxId         | 交易代碼             | Categorical | 經過神秘轉換                                                               |
|            | txbranch         | 分行代碼             | Categorical | 若為跨行交易，則僅代表交易對手銀行代碼，無分行資訊                         |
|            | cross_bank       | 是否為跨行交易       | Categorical | （0 = 非跨行；1 = 跨行）                                                   |
|            | ATM              | 是否為實體 ATM 交易  | Categorical | （0 = 非實體 ATM 交易；1 = 實體 ATM 交易）                                 |
| remit      | 外匯匯出資料     |                      |             | 僅有出項                                                                   |
|            | cust_id          | 顧客編號             |             |                                                                            |
|            | trans_date       | 外匯交易日（帳務日） | Categorical | 經過神秘轉換，數字序列有前後順序意義                                       |
|            | trans_no         | 交易編號             | Categorical | 經過神秘轉換，代表不同的匯出方式                                           |
|            | trade_amount_usd | 交易金額（美金）     | Numerical   | 經過神秘轉換                                                               |
| alert_date | 可疑活動態樣     |                      |             |                                                                            |
|            | alert_key        | alert 主鍵           |             |                                                                            |
|            | date             | 發生日期             | Categorical | 經過神秘轉換，數字序列有前後順序意義                                       |
| y          | 審查結果         |                      |             |                                                                            |
|            | alert_key        | alert 主鍵           |             |                                                                            |
|            | sar_flag         | SAR 與否             | Categorical | （0 = 未報 SAR；1 = 有報 SAR）                                             |

## public_train_x_dp_full_hashed

檔案大小超過 GitHub 限制，故拆分為 `public_train_x_dp_full_hashed_1.csv` 及 `public_train_x_dp_full_hashed_2.csv`