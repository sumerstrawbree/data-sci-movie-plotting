#Setting up the program
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

movieData = pd.read_csv('./rotten_tomatoes_movies.csv')
favMovie = "Black Panther"

print("My favorite movie is "+favMovie)


#Investigate the data
#print(movieData.head())
#print(movieData["movie_title"])

#Filter data
print("\nThe data for my favorite movie is:\n")
#Create a new variable to store your favorite movie information
favMovieBooleanList = movieData["movie_title"] == favMovie
#print(favMovieBooleanList)

favMovieData = movieData.loc[favMovieBooleanList]
print(favMovieData)

print("\n\n")

#Create a new variable to store a new data set with a certain genre
actionMovieBooleanList = movieData["genres"].str.contains("Action")

actionMovieData = movieData.loc[actionMovieBooleanList]

numOfMovies = actionMovieData.shape[0]

print("We will be comparing " + favMovie +
      " to other movies under the genre Action in the data set.\n")
print("There are " + str(numOfMovies) + " movies under the category Action.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see more information about how " + favMovie +
      " compares to other movies in this genre.\n")

#Describe data
#min
min = actionMovieData["audience_rating"].min()
print("The min audience rating of the data set is: " + str(min))
print(favMovie + " is rated " + str(79 - min) + " points higher than the lowest rated movie.")
print()

#find max
max = actionMovieData["audience_rating"].max()
print("The max audience rating of the data set is: " + str(max))
print(favMovie + " is rated " + str(max - 79) + " points lower than the highest rated movie.")
print()

#find mean
mean = actionMovieData["audience_rating"].mean()
print("The mean audience rating of the data set is: " + str(mean))
print(favMovie + " is lower than the mean movie rating.")

#find median
median = actionMovieData["audience_rating"].median()
print("The median audience rating of the data set is: " + str(median))
print(favMovie + " is higher than the median movie rating.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see data visualizations.\n")

#Create histogram
plt.hist(actionMovieData["audience_rating"], bins=20, range = (0,100))


#Adds labels and adjusts histogram
plt.grid(True)
plt.title("Audience Ratings of Action Movies Histogram")
plt.xlabel("Audience Ratings")
plt.ylabel("Number of Action Movies")

#Prints interpretation of histogram
print(
  "According to the histogram, ..."
)
print()

#Show histogram
plt.show()
input("Press enter to see the next data visualization.\n")
plt.close()

#Create scatterplot
plt.scatter(data = actionMovieData, x = "audience_rating", y = "critic_rating")

#Adds labels and adjusts scatterplot
plt.grid(True)
plt.title("Audience Rating vs Critic Rating")
plt.xlabel("Audience Rating")
plt.ylabel("Critic Rating")
plt.xlim(0, 100)
plt.ylim(0, 100)

#Prints interpretation of scatterplot
print(
  "According to the scatter plot, there are the most action movies with ratings between 60 and 65. There are about 280 action movies with those ratings."
)
print(
    "Additionally, the scatterplot shows a positive correlation. There is a pattern: as audience ratings increase, critic ratings increase. There are also some outliers: movies with high audience ratings but low critic ratings, and movies with low audience ratings but high critic ratings."
)


#Show scatterplot
plt.show()

print("\nThank you for reading through my data analysis!")
