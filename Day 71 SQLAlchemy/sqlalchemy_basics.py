from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Create SQLite database
engine = create_engine("sqlite:///student.db", echo=True)

Base = declarative_base()

# Define Table
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    course = Column(String)

# Create table
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Insert Data
student = Student(name="Chakri", course="Python")

session.add(student)
session.commit()

# Retrieve Data
students = session.query(Student).all()

print("\nStudent Records:\n")

for student in students:
    print(student.id, student.name, student.course)