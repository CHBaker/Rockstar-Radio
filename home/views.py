from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.template.response import TemplateResponse
import json


adjectives = [
    'Savage',
    'Exquisite',
    'Cackling',
    'Blood-red',
    'Raucous',
    'Trampled',
    'Yeeting',
    'Electric',
    'Die Hard',
    'Quantum',
    'Fluttering',
    'Screaming',
    'Fighting',
    'Dancing',
    'Delinquent',
    'Groovy',
    'Revolutionary',
    'Freedom-fighter',
    'Smooth',
    'Silent',
    'Wicked',
    'Heinous',
    'Bodacious',
    'Lone',
    'Coding',
    'Golden',
    'Fire-breathing',
    'Spunky',
    'Abominable',
    'Full Metal',
    'Dazzling'
];

otherAdjectives = [
    'Coldest',
    'Strongest',
    'Sleeping',
    'Punching',
    'Loudest',
    'Haunting',
    'Fallen',
    'Chosen',
    'Fighting',
    'Crushing',
    'Smoothest',
    'Swiftest',
    'Calming',
    'Damaging',
    'Lasting',
    'Amber',
    'Super',
    'Dapper',
    'Master',
    'Gossamer',
    'Alabaster',
    'Lackluster',
    'Airworthy',
    'Tributary',
    'Everlasting',
    'Rascally',
    'Shimmering',
    'Jabbing',
    'Slumbering',
    'Runaway',
    'Ghostly'
];

nouns = [
    'Soldier',
    'System',
    'Kite',
    'Mumbo-jumbo',
    'Dreamer',
    'Criminal',
    'Queen',
    'Fire',
    'Infiltration',
    'Death',
    'Developer',
    'Skull'
];

pluralNouns = [
    'Soldiers',
    'System',
    'Kites',
    'Dreamers',
    'Criminals',
    'Queens',
    'Army',
    'Skeletons',
    'Tabloids',
    'Tigers',
    'Wanderers',
    'Dancers'
];

def index(request):
    args = {
        'adjectives': json.dumps(adjectives),
        'otherAdjectives': json.dumps(otherAdjectives),
        'nouns': json.dumps(nouns),
        'pluralNouns': json.dumps(pluralNouns)
    }
    print(args)
    
    template = loader.get_template("home.html")
    return TemplateResponse(request, template, args)