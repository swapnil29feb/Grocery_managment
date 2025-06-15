from flask  import Blueprint, request, jsonify
from Grocery import db
from Grocery.models import Users, Address
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)


