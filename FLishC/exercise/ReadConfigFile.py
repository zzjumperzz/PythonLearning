import configparser
config = configparser.ConfigParser()
config.read('example.ini')
sections = config.sections()
for index in range(2):
    for key in config[sections[index]] :
        print(sections[index],key)

topsecret = config['DEFAULT']
print(topsecret['serveraliveinterval'])
