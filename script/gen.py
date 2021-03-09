import os
import yaml

def gen():
    data = yaml.safe_load(open('data.yaml', 'r'))
    
    introduction = data['introduction']
    publications = data['publications']

    with open('template.html', 'r') as f:
        html = f.read()
        html.replace('{{introduction}}', '<br/>'.join(introduction))



