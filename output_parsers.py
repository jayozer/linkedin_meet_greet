""" Pydantic is a data validation and settings management library in Python. Here's a concise explanation based on the provided search results:

• Pydantic is a library that provides data validation and settings management using Python type annotations. It allows you to define data schemas using Python data types and validate input data against these schemas [1,2].
• With Pydantic, you can create data models by defining classes with attributes that specify the expected data types. Pydantic then automatically validates and converts input data to match these defined models [1,2].
• Pydantic is commonly used for tasks like data validation, serialization, and deserialization in Python applications. It helps ensure that the data your application receives is of the correct type and structure, making your code more robust and reliable [1,2].
• Pydantic is known for its simplicity, performance, and integration with popular Python frameworks and libraries. It is widely used in various Python projects for handling data validation and management tasks efficiently [1,2].

In summary, Pydantic is a powerful Python library that simplifies data validation and settings management by leveraging Python type annotations and providing an intuitive way to define and validate data models.

We created a Pydantic output parser which simply defines the schema of the output that we want, and we define the class that had the attributes of summary,
of interesting_facts, so it has the schema that describing what the output we want.

This is the formal Pydantic schema to represent the output we want the LLM to return us

"""

from typing import List, Dict, Any
from langchain.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field


class Summary(BaseModel):
    summary: str = Field(description="summary")
    facts: List[str] = Field(description="interesting facts about them")

    def to_dict(self) -> Dict[str, Any]:
        return {"summary": self.summary, "facts": self.facts}


summary_parser = PydanticOutputParser(pydantic_object=Summary)
