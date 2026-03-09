import 'package:application/models/task.dart';
import 'package:application/models/todo.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:http/http.dart' as http;
import '/UI/mytheme.dart';
import '/UI/home.dart';
import 'dart:convert';

class MyAPI{
  Future<List<Task>> getTasks() async{
    await Future.delayed(Duration(seconds: 1));
    final dataString = await _loadAsset('data/tasks.json');
    final Map<String,dynamic> json = jsonDecode(dataString);
    if (json['tasks']!=null){
      final tasks = <Task>[];
      json['tasks'].forEach((element){
        tasks.add(Task.fromJson(element));
      });
      return tasks;
    }else{
      return [];
    }
  }
  Future<String> _loadAsset(String path) async {
    return rootBundle.loadString(path);
  }

  //ecran 3
  Future<List<Todo>> getTodo() async{

    final response = await http.get(Uri.parse('https://jsonplaceholder.typicode.com/todos'));

    if (response.statusCode == 200){
      final List<dynamic> json = jsonDecode(response.body);

      final todos= <Todo>[];
      for (var el in json){
        todos.add(Todo.fromJson(el));
    };
      return todos;

  }else{
      return [];
    }


    }


}