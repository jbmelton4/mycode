#!/usr/bin/env python3

classinfo = {
    "all": [
        {
            "name": "Travis",
            "skill level": "wondrous",
            "spirit animal": "Alpaca",
            "super power": "Structure Weakening",
        },
        {
            "name": "Aaron",
            "skill level": "admirable",
            "spirit animal": "Donkey",
            "super power": "Helicopter Propulsion",
        },
        {
            "name": "Casey",
            "skill level": "amazing",
            "spirit animal": "Goat",
            "super power": "Invisibility",
        },
        {
            "name": "Donny",
            "skill level": "astonishing",
            "spirit animal": "Guinea pig",
            "super power": "Immobility",
        },
        {
            "name": "Emmanuel",
            "skill level": "awesome",
            "spirit animal": "Horse",
            "super power": "Immutability",
        },
        {
            "name": "Eric",
            "skill level": "brilliant",
            "spirit animal": "Pig",
            "super power": "Invulnerability",
        },
        {
            "name": "Jaelen",
            "skill level": "cool",
            "spirit animal": "Rabbit",
            "super power": "Jet Propulsion",
        },
        {
            "name": "James",
            "skill level": "enjoyable",
            "spirit animal": "Water buffalo",
            "super power": "Matter Ingestion",
        },
        {
            "name": "Jay",
            "skill level": "excellent",
            "spirit animal": "Chicken",
            "super power": "Mobile Invulnerability",
        },
        {
            "name": "John",
            "skill level": "fabulous",
            "spirit animal": "Duck",
            "super power": "Muscle Manipulation",
        },
        {
            "name": "Ken",
            "skill level": "fantastic",
            "spirit animal": "Goose",
            "super power": "Nail Manipulation",
        },
        {
            "name": "Maurice",
            "skill level": "fine",
            "spirit animal": "Pigeon",
            "super power": "Needle Projection",
        },
        {
            "name": "Mike",
            "skill level": "incredible",
            "spirit animal": "Turkey",
            "super power": "Organic Constructs",
        },
        {
            "name": "Ryan",
            "skill level": "magnificent",
            "spirit animal": "Aardvark",
            "super power": "Prehensile Hair",
        },
        {
            "name": "Shamain",
            "skill level": "marvelous",
            "spirit animal": "Aardwolf",
            "super power": "Prehensile Tail",
        },
        {
            "name": "Tuang",
            "skill level": "outstanding",
            "spirit animal": "Elephant",
            "super power": "Prehensile Tongue",
        },
        {
            "name": "Tyler",
            "skill level": "phenomenal",
            "spirit animal": "Leopard",
            "super power": "Regenerative Healing Factor",
        },
        {
            "name": "Zhenqian",
            "skill level": "pleasant",
            "spirit animal": "Albatross",
            "super power": "Super Strength",
        },
    ]
}

print(f"My name is {classinfo['all'][7]['name']} and my spirit animal is {classinfo['all'][7]['spirit animal']}.")

for x in classinfo["all"]:
    print(f"{x['name']} an {x['skill level']} {x['spirit animal']} of a programmer, possesses a {x['super power']} factor for moonlighting as a superhero!\n")