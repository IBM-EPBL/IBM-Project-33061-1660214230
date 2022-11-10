from flask import Flask,request,json

app=Flask(__name__)

name={"1":"Thatcha", "2":"sakthi", "3":"karthi" ,"4":"manimegalai" ,"5":"saravanan" ,"6":"Shanmugam" }

@app.route('/data',methods=['GET','POST'])
def api():
    if request.method=='GET':
        return name
    if request.method=='POST':
        data=request.json
        name.update(data)
        return 'data got inserted in the database'

@app.route("/data/<id>",methods=['PUT'])
def update(id):
    data=request.form['item']
    name[str(id)]=data
    return 'data updated in the database'

@app.route("/data/<id>",methods=["DELETE"])
def deleteoperation(id):
    name.pop(str(id))
    return 'data deleted from the database'

if __name__=='__main__':
    app.run(debug=True)