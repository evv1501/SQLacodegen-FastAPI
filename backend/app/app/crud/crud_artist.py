from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.chinook import Artist
from app.schemas.artist import ArtistCreate, ArtistUpdate


class CRUDArtist(CRUDBase[Artist, ArtistCreate, ArtistUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: ArtistCreate, ArtistId: int
    ) -> Artist:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, ArtistId=ArtistId)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, ArtistId: int, skip: int = 0, limit: int = 100
    ) -> List[Artist]:
        return (
            db.query(self.model)
            .filter(Artist.ArtistId == ArtistId)
            .offset(skip)
            .limit(limit)
            .all()
        )


artist = CRUDArtist(Artist)