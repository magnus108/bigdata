# bigdata

* docker-compose bliver ikke brugt
* der var fejl i header på min csv fil og hvis det bugger uden at give error message så det nok der der går noget galt men deet bør virke nu

* kør docker build -t "<navn>" .       /.... husk hvergang der ændres i csv filerne skal docker buildes igen
* kør docker run -e NEO4J_AUTH=none \
    --publish=7474:7474 --publish=7687:7687 \
     "<navn>"
* kør python import.py   / kræver pip install py2neo
* bodies.py kan så hente eg bodies ud.

* har ikke lykkedes mig at finde noget svar på hvordan vi laver machin learning stuff
* måske er disse links gode
* http://stackoverflow.com/questions/17017878/is-scikit-learn-suitable-for-big-data-tasks / se svaret
* https://databricks.com/blog/2016/02/08/auto-scaling-scikit-learn-with-apache-spark.html
* https://adventuresindatascience.wordpress.com/2014/12/30/minibatch-learning-for-large-scale-data-using-scikit-learn/
