from pydantic import BaseModel, Field, field_validator

class PredictionDTO(BaseModel):
    email: str = Field(examples=["This is a spam email"], min_length=2, max_length=50)

    @field_validator('email')
    def email_must_contain_spaces(cls, value):
        if ' ' not in value:
            raise ValueError('must contain a space')
        return value.title()
