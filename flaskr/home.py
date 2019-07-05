from flask import Flask
from flask import request
from flask import render_template
import sys
sys.path.append("..")
from flaskr import app
from flaskr.view.home import *
