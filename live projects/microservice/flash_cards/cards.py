
from flask import  request, jsonify, Flask
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

cards=[]
class Card:
    def __init__(self,id:int,question:str,answer:str):
        self.id=id
        self.question=question
        self.answer=answer

    def toDict(self):
        return {"id":self.id,"question":self.question,"answer":self.answer}


@app.route("/cards",methods=['POST'])
def addCard():
    data=request.get_json()
    cardId=len(cards)+1
    #adding the new card details to the cards
    card=Card(cardId,data["question"],data["answer"])
    cards.append(card)
    return jsonify({"id":card.id,"question":card.question,"answer":card.answer}), 201

@app.route("/cards",methods=["GET"])
def getCards():
    return jsonify([card.toDict() for card in cards])



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
