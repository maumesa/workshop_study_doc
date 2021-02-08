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

### ステップ

- WEBマーケティングとは？  
  - [x] 書籍を読んでレポーティング  

- アウトプットイメージ及びサービス構成などの設計  
  - [ ] 随時実施  

- SNSのAPIを使用した特定ワードの情報取得  
  - [x] TwitterAPI申請  
  - [x] APIキーの払い出し終了  
  - [x] PythonのTweepyを使用して情報取得  

- 取得情報に対して「自然言語解析・感情分析」を実施  
  - [ ] STEP1 【対応中】S3にデータをおいて手動で分析（Comprehed)  
  - [ ] STEP2 Lambda関数からComprehend実行  
  - [ ] STEP3 （仮）Twitter検索用のWEBサイト作成  
  - [ ] STEP4 （仮）Amazon Quicksightを用いて解析結果をグラフ化  

 - その他上記に画像解析や音声認識での検索も詰め込めるか？  
  - [ ] （仮）音声分析  

---

### アウトプットイメージ及びサービス構成などの設計(随時更新)  

- 1STEP目の構成、まずは、シンプルに手動で  
![alt](assets/image/1STEP_FLOW.png)

- 2STEP目の構成、Lambda関数からComprehend実行    
![alt](assets/image/2STEP_FLOW.png)
　
---

### その他

　Amazon Comprehend  
  　無料利用枠は、AWS の新規および既存両方を対象としており、初回の Amazon Comprehend リクエストを行った日から 12 か月間利用可能  
    50,000 単位のテキスト (500 万文字)  
   
    無料では無い場合：キーフレーズ抽出	0.0001USDくらい  
    詳しくはAWSのサイトを参照  
    　https://aws.amazon.com/jp/comprehend/pricing/  

result_type で設定できる値は、三種類
"recent"： 時系列で最新のツイートを検索
"popular"： 人気のあるツイートを検索（何を基準に人気か判断しているかは不明）
"mixed"： 上記を混ぜたもの。

デフォルトだと "recent"

---

### ざっくり手順　後のメモ
 - Twtter API申請
   - 当初アドレスのサイト参考に実施  
     アドレス：https://tech-lab.sios.jp/archives/21238  
   - 理由の英訳などはGoogle翻訳を使用  
   - 申請3日後、日本語のメールで再度申請理由を求められる。   
   - 英語で返そうと考えたが、下記サイトで当初申請時から日本語でも行けると嘘か誠か記載あり  
     アドレス：https://qiita.com/newt0/items/66cb76b1c8016e9d0339
   - 試しに日本語で返信、数時間後には申請が通る  

 - Twtter API使用
   - Pythonのインストール
   - Tweepyを使用して投稿内容を取得
   - VSCodeに「Pylance」という拡張機能を追加、VSCode上でPythonの実行を可能に

 - Amazon Comprehend
   - S3に分析用のバケットを作成
   - Amazon Comprehendに分析用のjobを作成
   - Jsonがかえって来る

　 - 参考サイト；
　　https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F655635%2F57dc1c33-cab6-913c-27db-3950b4ec7fec.png?ixlib=rb-1.2.2&auto=format&gif-q=60&q=75&s=d71cb04f456d1dc752208c82b75ade00

