import pandas as pd
import streamlit as st
from bigml.logistic import LogisticRegression
from bigml.api import BigML
from PIL import Image
import altair as alt

logisticregression = LogisticRegression('logisticregression/607e21b3f7af1513af005db6',
                  api=BigML("vlv7",
                            "5bfb457d1ad360008520230eee0c229084b85f04",
                            domain="bigml.io"))
# To make predictions fill the desired input_data in next line.
@st.cache(suppress_st_warning=True)
def setup_fxn():
    #st.header("SetupFXN Run")
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
    # setup for initial data seeding
    main_df = pd.read_csv('data/IMDB Data v3.csv')
    d_df = pd.read_csv('data/directors.csv')
    a_df = pd.read_csv('data/actors.csv')
    w_df = pd.read_csv('data/writers.csv')
    g_df = pd.read_csv('data/genre.csv')
    p_df = pd.read_csv('data/pcomp.csv')
    #initial string
    modstring = "You have not queried anything yet! Set some parameters and click the button above to interact with our model."

    # initial art
    banner = Image.open('data/movie-reel-banner.jpg')

    #max value for budget
    maxval = int(main_df["budget"].max())
    maxdur = int(main_df["duration"].max())
    return main_df, d_df, a_df, w_df, banner, g_df, maxval, maxdur, p_df, modstring

def query(genre, director, writer, actors, budget, duration, prod_comp, month_inp, oscar, metascore):
    input_data = {
        "director": ", ".join(x for x in director),
        "writer": ", ".join(x for x in writer),
        "genre": ", ".join(x for x in genre),
        "duration": duration,
        "Month": month_inp,
        "production_company": prod_comp,
        "actors": ", ".join(x for x in actors),
        "OscarWinner": "TRUE" if oscar == "Yes" else "FALSE",
        "budget": budget,
        "Metascore": metascore
    }
    log = logisticregression.predict(input_data, full=True)
    return "Your latest query to the model yielded: **" + log['prediction'] + "** with a probability of **" + str(log['probability']) + "**", log['prediction'],

main_df, d_df, a_df, w_df, banner, g_df, maxval, maxdur, p_df, modstring = setup_fxn()
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
st.image(banner)
st.title("What Makes a Successful Movie?")
st.write("Designing Data Products Team 5 is pleased to introduce an analysis on the elements that allow a film to make back its budget")
scatter = alt.Chart(main_df[['budget', 'worlwide_gross_income']][:700]).mark_circle().encode(
    x = 'budget', y = 'worlwide_gross_income', color = 'budget', tooltip=['budget', 'worlwide_gross_income']
)
st.write("As seen here, there's a **huge variability** in budget and worldwide gross, even among high-budget projects...")
st.altair_chart(scatter)
st.write("...which is why we *made a model* to help producers and companies figure out what to expect. This model predicts if a film makes back at least **1.5x** what was spent on it for a **50% profit margin**. Put some options in the sidebar to try it out!")

#sidebar entry
genre = st.sidebar.multiselect("Start with a genre, or multiple for your film!", g_df['genre'])
director = st.sidebar.multiselect("Next, who will direct it?", d_df['director'])
writer = st.sidebar.multiselect("Choose your writer(s)", w_df['writer'])
actors = st.sidebar.multiselect("Who will act in your film? You can choose any number", a_df['actor'])
budget = st.sidebar.slider("What kind of budget are you looking at?", min_value=1000, max_value=maxval, step=1000)
duration = st.sidebar.slider("How long will your movie be in minutes?", min_value=1, max_value=maxdur)
prod_comp = st.sidebar.selectbox("Which company will produce your film?", p_df['production_company'])
month_inp = st.sidebar.selectbox("What month will it release in?", month)
oscar = st.sidebar.radio("Will this film win an Oscar?", ('Yes', 'No'), index=1 )
metascore = st.sidebar.slider("What Metascore should we assign your film?", min_value=0, max_value=100, step=5)

#output stuff for everyone
st.header("Currently you have selected:")
if not genre:
    st.write("You have not chosen any genres currently, please choose one")
else:
    st.write("**" + ", ".join(x for x in genre) + "**" + " as your genre(s)")
if not director:
    st.write("You have not chosen a director currently, please choose one")
else:
    st.write("**" + ", ".join(x for x in director) + "**" + " as your director(s)")
if not writer:
    st.write("You have not chosen a writer currently, please choose one")
else:
    st.write("**" + ", ".join(x for x in writer) + "**" + " as your writer(s)")
if not actors:
    st.write("You have not chosen any actors currently, please choose at least one")
else:
    st.write("**" + ", ".join(x for x in actors) + "**" + " as your cast of actors")
st.write("Your budget is currently: " + "**$" + str(budget) + "**")
st.write("Your movie duration is currently: " + "**" + str(duration) + " minute(s)**")
if not prod_comp:
    st.write("You have not chosen any production companies, please choose one")
else:
    st.write("**" + prod_comp + "**" + " as your production company")
st.write("You have chosen to release in **" + month_inp + "**   ")
if oscar == "Yes":
    st.write("Your film will **win an Oscar!** Congrats!")
else:
    st.write("You have chosen that your film will **not win an Oscar**")
st.write("You have set that your film will recieve a Metacritic Score of **" + str(metascore) + "**")
click = st.button("Click to Query Model")
resstring = ""
predict = ""
if click:
    if not actors or not director or not genre or not writer:
        resstring = "One of actor, writer, director, or genre is not properly filled in, please do so in order to query the logistic model"
    else:
        resstring, predict = query(genre, director, writer, actors, budget, duration, prod_comp, month_inp, oscar, metascore)
st.header("Results")
if resstring:
    st.write(resstring)
    if predict == "TRUE":
        st.write("Congrats on the successful movie! Your film is predicted to make at least 1.5x its budget")
    if predict == "FALSE":
        st.write("Back to the cinematic drawing board...")
else:
    st.write(modstring)