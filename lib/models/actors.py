from models.__init__ import CURSOR, CONN


class Actors:
    all = []

    def __init__(self, name, age, origin, oscars, id = None):
        self.name = name
        self.age = age
        self.origin = origin
        self.oscars = oscars
        self.id = id
        Actors.all.append(self)

    def all_actors(self):
        return [actor for actor in Actors.all]


    @classmethod
    def all(cls):
        sql = 'Select * FROM actors'
        list_of_tuples = CURSOR.execute(sql).fetchall()
        return [Actors.from_db(row) for row in list_of_tuples]

    @classmethod
    def from_db( cls, row_tuple ):
        zoo_instance = Zoo( row_tuple[1], row_tuple[2] )
        zoo_instance.id = row_tuple[0]
        return zoo_instance