'''
Created on Jul 31, 2014

@author: rodrigo.abreu
'''
from sandman import app, db
from sandman.model import register, Model
from sandman.model import activate


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/rodrigoabreu/Documents/Sakila.sqlite3'
#sqlite:////Users/rodrigo.abreu/Documents/Sakila.sqlite3'

# class Artist(Model):
#     __tablename__ = 'Artist'
#
# class Album(Model):
#     __tablename__ = 'Album'
#
# class Playlist(Model):
#     __tablename__ = 'Playlist'

# class Actor(Model):
#     __tablename__ = 'actor'
#
# class Customer(Model):
#     __tablename__ = 'customer'

# class Staff(Model):
#     __tablename__ = 'Staff'

# class Store(Model):
#     __tablename__ = 'Store'

#register((Actor, Customer))
activate(browser=True)
app.run(debug=True)



# class Api():
#     def __init__(self):
#         app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chinook'
#         register((Artist, Album, Playlist))
#         app.run()
