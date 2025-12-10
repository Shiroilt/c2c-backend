from flask import Flask
app=Flask(_name_)

@app.get("/")
def home():
	return{"massage":"cloud2cloud MVP backend running..."}