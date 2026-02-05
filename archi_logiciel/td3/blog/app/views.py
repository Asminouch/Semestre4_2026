from flask_restx import Resource, Namespace, abort
from .models import Article, Comment, get_all_articles, get_all_comment, create_article, get_article, get_comment, create_comment
from .api_models import article_model, comment_model, article_input_model, comment_input_model
# creation du namespace, racine de tous les endpoints
#namespace, regroupé  toute les routes
ns = Namespace("api") 

@ns.route("/hello")
class Hello(Resource):
    def get(self):
        return {"hello": "restx"}
    

@ns.route("/articles")
class ArticleCollection(Resource):
    @ns.marshal_list_with(article_model)
    def get(self):
        return get_all_articles()
    
    #post
    @ns.expect(article_input_model, validate = True) #sans validate expect sers que de doc, avec validate il bloque si entree pas bonne
    @ns.marshal_with(article_model)
    def post(self):
        article = create_article(title=ns.payload["title"], content=ns.payload["content"])
        return article,201 #201= article créé
         

### COMMENT ###        
@ns.route("/comments")
class CommentCollection(Resource):
    @ns.marshal_list_with(comment_model)
    def get(self):
        return get_all_comment()
    
    #post
    @ns.expect(comment_input_model, validate = True) #sans validate expect sers que de doc, avec validate il bloque si entree pas bonne
    @ns.marshal_with(comment_model)
    def post(self):

        if get_article(ns.payload["article_id"])== None:
            abort(404)
        else:

            comment = create_comment(content=ns.payload["content"])
            return comment,201 #201= article créé
     
    

@ns.route("/articles/<int:id>")
@ns.response(404, 'Article not found')
class ArticleItem(Resource):
    @ns.marshal_with(article_model)
    def get(self,id):
        article = get_article(id)
        if article is None:
            abort(404,"Article not found")
        return article
    


@ns.route("/comments/<int:id>")
@ns.response(404, 'comments not found')
class CommentsItem(Resource):
    @ns.marshal_with(comment_model)
    def get(self,id):
        comment = get_comment(id)
        if comment is None:
            abort(404,"comments not found")
        return comment