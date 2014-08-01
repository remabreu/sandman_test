'''
Created on Jul 31, 2014

@author: rodrigo.abreu
'''
from sandman import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/rodrigoabreu/Downloads/chinook'
app.config['SANDMAN_GENERATE_PKS'] = True

from sandman.model import activate

activate(browser=True)

app.run(debug=True)