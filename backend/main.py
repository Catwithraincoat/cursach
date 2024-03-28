from flask import Flask, render_template, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_bcrypt import Bcrypt
from datetime import timedelta

from db import Session
from models import Users, Character, Doctor, Enemy, Race, Message, Journey, Character_In_Journey, Time
from flask_cors import CORS, cross_origin
app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Replace with your own secret key
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=24)

jwt = JWTManager(app)
bcrypt = Bcrypt(app)
CORS(app, origins=['*'])


@app.route('/')
@jwt_required(optional=True)
def index():
    return render_template('index.html')

@app.route('/characters/<id>', methods=['GET'])
def get_character(id):
    session = Session()
    character = session.query(Character).filter_by(id=id).first()
    race = session.query(Race).filter_by(id=character.race_id).first()
    user = session.query(Users).filter_by(character_id=character.id).first()
    if character:
        res = {
            'name': character.name,
            'age': character.age,
            'state': character.state,
            'relationship': character.relationship,
            'user_id': user.id if user else None
        }
        if character.relationship == 'doctor':
            doctor = session.query(Doctor).filter_by(character_id=character.id).first()
            res['appearance'] = doctor.appearance
            res['personality'] = doctor.personality
        elif character.relationship == 'enemy':
            enemy = session.query(Enemy).filter_by(character_id=character.id).first()
            res['reason'] = enemy.reason
        res['race'] = race.name
        session.close()
        return res

@app.route('/messages/<userId>', methods=['GET'])
@jwt_required()
def get_messages(userId):
    session = Session()
    login = get_jwt_identity()
    user = session.query(Users).filter_by(login=login).first()
    user_id_to_character = {}
    character_me  = session.query(Character).filter_by(id=user.character_id).first()
    user_id_to_character[user.id] = character_me
    user_other = session.query(Users).filter_by(id=userId).first()
    character_other = session.query(Character).filter_by(id=user_other.character_id).first()
    user_id_to_character[int(userId)] = character_other

    messages_to_me = session.query(Message).filter_by(to_user_id=userId, from_user_id =user.id).all()
    messages_from_me = session.query(Message).filter_by(from_user_id=userId, to_user_id=user.id).all() if int(userId)!=user.id else []
    messages = [{"id": message.id, "from_user_id": message.from_user_id, "from_name": user_id_to_character[message.from_user_id].name, "to_user_id": message.to_user_id,"to_name": user_id_to_character[message.to_user_id].name, "message": message.message} for message in sorted(messages_to_me + messages_from_me, key=lambda x: x.id)]
    return messages

@app.route('/characters', methods=['GET'])
def get_characters():
    session = Session()
    characters = session.query(Character).all()
    res = []
    for character in characters:
        res.append({
            'id': character.id,
            'name': character.name,
            'age': character.age,
            'state': character.state,
            'relationship': character.relationship
        })
    return res

@app.route('/journeys', methods=['GET'])
@jwt_required()
def get_journeys():
    session = Session()
    login = get_jwt_identity()
    user = session.query(Users).filter_by(login=login).first()
    # character_me  = session.query(Character).filter_by(id=user.character_id).first()
    character_id = user.character_id

    journeys = session.query(Journey, Time).\
        join(Character_In_Journey, Character_In_Journey.journey_id == Journey.id).\
        join(Time, Time.id == Journey.time_id).\
        filter(Character_In_Journey.character_id == character_id).\
        all()
    
    res = []
    for journey, time in journeys:
        print(journey)
        res.append({
            'id': journey.id,
            'planet_id': journey.planet_id,
            'time': time.timerfbuinverse,
            'doctor_id': journey.doctor_id,
            'description': journey.description
        })
    return res

@app.route('/add_journey', methods=['POST'])
@jwt_required()
def add_journey():
    session = Session()
    login = get_jwt_identity()
    user = session.query(Users).filter_by(login=login).first()
    character_id = user.character_id

    
    journey_details = request.json

    new_time = Time(timerfbuinverse=journey_details['time'], timerfbplanet=journey_details['time'])
    session.add(new_time)
    session.commit()

    new_journey = Journey(
        planet_id=journey_details['planet'],
        time_id=new_time.id,
        doctor_id=journey_details['doctor'],
        description=journey_details['description']
    )

    session.add(new_journey)
    session.commit()

    new_character_in_journey = Character_In_Journey(
        character_id=character_id,
        journey_id=new_journey.id
    )

    session.add(new_character_in_journey)
    session.commit()

    return {'message': 'Journey added successfully'}, 201

@app.route('/send_message', methods=['POST'])
@jwt_required()
def send_message():
    session = Session()
    login = get_jwt_identity()
    user = session.query(Users).filter_by(login=login).first()
    to_user_id = request.json.get('to_user_id')
    message = request.json.get('message')
    message = Message(from_user_id=user.id, to_user_id=to_user_id, message=message)
    session.add(message)
    session.commit()
    session.close()
    return {'status': 'ok'}

@app.route('/login', methods=['POST'])
def login():
    session = Session()
    login = request.json.get('login')
    password = request.json.get('password')
    user = session.query(Users).filter_by(login=login).first()
    if user and bcrypt.check_password_hash(user.password_hash, password):
        access_token = create_access_token(identity=login)
        session.close()
        return {'access_token': access_token}
    else:
        session.close()
        return {'error': 'Invalid username or password'}, 401

@app.route('/me')
@jwt_required()
def me():
    login = get_jwt_identity()
    session = Session()
    user = session.query(Users).filter_by(login=login).first()
    character = session.query(Character).filter_by(id=user.character_id).first()
    race = session.query(Race).filter_by(id=character.race_id).first()
    res = {
        'login': login,
        'character': {
            'id': character.id,
            'name': character.name,
            'age': character.age,
            'state': character.state,
            'race': race.name,
        },

    }
    # Protected route that requires JWT token
    return res



@app.route('/signup', methods=['POST'])
def signup():
    # Create a new user account
    # Replace this with your own signup logic
    login = request.json.get('login')
    password = request.json.get('password')
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    name = request.json.get('name')
    race_name = request.json.get('race')
    age = request.json.get('age')
    relationship = request.json.get('relationship')
    reason = request.json.get('reason')
    appereance = request.json.get('appereance')
    personality = request.json.get('personality')
    
    session = Session()

    # Check if the username already exists in the database
    if session.query(Users).filter_by(login=login).first():
        return {'error': 'Username already exists'}, 400
    # Hash the password
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    # Create a new user object
    race = session.query(Race).filter_by(name=race_name).first()
    if not race:
        race = Race(name=race_name)
        session.add(race)
        session.commit()
    character = Character(name=name, age=age, state='alive', race_id=race.id)
    session.add(character)
    session.commit()
    if relationship == 'doctor':
        doctor = Doctor(character_id=character.id, appearance=appereance, personality=personality)
        session.add(doctor)
    elif relationship == 'enemy':
        enemy = Enemy(character_id=character.id, reason=reason)
        session.add(enemy)

    user = Users(login=login, password_hash=hashed_password, character_id=character.id)
    session.add(user)


    session.commit()
    session.close()
    return {'status': 'ok'}

@app.route('/protected')
@jwt_required()
def protected():
    # Protected route that requires JWT token
    return {'message': 'This is a protected route'}



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)