import re
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

def preprocess_text(text, keep_numbers=False):
    # Convert to lower case
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove numbers if keep_numbers is False
    if not keep_numbers:
        text = re.sub(r'\d+', '', text)
    
    # Tokenize the text
    words = text.split()
    
    # Remove stop words
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words]
    
    # Stemming or Lemmatization (using Porter Stemmer)
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]
    
    # Join the words back into a string
    text = ' '.join(words)
    
    return text

def vectorize_text(data, method='count'):
    if method == 'count':
        vectorizer = CountVectorizer()
    elif method == 'tfidf':
        vectorizer = TfidfVectorizer()
    else:
        raise ValueError("Unsupported vectorization method. Choose 'count' or 'tfidf'.")
    
    X = vectorizer.fit_transform(data)
    return X, vectorizer

def get_vectorized(abstracts: list[list[str]], keep_nums: bool = False, method: str='count') -> list[list[float]]:
    ans: list[list[float]] = []

    for title, abstract in abstracts:
        ans.append(preprocess_text(abstract, keep_numbers=keep_nums))

    return vectorize_text(ans, method=method)[0], ans
