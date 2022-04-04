import dataclasses


@dataclasses.dataclass
class User:
    """
    Representation of a GPA System user.
    """

    id: int
    name: str
    username: str
    email: str
    password: str
    role: str
