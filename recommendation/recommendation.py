# A dictionary of movie critics and their ratings of a small
# set of movies
critics = {'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
                         'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
                         'The Night Listener': 3.0},
           'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
                            'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
                            'You, Me and Dupree': 3.5},
           'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
                                'Superman Returns': 3.5, 'The Night Listener': 4.0},
           'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
                            'The Night Listener': 4.5, 'Superman Returns': 4.0,
                            'You, Me and Dupree': 2.5},
           'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                            'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
                            'You, Me and Dupree': 2.0},
           'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                             'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
           'Toby': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0, 'Superman Returns': 4.0}}


print("calculating similartity through distance")
from euclicdis import sim_distance as sd
print(sd(critics,"Toby","Gene Seymour"))
print("\n")

print("calculating similartity through Pearson Corrleation")
from Pcorel import sim_pearson as sp
print(sp(critics,"Toby","Gene Seymour"))
print('\n')

print('recommending critics to a person')
from rev_rank import topMatches as TM
print("Top 5 critics match according to Pearson correlation are:")
print(TM(critics,"Toby",n=5,similarity=sp))
print('\n')
print("Top 5 critics match according to Euclidean distance are:")
print(TM(critics,"Toby",n=5,similarity=sd))
print('\n')


print('Gets recommendations for a person by using a weighted average of every other user rankings')
from getrec import getRecommendations
print('recommended products uding PC')
print(getRecommendations(critics,"Toby",similarity=sp))
print('\n')
print('recommended products uding ED')
print(getRecommendations(critics,"Toby",similarity=sd))
print('\n')

print("for matching the products.we will match movies based on who likes them and how much they have rated it.")
from transformpref import transformPrefs
movies=transformPrefs(critics)
print("\n")
print(TM(movies,"Snakes on a Plane",n=5,similarity=sp))
print("\n")
print(TM(movies,"Snakes on a Plane",n=5,similarity=sd))