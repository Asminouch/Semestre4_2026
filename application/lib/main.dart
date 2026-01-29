import 'package:flutter/material.dart';
import 'UI/mytheme.dart';
import 'UI/home.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'TD2',
      theme: MyTheme.dark(),
      home: const MyHomePage(title: 'Mon application !!!'),
    );
  }
}


