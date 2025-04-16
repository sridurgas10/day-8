### Task 9:
#Create a `Movie` class and override `__str__` to return formatted movie info.class Movie:
    def __init__(self,moviename,showtime):
        self.moviename=moviename
        self.showtime=showtime
    def __str__(self):
        return f"moviename:{self.moviename}, showtime:{self.showtime}"
movie=Movie("amaron","3pm")
print(movie)
str_rep=str(movie)
print(str_rep)      
