# ParaphraseTree


## 	🚀 Quickstart
<h3>1. To run the project, you need to use this command to install all dependencies: </h3>

```bash
pip install -r requirements.txt

```

<h3>2. Make sure you are currently in the main tree to access manage.py:</h3>


<h3>3. You need to use this command to run the project:</h3>

```bash
python manage.py migrate
python manage.py runserver

```

<br>

## 	💫 Start

<h3>1. In your browser, run this path:</h3>

```bash
http://127.0.0.1:8000/paraphrase/?tree=<here your tree value without "<>" symbols>

```

<h4>After that, you will get the answer of your tree 20 times</h4>

<h3>2. To set a limit value - run this path and change the limit value:</h3>

```bash
http://127.0.0.1:8000/paraphrase/?tree=<here your tree value withour "<>" symbols>;limit=<limit int value>

```

<h3>Example: </h3>

```bash
http://127.0.0.1:8000/paraphrase/?tree=(S%20(NP%20(NP%20(DT%20The)%20(JJ%20charming)%20(NNP%20Gothic)%20(NNP%20Quarter)%20)%20(,%20,)%20(CC%20or)%20(NP%20(NNP%20Barri)%20(NNP%20G%C3%B2tic)%20)%20)(,%20,)%20(VP%20(VBZ%20has)%20(NP%20(NP%20(JJ%20narrow)%20(JJ%20medieval)%20(NNS%20streets)%20)%20(VP%20(VBN%20filled)%20(PP%20(IN%20with)%20(NP%20(NP%20(JJ%20trendy)%20(NNS%20bars)%20)%20(,%20,)%20(NP%20(NNS%20clubs)%20)%20(CC%20and)%20(NP%20(JJ%20Catalan)%20(NNS%20restaurants)%20)%20)%20)%20)%20)%20)%20);limit=1
```

<br>

## 👨‍💻 Tests
<h3>To start tests use this commamd</h3>

```bash

 python manage.py test
```
<br>

## 🛠 Tools
<h4>1. Django Rest Framework</h4>
<h4>2. Tests (in <i>ParaphraseTreeAPI/tests.py</i>)</h4>
<h4>3. Black (code style refactoring )</h4>
<h4>4. Class Based View (CBV) </h4>
<h4>5. nltk library for trees </h4>
