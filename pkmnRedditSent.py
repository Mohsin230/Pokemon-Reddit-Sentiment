from textblob import TextBlob
from dataclasses import dataclass
import csv

@dataclass
class Mood:
    emoji: str
    sentiment: float

def get_mood(input_text: str, *, threshold: float):
    sentiment: float = TextBlob(input_text).sentiment.polarity

    friendly_threshold: float = threshold
    hostile_threshold: float = -threshold

    if sentiment >= friendly_threshold:
        return Mood('👍', sentiment)
    elif sentiment <= hostile_threshold:
        return Mood('👎', sentiment)
    else:
        return Mood('😐', sentiment)

def parse_csv(file_path):
    data = []
    with open(file_path, 'r', encoding="utf8") as file:
        csv_reader = csv.reader(file)
        # Skip header if present
        next(csv_reader, None)
        for row in csv_reader:
            data.append(row[0])  #post title data
            data.append(row[6])  #body of the post
    return data

# Example usage:
file_path = 'pokemon.csv'  # Replace 'example.csv' with your CSV file path
parsed_data = parse_csv(file_path)
totalSent = 0
lowestSent = ['',0]
highestSent = ['',0]
dataSents = []
for text in parsed_data:
    mood  = get_mood(text, threshold=0.2)
    """ commented out as its a test feature
    #find post with the lowest sentiment
    if lowestSent[0] == '':
        lowestSent[0] = text
        lowestSent[1] = mood.sentiment
    elif lowestSent[1] > mood.sentiment:
        lowestSent[0] = text
        lowestSent[1] = mood.sentiment
    
    #find post with the highest sentiment
    if highestSent[0] == '':
        highestSent[0] = text
        highestSent[1] = mood.sentiment
    elif highestSent[1] < mood.sentiment:
        highestSent[0] = text
        highestSent[1] = mood.sentiment
    """
    #print(f'{mood.emoji} ({mood.sentiment})')
    totalSent += mood.sentiment
    dataSents.append([text,mood.sentiment])

print(f'Total Sentiment of the pokemon subreddit: {totalSent}')
#test to see if function get_mood to check if sentiment is accurate
print(get_mood('i love pizza!',threshold=0.2))
print(get_mood('i hate pizza!',threshold=0.2))
print(get_mood('i love to hate eating pizza!',threshold=0.3))
#print(f'lowest sentiment post: {lowestSent}')
#print(f'highest sentiment post: {highestSent}')
dataSents.sort(key=lambda x: x[1], reverse=True)
print('-------------------------------')
print(f'5 highest sentiment posts: \n{dataSents[:5]}\n') #top n highest sentiment
print(f'5 lowest sentiment posts: \n{dataSents[-5:]}\n') #top n lowest sentiment