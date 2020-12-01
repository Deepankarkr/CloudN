import requests
from flask import Flask, send_from_directory, jsonify, render_template, request, redirect, url_for, make_response

from flask_cors import CORS
from datetime import datetime
import json
from flask_restplus import Api, Resource,Namespace,fields
from .auth1 import auth
from .app import app
from flask_sqlalchemy import SQLAlchemy

secret_key = b'1234567890123456'

cipher = AES.new(secret_key,AES.MODE_ECB)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db= SQLAlchemy(app)




class items(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.String(500), nullable=False)
    images=db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.id


class order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(2000), nullable=False)


    def __repr__(self):
        return '<Task %r>' % self.id

class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(2000), nullable=False)
    email = db.Column(db.String(2000), nullable=False)
    address = db.Column(db.String(2000), nullable=False)


    def __repr__(self):
        return '<Task %r>' % self.id




@us_conf3.route("/getitem", methods=["GET"])
class getitem(Resource):
    @auth.login_required
    def get(self):
        #...
        return {}



@us_conf3.route("/updatecart", methods=["GET", "POST"])
class Login(Resource):
    @auth.login_required
    def get(self):
        return {}

    @auth.login_required
    def post(self):
        #...
        return x

