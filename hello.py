def HelloWorld():
    print("Hello World")
    return
 
def HomePlanet():
    planet = input("What is your home planet? Enter here: ").lower()
    responses = {
    "earth": "Good choice.",
    "venus": "I heard the weather is nice there.",
    "mars": "I heard they have cool machines over there.",
    "jupiter": "I heard the weather sucks there.",
    "mercury": "Do you have a good view of the sun there?",
    "saturn": "Is it true that you can surf on the rings?",
    "uranus": "Do they have Uranium there?",
    "neptune": "Is it true that it has a sub-surface ocean?"
    }
    if planet in responses:
        print(responses[planet])
    elif planet == "pluto":
        print("I don't know how to tell you this...")
    else:
        print("What? Where even is that?")
    return

HelloWorld()
HomePlanet()