# Stryktipset


## Setup
*Make sure you have at least python 3.6.0 installed*<br>
*Make sure you have chrome drivers for you'r version of chrome installed*<br>
*If you intend to change c++ files make sure you have some way of recompiling those files*</br></br>

Navigate into to project, create an environment, activate it, and install the required packages
<pre>
python3 -m venv env
</pre>
<br></br>
<b>Activate environment:</b> <br>
Windows:
<pre>source env/Scripts/activate </pre>
<b><i>Or</i></b><br>
Unix/MacOS:
<pre>source env/bin/activate </pre>
<br></br>
<b>Install packages</b>
<pre>python3 -m pip install -r requirements.txt</pre>
<br></br>

Create a file named "config.cfg" and fill in the following (example can be found in the project):
```
{
    "chrome_driver_path" : "ABSOLUTE PATH TO CHROME DRIVER",
    "headless" : true,
    "login_op" : {
        "username" : "YOU'R USERNAME TO ODDS PORTAL",
        "password" : "YOU'R PASSWORD TO ODDS PORTAL"
    },
    "login_stl" : {
        "email" : "YOU'R EMAIL TO STRYKTIPSETETLEAGUE",
        "password" : "YOU'R PASSWORD TO STRYKTIPSETETLEAGUE"
    }
}
```
<br></br>
## Run
From the top folder simply run:
```
python ./main.py
```

## Notes
* When compiling dijkstras remember to compile for 64 but systems in order to not run out of memory when running.
