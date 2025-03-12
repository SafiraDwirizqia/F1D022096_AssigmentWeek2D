import sys
from PyQt5.QtWidgets import *

class UserRegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Week 2 : Layout - User Registration Form")
        self.setGeometry(500, 500, 800, 950)


        # main layout
        main_layout = QVBoxLayout()

        # identitas layout
        identity_group = QGroupBox("Identitas")
        identity_layout = QVBoxLayout()
        identity_layout.addWidget(QLabel("Nama : Safira Dwirizqia"))
        identity_layout.addWidget(QLabel("Nim : F1D022096"))
        identity_layout.addWidget(QLabel("Kelas : D"))
        identity_group.setLayout(identity_layout)
        main_layout.addWidget(identity_group)

        # navigasi layout
        navigation_group = QGroupBox("Navigation")
        navigation_layout = QHBoxLayout()
        navigation_layout.addWidget(QPushButton("Home"))
        navigation_layout.addWidget(QPushButton("About"))
        navigation_layout.addWidget(QPushButton("Contact"))
        navigation_group.setLayout(navigation_layout)
        main_layout.addWidget(navigation_group)

        # registrasi layout
        registration_group = QGroupBox("User Registration")
        registration_layout = QFormLayout()

        self.full_name = QLineEdit()
        self.email = QLineEdit()
        self.phone = QLineEdit()

        self.male_radio = QRadioButton("Male")
        self.female_radio = QRadioButton("Female")
        gender_layout = QHBoxLayout()
        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)

        self.country = QComboBox()
        self.populate_countries()

        registration_layout.addRow("Full Name:", self.full_name)
        registration_layout.addRow("Email:", self.email)
        registration_layout.addRow("Phone:", self.phone)
        registration_layout.addRow("Gender:", gender_layout)
        registration_layout.addRow("Country:", self.country)

        registration_group.setLayout(registration_layout)
        main_layout.addWidget(registration_group)

        # aksi layout
        action_group = QGroupBox("Actions")
        action_layout = QHBoxLayout()
        submit_button = QPushButton("Submit")
        cancel_button = QPushButton("Cancel")
        action_layout.addWidget(submit_button)
        action_layout.addWidget(cancel_button)
        action_group.setLayout(action_layout)
        main_layout.addWidget(action_group)

        self.setLayout(main_layout)

    def populate_countries(self):
        country_list = ["Indonesia", "Malaysia", "Singapore", "Thailand", "Vietnam", "Korea Selatan", "Korea Utara", "Jepamg", "China"]
        self.country.addItem("")
        self.country.addItems(country_list)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserRegistrationForm()
    window.show()
    sys.exit(app.exec_())