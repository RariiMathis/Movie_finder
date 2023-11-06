from models.__init__ import CURSOR, CONN


class Actor:
    # all = []

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

    


    def __repr__( self ):
        return f'<Actor id: {self.id} name: {self.name} Age: {self.age} Origin: {self.origin} Oscars: {self.oscars}>'