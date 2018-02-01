import praw #praw is used to parse through data given on Reddit
import config
import time
import os
def bot_login():
    red = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "DrDezzz's  ThicccBot comment responder v0.1")
    print("logged on!")
    return red

def bot_reply(red,replied_to_list):
    print replied_to_list
    for comments in red.subreddit('test').comments(limit=10):
        if "dog" in comments.body and comments.id not in replied_to_list:
            print("Haiy dawgy!")
            comments.reply("Haiy [Dawgy!](https://imgur.com/gallery/wKOCiRk)")
            print "Repelied to comment" + comments.id
            replied_to_list.append(comments.id)
            with open("post_replied","w") as f:
                for post_id in replied_to_list:
                    f.write(post_id + "\n")


    #Sleep for q10 seconds
    print "Sleeping for 10 seconds..."
    time.sleep(10)
def get_comment_replied():
    if not os.path.isfile("post_replied.txt"):
        replied_to_list = []
    else:
        with open("posts_replied.txt","r") as f:
            replied_to_list = f.read()
            replied_to_list = replied_to_list.split("\n")
            replied_to_list = list(filter(None, replied_to_list))
    return replied_to_list
replied_to_list = []
red = bot_login()
while True:
    bot_reply(red,replied_to_list)
