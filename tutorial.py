import json

import praw
from pprint import pprint

reddit = praw.Reddit("bot1")

# get hot topics in wallstreetbets
subreddit = reddit.subreddit("wallstreetbets")
print(subreddit.display_name)

# submission = reddit.subreddit("wallstreetbets").random()
submission = reddit.submission(id="p0j8bg")
print(submission.title)
print(submission.id)
print(submission.url)

print(type(submission))
submission.comments.replace_more(limit=30)
# pprint(vars(submission))
# pprint(submission.selftext)
for comment in submission.comments.list():
    print(type(comment))
    # print(comment.body)
    # pprint(vars(comment))
    print(type(vars(comment)))
    comment = vars(comment)
    comment = {key: comment[key] for key in ['body', 'score']}
    print(comment)
    data = json.dumps(comment)

    break

# submission = subreddit.hot(limit=1)

# submission_id = [element.id for element in submission][0]
# print(submission_id)
# print(submission.url)
# print(submission.title)
#
# submission = reddit.submission(id=submission_id)
#
# first_comment = submission.comments[0]
# print(first_comment.body)

# submission.comments.replace_more(limit=None)
# for comment in submission.comments.list():
#     print(comment.body)

# for submission in submission:
#     print(submission.title)
#     print(submission.score)
#     print(submission.id)
#     print(submission.url)
#
#     submission_cl = reddit.submission(id=submission.id)
#     first_comment = submission_cl.comments[0]
#     print(first_comment)

