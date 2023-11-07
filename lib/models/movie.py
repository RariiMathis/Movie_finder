from models.__init__ import CURSOR, CONN

class Movie:
    # all = []
    
    def __init__(self, title, genre, year, made, id = None):
        self.title = title
        self.genre = genre
        self.made = made
        self.year = year
        self.id = id 
        # Movie.all.append(self)
        
    # def all_movies(self):
    #     return [movie for movie in Movie.all]
    
    @classmethod
    def all(cls):
        result = f""
        sql = 'Select * FROM movie'
        list_of_tuples = CURSOR.execute(sql).fetchall()
        movie_list = [Movie.from_db(row) for row in list_of_tuples]
        for movie_inst in movie_list:
            result += f"Movie's id:{movie_inst.id}\n"
            result += f"Title:{movie_inst.title}\n"
            result += f"Genre:{movie_inst.genre}\n"
            result += f"Made by:{movie_inst.made}\n"
            result += f"Year:{movie_inst.year}\n"
            result+= f"\n"
            
        return result

    @classmethod
    def all_rating(cls,rating):
        result = f""
        sql = 'Select * FROM movie where rating =?'
        list_of_tuples = CURSOR.execute(sql,(rating,)).fetchall()
        movie_list = [Movie.from_db(row) for row in list_of_tuples]
        for movie_inst in movie_list:
            result += f"Movie's id:{movie_inst.id}\n"
            result += f"Title:{movie_inst.title}\n"
            result += f"Genre:{movie_inst.genre}\n"
            result += f"Made by:{movie_inst.made}\n"
            result += f"Year:{movie_inst.year}\n"
            result+= f"\n"
            
        return result

    @classmethod
    def from_db( cls, row_tuple ):
        movie_instance = Movie( row_tuple[1], row_tuple[2], row_tuple[3], row_tuple[4], row_tuple[5] )
        movie_instance.id = row_tuple[0]
        return movie_instance

    @classmethod
    def delete_movie(cls,id):
        sql = 'DELETE FROM movie Where id = ?'
        params_tuple = (id,)
        CURSOR.execute(sql,params_tuple)
        CONN.commit()
        # id = None

    def __repr__(self):
        return f'<Id: {self.id} Title: {self.title} Genre: {self.genre} Year: {self.year} Made: {self.made}>'
        