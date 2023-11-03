from pydantic import BaseModel, constr
from typing import Optional

from config import TextSchemaCreateMaxLength as TSCML


class TextSchemaCreate(BaseModel):
    text: Optional[constr(max_length=TSCML)]


