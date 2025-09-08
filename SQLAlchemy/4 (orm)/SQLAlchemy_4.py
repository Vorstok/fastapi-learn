from sqlalchemy import BigInteger, ForeignKey, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)


class AbstractModel(DeclarativeBase):
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)


class UserModel(AbstractModel):
    __tablename__ = "users"
    user_id: Mapped[int] = mapped_column(
        BigInteger
    )  # если id большое(как в телеграмм), то используем BigInteger
    name: Mapped[str] = mapped_column()
    fullname: Mapped[str] = mapped_column()


class AddressModel(AbstractModel):
    __tablename__ = "addresses"
    email: Mapped[str] = mapped_column(nullable=False)
    user_id = mapped_column(ForeignKey("users.id"))


with Session(engine) as session:
    with session.begin():
        AbstractModel.metadata.create_all(engine)
        user = UserModel(user_id="1", name="Vsevolod", fullname="Vsevolod")
        session.add(user)
    with session.begin():
        res = session.execute(select(UserModel).where(UserModel.user_id == 1))
        user_res = res.scalar()
        print(user_res.fullname)