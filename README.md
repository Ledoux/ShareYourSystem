
#Install the python packages

##Install

On a Terminal :
```bash
$ pip install ShareYourSystem
```

##Uninstall

On a Terminal :
```bash
$ pip uninstall ShareYourSystem
```

#Docs

1. Put yours markdowned files docs/
2. Set the mkdocs.yml to refer to these docs
3. On the ShareYourSystem-master dir, build your site (it updates the the site/ folder)
```bash
$ mkdocs build --clean
```
4. Deploy on your http server (It is Ouvaton for here)

#Meteor GUI

1. Put your meteor js files in Meteor/
2. Deploy your application on the meteor free test server (with your specific name, ie replace shareyoursystem by your app name). On the ShareYourSystem-master dir :
```
$ meteor deploy shareyoursystem.meteor.com
```

#Reveal Slides

1. Go in Convert your modules Docs into reveal html, on the ShareYourSystem-master dir :
```
$ python inform.py
```
2. Then deploy the html slides in the http server that you want. (Ouvaton for here)


