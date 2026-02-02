import json 
from .app import db

ID =0
#questionnaires=[]

class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer)
    enonce = db.Column(db.String(200))

    questionnaire_id = db.Column(db.Integer, db.ForeignKey('questionnaires.id'))

    def __init__(self, num, enonce, questionnaire_id):
        self.num = num
        self.enonce = enonce
        self.questionnaire_id = questionnaire_id

    def to_json(self):
        x= {"num": self.num, "enonce": self.enonce }
        return x
    
    def set_num(self, num):
        self.num = num

class Questionnaire(db.Model):
    

    __tablename__ = 'questionnaires'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(200), nullable=False)

    liste_q = db.relationship('Question', backref='questionnaire', lazy=True)
    

    def __init__(self, id, nom):
        self.id = id
        self.nom = nom
        self.liste_q= []


    def get_id(self):
        return self.id


    def to_json(self):
        quest_json=[]
        for q in self.liste_q:
            quest_json.append(q.to_json())
        x= {"id": self.id,
            "nom": self.nom,
            "questions": quest_json }
        return x


    # Méthodes question 
    def get_liste(self):
        return self.liste_q

    def add_question(self, enonce):
        num = len(self.liste_q) + 1
        quest = Question(num, enonce, self.id)
        self.liste_q.append(quest)
        db.session.commit()
        return quest

    def supp_question(self, num):
        i=0
        for q in self.liste_q:
            if q.num == num:
                self.liste_q.remove(q)
                self.q.set_num()
                db.session.commit()

        

def get_all_questionnaires():
    return Questionnaire.query.all()

def get_questionnaire_id(id):
    return Questionnaire.query.get(id)
   

def create_quest(nom):
    global ID
    ID +=1
    
    quest = Questionnaire(ID, nom)
    db.session.add(quest)
    db.session.commit()
    return quest


def delete_quest(id):
    quest = get_questionnaire_id(id)
    if quest:
        db.session.delete(quest)
        db.session.commit()

class QuestionOuverte(Question):
    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer)
    enonce = db.Column(db.String(200))

    questionnaire_id = db.Column(db.Integer, db.ForeignKey('questionnaires.id'))
    pass




class QuestionChoixMultiple(Question):
    pass
