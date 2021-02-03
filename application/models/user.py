import uuid
from settings import db, ma
from application.models.base_model import BaseModel
from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class User(db.Model, BaseModel):
    __tablename__ = 'users'

    def __init__(self, email, password, name, lastname, roles=None):
        self.email = email
        self.set_password(password)
        self.name = name
        self.lastname = lastname
        self.roles = roles

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    email = db.Column(db.String(255), index=True, unique=True, nullable=False)
    password = db.Column(db.String(255), index=True, unique=True, nullable=False)
    name = db.Column(db.String(120), index=True, nullable=False)
    lastname = db.Column(db.String(120), index=True, nullable=False)
    roles = db.Column(db.JSON, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, default=None, nullable=True, onupdate=datetime.now)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'name', 'lastname', 'roles', 'created_at', 'updated_at')
        ordered = True
