from flask import jsonify , abort , make_response , request , url_for
from.app import app
from.models import tasks

@app.route('/todo/api/v1.0/tasks', methods = ['GET'])
def get_tasks () :
    public_tasks = []
    for task in tasks :
        public_tasks.append(make_public_task(task))
    return jsonify ({'tasks': public_tasks })

@app.route('/todo/api/v1.0/tasks/<int:task_id>' , methods = [ 'GET' ])
def get_task(task_id) :
    for task in tasks :
        if task ['id'] == task_id :
            return jsonify ({ 'task': make_public_task(task) })
    return {'error': 'Not found'}, 404 #<=> abort(404)


def make_public_task ( task ) :
    new_task = {}
    for field in task :
        if field == 'id': #url for va retrouver l'url get_task
            new_task [ 'uri'] = url_for ( 'get_task' , task_id = task [ 'id'] ,_external = True )
        else:
            new_task [ field ] = task [ field ]
    return new_task


@app.route ('/todo/api/v1.0/tasks', methods = [ 'POST'])
def create_task () :
    # v é rification des donn é es re ç ues
    if not request.json or not 'title' in request.json :
        return{'error': 'Bad request'} ,400
    # construction de la nouvelle t â che
    if tasks == []:
        new_id = 1
    else:
        new_id = tasks [-1]['id'] + 1
    task = {
    'id': new_id ,
    'title': request . json ['title'] , #title obligatoire 
    'description': request.json.get ( 'description', " " ) ,
    'done': request.json.get ( 'done', False ),
    }
    # ajout de la nouvelle t â che aux t â ches existantes
    tasks.append ( task )
    # retour de la nouvelle t â che avec son uri 201 indique qu 'une ressource a été créé

    return jsonify ({ 'task': make_public_task ( task ) }) , 201



# erreur personnalisé
@app.errorhandler (404)
def not_found ( error ) :
    return make_response ( jsonify({'error ': 'Not found '} ) , 404)


@app.errorhandler (400)
def bad_request ( error ) :
    return make_response ( jsonify ({'error ': 'Bad request'} ) , 400)


@app.route ('/todo/api/v1.0/tasks/<int:task_id>', methods = ['PUT'])
def update_task (task_id) :
    # Recherche de la t â che à modifier avec son id
    task = None
    for taski in  tasks :
        if taski ['id'] == task_id :
            task = taski
            break
    # la t â che avec cette id n 'existe pas
    if task is None :
        abort (404)
    # la requ ê te n 'est pas au format json
    if not request.json :
        abort (400)
    # Verification des types
    if 'title'in  request.json and not isinstance( request.json ['title'] , str):
        abort (400)
    if 'description'in  request.json and not isinstance(request.json ['description'] , str ) :
        abort (400)
    if 'done'in  request.json and not isinstance(request . json ['done'] ,bool) :
        abort (400)
    # modification des champs de la t â che
    task ['title'] = request.json.get ('title', task ['title'])
    task ['description'] = request.json.get ( 'description', task ['description'])
    task ['done'] = request.json.get ('done', task ['done'])
    # retour de la t â che modifi é e
    return jsonify ({ 'task': make_public_task ( task ) })

@app.route ('/todo/api/v1.0/tasks/<int:task_id>', methods = ['DELETE'])
def delete_task (task_id) :

    task = None
    for taski in  tasks :
        if taski ['id'] == task_id :
            task = taski
            tasks.remove(task)

    if task is None :
        abort (404)

    return {"status": "deleted"}

# task: [{0}, {1},...]