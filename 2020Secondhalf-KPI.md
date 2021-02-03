## <u>AWSのサービスを用いたSNSマーケティングサイトの構築を目指す</u>  

雑多な情報が飛び交うSNSの中から、特定ワードを指定して  
SNS上でそのワードに対してどのような感情を抱いているのか解析を行う

---

### 使用予定技術
 - SNS側のAPI（Twitterを予定）

 - AmazonComprehend  
   自然言語解析・感情分析

 - AmazonTranscribe  
   音声認識

 - AmazonRekognitin(?)   
   画像解析

---

### ステップ（2021/02/01時点）

 - WEBマーケティングとは？  
  →　書籍を読んでレポーティング
   → 完了　

 - アウトプットイメージ及びサービス構成などの設計  
   → 作成中　

 - SNSのAPIを使用した特定ワードの情報取得  
  →　TwitterAPI申請、キーの払い出し終了  
  →　PythonのTweepyを使用して情報取得予定  

 - 取得情報に対して「自然言語解析・感情分析」を実施  
　→ Amazon Comprehend  
  　無料利用枠は、AWS の新規および既存両方を対象としており、初回の Amazon Comprehend リクエストを行った日から 12 か月間利用可能  
    50,000 単位のテキスト (500 万文字)  
   
    無料では無い場合：キーフレーズ抽出	0.0001USDくらい  
    詳しくはAWSのサイトを参照  
    　https://aws.amazon.com/jp/comprehend/pricing/  

 - 上記を操作可能なフロント部分の作成(WEBサイト？チャットボット？)  
  →　今のところWEBサイト

 - 結果のアウトプット

 - その他上記に画像解析や音声認識での検索も詰め込めるか？  
  →　音声分析

---

### スケジュール
![alt](assets/image/gantt-mermaid.png)

