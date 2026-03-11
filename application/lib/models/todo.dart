import 'package:flutter/material.dart';
import '/UI/mytheme.dart';
import '/UI/home.dart';


class Todo {
  int userid;
  int id;
  String title;
  bool completed;

  Todo({required this.userid, required this.id,required this.title, required this.completed});

  /*static List<Todo> generateTodo(int i){
    List<Todo> todo=[];
    for(int n=0;n<i;n++){
      todo.add(Todo(id: n, title: "title $n", tags: ['tag $n','ta${n+1}'], nbhours: n, difficuty: n, description: '$n'));
    }
    return todo;
  }*/

  static Todo fromJson(Map<String, dynamic> json){
    final tags = <String>[];
    final Color clr;

    clr = Colors.indigo;
    if(json['tags'] != null){
      json['tags'].forEach((t){
        tags.add(t);
      });
    }

    return Todo(userid: json['userId'],
      id: json['id'],
      title: json['title'],
      completed: json['completed'],
    );
  }
}