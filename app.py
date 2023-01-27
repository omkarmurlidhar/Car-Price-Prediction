from flask import Flask,request,render_template
import pickle
app=Flask(__name__,template_folder='Template')
filename="model13.pkl"
fileobj=open(filename,'rb')
b= pickle.load(fileobj)
@app.route('/')
def kaisecar():
    return render_template('car.html')

@app.route('/end')
def murli():
    return render_template('car_form.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
        Present_Price=float(request.form['Present_Price'])
        Kms_Driven=float(request.form['Kms_Driven'])
        age=int(request.form['no_year'])
        no_year=2023-age
        fuel=request.form['fuel']
        if(fuel=='Petrol'):
            Petrol=1.0
            Diesel=0.0
        else:
            Petrol=0.0
            Diesel=1.0

        seller_type=request.form['seller_type']
        if(seller_type=='Individual'):
            Individual=1.0
            Dealer=0.0
        else:
            Individual=0.0
            Dealer=1.0

        transmission=request.form['transmission']
        if(transmission=='Manual'):
            Manual=1.0
            Automatic=0.0
        else:
            Manual=0.0
            Automatic=1.0

        

        prediction=b.predict([[Present_Price,Kms_Driven,no_year,Petrol,Individual,Manual]])
        
        return render_template("car_form.html",prediction_text="Total Car Price is Rs {:.2f} ".format(float(prediction)))

    else:
        return render_template('car_form.html')

if __name__=='__main__':
    app.run(debug=True,port=5)