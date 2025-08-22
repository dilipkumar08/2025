import cardSchedule
from datetime import date, timedelta


class ReviewScheduler:

    def __init__(self):
        self.schedules = {}
    
    def review(self,cardId:int, correct:bool) -> dict:
        
        if cardId not in self.schedules:
            self.schedules[cardId] = cardSchedule.CardScheduler(cardId)
        schedule = self.schedules[cardId]
        schedule.cardReview(correct)
        return schedule.toDict()
