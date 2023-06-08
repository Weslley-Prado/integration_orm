import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, inspect
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"

    # attributes
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"Address (id={self.id}, email={self.email_address})"


print(User.__tablename__)
print(Address.__tablename__)

# connection with database
engine = create_engine("sqlite://")

# create the class with table
Base.metadata.create_all(engine)

inspector_engine = inspect(engine)
print(inspector_engine.has_table("user_account"))
print(inspector_engine.get_table_names())
print(inspector_engine.default_schema_name)
