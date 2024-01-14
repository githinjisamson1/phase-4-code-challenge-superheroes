from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db = SQLAlchemy()


class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    heropowers = db.relationship("HeroPower", backref="hero")

    serialize_rules = ("-heropowers.hero")

    def __repr__(self):
        return f'''Hero {self.name} {self.super_name}'''


class HeroPower(db.Model, SerializerMixin):
    __tablename__ = 'heropowers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)
    hero_id = db.Column(db.Integer, db.ForeignKey("heroes.id"))
    power_id = db.Column(db.Integer, db.ForeignKey("powers.id"))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    serialize_rules = ("-hero.heropowers", "-power.heropowers")

    def __repr__(self):
        return f'''HeroPower {self.strength}'''


class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    heropowers = db.relationship("HeroPower", backref="power")

    serialize_rules = ("-heropowers.power")

    def __repr__(self):
        return f'''Power {self.name} {self.description}'''


# add any models you may need.