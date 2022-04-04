from app.user.domain.user import User
from flask_restful import Resource


class UserResource(Resource):
    """
    User related resources
    """

    def __init__(self):
        pass

    def post(self, current_user: User, path: str):

        if current_user.role != "ADMIN":
            return {"status": "error", "message": "Unauthorized"}, 403
