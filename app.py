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
    output +=" ".join(form)+ "<br>"
    output += "In this example, W(I) = |I|, where I is a set of integers and I is a subset of S" + "<br>"
    for n in range(1,5):
        output +=" ".join(str(i) for i in create_list(n))+ "<br>"
        output += "Auto Enter a number <i>n</i> such that <b>S</b> =  <b>{1..<i>" + str(n) + "</i>}</b><br>"
        start_time = time.time() 
        output += str(compute(create_list(n),n,'not_fixed')) + "<br>"
        output += str(time.time() - start_time) + " seconds<br>" 
        output += "<br>"
    output += "</div></body></html>" + "<br>"
    return output
# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

        