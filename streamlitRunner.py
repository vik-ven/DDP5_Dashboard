import streamlit as st
# Requires BigML Python bindings
#
# Install via: pip install bigml
#
# or clone it:
#   git clone https://github.com/bigmlcom/python.git
from bigml.logistic import LogisticRegression
from bigml.api import BigML
# Downloads and generates a local version of the logistic regression,
# if it hasn't been downloaded previously.
logisticregression = LogisticRegression('logisticregression/607d83667ca0e613bd0023db',
                  api=BigML("vlv7",
                            "5bfb457d1ad360008520230eee0c229084b85f04",
                            domain="bigml.io"))
# To predict probabilities fill the desired input_data
# in next line. Numeric fields are compulsory if the model was not
# trained with missing numerics.
input_data = {
    "director": "Woody Allen",
    "writer": "Woody Allen",
    "genre": "Drama",
    "duration": 1,
    "Month": "October",
    "production_company": "pictures",
    "actors": "Samuel L. Jackson",
    "OscarWinner": "FALSE",
    "budget": 1
}
print(logisticregression.predict(input_data, full=True))
#
# input_data: dict for the input values
# (e.g. {"petal length": 1, "sepal length": 3})
# full: if set to True, the output will be a dictionary that includes the
# distribution of each class in the objective field, the predicted class and
# its probability. Please check:
# https://bigml.readthedocs.io/en/latest/#local-logistic-regression-predictions

