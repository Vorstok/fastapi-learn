from pydantic import BaseModel, Field, EmailStr, ConfigDict

data = {
    "email": "abc@mail.ru",
    "bio": "Я человек",
    "age": 12,
}

data_wo_age = {
    "email": "abc@mail.ru",
    "bio": "Я человек",
    "gender": "male",
    "birthday": "2022"
}


class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=10)


class UserAgeSchema(UserSchema):
    age: int = Field(ge=0, le=130)


print(repr(UserSchema(**data_wo_age)))
# print(repr(UserAgeSchema(**data)))
