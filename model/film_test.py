'''
Created on Jul 31, 2014

@author: rodrigo.abreu
'''
import slumber

api = slumber.API("http://localhost:5000/")

print api.Actor.first_name("PENELOPE").get()

