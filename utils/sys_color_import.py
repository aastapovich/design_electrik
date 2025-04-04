from Cocoa import NSUserDefaults

def get_mac_theme():
    # Получить стандартные настройки пользователя
    defaults = NSUserDefaults.standardUserDefaults()
    # Получить значение для определенного ключа (например, для темы)
    font_color = defaults.objectForKey_("fontColorKey") 
    
    if font_color == "Dark":
        return "white"
    else:
        return "black"
