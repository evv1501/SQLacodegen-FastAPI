from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Artist])
def read_Artists(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve artists.
    """
    if crud.user.is_superuser(current_user):
        artists = crud.artist.get_multi(db, skip=skip, limit=limit)
    else:
        artists = crud.artist.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return artists


@router.post("/", response_model=schemas.Artist)
def create_Artist(
    *,
    db: Session = Depends(deps.get_db),
    artist_in: schemas.ArtistCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new artist.
    """
    artist = crud.artist.create_with_owner(db=db, obj_in=artist_in, owner_id=current_user.id)
    return artist


@router.put("/{id}", response_model=schemas.Artist)
def update_Artist(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    artist_in: schemas.ArtistUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an artist.
    """
    artist = crud.artist.get(db=db, id=id)
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    artist = crud.artist.update(db=db, db_obj=artist, obj_in=artist_in)
    return artist


@router.get("/{id}", response_model=schemas.Artist)
def read_Artist(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get Artist by ID.
    """
    artist = crud.artist.get(db=db, id=id)
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    return artist


@router.delete("/{id}", response_model=schemas.Artist)
def delete_Artist(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an Artist.
    """
    artist = crud.artist.get(db=db, id=id)
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    artist = crud.artist.remove(db=db, id=id)
    return artist
