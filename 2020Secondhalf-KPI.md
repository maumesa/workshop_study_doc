---
theme: "beige"  
transition: "default" 
title: 2020下期考課
---

#### <u>AWSのサービスを用いたSNSマーケティングサイトの構築を目指す</u>  

<span style="font-size:0.8em">
<div>雑多な情報が飛び交うSNSの中から、特定ワードを指定して</div>
<div>SNS上でそのワードに対してどのような感情を抱いているのか</div>
<div>解析を行う</div>
</span>

---

### 使用予定技術
 - SNS側のAPI（Twitterを予定）

 - AmazonComprehend  
   自然言語解析・感情分析

 - AmazonRekognitin  
   画像解析

 - AmazonTranscribe  
   音声認識

---

### ステップ

 - マーケティングとは？
 - SNSのAPIを使用した特定ワードの情報取得
 - 取得情報に対して「自然言語解析・感情分析」を実施
 - 結果のアウトプット
 - 上記を操作可能なフロント部分の作成(WEBサイト？チャットボット？)
 - その他上記に画像解析や音声認識での検索も詰め込めるか？

---

### スケジュール
```mermaid
gantt
    dateFormat YYYY-MM-DD

    section 準備期間
    SAA対策                 :a1 ,2020-09-28 ,21d
    WEBマーケティング学習    :a2 ,after a1 ,28d
    設計                    :b1 ,2020-11-02 ,28d
```

```mermaid
gantt
    dateFormat YYYY-MM-DD

    section サービス作成
    SNSとの連携              :b2 ,2020-12-01 ,28d
    自然言語解析と感情分析    :b3 ,after b2 ,28d
    フロントとアウトプット作成 :b4 ,after b3 ,28d
    音声認識と画像解析        :b5 ,after b4 ,28d

```

