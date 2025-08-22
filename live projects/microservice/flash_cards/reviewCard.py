from flask import Flask,request,jsonify
import reviewSchedule
scheduler=reviewSchedule.ReviewScheduler()
app = Flask(__name__)

@app.route("/schedule/<int:cardId>",methods=['POST'])
def ReviewCard(cardId):
    data=request.get_json()
    correct=data.get("correct",False)

    result=scheduler.review(cardId,correct)
    return jsonify(result)


if __name__== "__main__":
    app.run(host="0.0.0.0",port="5001",debug=True)