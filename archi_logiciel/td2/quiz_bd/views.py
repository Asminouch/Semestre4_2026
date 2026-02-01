from flask import jsonify , abort , make_response , request , url_for
from.app import app
from.models import *

@app.route('/quiz/api/v1.0/questionaires', methods = ['GET'])
def get_questionnaires() :
    public_questionaires = []
    questionnaires = get_all_questionnaires()
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
@app.route('/quiz/api/v1.0/questionaires/<int:quest_id>/questions', methods = ['GET'])
def get_questions(quest_id):
    
    q= get_questionnaire_id(quest_id)
    if q is None:
        abort(400)
    res=[]
    for question in q.get_liste():
        res.append(question.to_json())
    return jsonify ({'questions':res})


@app.route('/quiz/api/v1.0/questionaires/<int:quest_id>/questions', methods = ['POST'])
def ajout_question(quest_id):
    q= get_questionnaire_id(quest_id)
    if q is None:
        abort(400)
    if not request.json or not 'enonce' in request.json :
        abort(400)
    quest = q.add_question(request.json['enonce'])
    return jsonify ({'question ajoutée':quest.to_json()})

@app.route('/quiz/api/v1.0/questionaires/<int:quest_id>/questions/<int:question_num>', methods = ['DELETE'])
def supprimer_question(quest_id, question_num):
    q= get_questionnaire_id(quest_id)
    if q is None:
        abort(400)
    q.supp_question(question_num)
    return jsonify ({'questionnaire':q.to_json()})