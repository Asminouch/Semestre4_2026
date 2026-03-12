import 'package:application/UI/page4.dart';
import 'package:flutter/material.dart';
import 'mytheme.dart';
import '/models/task.dart';
import 'detail.dart';


class SettingViewModel extends ChangeNotifier {
  late bool _isDark;
  late SettingRepository _settingRepository;
  bool get isDark => _isDark;
  SettingViewModel() {
    _isDark = false;
    _settingRepository = SettingRepository();
    getSettings();
  }
//Switching the themes
  set isDark(bool value) {
    _isDark = value;
    _settingRepository.saveSettings(value);
    notifyListeners();
  }
  getSettings() async {
    _isDark = await _settingRepository.getSettings();
    notifyListeners();
  }
}