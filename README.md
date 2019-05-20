# csod-automation

This app will assist you in automating tasks in CornerStone On-Demand.


## Prerequisites

In order to master this project you need to have a have prior knowledge in Python, HTML and JavaScript.

Have the following installed:

* Python v3.6 and above - [Download](https://www.python.org/downloads/)
* Google Chrome v72 and above - [Download](https://www.google.com/chrome/?brand=CHBD&gclid=Cj0KCQjwoInnBRDDARIsANBVyARevoFaEE-jEXuazgudYsWXTSx7Z_R8isbF7VVtIZS0OKlfSL6TaEUaAubaEALw_wcB&gclsrc=aw.ds)
* GIT - [Download](https://git-scm.com/downloads)

## Installing

#### Cloning repository to local machine

Create a folder anywhere on your machine, name it: *csod-project*

Open Command-Prompt (Terminal) in that *csod-project* folder and clone the project to local repository
```
git clone https://github.com/unfor19/csod-automation/
```

#### Current folder structure ####
```
C:\Users\my_user\Documents\csod-project\csod-automation\
```

#### Creating a new Python virtual environment
Still in Command-Prompt (Terminal) in the same folder *csod-project*, create a new virtual environment.

The name of the folder will be: *ENV*

**Note**: The module *venv* comes out-of-the box with Python v3.6 and above.
```
python -m venv ENV
```

#### Current folder structure ####
```
C:\Users\my_user\Documents\csod-project\csod-automation\
C:\Users\my_user\Documents\csod-project\ENV\
```

#### Activate virtual environment ####
Assuming we are currently in the *csod-project* folder, then:

```
C:\Users\my_user\Documents\csod-project>ENV\Scripts\activate
(ENV) C:\Users\my_user\Documents\csod-project>
```

#### Install necessary requirements with pip ####

``` (ENV) C:\Users\my_user\Documents\csod-project>pip install -r requirements.txt ```

**Note**: The installed packages will be available only for the *ENV* virtual environment.

#### Modify the constants in csod_CONSTANTS.py ####
```
# URL
MY_PORTAL_URL = "https://my-portal.csod.com"

# Credentials
MY_USERNAME = "admin"
MY_PASSWORD = "adminPassword"
```

## Getting Started

#### Activate virtual environment ####
Assuming we are currently in the *csod-project* folder, then:

```
C:\Users\my_user\Documents\csod-project>ENV\Scripts\activate
(ENV) C:\Users\my_user\Documents\csod-project>
```

#### Adjusting the code ####
// TODO
Adjust the code according to your needs by editing: csod_edit_lo.py

## Built With

* [Visual Studio Code](https://code.visualstudio.com/) - IDE
* [Python](https://www.python.org) - Programming language for automation
* [Selenium](https://www.seleniumhq.org/) - Browser automation framework
* JavaScript - Manipulating HTML objects

## Authors

* **Meir Gabay** - *Owner*
* **Yuval Gross** - *Contriubutor*

See also the list of [contributors](https://github.com/unfor19/csod-automation/contributors) who participated in this project.

## License

This project is licensed under the GPL v3.0 License - see the [LICENSE.md](LICENSE.md) file for details
