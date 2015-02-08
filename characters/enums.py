from django.db import models
from Enumfields import EnumField, Enum

class Skills(models.Model):
    class Mental(Enum)
Academics='Academics'
            Computer='Computer'
            Crafts='Crafts'
            Investigation='Investigation'
            Medicine='Medicine'
            Occult='Occult'
            Politics='Politics'
            Science='Science'

    class Physical(Enum):
            Athletics='Athletics'
            Brawl='Brawl'
            Drive='Drive'
            Firearms='Firearms'
            Larceny='Larceny'
            Stealth='Stealth'
            Survival='Survival'
            Weaponry='Weaponry'

    class Social(Enum):
            Animal='Animal' Ken
            Empathy='Empathy'
            Expression='Expression'
            Intimidation='Intimidation'
            Persuasion='Persuasion'
            Socialize='Socialize'
            Streetwise='Streetwise'
            Subterfuge='Subterfuge'
        

class Attributes(models.Model)
    class Mental(Enum):
            Intelligence='Intelligence'
            Wits='Wits'
            Resolve='Resolve'
    class Physical(Enum):
            Strength='Strength'
            Dexterity='Dexterity'
            Stamina='Stamina'
    class Social(Enum):
            Presence='Presence'
            Manipulation='Manipulation'
            Composure='Composure'
            