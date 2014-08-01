'''
Created on Jul 31, 2014

@author: rodrigo.abreu
'''
import slumber

api = slumber.API("http://localhost:5000/", append_slash=False)

print api.actor.get(first_name="PENELOPE")

