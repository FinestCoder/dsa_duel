import random
import string
import secrets
from app.schemas.room import RoomCreate
from app.models.room import Room


class RoomService:

    def __init__(self, db):
        self.db = db

    def _generate_room_code(self):
        while True:
            characters=string.ascii_uppercase+string.digits
            room_code=''.join(secrets.choice(characters) for _ in range(6))
            # if room_code doesn't exist:
            #     break
            return room_code
    def create_room(
        self,
        room_data: RoomCreate,
        host_user_id: int,
    ):
        generated_room_code = self._generate_room_code()
        room = Room(
            room_code=generated_room_code,
            host_user_id=host_user_id,
            topic=room_data.topic,
            difficulty=room_data.difficulty.value,
            num_questions=room_data.num_questions,
            time_per_question=room_data.time_per_question,
        )
        self.db.add(room)
        self.db.commit()
        self.db.refresh(room)
        return room
