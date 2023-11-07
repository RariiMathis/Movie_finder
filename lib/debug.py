#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
import ipdb
from models.actor import Actor
from models.movie import Movie

a1 = Actor ("Keanue Reeves", 59,"Beirut,Lebanon",0,1)

ipdb.set_trace()
