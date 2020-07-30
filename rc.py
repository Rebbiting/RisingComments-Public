import praw
import time
import time
from praw.models import MoreComments

while True:
    try:
        reddit = praw.Reddit(client_id = '5Y0G8MCHSf0c4Q',
                             client_secret = 'zNBGH6xoCU7dg5mBFyA_ZCPUT9g',
                             user_agent = 'Hopefully there are no problems',
                             username = 'CommentThatGiveKarma',
                             password = 'CommentThatGiveKarma')

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
                                #cmnt = reddit.subreddit('RisingPostComments').submit('Rising comment:', 'PK: ' + str(submission.score) + ' CK: ' + str(comment.score) + ' CKPKP: {:.3f}'.format(ckpkp) + '% C: ' + str(submission.num_comments) + ' \n \nRising comment: \n \n>' + comment.body + '\n \n ^(Comment permalink: https://old.reddit.com' + comment.permalink + ')')
                                #cmnt.mod.distinguish()
                                #if submission.over_18:
                                #    cmnt.mod.nsfw()
                                #if submission.spoiler:
                                #    cmnt.mod.spoiler()
                                #cmnt.mod.flair(text=submission.subreddit.display_name)
                                #print("PENIS! " + submission.subreddit.display_name)
                                #comment.save()
                                submission.save()
                                now = time.time()
                                #print("1")
                                post_age = (now - submission.created_utc)/60
                                #print("2")
                                comment_age = (now - comment.created_utc)/60
                                #print("3")
                                post_kpm = submission.score / post_age
                                #print("4")
                                comment_kpm = comment.score / comment_age
                                #print("5")
                                #reddit.submission(id='g49xp9').reply('PK: ' + str(submission.score) + 'PA: {:.3}'.format(post_age / 60) + 'm PKPS: {:.3}'.format(post_kpm * 60) + ' CK: ' + str(comment.score) + ' CA: {:.3}'.format(comment_age / 60) + 'CKPM: {:.3}'.format(comment_kpm * 60) + ' CKPKP: {:.3f}'.format(ckpkp) + '% C: ' + str(submission.num_comments) + ' \n \nRising comment: \n \n>' + comment.body + '\n \n ^(Comment permalink: https://old.reddit.com' + comment.permalink + ')')
                                #reddit.submission(id='iOct2z').reply('PK: ' + str(submission.score) + ' CK: ' + str(comment.score) + ' CKPKP: {:.3f}'.format(ckpkp) + '% C: ' + str(submission.num_comments) + ' \n \nRising comment: \n \n>' + comment.body + '\n \n ^(Comment permalink: https://old.reddit.com' + comment.permalink + ')')
                                #reddit.live('15dw9z47l1x9p').contrib.add('PL: ' + str(submission.score) + ' CK: ' + str(comment.score) + ' CKPKP: {:.3f}'.format(ckpkp) + '% C: ' + str(submission.num_comments) + ' \n \nRising comment: \n \n>' + comment.body + '\n \n ^(Comment permalink: https://old.reddit.com' + comment.permalink + ')')
                                reddit.live('15dw9z47l1x9p').contrib.add("PK: {0} | PT: {1}m |  PKPT: {2}/m | CK: {3} | CT: {4}m | CKPT: {5}/m | CKPPK: {6:.3f}% | C: {7}\n\nRising comment:\n\n> {8:.3500}\n\n^(Comment permalink: https://old.reddit.com{9})".format(submission.score, round(post_age,2) if round(post_age) > 0.01 else "<0.01", round(post_kpm,2) if round(post_kpm,2) > 0.01 else "<0.01", comment.score, round(comment_age,2) if round(comment_age,2) > 0.01 else "<0.01", round(comment_kpm,2) if round(comment_kpm,2) > 0.01 else "<0.01", ckpkp, submission.num_comments, comment.body, comment.permalink))
                                print("PENIS 2!")
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
