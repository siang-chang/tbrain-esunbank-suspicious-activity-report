# Record-based
基於過去 N 筆資料訓練的時間序列模型

## feature

### custinfo
- risk_rank: min-max
- total_asset: z-norm
- AGE: min-max
- occupation_code: 缺值補上 `max + 1`，one-hot

### cdtx
- date: 無額外處理
- country_is_tw: `1` if `country == 130` else `0`
- cur_type_is_tw: `1` if `cur_type == 47` else `0`
- amt: z-norm

### ccba
- lupay, cycam, usgam, clamt, csamt, inamt, cucsm, cucah: z-norm

### dp
- is_CR: `1` if `debit_credit == CR` else `0`
- tx_datetime: `tx_date + tx_time / 24`
- amt: `tx_amt * exchg_rate` 之後 z-norm，並移除 `amt` 為空的紀錄
- is_linguae: `1` if `tx_type == 1 && info_asset_code == 12` else `0`
- cross_bank, ATM: 無額外處理
- fiscTxId: 缺值補上 `max + 1`，one-hot
- tx_type, info_asset_code: one-hot

### remit
- trade_amount_usd: z-norm
- trans_no: z-norm

## training

Merge 下列特徵並各自訓練模型，ensemble 方法為取所有模型輸出機率之 **max**
- custinfo + cdtx, histNum: 135
- custinfo + ccba, histNum: 12
- custinfo + dp, histNum: 115
- custinfo + remit, histNum: 10

其中 histNum 表示每筆 alert 生成特徵時，要往回抓 `histNum` 筆紀錄。該值取自於計算每個 alert 發生時，過去出現過的紀錄**筆數的十分位距**的第 8 分位

### LSTM-baseline

Model summary
```
 Layer (type)                Output Shape     
===========================================================
 input_1 (InputLayer)        [(None, histNum, featureNum)]
                                              
 lstm (LSTM)                 (None, 64)       
                                              
 dense_1 (Dense, sigmoid)    (None, 1)        
                                              
===========================================================
```
- epochs: 1000
- batchSize: 512
- opt: adam
- loss: BinaryCrossentropy(label_smoothing=0.1)
- strategy: save **max** rap

ccba, dp, remit 訓練時忘記加入各自的 `date` 欄位時:
train RAP: 0.3284132841328413
valid RAP: 0.004707523319675704
submission RAP: 0.007017

補上 `date` 欄位後:
train RAP: 0.03759239704329462
valid RAP: 0.004884225759768451
submission RAP: 0.011049

### Dense-LSTM

Model summary
```
 Layer (type)                Output Shape                  
===========================================================
 input_1 (InputLayer)        [(None, histNum, featureNum)]
                                              
 dense (Dense)               (None, histNum, 128) 
                                              
 lstm (LSTM)                 (None, 64)       
                                              
 dense_1 (Dense, sigmoid)    (None, 1)        
                                              
===========================================================
```
- epochs: 1000
- batchSize: 512
- opt: adam
- loss: BinaryCrossentropy(label_smoothing=0.1)
- strategy: save **max** rap
- ccba, dp, remit 訓練時忘記加入各自的 `date` 欄位

ccba, dp, remit 訓練時忘記加入各自的 `date` 欄位時:
train RAP: 0.03563563563563563
valid RAP: 0.004969630038652678
submission RAP: 0.017035

補上 `date` 欄位後:
train RAP: 0.06336774652901389
valid RAP: 0.0049126637554585155
submission RAP: 0.007446