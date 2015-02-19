# nWoD-db
Web app for creating new world of darkness characters and browsing character data (Mage spells, vampire disciplines merits, etc)


## To do
 1. ~~Model References to 'character' should be changed to use Generic Foreign Keys~~
 2. ~~Change nWoDCharacter to Characteristics, and use GFKs.~~ Done better than this....
 3. ~~Limit GFKs to playable templates~~
 3. [Implement bulk upload of spell data](https://github.com/AncientSwordRage/nWoD-db/issues/3)
 4. ~~Add serialization~~
 5. ~~Add values to serialization of Traits (Skills etc)~~
 6. Nest traits by priority *in progress*
 7. [Implement Swagger](https://github.com/AncientSwordRage/nWoD-db/issues/5)
 8. [Create serialization for spells](https://github.com/AncientSwordRage/nWoD-db/issues/7)
 9. Improve Spell model
 10. Review Character models - Should each template be a [proxy model](https://docs.djangoproject.com/en/1.7/topics/db/models/#proxy-models) and access a template via foreign key? Then specific functionality (spells, arcana etc) be accessed by @property function defs
 11. Add Angular front end
