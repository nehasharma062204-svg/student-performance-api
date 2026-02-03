from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)
df = pd.read_csv("students.csv")

@app.route("/")
def home():
    return "Student Performance API is running"

@app.route("/summary")
def summary():
    return jsonify({
        "total_students": df["name"].nunique(),
        "average_marks": round(df["marks"].mean(), 2)
    })

@app.route("/topper")
def topper():
    top = df.loc[df["marks"].idxmax()]
    return jsonify(top.to_dict())

@app.route("/subject/<subject>")
def subject(subject):
    sub_df = df[df["subject"].str.lower() == subject.lower()]
    return jsonify({
        "subject": subject,
        "average": round(sub_df["marks"].mean(), 2),
        "max": int(sub_df["marks"].max()),
        "min": int(sub_df["marks"].min())
    })

app.run(debug=True)
