from flask import Flask, render_template, request
# from extractors.indeed import extract_indeed_job
from extractors.wwr import extract_wwr_jobs

app = Flask("JobScrapper")

@app.route('/') #decorator #Syntactic sugar #데코레이터를 함수위에두면 user가 page를 방문했을때 호출해야하는 것을 알게됨
def home():
    return render_template("home.html", name="Bee")

@app.route("/search")
def hello():
    keyword = request.args.get("keyword")
    # indeed = extract_indeed_job(keyword)
    wwr = extract_wwr_jobs(keyword)
    jobs = wwr
    return render_template("search.html", keyword=keyword, jobs=jobs)


app.run("0.0.0.0")