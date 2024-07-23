import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from rasa.nlu.components import Component
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.tokenizers import Tokenizer
from rasa.nlu.featurizers import Featurizer
from rasa.nlu.classifiers import Classifier

nltk.download('punkt')
nltk.download('wordnet')
class CustomTokenizer(Tokenizer):
    def process(self, text, context):
        tokens = word_tokenize(text)
        return
    {
            "tokens": [token for token in tokens if token.isalpha()]
    }
class CustomFeaturizer(Featurizer):
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()

    def process(self, tokens, context):
        features = []
        for token in tokens:
            lemma = self.lemmatizer.lemmatize(token)
            features.append(lemma)
        return {
            "text_features": features
        }
class CustomClassifier(Classifier):
    def __init__(self):
        self.intents = {
            'greeting': ['hello', 'hi', 'hey'],
            'goodbye': ['bye', 'goodbye', 'see you later']
        }

    def process(self, text_features, context):
        for intent, keywords in self.intents.items():
            for keyword in keywords:
                if keyword in text_features:
                    return {
                        "intent": intent
                    }
        return {
            "intent": 'unknown'
        }

nlu_config = RasaNLUModelConfig({
    'pipeline': [
        {'name': CustomTokenizer},
        {'name': CustomFeaturizer},
        {'name': CustomClassifier}
    ]
})
nlu_model = Component(nlu_config)
def process_input(user_input):
    
    output = nlu_model.process(user_input)
    intent = output.get('intent')
    if intent == 'greeting':
        response = 'Hello! How can I help you today?'
    elif intent == 'goodbye':
        response = 'Goodbye! It was nice chatting with you.'
    else:
        response = 'I didn\'t understand that. Can you please rephrase?'

    return response

# Test the chatbot
user_input = 'Hello, how are you?'
response = process_input(user_input)
print(response) 
