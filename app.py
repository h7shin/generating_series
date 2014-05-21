import os
from flask import Flask
from compute_local import compute
from client import get_num_map_nodes, create_list
import time

# Init
app = Flask(__name__)
app.config.update(
    DEBUG = True,
)

# Controller
@app.route("/")
def runapp():
     
    output = "<html><body><div style='font-family: Arial '>"
    output += "<h2>Generating Series Live Demonstration</h2>"
    output += "<br>"
    output += "<b>Plan, Source Code and Documentation: <a href='https://github.com/hyunwookshin/generating_series'>github/hyunwookshin/generating_series</b></a><br>"
    output += "Last edited: May 21, 2014<br>"
    output += "<br>"
    output += "In this example, Let weight function W(I) = |I| (size of I), where I is a set of some integers and I is a subset of S" + "<br>"
    output += "<img src='https://raw.githubusercontent.com/hyunwookshin/generating_series/master/equation/equation.png' width='500px'><br>"
    for n in 2,4,8:
        output += "<h3><b><i>n</i></b> = " + str(n) + "</h3><br>"
        output += "Automatically entered a number <i>n</i> = " + str(n) + " such that <b>S</b> is a set of all subsets of  <b>{1,..," + str(n) + "}</b><br>"
        output += "S = {" + ", ".join(str(i) for i in create_list(n))+ "} <br>"
        start_time = time.time() 
        output += "Sum: " + str(compute(create_list(n),n,'not_fixed')) + "<br>"
        output += "Compute Time " + str(time.time() - start_time) + " seconds<br>" 
        output += "<br>"
    output += "</div></body></html>" + "<br>"
    return output

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

 # Credits
 # Heroku Tutorial:
 # Link: http://www.shea.io/lightweight-python-apps-with-flask-twitter-bootstrap-and-heroku/