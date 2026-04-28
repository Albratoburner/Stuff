from database import engine, Base
import Model
Base.metadata.create_all(bind=engine)
 