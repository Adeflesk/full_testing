## Learning full stack testing with python

Firt step was to creat unit tests/unit
   Using nosetests //pip install nosetests
   Testing account with creation and returns balance
   Testing bank with adding accounts and returning balance

Accepting testing
   Using the RobotFramework as lettuce does not support python3
   Using Gherkin style langaug GIVEN WHEN 
   One test in test/robots/test/bank.robot

   Creating web app with flask
   The flask app is in bank/bank_app.py
   
Preformance Testing
   Set up JMeter this produced file HTTP Request.jmx
   Jmeter can be run on the command line with 
   jmeter -n -t HTTP\ Request.jmx -l results.jtl
   This puts all resultes into file results.jtl
   
Code profiling 
   Adding cProfile to the bank_app run code to profile the calls
   installing $ pip install pycallgraph to create a visual 
   run code by $ pycallgraph graphviz -- bank_app.py
