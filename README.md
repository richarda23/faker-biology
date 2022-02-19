# faker-biology
Biology-related fake data provider for Python Faker

Some providers for biology-related concepts and resources.

Usage:

Standard code to access Faker
```python
    from faker import Faker
    fake = Faker()
```
from faker_biology.physiology import CellType, Organ


fake.add_provider(CellType)
fake.add_provider(Organ)

