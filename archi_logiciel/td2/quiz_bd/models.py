import json 
from .app import db

ID =0
#questionnaires=[]

class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer)
    enonce = db.Column(db.String(200))

    type= db.Column(db.String(50))

    questionnaire_id = db.Column(db.Integer, db.ForeignKey('questionnaires.id'))

    def __init__(self, num, enonce, questionnaire_id):
        self.num = num
        self.enonce = enonce
        self.questionnaire_id = questionnaire_id

    def to_json(self):
        x= {"num": self.num, "enonce": self.enonce, "type": self.type }
        return x
    
    def set_num(self, num):
        self.num = num

    __mapper_args__ = {
        'polymorphic_identity': 'question',
        'polymorphic_on': type
    }


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
                #self.liste_q.remove(q)
                db.session.delete(q)
                #self.q.set_num()
                db.session.commit()      
    
class QuestionOuverte(Question):
    # Intégrer un champ réponse pour les questions ouvertes
    id = db.Column(db.Integer, db.ForeignKey('questions.id'), primary_key=True)
    rep = db.Column(db.String(200))

    __mapper_args__ = {
        'polymorphic_identity': 'question_ouverte',
    }

    def __init__(self, num, enonce, questionnaire_id, rep=""):
        super().__init__(num, enonce, questionnaire_id)
        self.rep = rep
    
    def to_json(self):
        x = super().to_json()
        x["rep"] = self.rep
        return x


class QuestionChoixMultiple(Question):
    #pour les questions fermées, deux propositions et le numéro de la bonne réponse
    id = db.Column(db.Integer, db.ForeignKey('questions.id'), primary_key=True)

    prop1= db.Column(db.String(200))
    prop2= db.Column(db.String(200))
    rep_multiple = db.Column(db.Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'question_choix_multiple',
    }

    def __init__(self, num, enonce, questionnaire_id, prop1, prop2, rep_multiple):
        super().__init__(num, enonce, questionnaire_id)
        self.prop1 = prop1
        self.prop2 = prop2
        self.rep_multiple = rep_multiple

    def to_json(self):
        x = super().to_json()
        x["prop1"] = self.prop1
        x["prop2"] = self.prop2
        x["rep_multiple"] = self.rep_multiple
        return x


def get_all_questionnaires():
    return Questionnaire.query.all()

def get_questionnaire_id(id):
    return Questionnaire.query.get(id)
   

def create_quest(nom):
    # global ID
    # ID +=1
    plus_grand_id = Questionnaire.query.order_by(Questionnaire.id.desc()).first()

    if plus_grand_id is None:
        ID = 1
    else:
        ID = plus_grand_id.id + 1


    quest = Questionnaire(ID, nom)
    db.session.add(quest)
    db.session.commit()
    return quest


def delete_quest(id):
    quest = get_questionnaire_id(id)
    if quest:
        db.session.delete(quest)
        db.session.commit()

