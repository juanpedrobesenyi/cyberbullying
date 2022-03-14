import numpy as np
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.preprocessing import FunctionTransformer
from sklearn.metrics import ConfusionMatrixDisplay,confusion_matrix

def clean_text(text, remove_punctuation=True, lower_text=True,
                remove_numbers=True, remove_stopwords=True, lemmatize=True):

    text = str(text)

    # remove twitter mentions @


    # keep only letters
    if remove_punctuation:
        text = re.sub(r'[^a-zA-Z]+', ' ', text)

    # lower text
    if lower_text:
        text = text.lower()

    # remove numbers
    if remove_numbers:
        text = ''.join([w for w in text if not w.isdigit()])

    # remove stopwords
    if remove_stopwords:
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(text)
        text = ' '.join([w for w in word_tokens if not w in stop_words])

    # lemmatize
    if lemmatize:
        lemmatizer = WordNetLemmatizer()
        text = ''.join([lemmatizer.lemmatize(word) for word in text]) # no entiendo por qué no va un espacio

    # remove spam
    regex = r'\b(\w+)(?:\W+\1\b)+'
    text = re.sub(regex, r'\1', text, flags=re.IGNORECASE)

    # remove empty spaces
    text = text.strip()

    return text


def clean_df(df, remove_punctuation=True, lower_text=True,
            remove_numbers=True, remove_stopwords=True, lemmatize=True):

    df = preprocess_x(df)

    df = df.copy()

    #df = df.drop_duplicates()

    df['text'] = df['text'].apply(lambda text: clean_text(text,
                                                        remove_punctuation,
                                                        lower_text,
                                                        remove_numbers,
                                                        remove_stopwords,
                                                        lemmatize))

    #df = df.drop_duplicates()

    #df = df.replace(['', ' '], np.nan)
    #df = df.dropna().reset_index(drop=True)
    df = df.replace(['', np.nan, -np.inf, np.inf], 'a')

    return df


def preprocess_x(X):
    if not isinstance(X, pd.DataFrame):
        if isinstance(X, str):
            X = [X]
        X = pd.DataFrame({'text': X})
    return X


def conf_mx_all(y_test, y_pred):

    cm = confusion_matrix(y_test, y_pred)

    TN = cm[0,0]
    TP = cm[1,1]
    FN = cm[1,0]
    FP = cm[0,1]

    recall = np.round_(TP/(TP+FN),3)
    precision = np.round_(TP/(TP+FP),3)
    accuracy = np.round_((TP+TN)/(TP+TN+FP+FN),3)
    F1= np.round((2*precision*recall)/(precision+recall), 3)

    print(f"Recall: {recall}")
    print(f"Precision: {precision}")
    print(f"Accuracy: {accuracy}")
    print(f"F1-score: {F1}")

    disp = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=[0,1])
    disp.plot()

    return recall, precision, accuracy, F1
