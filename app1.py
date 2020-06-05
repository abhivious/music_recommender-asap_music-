from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle
import random
import matplotlib.pyplot as plt

app = Flask(__name__)
ml_model1 = pickle.load(open('dtmodel1.pkl','rb'))
@app.route('/')
def home():
	return render_template('home_url.html')

@app.route('/home_predict')
def home_predict():
	return render_template('home_predict.html')

@app.route("/predict",methods=['GET','POST'])
def predict():
	if request.method=='POST':
		try:
			name = request.form['name']
			age = request.form['age']
			gen = request.form['gen']
			pred_args = [age,gen]
			pred_args_arr = np.array(pred_args)
			pred_args_arr = pred_args_arr.reshape(1,-1)
			model1_pred = ml_model1.predict(pred_args_arr)
			songs_data=pd.read_csv('songsdb1.csv')
			pred_df=songs_data['Genre']==model1_pred[0]
			a=songs_data[pred_df]
			l=list(a['Name'])
			song=random.choice(l)
			#ref=a['Name']==song
			#l1=list(ref['Ref_track'])
			#link=l1[0]
		except valueError:
			return 'please check if the values are entered correctly'
	return render_template('predict.html',prediction = song)

@app.route('/about_us')
def about_us():
	return render_template('about_us.html')

@app.route('/no_songs')
def songs():
	return render_template('no_songs.html')


@app.route('/dance',methods=['GET','POST'])
def dance():
	df = pd.read_csv('songsdb1.csv')
	sortd = df.sort_values('Danceability',ascending=False)
	Dsong=sortd.head()
	dcol=Dsong['Danceability']
	l1=list(dcol)
	ncol=Dsong['Name']	
	l2=list(ncol)
	plt.figure(figsize=(20,15))
	plt.axis([-1,5,0.9,1])
	plt.xlabel('Name of song')
	plt.ylabel('Danceability')
	plt.bar(l2,l1)
	plt.xticks(rotation=90)
	plt.savefig('static/dancewhite.png')
	new_name='static/dancewhite.png'
	return render_template('dance.html')

@app.route('/energy',methods=['GET','POST'])
def energy():
	df = pd.read_csv('songsdb1.csv')
	sortd = df.sort_values('Energy',ascending=False)
	Dsong=sortd.head()
	dcol=Dsong['Energy']
	l1=list(dcol)
	ncol=Dsong['Name']	
	l2=list(ncol)
	plt.figure(figsize=(20,15))
	plt.axis([-1,5,0.9,1])
	plt.xlabel('Name of song')
	plt.ylabel('Energy')
	plt.bar(l2,l1)
	plt.xticks(rotation=90)
	plt.savefig('static/energywhite.png')
	new_name='static/energywhite.png'
	return render_template('energy.html')

@app.route('/loud',methods=['GET','POST'])
def loud():
	df = pd.read_csv('songsdb1.csv')
	sortd = df.sort_values('Loudness',ascending=False)
	Dsong=sortd.head()
	dcol=Dsong['Loudness']
	l1=list(dcol)
	ncol=Dsong['Name']	
	l2=list(ncol)
	plt.figure(figsize=(20,15))
	plt.axis([-1,5,0,-1])
	plt.xlabel('Name of song')
	plt.ylabel('Loudness')
	plt.bar(l2,l1)
	plt.xticks(rotation=90)
	plt.savefig('static/loudwhite.png')
	new_name='static/loudwhite.png'
	return render_template('loud.html')


@app.route('/acoustic',methods=['GET','POST'])
def acoustic():
	df = pd.read_csv('songsdb1.csv')
	sortd = df.sort_values('Acousticness',ascending=False)
	Dsong=sortd.head()
	dcol=Dsong['Acousticness']
	l1=list(dcol)
	ncol=Dsong['Name']	
	l2=list(ncol)
	plt.figure(figsize=(20,15))
	plt.axis([-1,5,0.8,1])
	plt.xlabel('Name of song')
	plt.ylabel('Acousticness')
	plt.bar(l2,l1)
	plt.xticks(rotation=90)
	plt.savefig('static/acoustic1white.png')
	new_name='static/acoustic1white.png'
	return render_template('acoustic.html')

@app.route('/instrumental',methods=['GET','POST'])
def instrument1():
	df = pd.read_csv('songsdb1.csv')
	sortd = df.sort_values('Instrumentalness',ascending=False)
	Dsong=sortd.head()
	dcol=Dsong['Instrumentalness']
	l1=list(dcol)
	ncol=Dsong['Name']	
	l2=list(ncol)
	plt.figure(figsize=(20,15))
	plt.axis([-1,5,0.9,1])
	plt.xlabel('Name of song')
	plt.ylabel('Instrumentalness')
	plt.bar(l2,l1)
	plt.xticks(rotation=90)
	plt.savefig('static/instrumentwhite.png')
	new_name='static/instrumentwhite.png'
	return render_template('instrumental.html')

@app.route('/lively',methods=['GET','POST'])
def lively():
	df = pd.read_csv('songsdb1.csv')
	sortd = df.sort_values('Liveness',ascending=False)
	Dsong=sortd.head()
	dcol=Dsong['Liveness']
	l1=list(dcol)
	ncol=Dsong['Name']	
	l2=list(ncol)
	plt.figure(figsize=(20,15))
	plt.axis([-1,5,0.9,1])
	plt.xlabel('Name of song')
	plt.ylabel('Liveness')
	plt.bar(l2,l1)
	plt.xticks(rotation=90)
	plt.savefig('static/livewhite.png')
	new_name='static/livewhite.png'
	return render_template('lively.html')

@app.route('/valence',methods=['GET','POST'])
def Valence():
	df = pd.read_csv('songsdb1.csv')
	sortd = df.sort_values('Valence',ascending=False)
	Dsong=sortd.head()
	dcol=Dsong['Valence']
	l1=list(dcol)
	ncol=Dsong['Name']	
	l2=list(ncol)
	plt.figure(figsize=(20,15))
	plt.axis([-1,5,0.9,1])
	plt.xlabel('Name of song')
	plt.ylabel('valence')
	plt.bar(l2,l1)
	plt.xticks(rotation=90)
	plt.savefig('static/valwhite.png')
	new_name='static/valwhite.png'
	return render_template('valence.html')

@app.route('/speech',methods=['GET','POST'])
def speech():
	df = pd.read_csv('songsdb1.csv')
	sortd = df.sort_values('Speechness',ascending=False)
	Dsong=sortd.head()
	dcol=Dsong['Speechness']
	l1=list(dcol)
	ncol=Dsong['Name']	
	l2=list(ncol)
	plt.figure(figsize=(20,15))
	plt.axis([-1,5,0.4,1])
	plt.xlabel('Name of song')
	plt.ylabel('Speechness')
	plt.bar(l2,l1)
	plt.xticks(rotation=90)
	plt.savefig('static/speechwhite.png')
	new_name='static/speechwhite.png'
	return render_template('speech.html')

@app.route('/tempo',methods=['GET','POST'])
def tempo():
	df = pd.read_csv('songsdb1.csv')
	sortd = df.sort_values('Tempo',ascending=False)
	Dsong=sortd.head()
	dcol=Dsong['Tempo']
	l1=list(dcol)
	ncol=Dsong['Name']	
	l2=list(ncol)
	plt.figure(figsize=(20,15))
	plt.axis([-1,5,170,210])
	plt.xlabel('Name of song')
	plt.ylabel('Tempo')
	plt.bar(l2,l1)
	plt.xticks(rotation=90)
	plt.savefig('static/tempowhite1.png')
	new_name='static/tempowhite1.png'
	return render_template('tempo.html')

@app.route('/datasetgraph',methods=['GET','POST'])
def graphical():
	df = pd.read_csv('songsdb1.csv')
	gcol = df['Genre']
	l = list(gcol)
	garray = np.array(l)
	pop = len(garray[garray=='pop'])
	jazz = len(garray[garray=='jazz'])
	hiphop = len(garray[garray=='hiphop'])
	acoustic = len(garray[garray=='acoustic'])
	dance = len(garray[garray=='dance'])
	country = len(garray[garray=='country'])
	rock = len(garray[garray=='rock'])
	metal = len(garray[garray=='metal'])
	categ = [pop,jazz,hiphop,acoustic,dance,country,rock,metal]
	plt.ylabel('No of songs')
	plt.bar(['POP','JAZZ','HIPHOP','ACOUSTIC','DANCE','COUNTRY','ROCK','METAL'],categ)
	plt.xticks(rotation=45)
	plt.savefig('static/grawhite1.png')
	return render_template('datasetgraph.html')

if __name__=="__main__":
	app.run(debug=True)
