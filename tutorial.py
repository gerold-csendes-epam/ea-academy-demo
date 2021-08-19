import json
import praw
import time
from pprint import pprint

import boto3
import uuid

client = boto3.client('kinesis', region_name='us-east-1')
partition_key = str(uuid.uuid4())

if __name__ == "__main__":

    reddit = praw.Reddit("bot1")
    # get hot topics in wallstreetbets
    subreddit = reddit.subreddit("wallstreetbets")
    print(subreddit.display_name)

    num_posts = 100

    for i in range(num_posts):

        submission = reddit.subreddit("wallstreetbets").random()
        # submission = reddit.submission(id="p0j8bg")
        print(submission.title)
        print(submission.id)
        print(submission.url)

        # print(type(submission))
        submission.comments.replace_more(limit=50)
        # pprint(vars(submission))

        for cnt, comment in enumerate(submission.comments.list()):
            pprint(vars(comment))
            comment = vars(comment)
            comment = {key: comment[key] for key in ['body', 'score']}
            comment['permalink'] = submission.permalink
            comment['submission_id'] = submission.id

            pprint(comment)
            data = json.dumps(comment)

            # client.put_record(
            #     StreamName='wallstreetbets',
            #     Data=data,
            #     PartitionKey=partition_key)

            time.sleep(1)
            break

        break

        print(cnt)
