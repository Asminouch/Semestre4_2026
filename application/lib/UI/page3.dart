import 'package:flutter/material.dart';
import 'mytheme.dart';

class Page3 extends StatelessWidget {
  const Page3();

  @override
  Widget build(BuildContext context) {
    return Material(
        color: Color.fromRGBO(3, 15, 80, 1.0),
        shape:
        RoundedRectangleBorder(borderRadius: BorderRadius.circular(200)),
        child: Center(
            child: Text(
              'index3: school',
            )));
  }
}
