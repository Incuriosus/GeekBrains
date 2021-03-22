import json

config_dict = {}
config_dict['my_project'] = {}
config_dict['my_project']['settings'] = {}
config_dict['my_project']['settings']['__init__.py'] = {}
config_dict['my_project']['settings']['dev.py'] = {}
config_dict['my_project']['settings']['prod.py'] = {}
config_dict['my_project']['mainapp'] = {}
config_dict['my_project']['mainapp']['__init__.py'] = {}
config_dict['my_project']['mainapp']['models.py'] = {}
config_dict['my_project']['mainapp']['views.py'] = {}
config_dict['my_project']['mainapp']['templates'] = {}
config_dict['my_project']['mainapp']['templates']['mainapp'] = {}
config_dict['my_project']['mainapp']['templates']['mainapp']['base.html'] = {}
config_dict['my_project']['mainapp']['templates']['mainapp']['index.html'] = {}
config_dict['my_project']['authapp'] = {}
config_dict['my_project']['authapp']['__init__.py'] = {}
config_dict['my_project']['authapp']['models.py'] = {}
config_dict['my_project']['authapp']['views.py'] = {}
config_dict['my_project']['authapp']['templates'] = {}

with open('config.json', 'w', encoding='utf-8') as config:
    json.dump(config_dict, config)
