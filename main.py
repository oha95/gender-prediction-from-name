import random
import nltk
nltk.download('names')
from nltk import NaiveBayesClassifier
from nltk.classify import accuracy as nltk_accuracy
from nltk.corpus import names

def extract_features(word, N=2):
    last_n_letters = word[-N:]
    return {'feature': last_n_letters.lower()}

# Create training data using labeled names available in NLTK
male_list = [(name, 'male') for name in names.words('male.txt')]
female_list = [(name, 'female') for name in names.words('female.txt')]
data = (male_list + female_list)

# Seed the random number generator
random.seed(5)

# Shuffle the data
random.shuffle(data)

# Create test data
input_names = ['Alexander', 'Samantha', 'Robin', 'David']

# Define the number of samples used for train and test
num_train = int(0.8 * len(data))

# Iterate through different lengths to compare the accuracy
for i in range(1, 6):
    print('\nNumber of end letters:', i)
    features = [(extract_features(n, i), gender) for (n, gender) in data]
    train_data, test_data = features[:num_train], features[num_train:]
    classifier = NaiveBayesClassifier.train(train_data)

    # Compute the accuracy of the classifier 
    accuracy = round(100 * nltk_accuracy(classifier, test_data), 2)
    print('Accuracy = ' + str(accuracy) + '%')

    # Predict outputs for input names using the trained classifier model
    for name in input_names:
        print(name, 'is', classifier.classify(extract_features(name, i)))
        
def predict_name_gender_prefix(name, i):
    return classifier.classify(extract_features(name, i))

def a6_predict_name_gender(name: str):
    return predict_name_gender_prefix(name, len(name))
