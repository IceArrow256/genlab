import sys

import PyQt5.QtWidgets as W
import ia256utilities.filesystem as FS
import appdirs
import datetime
import docxtpl
import os

import genlab.mainwindow as MW


class mywindow(W.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = MW.Ui_MainWindow()
        self.ui.setupUi(self)
        self.data_dir = appdirs.user_data_dir("GenLab", "IceArrow256")
        self.load_settings()
        self.save_settings()

        self.ui.push_button_process.clicked.connect(self.process)

    def get_gender(self, teacher_name):
        if teacher_name == "Пахальчук Є.В.":
            return "в"
        else:
            return "ла"

    def process(self):
        now = datetime.datetime.now()
        year = '{:02d}'.format(now.year)
        index = self.ui.combo_box_subjects.currentIndex()
        data = {
            "department_name": self.settings["department_name"][self.settings["teacher_name"][self.ui.combo_box_subjects.itemText(index)]],
            "number": str(self.ui.spin_box.value()),
            "subjects": self.ui.combo_box_subjects.itemText(index),
            "work_theme": self.ui.line_edit_work_theme.text().upper(),
            "name": self.ui.line_edit_name.text(),
            "teacher_name": self.settings["teacher_name"][self.ui.combo_box_subjects.itemText(index)],
            "year": str(year),
            "work_purpose": self.ui.text_edit_work_purpose.toPlainText(),
            "conclusion": self.ui.text_edit_conclusion.toPlainText(),
            "end": self.get_gender(self.settings["teacher_name"][self.ui.combo_box_subjects.itemText(index)])
        }
        doc = docxtpl.DocxTemplate(os.path.dirname(__file__) + "/lab.docx")
        doc.render(data)
        doc.save("{} - lab {}.docx".format(
            self.settings["short"][self.ui.combo_box_subjects.itemText(index)], str(self.ui.spin_box.value())))

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
                                                "Тузенко О.О.": "Інформатики",
                                                "Молчанова В.С.": "Інформатики",
                                                "Сергієнко А.В.": "Інформатики"}

            self.settings["short"] = {"Організації баз даних і знань": "DB",
                                      "Теорія прийняття рішень": "Decision theory",
                                      "Розподілені інформаційно-аналітичні системи": "Distributed computing",
                                      "Моделювання та аналіз динамічних процесів": "MADP",
                                      "Теорія програмування": "PT",
                                      "Програмування і підтримка веб застосувань": "Web",
                                      "Технології розподільних систем та паралельних обчислень": "TDSPC"}

        self.ui.line_edit_name.setText(self.settings["name"])
        self.ui.combo_box_subjects.addItems(self.settings["subjects"])

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
