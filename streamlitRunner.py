import pandas as pd
import streamlit as st
from bigml.logistic import LogisticRegression
from bigml.api import BigML

# Downloads and generates a local version of the logistic regression,
# if it hasn't been downloaded previously.

logisticregression = LogisticRegression('logisticregression/607da8de7ca0e613bd002400',
                  api=BigML("vlv7",
                            "5bfb457d1ad360008520230eee0c229084b85f04",
                            domain="bigml.io"))

# To predict probabilities fill the desired input_data
# in next line. Numeric fields are compulsory if the model was not
# trained with missing numerics.
#
# input_data: dict for the input values
# (e.g. {"petal length": 1, "sepal length": 3})
# full: if set to True, the output will be a dictionary that includes the
# distribution of each class in the objective field, the predicted class and
# its probability. Please check:
# https://bigml.readthedocs.io/en/latest/#local-logistic-regression-predictions
input_data = {
    "director": "Woody Allen",
    "writer": "Woody Allen",
    "genre": 'Drama',
    "duration": 1,
    "Month": 'October',
    "production_company": 'twentieth century fox',
    "actors": 'Maggie Smith',
    "OscarWinner": 'FALSE',
    "budget": 10000
}
#setup for initial data seeding
main_df = pd.readcsv('IMDB Data v2.csv')


#print(logisticregression.predict(input_data, full=True))
st.title("Can you create a successful movie?")
st.write("Designing Data Products Team 5 brings y")

