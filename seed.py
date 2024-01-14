from models import db, Hero, HeroPower, Power
from app import app
from faker import Faker
import random

fake = Faker()


def seed_database():

    Hero.query.delete()
    HeroPower.query.delete()
    Power.query.delete()

    heroes = []
    for _ in range(10):
        hero = Hero(
            name=fake.unique.name(),
            super_name=fake.word()
        )

        heroes.append(hero)

    db.session.add_all(heroes)

    strengths = ["Strong", "Weak", "Average"]
    heropowers = []
    for _ in range(10):
        heropower = HeroPower(
            strength=random.choice(strengths),
            hero_id=random.randint(1, 10),
            power_id=random.randint(1, 10)
        )

        heropowers.append(heropower)

    db.session.add_all(heropowers)

    powers = []
    for _ in range(10):
        power = Power(
            name=fake.unique.name(),
            description=fake.text(max_nb_chars=10)
        )

        powers.append(power)

    db.session.add_all(powers)

    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        seed_database()
