PyQt5 Modular Desktop Application
=================================

This is a modular and scalable PyQt5-based desktop application skeleton following the MVC (Model-View-Controller) architecture. It is designed to help you build maintainable and feature-rich GUI applications with a clean project structure.

* * *

🚀 Features
-----------

*   ✅ Modular MVC Architecture
*   ✅ Qt Designer support for `.ui` files
*   ✅ Resource management with `.qrc` files
*   ✅ Settings persistence with `QSettings`
*   ✅ Plug-and-play structure for models, views, and controllers
*   ✅ Ready to extend with database, threading, or APIs

* * *

📁 Project Structure
--------------------

    my_app/
    │
    ├── main.py                  # Entry point of the application
    ├── requirements.txt         # Dependencies
    ├── resources.qrc            # Qt resource file (images, icons, etc.)
    ├── resources_rc.py          # Auto-generated Python file from resources.qrc
    │
    ├── ui/                      # .ui files created with Qt Designer
    │   └── main_window.ui
    │
    ├── views/                   # GUI classes and window logic
    │   └── main_window.py
    │
    ├── controllers/             # Application logic
    │   └── main_controller.py
    │
    ├── models/                  # Data models (User, Task, etc.)
    │   └── user_model.py
    │
    ├── services/                # Helper classes like settings, DB, API
    │   └── settings_service.py
    │
    ├── utils/                   # Utility tools (e.g., logger)
    │   └── logger.py
    │
    └── assets/                  # Images, icons, fonts, etc.
        └── logo.png
    

* * *

🛠️ Installation
----------------

1.  **Clone the repository**
    
        git clone https://github.com/ernakkc/pyqt5-modular-app.git
        cd pyqt5-modular-app
    
2.  **Create virtual environment (recommended)**
    
        python -m venv venv
        source venv/bin/activate  # On Windows: venv\Scripts\activate
    
3.  **Install dependencies**
    
        pip install -r requirements.txt
    
4.  **(Optional) Convert .ui file to .py (if needed)**
    
        pyuic5 ui/main_window.ui -o views/ui_main_window.py
