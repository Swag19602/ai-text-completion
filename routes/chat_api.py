from os import environ
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import Blueprint, jsonify, request
from config import db
from models.chat_logs import ChatLogs
from models.users import Users
from openai import OpenAI

api_key=environ.get('API_KEY')
event_bp = Blueprint("event_bp", __name__)
limiter = Limiter(key_func=get_remote_address) #limitter used to limit number of requests
openai = OpenAI(api_key=api_key)


@event_bp.route("/openai-completion", methods=["POST"])
@limiter.limit("10 per minute") 
def openai_completion():
    data = request.json
    prompt = data['prompt']
    user_id = data['user_id']

    # Handle missing prompt or user_id 
    if "prompt" not in data or not data["prompt"] or not user_id:
        return jsonify({"error": "data is missing"}), 400
    
    # Retrieve the user or create a new one if it doesn't exist
    user = Users.query.filter_by(user_id=user_id).first()
    if not user:
        user = Users(user_id=user_id)
        db.session.add(user)
        db.session.commit()

    # Call OpenAI API to generate completion
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Comportati come se fossi un SEO copywriter professionista."},
                {"role": "user", "content": prompt}
            ],
            temperature=0,
            max_tokens=1500,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=['\n']
        )
        completion = response.choices[0].message.content.strip()
        chat_logs = ChatLogs(user_id=user_id, prompt=prompt, completion=completion)
        db.session.add(chat_logs)
        db.session.commit()

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    chat_logs = ChatLogs.query.all()

    return jsonify({"completion": completion}), 200


@event_bp.route("/", methods=["GET"])
def welcome():
    return jsonify({"msg": "welcome to openAI text completion project"})

    