import tweepy
import openai
import random

api_key = '7FjjKNPnuPAeKKX1Olf8UK6LI'
api_key_secret = 'CtinivKoWSDema1QfK7by1gbDa0tjcRnvtSw8Fa51f9UJOskew'
bearer_token = "AAAAAAAAAAAAAAAAAAAAAEd8cwEAAAAAJV89VibVexBGPSSvqkq9mU2ohIs%3DyC3TzMKNxIaM3mcuqRVamBKhzo3xvs4SKx1RPokzbV7fN6AZXc"
access_token = "1528045807454257152-g7yq7HN7twlh5DKyu6UF8Oox8GHcnX"
access_token_secret = "p8gmpYbslTQGMnErbgpezliUpIQRaiv5bHc40A2MtwP3E"
openai.api_key = "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"
USA_WOE_ID = "23424977"


client = tweepy.Client(consumer_key=api_key,
                       consumer_secret=api_key_secret,
                       access_token=access_token,
                       access_token_secret=access_token_secret,
                       bearer_token=bearer_token)


def gpt3(text):
    openai.api_key = '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'
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text,
        temperature=0.7,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0.1,
        presence_penalty=0
    )
    return response.choices[0].text

auth = tweepy.OAuth2BearerHandler(bearer_token)
api = tweepy.API(auth)

usa_trends = api.get_place_trends(USA_WOE_ID)
trends = []

for trend in usa_trends[0]["trends"]:
    trends.append(trend["name"])

trend_to_tweet = trends[random.randint(0, len(trends) - 1)]
trend_to_tweet_without_hashtag = trend_to_tweet.split("#")
print(trend_to_tweet)

#GENERATE POEM

prompt = "write a poem like Edgar Allen Poe about " + trend_to_tweet_without_hashtag[0]

poem = gpt3(prompt)

while len(poem) > 270:
   poem = gpt3(prompt)

trend_to_tweet_without_hashtag = "#" + trend_to_tweet_without_hashtag[0].replace(" ", "")

poem += "\n\n " + trend_to_tweet_without_hashtag

#tweet the poem
client.create_tweet(text=poem)