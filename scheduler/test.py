import json

import requests
import random
from string import digits, ascii_letters

http = 'http://app:8000'

def create_record():
    record = "".join(random.choices(digits+ascii_letters,k=1000))
    res = requests.post(http + '/create_record/', json={"text":record}).text
    res = eval(res)
    assert type(res['object_id']) == str
    assert type(res['password']) == str
    res = requests.get(http + '/get_record/',params={
        "object_id":res['object_id'],"password":res['password']})
    assert record == res.text

create_record()