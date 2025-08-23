from datetime import date,timedelta

class CardScheduler:
    def __init__(self,cardId:int):
        self.cardId=cardId
        self.intervalDays=1
        self.nextReviewDate=date.today() + timedelta(1)

    def cardReview(self,correct:bool):
        if correct:
            self.intervalDays*=2
        else:
            self.intervalDays=1
        self.nextReviewDate=date.today()+timedelta(self.intervalDays)
    
    def toDict(self):
        return {"cardId":self.cardId,
                "intervalDays":self.intervalDays,
                "nextReviewDate":str(self.nextReviewDate)}
