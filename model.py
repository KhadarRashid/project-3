from dataclasses import dataclass

# @dataclass
# class Artist():
#     name: str
#     age: int



class Artist:

    def __init__(self, name, email, artist_id=None):
        self.name = name
        self.email = email
        self.artist_id = artist_id

    def insert_artist(self):
        if not self.artist_id:
