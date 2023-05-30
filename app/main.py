
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

# models.Base.metadata.create_all(bind=engine)
 
app =FastAPI()


origins = ["*",]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 

#link routers
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/") #path operators
def root():
    return {"message": "Hello World"}

#@app.get("/posts", response_model=schemas.PostR)
#def get_posts(db: Session = Depends(get_db)):
    #all_posts = db.query(models.Post).all()
    #return all_posts

#@app.put("/posts/{id}", response_model=schemas.PostR)
#def update_post(id: int, updated_post: schemas.PostBase, db: Session = Depends(get_db)):
    #cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s  returning *""", (post.title, post.content, post.published, str(id)))

    #updated_post = cursor.fetchone()
    #conn.commit() # Add this line

    #update =db.query(models.Post).filter(models.Post.id == id)
    #post = update.first()

    #if post == None:
        #raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"post with id: {id} was not found")


    #update.update(updated_post.dict(), synchronize_session=False)
   
    #db.commit()

    #return update.first()



# title str, content 
# check out for link parameters. they should always come last in code
# latest post should always have an id of 001