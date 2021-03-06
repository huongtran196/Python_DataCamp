import pandas as pd

movies = pd.read_csv('movies.csv')
scifi_movies = pd.read_csv('scifi_movies')
action_movies = pd.read_csv('action_movies')

action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right'
                                    suffixes=('_act', '_sci'))
scifi_only = action_scifi[action_scifi['genre_act'].isnull()]
movies_scifi_only = movies.merge(scifi_only, left_on='id', right_on='movie_id')

print(movies_scifi_only.head())
print(movies_scifi_only.shape)


pop_movies = pd.read_csv('pop_movies.csv')
movies_to_genres = pd.read_csv('movies_to_genres')

genres_movies = movie_to_genres.merge(pop_movies, how='right', 
                                      left_on='movie_id', 
                                      right_on='id')
genre_count = genres_movies.groupby('genre', as_index=False).agg({'id':'count'})

genre_count.plot(kind='bar')
plt.show()