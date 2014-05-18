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
    
    output = "<html><body><textarea rows='50' cols='50'>"
    output +=" ".join(form)+ "\n"
    output += "In this example, W(I) = |I|, where I is a set of integers and I is a subset of S" + "\n"
    for n in range(1,5):
        output +=" ".join(create_list(n))+ "\n"
        output += "Auto Enter a number n such that S =  {1.." + str(n) + "}\n"
        start_time = time.time() 
        output += str(compute(create_list(n),n,'not_fixed')) + "\n"
        output += str(time.time() - start_time) + " seconds\n" 
    output += "</textarea></body></html>" + "\n"
    return output
# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

        