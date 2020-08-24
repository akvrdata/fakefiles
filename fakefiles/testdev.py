import yaml
import os
from mimesis import Generic,Random

# config_path = os.getcwd()
# config_file = 'configs/config.yml'
# config_file_path_location = config_path + '/' + config_file

# with open(config_file_path_location) as stream:
#     data = yaml.load(stream,Loader=yaml.FullLoader)
#     print(data)
#     print(data['tables'])
fake = Generic('en')

# l = ['fake.random.schoice(seq=["d","t","c"],end=1)']
# l_str = str(l).replace("'","")
# print(eval(l_str))

print(fake.person.full_name())
print(fake.random.schoice(seq=["d", "t", "c"], end=1))
