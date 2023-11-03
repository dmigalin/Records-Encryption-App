
import requests
import random
from string import digits, ascii_letters

from config import TextSchemaCreateMaxLength as TSCML


http = 'http://app:8000'
record = "".join(random.choices(digits+ascii_letters,k=TSCML+50))
object_id = ""
password = ""


def test_create_overlength_record():
    res = requests.get(http + '/get_record/',params={
        "object_id":'652d72688d332442dfe92c1e',"password":record})
    assert res.status_code == 404
    assert eval(res.text) == {"detail":"Text with this ID does not exsist."}


def test_get_record_wrong_data():
    res = requests.get(http + '/get_record/',params={
    "object_id":record[0:24],"password":record})
    assert res.status_code == 500


def test_create_record():
    global object_id
    global password
    res = requests.post(http + '/create_record/', json={"text":record[0:TSCML]})
    assert res.status_code == 200
    res = eval(res.text)
    assert type(res['object_id']) == str
    assert type(res['password']) == str
    object_id = res['object_id']
    password = res['password']    
    res = requests.get(http + '/get_record/',params={
        "object_id":object_id,"password":password})
    assert record[0:TSCML] == res.text


def test_wrong_password():
    res = requests.get(http + '/get_record/',params={
        "object_id":object_id,"password":"123"})
    assert res.status_code == 404
    assert eval(res.text) == {"detail":"Wrong Password."}
