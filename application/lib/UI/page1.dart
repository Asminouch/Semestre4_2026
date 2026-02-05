import 'package:flutter/material.dart';
import 'mytheme.dart';
import '/models/task.dart';

List<int> colorCodes= <int>[600, 500, 100];
List<String> entries = <String>['A', 'B', 'C'];
int _selectedIndex = 0;
List<Task> task =Task.generateTask(5);

class Page1 extends StatelessWidget {
  const Page1();

  @override
  Widget build(BuildContext context) {
    return ListView.separated(
      padding: const EdgeInsets.all(8),

      itemCount: task.length,
      itemBuilder: (BuildContext context, int index) {
        return Container(
          height: 50,
          color: Colors.amber[colorCodes[index]],
          child: ListTile(
            title: Text(task[index].title),
            subtitle:Text(task[index].tags.join(" ")),
          ),
        );
      },
      separatorBuilder: (BuildContext context, int index) => const Divider(),
    );
  }
}
