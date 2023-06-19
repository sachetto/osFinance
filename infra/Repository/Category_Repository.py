from Entities.Category import Category

class CategoryRepository:
    def __init__(self, conn_handler) -> None:
        self.__ConnectionHandler = conn_handler

    def Select(self, category_name = None):
        with self.__ConnectionHandler as db:
            if category_name == None:
                data = db.Section.query(Category).all()
            else:
                data = db.Section.query(Category).\
                    filter_by(Category=category_name).\
                    first()
            return data
        
    def Insert(self, category):
        with self.__ConnectionHandler as db:
            db.Section.add(category)
            db.Section.commit()