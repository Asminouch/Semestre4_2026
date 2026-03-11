import 'package:http/http.dart' as http;
import 'package:flutter/material.dart';
import 'mytheme.dart';
import 'dart:convert';
import '/models/MyAPI.dart';
import 'package:application/models/todo.dart';
import 'package:application/models/task.dart';

class Detail extends StatelessWidget {
  final Task task;
  Detail({super.key, required this.task});

  @override
  Widget build(BuildContext context) {
    // Use the Todo to create the UI.
    return Scaffold(
      appBar: AppBar(title: Text(task.title)),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Text(task.description),
      ),
    );
  }
}

