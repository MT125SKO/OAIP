class SettingsManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, theme="белая", language="ru", config="config.json"):
        self.theme = theme
        self.language = language
        self.config = config

    def __str__(self):
        return f" тема={self.theme}, язык={self.language}, путь к файлам конфигурации={self.config}"


if __name__ == "__main__":
    settings_1 = SettingsManager()

    print("Настройка_1", settings_1)

    settings_1.theme = "тёмная"
    settings_1.language = "анг"

    print("Настройка_2", settings_1)
    assert settings_1.theme == "тёмная"
    assert settings_1.language == "анг"