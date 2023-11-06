from models.__init__ import CURSOR, CONN

class Movie:
    all = []
    
    def __init__(self, title, actor, director, year id = None):
        self.title = title
        self.actor = actor
        self.director = director
        self.year = year
        self.id = id 
        Movie.all.append(self)
        
    def all_movies(self):
        return [movie for movie in Movie.all]
    
    @classmethod
    def all(cls):
        sql = 'Select * FROM movies'
        list_of_tuples = CURSOR.execite(sql).fetchall()
        return [Movie.from_db(row) for row in list_of_tuples]
        