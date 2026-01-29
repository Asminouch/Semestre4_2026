from flask import jsonify , abort , make_response , request , url_for
from.app import app
from.models import *

@app.route('/quiz/api/v1.0/questionaires', methods = ['GET'])
def get_questionnaires() :
    public_questionaires = []
    for q in questionnaires :
        public_questionaires.append(q.to_json())
    return jsonify ({'questionnaires':public_questionaires})


@app.route('/quiz/api/v1.0/questionaires/<int:quest_id>', methods = ['GET'])
def get_questionnaire(quest_id):
    quest= get_questionnaire_id(quest_id)
    if  quest !=  None:

        return jsonify ({'questionnaire':quest.to_json()})
    abort(404)

@app.route('/quiz/api/v1.0/questionaires', methods = ['POST'])
def create_question(): 
    if not request.json or not 'nom' in request.json :  #Nom = ce qu'il y a dans le curl
        abort(400)

    new= create_quest(request.json['nom'])
    return jsonify ({'questionnaire crée ':new.to_json()})


@app.route('/quiz/api/v1.0/questionaires/<int:quest_id>', methods = ['DELETE'])
def delete_question (quest_id) :
    
    delete_quest(quest_id)
    return jsonify ({'questionnaire':"delete"})



##### Route avec Question ######



