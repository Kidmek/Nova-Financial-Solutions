
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, regexp_tokenize
from nltk.collocations import BigramCollocationFinder, TrigramCollocationFinder
from nltk.metrics import BigramAssocMeasures, TrigramAssocMeasures
from collections import Counter
import pandas as pd

def analyze_sentiment(original_data):
    data = original_data.copy()
    # Initialize VADER sentiment analyzer
    sid = SentimentIntensityAnalyzer()
    
    # Function to get sentiment score
    def get_sentiment_score(text):
        scores = sid.polarity_scores(text)
        return scores['compound']
    
    # Apply sentiment analysis
    data['sentiment_score'] = data['headline'].apply(get_sentiment_score)
    
    # Classify sentiment
    def classify_sentiment(score):
        if score >= 0.05:
            return 'Positive'
        elif score <= -0.05:
            return 'Negative'
        else:
            return 'Neutral'
    
    data['sentiment'] = data['sentiment_score'].apply(classify_sentiment)
    sentiment_df = pd.DataFrame({'Headline': data['headline'],'Sentiment':data['sentiment'], 'Score': data['sentiment_score']})
    
    return sentiment_df



def extract_keywords(original_data):
    data = original_data.copy()

    # Initialize stop words
    stop_words = set(stopwords.words('english'))
    
    # Tokenize and clean text
    def tokenize_and_clean(text):
        tokens = word_tokenize(text.lower())
        return [word for word in tokens if word.isalpha() and word not in stop_words]
    
    # Combine all headlines into a single list of words
    all_words = []
    for headline in data['headline']:
        all_words.extend(tokenize_and_clean(headline))
    
    # Count word frequencies
    word_freq = Counter(all_words)

    # Compute a simple score based on frequency (can be customized)
    word_scores = {word: freq for word, freq in word_freq.items()}

    return pd.DataFrame({
        'Keyword': word_scores.keys(),
        'Frequency': word_scores.values(),
        'Score': word_scores.values()  # Score is the same as Frequency here
    }).sort_values(by='Frequency', ascending=False)

def extract_keyphrases(original_data,length =2):
    data = original_data.copy()

    # Initialize stop words
    stop_words = set(stopwords.words('english'))
    
    # Tokenize and clean text
    def tokenize_and_clean(text):
        tokens = regexp_tokenize(text.lower(), pattern=r'\s|[\.,;\'\"\-!\?]', gaps=True)
        return [word for word in tokens if word.isalpha() and word not in stop_words]

    # Combine all headlines into a single list of words
    all_words = []
    for headline in data['headline']:
        all_words.extend(tokenize_and_clean(headline))
    
    # Find and count bigrams and trigrams
    if length == 2:
         # Find bigrams
        bigram_finder = BigramCollocationFinder.from_words(all_words)
        bigram_freq = bigram_finder.ngram_fd
        
        # Score bigrams
        bigram_scores = bigram_finder.score_ngrams(BigramAssocMeasures().pmi)
        
        # Create DataFrame with bigram, frequency, and score
        bigrams_df = pd.DataFrame(
            [(bigram, bigram_freq[bigram], score) for bigram, score in bigram_scores],
            columns=['Bigram', 'Frequency', 'Score']
        ).sort_values(by='Score', ascending=False)
        return bigrams_df

    else:
        trigram_finder = TrigramCollocationFinder.from_words(all_words)
        trigram_scores = trigram_finder.score_ngrams(TrigramAssocMeasures().pmi)
        trigram_freq = Counter(trigram_finder.ngram_fd)
        trigrams_df = pd.DataFrame({
            'Trigram': [f"{x[0]} {x[1]} {x[2]}" for x, _ in trigram_scores],
            'Frequency': [trigram_freq[x] for x, _ in trigram_scores],
            'Score': [score for _, score in trigram_scores]
        }).sort_values(by='Score', ascending=False)
        return trigrams_df

    
    
    

