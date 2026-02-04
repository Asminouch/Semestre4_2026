import 'package:flutter/material.dart';
import 'mytheme.dart';

class Page2 extends StatelessWidget {
  const Page2();

  @override
  Widget build(BuildContext context) {
    return Material(
        color: Color.fromRGBO(50, 0, 0, 1.0),
        shape:
        RoundedRectangleBorder(borderRadius: BorderRadius.circular(200)),
        child: Center(
            child: Text(
              'index2: businness',
            )));
  }
}
