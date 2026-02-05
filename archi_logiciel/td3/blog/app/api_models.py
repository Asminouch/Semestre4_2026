from flask_restx import fields
from .extensions import api

article_model = api.model("Article",{
    "id": fields.Integer,  #champs qui va chercher dans classe article et recup champs id 
    "title":fields.String,
    "content":fields.String
})

comment_model = api.model("Comment",{
    "id": fields.Integer,  #champs qui va chercher dans classe article et recup champs id 
    "content":fields.String
})

article_input_model = api.model("ArticleInput",{
    "title": fields.String,
    "content":fields.String
})

comment_input_model = api.model("CommentInput",{
    "content":fields.String,
    "article_id": fields.Integer
})