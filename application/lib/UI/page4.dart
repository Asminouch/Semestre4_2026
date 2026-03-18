import 'package:application/UI/viewmodel.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:settings_ui/settings_ui.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'mytheme.dart';

class EcranSettings extends StatefulWidget{
  @override
  State<EcranSettings> createState() => _EcranSettingsState();
}
class _EcranSettingsState extends State<EcranSettings> {
  @override
  Widget build(BuildContext context) {
    return Center(
        child: SettingsList(
            darkTheme: SettingsThemeData(
                settingsListBackground:
                MyTheme.dark().scaffoldBackgroundColor,
                settingsSectionBackground:
                MyTheme.dark().scaffoldBackgroundColor
            ),
            lightTheme: SettingsThemeData(
                settingsListBackground:
                MyTheme.light().scaffoldBackgroundColor,
                settingsSectionBackground:
                MyTheme.light().scaffoldBackgroundColor
            ),
            sections: [
        SettingsSection(
        title: const Text('Theme'),
        tiles: [
    SettingsTile.switchTile(
    initialValue: context.watch<SettingViewModel>
        ().isDark, //Provider.of<SettingViewModel>(context).isDark,
    onToggle: (bool value)
    {context.read<SettingViewModel>
    ().isDark=value;},//Provider.of<SettingViewModel(context,listen:false).isDark=value) },
  title: const Text('Dark mode'),
  leading: const Icon(Icons.invert_colors),)
  ])
  ],
  ),
  );
}
}
  // _onToggle(bool value) {
    //debugPrint('value $value');
    //setState(() {
      //_dark = !_dark;
    //});
  //}
//}


class SettingRepository{
  static const THEME_KEY = "darkMode";
  saveSettings(bool value) async {
    SharedPreferences sharedPreferences = await
    SharedPreferences.getInstance();
    sharedPreferences.setBool(THEME_KEY, value);
  }
  Future<bool> getSettings() async {
    SharedPreferences sharedPreferences = await
    SharedPreferences.getInstance();
    return sharedPreferences.getBool(THEME_KEY) ?? false;
  }
}
