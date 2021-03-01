from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/', defaults={'result': "Unavailable!"})
@app.route('/<result>')
def mainpage(result):
    return render_template("index.html", result = result)


def checker(input):
    data = int(input)
    flag = False
    if(((data % 4 == 0) and (data % 100!= 0)) or (data %400 == 0)):
        flag = True
    return flag     


@app.route('/submit',methods = ['GET'])
def submit():
   if request.method == 'GET':
    year = request.args['number'];
    y = int(year)
    flag = False
    if(checker(y)== True):
        flag = True
            
            
    if(flag == True):  
         return redirect(url_for('mainpage',result = "Yes, It is a leap year"))
    else:
        return redirect(url_for('mainpage',result = "No, It is not a leap year"))
if __name__ == '__main__':
    app.run()
