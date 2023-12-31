from flask import Flask ,request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route('/about')
def details():
    return 'this is the about '

@app.route("/demo",methods = ['POST'])
def math_operation():
    if request.method == 'POST':
        operation = request.json['operation']
        num1 = request.json['num1']
        num2 = request.json['num2']
        result = num1 + num2
        return jsonify("opeation is {} result of the both is {} and first value is {} and second is {} ".format(operation,result,num1,num2))



@app.route("/calculator",methods= ['POST'])
def calc():
    if request.method == "POST":
        operation = request.json["operation"]
        num1 = request.json["num1"]
        num2 = request.json["num2"]
        res = 0

        if operation == "add":
            res = int(num1) + int(num2)

        elif operation == "sub":
            res = int(num1) - int(num2)

        elif operation == "multi":
            res = int(num1) * int(num2)

        elif operation == "division":
            res = int(num1)/int(num2)

        return jsonify("for this operation is {} and the result is {}".format(operation ,res))
        #return "clear the exam{}".format(res)



@app.route("/calcul",methods= ['POST'])
def calcu():
    if request.method == "POST":
        operation = request.form["operation"]
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])
        res = 0

        if operation == "add":
            res = int(num1) + int(num2)

        elif operation == "sub":
            res = int(num1) - int(num2)

        elif operation == "multi":
            res = int(num1) * int(num2)

        elif operation == "division":
            res = int(num1)/int(num2)

        return render_template("result.html", result= res)
        #return "for this operation is {} and the result is {}".format(operation ,res)
        #return "clear the exam{}".format(res)




@app.route("/company",methods = ['POST'])
def add():
    re = request.json["num1"] + request.json["num2"]
    return "this is additoin operation {}".format(re)

if __name__ == '__main__':
    app.run(host= "0.0.0.0",port = 5000)