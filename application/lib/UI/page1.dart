import 'package:flutter/material.dart';
import 'mytheme.dart';
import '/models/task.dart';
import 'detail.dart';

List<int> colorCodes= <int>[600, 500, 100];
List<String> entries = <String>['A', 'B', 'C'];
int _selectedIndex = 0;


class Page1 extends StatelessWidget {
  final List<Task> myTasks =Task.generateTask(5);

  Page1({super.key});


  @override
  Widget build(BuildContext context) {
    return ListView.separated(
      padding: const EdgeInsets.all(8),

      itemCount: myTasks.length,
      itemBuilder: (BuildContext context, int index) {
        return Card(
          color: Colors.white,
          elevation: 7,
          margin: const EdgeInsets.all(10),
          child: ListTile(
            leading: CircleAvatar(backgroundColor: Colors.lightBlue, child: Text(myTasks[index].id.toString())),
            title: Text(myTasks[index].title),
            subtitle:Text(myTasks[index].tags.join(" ")),
            trailing: IconButton(
              icon: const Icon (Icons.edit),
              onPressed: (){
                Navigator.push(context, MaterialPageRoute(builder: (context) => Detail(task: myTasks[index])));

              },
          ),
          ),

        );
      },
      separatorBuilder: (BuildContext context, int index) => const Divider(),
    );
  }
}

