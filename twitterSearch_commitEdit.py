# coding:utf-8

import tweepy
import csv
import datetime

### Twitter API KEY
Consumer_key = 
Consumer_secret = 
Access_token = 
Access_secret = 

### tweerData格納配列
tweet_data = []

### システム日付
dt_now = datetime.datetime.now()
fromDate = dt_now - datetime.timedelta(days=2)

### TwitterAPI認証用関数
def authTwitter():
  auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
  auth.set_access_token(Access_token, Access_secret)
  api = tweepy.API(auth, wait_on_rate_limit = True) # API利用制限にかかった場合、解除まで待機する
  return(api)

### Tweetの検索結果を標準出力
def printTweetBySearch(s, since, until):
  ## vars
  sinceDate = since # この日付以降のツイートを取得する
  untilDate = until # この日付以前のツイートを取得する

  print('sinceDate:',sinceDate)
  print('untilDate:',untilDate)
  api = authTwitter() # 認証

  # APIの種類と検索文字列 省略されたリンクを全て取得 省略されたツイートを全て取得 日本のツイートのみ取得
  tweets = tweepy.Cursor(api.search, q = s, \
                         include_entities = True, \
                         tweet_mode = 'extended', \
                         result_type="mixed", \
                         since = sinceDate, \
                         until = untilDate, \
                         lang = 'ja').items()

  try:
    for tweet in tweets:
      tweet_data.append([tweet.id, tweet.user.screen_name, tweet.created_at, tweet.full_text.replace('\n',''), tweet.favorite_count, tweet.retweet_count])
  except Exception as e:
    print(e)

def main():
  print('start：',dt_now)
  printTweetBySearch('python exclude:retweets', \
                   fromDate.strftime('%Y-%m-%d_00:00:00_JST'), \
                   dt_now.strftime('%Y-%m-%d_00:00:00_JST'))
  # CSV出力
  with open('searchWord_python_tweet.csv', 'w',newline='',encoding='utf-8') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(["id","user","created_at","text","fav","RT"])
    writer.writerows(tweet_data)
  pass
  print('end：',dt_now)

if __name__ == "__main__":
  main()