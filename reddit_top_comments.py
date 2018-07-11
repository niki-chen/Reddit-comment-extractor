# This script takes the main comments for a submission and writes each to a separate line of a .csv file
# You need to specify the submission ID, the sort order, and the name of the .csv file

import praw
import csv
import pandas as pd

#create Reddit instance
reddit = praw.Reddit(client_id='y800W9SL88E1jQ', client_secret="hNluLrmJfNpq5djab4Q9JfA6l1s", user_agent='my user agent')

# get suicide prevention megathread submission as submission
submission = reddit.submission('8pks1u') #specify what submission to scrape
submission.comment_sort = 'controversial' #choose how you want to sort the comments

#create a list of top level comments as a list called toplevelcomment
from praw.models import MoreComments # MoreComments ignores 'load more comments' and 'continue this thread' links - otherwise a [AttibuteError: 'MoreComments' object has no attribute body] will be thrown
toplevelcomment = []
for top_level_comment in submission.comments:
    if isinstance(top_level_comment, MoreComments):
        continue
    toplevelcomment.append(top_level_comment.body)

#create .csv file - here specify sort method in filename 
csvfile = open("top_level_commentSortControversial.csv","w")
csvfile.close()

#turn list of top level comments into a pandas dataframe
comment_df = pd.DataFrame(toplevelcomment)
#write pandas dataframe to .csv file
comment_df.to_csv('top_level_commentSortControversial.csv', index=False, header=False)