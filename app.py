import os
from flask import Flask
from compute_local import compute
from client import get_num_map_nodes, create_list
import cgi          # for _GET variable
import time

# initialization
app = Flask(__name__)
app.config.update(
    DEBUG = True,
)

# controllers
@app.route("/")
def hello():
    form = cgi.FieldStorage()
    
    output = "<html><body><div style='font-family: Arial '>"
    output += "<h2>Generating Series Live Demonstration</h2>"
    output += "<br>"
    output += "<a href='https://github.com/hyunwookshin'><b>Source Code: github/hyunwookshin</b></a><br>"
    output += "Last Edited: May 18, 2014<br>"
    output +=" ".join(form)+ "<br>"
    output += "In this example, Let weight function W(I) = |I| (size of I), where I is a set of integers and I is a subset of S" + "<br>"
    output += "<img src='https://raw.githubusercontent.com/hyunwookshin/generating_series/master/equation/equation.png'><br>"
    for n in range(1,5):
        
        output += "Automatically entered a number <i>n</i> = " + str(n) + " such that <b>S</b> =  <b>{1..<i>" + str(n) + "</i>}</b><br>"
        output += "S = {" + ", ".join(str(i) for i in create_list(n))+ "} <br>"
        start_time = time.time() 
        output += "Sum: " + str(compute(create_list(n),n,'not_fixed')) + "<br>"
        output += "Compute Time " + str(time.time() - start_time) + " seconds<br>" 
        output += "<br>"
    output += "</div></body></html>" + "<br>"
    return output
# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

        