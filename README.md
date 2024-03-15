Program purpose:
testing the capabilities of conducting a sentiment analysis on a public forum such as a subreddit
to gain insight as to how positive or negative the community is on a given topic, will further extend the learnings from this excercise to make a sentiment analysis 
on more specialized areas (sentiment on specific pokemon, sentiment of each league champs subreddit, sentiment of tekken characters)

File Descriptors:

pkmnRedditSent.py - python file that creates a sentiment analysis based on comments and posts from the pokemon subreddit
the sentiment analysis was done using the textblob plugin and does a decent job of categorizing texts as either positive, negative or neutral

pokemon.csv - a csv file that contains tons of comments and posts from the pokemon subreddit, this dataset was collected from the kaggle website and has semi outdated data (hasnt been updated in a year)
however the purpose of this program is to test the capabilities of a sentiment analysis on a given subreddit and if it can be generally accurate

results:
the sentiment analysis was very posistive on the subreddit as a whole, however data is pretty outdated so more recenet posts/comments on the subreddit may yield a more negative response from the program
the textblob plugin did have issues with some comments being viewed as negative or positive, for example if a post was talking about an "evil team" such as team rocket from the pokemon games, it would categorize it
as a very negative post, even though it's very much a neutral post just talking about team rocket

for further use of the concepts learned in this excercise, I will need to find a way to improve the quality of the sentiment analysis and also when it comes to the dataset I will need to find a way to get more up to
date data, potentially through a scrapper, api, pushshift, or a more regularly updated dataset from a public source

