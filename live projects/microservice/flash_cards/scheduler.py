import cardSchedule
from datetime import date, timedelta

app=Flask(__name__)

class SchedulerService:

    def __init__(self):
        self.schedules = {}
    
    def reviewCard(self,cardId:int, correct:bool) -> dict:
        if cardId not in self.schedules:
            self.schedules[cardId] = CardSchedule(cardId)

        schedule = self.schedules[cardId]
        schedule.review(correct)
        return schedule.to_dict()

