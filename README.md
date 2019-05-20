# csod-automation

This app will assist you in automating tasks in CornerStone On-Demand.


## Prerequisites

In order to master this project you need to have a have prior knowledge in Python, HTML and JavaScript.
Have the following installed:

* Python v3.6 and above - [Download](https://www.python.org/downloads/)
* Google Chrome v72 and above - [Download](https://www.google.com/chrome/?brand=CHBD&gclid=Cj0KCQjwoInnBRDDARIsANBVyARevoFaEE-jEXuazgudYsWXTSx7Z_R8isbF7VVtIZS0OKlfSL6TaEUaAubaEALw_wcB&gclsrc=aw.ds)
* GIT - [Download](https://git-scm.com/downloads)

## Installing

### Folder structure
..\csod-project\
    \ENV\
    \code-automation    <-- this is created after you clone it
    
    
Create a folder anywhere on your machine, name it: *csod-project*

Open cmd.exe in that folder and clone the project to local repository
```
git clone https://github.com/unfor19/csod-automation/
```

Install necessary requirements with pip

Modify the variables in csod_CONSTANTS.py
```
# URL
MY_PORTAL_URL = "https://my-portal.csod.com"

# Credentials
MY_USERNAME = "admin"
MY_PASSWORD = "adminPassword"
```

Adjust the code according to your needs by editing: csod_edit_lo.py


```
Give examples
```

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
