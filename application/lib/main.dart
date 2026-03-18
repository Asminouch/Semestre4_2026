import 'package:flutter/material.dart';
import 'UI/mytheme.dart';
import 'UI/home.dart';
import 'UI/task_view_model.dart';
import 'UI/viewmodel.dart';
import 'package:provider/provider.dart';

void main() {
  runApp(MyTD2());
}

/*class MyApp extends StatelessWidget {
  //const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'TD2',
      theme: MyTheme.dark(),
      home: const MyHomePage(title: "Home page"),
    );
  }
}*/

class MyTD2 extends StatelessWidget{
  @override
  Widget build(BuildContext context){
    return MultiProvider(
      providers: [
        ChangeNotifierProvider(
            create: (_){
              SettingViewModel settingViewModel = SettingViewModel();
//getSettings est deja appelee dans le constructeur
              return settingViewModel;
            }),
        ChangeNotifierProvider(
            create:(_){
              TaskViewModel taskViewModel = TaskViewModel();
              taskViewModel.generateTasks();
              return taskViewModel;
            } )
      ],
      child: Consumer<SettingViewModel>(
        builder: (context,SettingViewModel notifier,child){
          return MaterialApp(
              theme: notifier.isDark ? MyTheme.dark():MyTheme.light(),
              title: 'TD2',
              home: MyHomePage(title: "td2")
          );
        },
      ),
    );
  }
}

