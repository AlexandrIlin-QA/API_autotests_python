import pytest
import requests
import json

base_url = "http://130.193.52.217:8003"
user_id = 20

def send_request():
	data = {
  		"credit_target": {
    		"value": "credit_card",
    		"title": "Кредитная карта"
  		},
  		"credit_sum": "130 000",
  		"name": "Тест",
  		"surname": "Тест",
  		"patronymic": "Тест",
  		"email": "test@mail.ru",
  		"phone_number": "78888888888",
  		"gender": {
    		"value": "FEMALE",
    		"title": "Женский"
  		}
	}
	req = requests.post(F"{base_url}/api/form/create/credit_parameters_info?user_id={user_id}", json=data)
	return req

@pytest.mark.parametrize("raw", send_request())
class TestRequests:
	def test_code(self, raw):
		assert json.loads(raw) == "Данные успешно сохранены/изменены на первом этапе", "Ошибка запроса"