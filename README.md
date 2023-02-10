# neurolab-mongo-python

![image](https://user-images.githubusercontent.com/57321948/196933065-4b16c235-f3b9-4391-9cfe-4affcec87c35.png)

### Step 1 - Install the requirements

```bash
pip install -r requirements.txt
```

### Step 2 - Run main.py file

```bash
python main.py
```

### To download datasets###

```
wget https://raw.githubusercontent.com/avnyadav/sensor-fault-detection/main/aps_failure_training_set1.csv
```

This is changes made in Neurolab


Git commands 
If starting a new project, and want to use GIT in your project, execute 
```
git init
```

This is going to initialize git in the source code

OR

one can clone existing github repo using githib URL 

```
git clone <github_url>

```
Note : clone /Download github repo on your system

Add your files or changes made in file to git staging are

```
git add file_name
```
Note: One can give file name or use add . to add everything to staging area

Git commit 
```
git commit -m "write down msg"
```

To push changes to git
```
git push origin main 
```
Note - Origin contains URL to your github repo
main --> your branch name

OR 
To push changes forcefully 
```
git push origin main -f
```



To pull changes from Github repo 
``` 
git pull origin main
```
Note - Origin contains URL to your github repo
main --> your branch name



