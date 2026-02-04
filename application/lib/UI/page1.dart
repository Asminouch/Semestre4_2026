import 'package:flutter/material.dart';
import 'mytheme.dart';

class Page1 extends StatelessWidget {
  const Page1();

  @override
  Widget build(BuildContext context) {
    return Material(
        color: Color.fromRGBO(50, 0, 50, 1.0),
        shape:
        RoundedRectangleBorder(borderRadius: BorderRadius.circular(200)),
            child: Center(
              child: Text(
                'index1: api',
              )));
  }
}
