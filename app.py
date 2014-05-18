import os
from flask import Flask
from compute_local import compute
from client import get_num_map_nodes, create_list

# initialization
app = Flask(__name__)
app.config.update(
    DEBUG = True,
)

# controllers
@app.route("/")
def hello():
    output = "Testing...."
    output += "W(I) = |I| where I is a set of integers and I is a subset of S")
    for n in range(1,5):
        output += "Enter a number n such that S =  {1...n}:  " + str(n) + "\n"
    return output
        #compute(create_list(1),,'not_fixed')

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

        