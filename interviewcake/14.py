""" write a function that takes an integer
flight_length (in minutes) and a list of 
integers movie_lengths(in minutes) and returns
a boolean indicating whether there are two numbers in 
movie_lengths whose sum equals flight_length """

# 0(n)
def find_movie(flight_length, movie_lengths):
    
    seen_movies = set()

    for first_movie_length in movie_lengths:

        matching_second_movie_length = flight_length - first_movie_length

        if matching_second_movie_length in seen_movies:
            return True

        seen_movies.add(first_movie_length)
    return False
