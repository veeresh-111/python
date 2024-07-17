import configparser

config = configparser.ConfigParser()

# Writing to a config file
config['DEFAULT'] = {'Server': 'localhost', 'Port': '8080'}
with open('config.ini', 'w') as configfile:
    config.write(configfile)

# Reading from a config file
config.read('config.ini')
print('Server:', config['DEFAULT']['Server'])
print('Port:', config['DEFAULT']['Port'])
