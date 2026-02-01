import json 

ID =0
questionnaires=[]

class Questionnaire:
    

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
        quest = Question(num, enonce)
        self.liste_q.append(quest)
        return quest

    def supp_question(self, num):
        for q in self.liste_q:
            if q.num == num:
                self.liste_q.remove(q)

def get_all_questionnaires():
    return questionnaires

def get_questionnaire_id(id):
    for i in range(len(questionnaires)):
        if questionnaires[i].get_id() == id:
            return questionnaires[i]
    return None


def create_quest(nom):
    global ID
    ID +=1
    
    quest = Questionnaire(ID, nom)
    questionnaires.append(quest)
    return quest


def delete_quest(id):
    for el in questionnaires:
        if el.get_id() == id:
            questionnaires.remove(el)


    

#get_all_questionnaires()
create_quest("plat")
create_quest("salut")
create_quest("hello")
print(get_questionnaire_id(1))



class Question():
    def __init__(self, num, enonce):
        self.num = num
        self.enonce = enonce

    def to_json(self):
        x= {"num": self.num, "enonce": self.enonce }
        return x




