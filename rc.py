import praw
import time
import time
from praw.models import MoreComments

CLIENT_ID = "CLIENT_ID"
CLIENT_SECRET = "CLIENT_SECRET"
USER_AGENT = "Type random shit here."
USERNAME = "USERNAME"
PASSWORD = "PASSWORD"
LIVE = "LIVE"

while True:
    try:
        reddit = praw.Reddit(client_id = CLIENT_ID,
                             client_secret = CLIENT_SECRET,
                             user_agent = USER_AGENT,
                             username = USERNAME,
                             password = PASSWORD)

        def rcomment():
            for submission in reddit.subreddit('All').rising(limit=25):
                try:
                    submission.comment_sort='confidence'
                    submission.comment_limit=3
                    for comment in submission.comments:
                        #cmnt = ""
                        try:
                            if isinstance(comment,MoreComments):
                                continue
                            if not comment.distinguished and not submission.saved:
                                ckpkp = 100 * comment.score / submission.score
                                submission.save()
                                now = time.time()
                                post_age = (now - submission.created_utc)/60
                                comment_age = (now - comment.created_utc)/60
                                post_kpm = submission.score / post_age
                                comment_kpm = comment.score / comment_age
                                contrib = reddit.live(LIVE).contrib.add("PK: {0} | PT: {1}m |  PKPT: {2}/m | CK: {3} | CT: {4}m | CKPT: {5}/m | CKPPK: {6:.3f}% | C: {7}\n\nRising comment:\n\n> {8:.3500}\n\n^(Comment permalink: https://old.reddit.com{9})".format(submission.score, round(post_age,2) if round(post_age) > 0.01 else "<0.01", round(post_kpm,2) if round(post_kpm,2) > 0.01 else "<0.01", comment.score, round(comment_age,2) if round(comment_age,2) > 0.01 else "<0.01", round(comment_kpm,2) if round(comment_kpm,2) > 0.01 else "<0.01", ckpkp, submission.num_comments, comment.body, comment.permalink))
                                print(contrib)
                                time.sleep(1)
                                break
                        except Exception as e:
                            print(e)
                            time.sleep(4)
                except Exception as e:
                    print(e)
                    time.sleep(4)
        while True:
            rcomment()
    except Exception as e:
        print(e)
        time.sleep(10)
