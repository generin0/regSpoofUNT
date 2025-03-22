import winreg
import random

values = ['Screenmanager Stereo 3D_h1665754519',
'Screenmanager Resolution Width Default_h680557497',
'Screenmanager Resolution Height Default_h1380706816',
'Screenmanager Resolution Use Native Default_h1405981789',
'UnitySelectMonitor_h17969598',
'Screenmanager Window Position X_h4088080503',
'Screenmanager Window Position Y_h4088080502',
'Screenmanager Resolution Width_h182942802',
'Screenmanager Resolution Height_h2627697771',
'Screenmanager Fullscreen mode_h3630240806',
'unity.player_session_count_h922449978',
'unity.player_sessionid_h1351336811',
'UnityGraphicsQuality_h1669003810',
'CloudStorageHash_h1878083263']

values_delete = values

try:
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Smartly Dressed Games\Unturned", winreg.KEY_SET_VALUE) as key:
        for value in values_delete:
            try:
                winreg.DeleteValue(key, value)
                print("Значение удалено: {value}")
            except FileNotFoundError:
                print("File not found: {value}")
except FileNotFoundError:
    print("File not found.")
input()