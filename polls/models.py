from django.db import models
from mongoengine import *

class Choice(Document):
    choice_text = StringField(max_length=200)
    votes = IntField(default=0)

class Poll(Document):
    question = StringField(max_length=200)
    pub_date = DateTimeField(help_text='date published')
    choices = ReferenceField(Choice)

    


# from polls.models import *

# In [2]: from datetime import datetime

# In [3]: P = Poll(question="First question", pub_date=datetime.now())

# In [4]: P.save()
# Out[4]: <Poll: Poll object>

# In [5]: C = Choice(choice_text="First choice", votes=1)

# In [6]: P.choices.append(C)

# In [7]: P.save()
# Out[7]: <Poll: Poll object>
