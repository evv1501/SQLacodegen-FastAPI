from typing import Optional

from pydantic import BaseModel


# Shared properties
class ArtistBase(BaseModel):
    Name: Optional[str] = None


# Properties to receive on Artist creation
class ArtistCreate(ArtistBase):
    Name: str


# Properties to receive on Artist update
class ArtistUpdate(ArtistBase):
    pass


# Properties shared by models stored in DB
class ArtistInDBBase(ArtistBase):
    ArtistId: int
    Name: str

    class Config:
        orm_mode = True


# Properties to return to client
class Artist(ArtistInDBBase):
    pass


# Properties properties stored in DB
class ArtistInDB(ArtistInDBBase):
    pass
