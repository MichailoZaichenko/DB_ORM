from sqlalchemy import create_engine
from sqlalchemy import INTEGER, DATE, TEXT, Column
from sqlalchemy import desc
from sqlalchemy import String
from sqlalchemy import ForeignKey, select
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base

BaseClass = declarative_base()

class Students(BaseClass):
    __tablename__ = "Students"

    id = Column(INTEGER, primary_key = True, autoincrement = True)
    lastName = Column(TEXT)
    name = Column(TEXT)
    surName = Column(TEXT)
    points = Column(INTEGER)

class Creature_bd:
    # функция добавления строки в таблицу Orders
    engine = create_engine("sqlite:///students_db.db")

    BaseClass.metadata.drop_all(engine)
    BaseClass.metadata.create_all(engine)

    def add_students(studentDictionary:dict)->Students:
        with Session(Creature_bd.engine) as db:
            row = Students(
                lastName = studentDictionary['lastName'],
                name = studentDictionary['name'], 
                surName = studentDictionary['surName'],
                points = studentDictionary["points"]
            )
            db.add(row)
            db.commit()
    
    def delStudents():
        with Session(Creature_bd.engine) as db:
            db.query(Students).filter(Students.points < 300).delete()
            db.commit()

    def setStudent_add_points(id):
        with Session(Creature_bd.engine) as db:
            singleSelect = db.get(Students, id)
            singleSelect.points = singleSelect.points + 5
            db.commit()
            db.refresh(singleSelect)

    def selectStudents():
        with Session(Creature_bd.engine) as db:
            db.query(Students).filter(Students.points > 428).all()
            db.commit()

# Создать БД и таблицу в ней со студентами
# Добавить всех студентов своей группы;
studentDictionary = {'lastName':"Сергій", 'name': "Ярошкін", "surName":"Сергійович", "points":539}
Creature_bd.add_students(studentDictionary)

studentDictionary = {'lastName':"Андрій", 'name': "Таран",  "surName":"Ігорович", "points":536}
Creature_bd.add_students(studentDictionary)

studentDictionary = {'lastName':"Бєлоусов", 'name': "Юрій",  "surName":"Володимирович", "points":490}
Creature_bd.add_students(studentDictionary)

studentDictionary = {'lastName':"Марченко", 'name': "Ілля",  "surName":"Андрійович", "points":433}
Creature_bd.add_students(studentDictionary)

studentDictionary = {'lastName':"Зайченко", 'name': "Михайло",  "surName":"Андрійович", "points":428}
Creature_bd.add_students(studentDictionary)

studentDictionary = {'lastName':"Діденко", 'name': "Нікіта",  "surName":"Сергійович", "points":303}
Creature_bd.add_students(studentDictionary)

studentDictionary = {'lastName':"Лозовий", 'name': "Олексій",  "surName":"Андрійович", "points":298}
Creature_bd.add_students(studentDictionary)

studentDictionary = {'lastName':"Ахмедов", 'name': "Ахмед",  "surName":"Анар Огли", "points":263}
Creature_bd.add_students(studentDictionary)

studentDictionary = {'lastName':"Рыжков", 'name': "Владислав",  "surName":"Андреевич", "points":227}
Creature_bd.add_students(studentDictionary)

studentDictionary = {'lastName':"Каштаєв", 'name': "Артур",  "surName":"Віталійович", "points":225}
Creature_bd.add_students(studentDictionary)

studentDictionary = {'lastName':"Тараканов", 'name': "Сергiй",  "surName":"Михайлович", "points":200}
Creature_bd.add_students(studentDictionary)

studentDictionary = {'lastName':"Стрельченко", 'name': "Дмитро",  "surName":"Олександрович", "points":164}
Creature_bd.add_students(studentDictionary)

# Удалить студентов у которых рейтинг рейтинг меньше заданного значения (любое число)
Creature_bd.delStudents()

# Увеличить в своей записи рейтинг на 5 ед.
Creature_bd.setStudent_add_points(5)

# Вывести всех студентов у которых рейтинг больше чем у вас.
Creature_bd.selectStudents()