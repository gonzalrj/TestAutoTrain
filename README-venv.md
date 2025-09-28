# Venv Set-up and installation

The first step is to create your individual lightweight virtual environment. Some computers like Macs often have pre-installed Python interpreters but as a good practice you need to have your own lightweight environment that can be used by your project/s. You can also have multiple virtual environments for different purposes, that you can assign to different projects.

## A virtual environment is (amongst other things)
Used to contain a specific Python interpreter and software libraries and binaries which are needed to support a project (library or application). These are by default isolated from software in other virtual environments and Python interpreters and libraries installed in the operating system.
Contained in a directory, conventionally named .venv or venv in the project directory, or under a container directory for lots of virtual environments, such as ~/.virtualenvs.
Not checked into source control systems such as Git.
Considered as disposable – it should be simple to delete and recreate it from scratch. You don’t place any project code in the environment.
Not considered as movable or copyable – you just recreate the same environment in the target location.

### Common Terminal Commands
* MacOS
* Windows

## MacOS
### Install Python 3.12 (MacOS)
1. Check if Homebrew is already installed: brew --version
2. Install Homebrew is you don’t have it: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
3. Install pyenv with Homebrew: brew install pyenv
4. pyenv install 3.12
5. TODO WHEN PROJECT IS AVAILABLE:
Navigate to project’s root and set the local version to 3.12: 
cd your-project-directory
pyenv local 3.12
6. Verify the Python version by running python3 --version

### Create virtual environment (MacOS)
1. Move to the directory you want to create your virtual environment and run python3 -m venv py3.12-selen
2. Activate your environment by running source py3.12-selen/bin/activate to start installing project dependencies. IMPORTANT: Always activate a virtual environment before installing a dependency, otherwise the packages will be installed into your global Python environment. This is bad practice and will pollute your global namespace. It creates potential version conflicts where one project’s dependency breaks another’s.
3. Install Selenium by running pip install selenium
4. Install PyTest by running pip install pytest.
5. Repeat the same steps for 2 optional packages: pytest-base-url and pytest-html.
6. Verify all installations by running a pip list. Make sure both packages are shown from the list.

### Replace virtual environment (MacOS)
1. Deactivate the current environment: deactivate
2. Export current dependencies from the old environment: pip freeze > requirements.txt
3. Remove the old environment (optional but recommended): rm -rf py3.11-selen
4. Create a new virtual environment with Python 3.12: python3.12 -m venv py3.12-selen
5. Activate the new environment: source py3.12-selen/bin/activate
6. Upgrade pip (best practice): pip install --upgrade pip
7. Reinstall dependencies from requirements.txt: pip install -r requirements.txt
8. Verify installation: pip list

## Windows
### Install Python 3.12 and create Virtual Environment (Windows)
1. Install Python
   * Download installers from python.org. 
   * During install, make sure:
   * ✅ Install launcher for all users (recommended) is checked.
   * ❌ Add Python to PATH can be left unchecked (not needed if you use py).
2. Check available Python version
   * py -0
   * This shoul list all installed Pythons
3. Navigate to your project folder (or where you want to put your venv)
   * cd C:\Users\YourName\YourProject
4. Create a virtual environment with the version you want
   * py -3.12 -m venv [venv-name]
   * venv-name can be anything, I normally use the convention “py-3.12-selen”
5. Activate the virtual environment
   * venv-name\Scripts\activate
6. Install required project dependencies
   * pip install selenium requests pytest lxml cssselect
7. Deactivate when done
   * deactivate

## Replace virtual environment
1. Deactivate current environment: deactivate
2. Export current dependencies from old venv:
   * pip freeze > requirements.txt
3. Remove the old environment (PowerShell)
   * Remove-Item -Recurse -Force .\py3.11-selen 
4. Create a new venv with Python 3.12: py -3.12 -m venv py3.12-selen 
5. Activate the new environment: .\py3.12-selen\Scripts\Activate.ps1 
6. Upgrade pip: pip install --upgrade pip
7. Reinstall dependencies from requirements.txt:
   * pip install -r requirements.txt
8. Verify everything is installed: pip list

## Cloning repository to local machine
1. Get the GitHub repo URL.
2. Via Terminal, navigate to the folder you want to save a copy of your project locally.
3. Clone the repo by running git clone https://github.com/yourusername/your-repo-name.git (your GitHub repo URL).
4. Via Terminal, activate your venv by running source venv-path-name/bin/activate
5. Verify that your desired dependencies are captured by running pip list
6. Once confirmed, create a requirements.txt file from it by executing pip freeze > requirements.txt
7. The project can now be opened in your preferred IDE, in my case it is PyCharm. Make sure to use the created virtual environment for this project.

