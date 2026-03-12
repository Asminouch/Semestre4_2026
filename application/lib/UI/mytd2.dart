import 'package:application/UI/page4.dart';
import 'package:flutter/material.dart';
import 'mytheme.dart';
import '/models/task.dart';
import 'detail.dart';
import 'home.dart';

class MyTD2 extends StatelessWidget{
  @override
  Widget build(BuildContext context){
//creation d'un provider
    return ChangeNotifierProvider(
        create: (_){
          SettingViewModel settingViewModel = SettingViewModel();
//getSettings est deja appelee dans le constructeur
          return settingViewModel;
        },
        child: Consumer<SettingViewModel>(
            builder: (context,SettingViewModel notifier,child){
              return MaterialApp(
                theme: notifier.isDark ? MyTheme.dark():MyTheme.light(),
                title: 'TD2',
                  home: MyHomePage()
              );
            },
        ),
    );
  }
}