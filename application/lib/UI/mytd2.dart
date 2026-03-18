import 'package:application/UI/page4.dart';
import 'package:application/UI/task_view_model.dart';
import 'package:application/UI/viewmodel.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'mytheme.dart';
import '/models/task.dart';
import 'detail.dart';
import 'home.dart';

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