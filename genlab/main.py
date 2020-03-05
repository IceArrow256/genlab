import sys

import PyQt5.QtWidgets as W
import ia256utilities.filesystem as FS
import appdirs

import genlab.mainwindow as MW
import genlab.gendoc as GD


class mywindow(W.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = MW.Ui_MainWindow()
        self.ui.setupUi(self)
        self.data_dir = appdirs.user_data_dir("GenLab", "IceArrow256")
        self.load_settings()
        self.save_settings()

    def __del__(self):
        self.save_settings()

    def load_settings(self):
        self.settings = FS.load_json(self.data_dir + "/settings.json")
        if not self.settings:
            self.settings["name"] = "Призвище І.Б."
            self.settings["subjects"] = ["Організації баз даних і знань",
                                         "Теорія прийняття рішень",
                                         "Розподілені інформаційно-аналітичні системи",
                                         "Моделювання та аналіз динамічних процесів",
                                         "Теорія програмування",
                                         "Програмування і підтримка веб застосувань",
                                         "Технології розподільних систем та паралельних обчислень"]
            self.settings["teacher_name"] = {"Організації баз даних і знань": "Пахальчук Є.В.",
                                             "Теорія прийняття рішень": "Проніна О.І.",
                                             "Розподілені інформаційно-аналітичні системи": "Пахальчук Є.В.",
                                             "Моделювання та аналіз динамічних процесів": "Тузенко О. О.",
                                             "Теорія програмування": "Молчанова В.С.",
                                             "Програмування і підтримка веб застосувань": "Сергієнко А.В.",
                                             "Технології розподільних систем та паралельних обчислень": "Сергієнко А.В."}
            self.settings["department_name"] = {"Пахальчук Є.В.": "Комп’ютерних Наук",
                                                "Проніна О.І.": "Комп’ютерних Наук",
                                                "Тузенко О.О.": "Кафедра Інформатики",
                                                "Молчанова В.С.": "Кафедра Інформатики",
                                                "Сергієнко А.В.": "Кафедра Інформатики"}
        self.ui.line_edit_name.setText(self.settings["name"])

    def save_settings(self):
        self.settings["name"] = self.ui.line_edit_name.text()
        FS.save_json(self.settings, self.data_dir + "/settings.json")


def main():
    app = W.QApplication([])
    application = mywindow()
    application.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
