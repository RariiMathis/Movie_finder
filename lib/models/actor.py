from models.__init__ import CURSOR, CONN


class Actor:
    # all = []
    input_counter = 0

    def __init__(self, name, age, origin, oscars, id = None):
        self.name = name
        self.age = age
        self.origin = origin
        self.oscars = oscars
        self.id = id
        # Actor.all.append(self)

    @classmethod
    def all(cls):
        result = f''
        sql = 'Select * FROM actors'
        list_of_tuples = CURSOR.execute(sql).fetchall()
        actor_list = [Actor.from_db(row) for row in list_of_tuples]
        for label in actor_list:
            result +=  f'actor\'s id:{label.id}\n'
            result+= f'Name:{label.name}\n'
            result+= f'Origin:{label.origin}\n'
            result+= f'Oscars:{label.oscars}\n'
            result+= f'\n'
        return result
        
    @classmethod
    def from_db( cls, row_tuple ):
        actor_instance = Actor( row_tuple[1], row_tuple[2], row_tuple[3], row_tuple[4] )
        actor_instance.id = row_tuple[0]
        return actor_instance

    @classmethod
    def add_actor(cls, choice):
        if cls.input_counter == 0:
            cls.val1 = choice
            cls.input_counter += 1
            return 'Name was added\nWaiting for an Age'
        elif cls.input_counter == 1:
           
            cls.val2 = choice
            cls.input_counter += 1
            return 'Age was added\nWaiting for an Origin'
        elif cls.input_counter == 2:
            
            cls.val3 = choice
            cls.input_counter += 1
            return 'Origin was added\nWaiting for a Number Of Oscars'
        elif cls.input_counter == 3:
            
            cls.val4 = choice
            cls.input_counter = 0
            input_sql = f'INSERT INTO actors (name, age, origin, numberOfOscars) VALUES (?, ?, ?, ?);'
            CURSOR.execute(input_sql, (cls.val1, cls.val2, cls.val3, cls.val4))
            CONN.commit()
            return 'Actor was created\nWaiting for a Name'
    @classmethod
    def delete(cls,id):
        sql = 'DELETE FROM actors Where id = ?'
        params_tuple = (id,)
        CURSOR.execute(sql,params_tuple)
        CONN.commit()
        # id = None


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not hasattr(self, "_name"):
            if isinstance(new_name, str) and len(new_name)>1:
                self._name = new_name

                # // need return?


    def __repr__( self ):
        return f'<Actor id: {self.id} name: {self.name} Age: {self.age} Origin: {self.origin} Oscars: {self.oscars}>'