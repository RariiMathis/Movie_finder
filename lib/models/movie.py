from models.__init__ import CURSOR, CONN

class Movie:
    # all = []
    input_counter = 0
    
    def __init__(self, title, genre, year, made, rating, id = None):
        self.title = title
        self.genre = genre
        self.made = made
        self.year = year
        self.rating = rating
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
    def search_movies(cls, title):
        result = f""
        sql = 'SELECT * FROM movie WHERE title = ?'
        list_of_tuples = CURSOR.execute(sql, (title,)).fetchall()
        movies_list = [Movie.from_db(row) for row in list_of_tuples]
        for movie_inst in movies_list:
            result += f"Title:{movie_inst.title}\n"
            result += f"Made by:{movie_inst.made}\n"
            result += f"Year:{movie_inst.year}\n"
            result += "\n"
            
        return result
        
    # @classmethod
   
            

    @classmethod
    def delete_movie(cls,id):
        sql = 'DELETE FROM movie Where id = ?'
        params_tuple = (id,)
        CURSOR.execute(sql,params_tuple)
        CONN.commit()
        # id = None


    @classmethod
    def add_movie(cls, choice):
        if cls.input_counter == 0:
            cls.val1 = choice
            cls.input_counter += 1
            return 'Title was added\nWaiting for a genre'
        elif cls.input_counter == 1:
            
            cls.val2 = choice
            cls.input_counter += 1
            return 'Genre was added\nWaitnig for a year'
        elif cls.input_counter == 2:
            
            cls.val3 = choice
            cls.input_counter += 1
            return 'Year was added\nWaiting for a made'
        elif cls.input_counter == 3:
            
            cls.val4 = choice
            cls.input_counter += 1
            return 'Made was added\nWaiting for a rating'    
        elif cls.input_counter == 4:
            
            cls.val5 = choice
            cls.input_counter = 0
            input_sql = f'INSERT INTO movie (title, genre, year, made, rating) VALUES (?, ?, ?, ?,?);'
            CURSOR.execute(input_sql, (cls.val1, cls.val2, cls.val3, cls.val4, cls.val5))
            CONN.commit()
            return 'Rating was added\nMovie Was Created\nWaiting for a new tittle'

    def __repr__(self):
        return f'<Id: {self.id} Title: {self.title} Genre: {self.genre} Year: {self.year} Made: {self.made}>'
        