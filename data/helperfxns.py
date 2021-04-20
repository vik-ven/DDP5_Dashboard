#define helper functions to generate some initial data creation that we save so it's not a pain later
import pandas as pd
main_df = pd.read_csv('IMDB Data v2_stream.csv')
#generate unique actor set
def get_unique_vals():
    actorlist = []
    directorlist = []
    writerlist = []
    genrelist = []
    for index, row in main_df.iterrows():
        #actorlist.extend(row['actors'].split(", "))
        #directorlist.extend(row['director'].split(", "))
        #writerlist.extend(row['writer'].split(", "))
        genrelist.extend(row['production_company'].split(", "))
    tempset = set(actorlist)
    actors = pd.DataFrame(sorted(tempset), columns=['actor'])
    tempset = set(directorlist)
    directors= pd.DataFrame(sorted(tempset), columns=['director'])
    tempset = set(writerlist)
    writers = pd.DataFrame(sorted(tempset), columns = ['writer'])
    tempset = set(genrelist)
    genre = pd.DataFrame(sorted(tempset), columns = ['production_company'])

    #actors.to_csv('actors.csv')
    genre.to_csv('pcomp.csv')
    #directors.to_csv('directors.csv')
    #writers.to_csv('writers.csv')
get_unique_vals()