from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

class IntentClassifier:
    def __init__(self):
        # Liste des mots vides français
        french_stop_words = [
            'le', 'de', 'un', 'à', 'être', 'et', 'en', 'avoir', 'que', 'pour',
            'dans', 'ce', 'il', 'une', 'sur', 'avec', 'ne', 'se', 'pas', 'tout',
            'plus', 'par', 'grand', 'ce', 'le', 'premier', 'vous', 'ou', 'son',
            'lui', 'nous', 'comme', 'mais', 'pouvoir', 'dire', 'elle', 'si',
            'leur', 'temps', 'un', 'mon', 'celui', 'ci', 'contre', 'très',
            'votre', 'faire', 'dès', 'lors', 'sans', 'sous', 'entre', 'bien',
            'encore', 'alors', 'où', 'tous', 'dont', 'aussi', 'autre', 'moins',
            'depuis', 'vers', 'jusqu', 'aux', 'mes', 'tes', 'ses', 'nos', 'vos',
            'leurs', 'du', 'des', 'au', 'je', 'tu', 'il', 'elle', 'on', 'nous',
            'vous', 'ils', 'elles', 'me', 'te', 'se', 'la', 'les', 'un', 'une',
            'des', 'ce', 'cette', 'ces', 'cet', 'mon', 'ma', 'mes', 'ton', 'ta',
            'tes', 'son', 'sa', 'ses', 'notre', 'nos', 'votre', 'vos', 'leur',
            'leurs', 'qui', 'que', 'quoi', 'dont', 'où', 'quand', 'comment',
            'pourquoi', 'est', 'a', 'ai', 'as', 'avons', 'avez', 'ont', 'suis',
            'es', 'sommes', 'êtes', 'sont', 'était', 'étais', 'étions', 'étiez',
            'étaient', 'sera', 'seras', 'serons', 'serez', 'seront', 'serait',
            'serais', 'serions', 'seriez', 'seraient', 'aura', 'auras', 'aurons',
            'aurez', 'auront', 'aurait', 'aurais', 'aurions', 'auriez', 'auraient'
        ]
        
        self.pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(
                stop_words=french_stop_words,
                ngram_range=(1, 2),
                max_features=5000
            )),
            ('classifier', SVC(
                kernel='linear',
                probability=True
            ))
        ])
    
    def train(self, texts, labels):
        self.pipeline.fit(texts, labels)
    
    def predict(self, text):
        return self.pipeline.predict([text])
    
    def predict_proba(self, text):
        return self.pipeline.predict_proba([text])