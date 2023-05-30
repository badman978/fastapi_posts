from fastapi import Depends, FastAPI, Response, status, HTTPException, APIRouter
from sqlalchemy import func
from sqlalchemy.orm import Session
from typing import List, Optional

from ..database import get_db
from .. import models, schemas, oauth2



router = APIRouter( 
    prefix="/posts",
    tags = ['Posts']
)
# @router.get("/", response_model=list[schemas.Post])
@router.get("/", response_model=list[schemas.PostVote])
def get_posts(db: Session = Depends(get_db), limit : int = 10, skip: int=0, search: Optional[str]= ""):
    print(search)
    # all_posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    return posts


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostR)
def create_post(post: schemas.PostBase, db: Session = Depends(get_db), current_user: int=Depends(oauth2.get_current_user), ):
    
    new_post = models.Post(owner_id=current_user.id, **post.dict())

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


#db.query(models.Post).filter(models.Post.id == id).first()
@router.get("/{id}", response_model=schemas.PostVote)
def get_post(id: int, db: Session = Depends(get_db), current_user: int=Depends(oauth2.get_current_user)):
    # post =db.query(models.Post).

    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f" post with id: {id}, was not found")
        # reply = response.status_code = status.HTTP_404_NOT_FOUND

    return post 


@router.delete("/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int=Depends(oauth2.get_current_user)):
   # cursor.execute("""DELETE FROM posts WHERE id = %s returning *""", (str(id)))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    #verify = db.query(models.Post)
    post = db.query(models.Post).filter(models.Post.id == id).first()

    if post == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,)
    
    
    if post.owner_id != current_user.id:
       raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="not authorized to perform action")
    
    db.delete(post)
    db.commit()

    return Response(status_code= status.HTTP_204_NO_CONTENT, )


@router.put("/{id}", response_model=schemas.PostR)
def update_post(
    id: int,
    updated_post: schemas.PostBase,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user)
):
    post = db.query(models.Post).filter(models.Post.id == id).first()

    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform action")

    db.query(models.Post).filter(models.Post.id == id).update(updated_post.dict())
    db.commit()

    # Retrieve the updated post
    updated_post = db.query(models.Post).filter(models.Post.id == id).first()

    return updated_post

