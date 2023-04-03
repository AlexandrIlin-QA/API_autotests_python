import pytest
import requests
import json

base_url = "http://130.193.52.217:8003"
user_id = 20

def send_request():
	data = {
  		"user_agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0",
  		"phone_number": "78888888888",
  		"checkin_page": "https://sobank.online/",
  		"sms_code": "2587"
	}
	req = requests.post(F"{base_url}/api/form/create/auth_info?user_id={user_id}", json=data)
	return req

@pytest.mark.parametrize("raw", send_request())
class TestRequests:
	def test_code(self, raw):
		assert json.loads(raw) == "Данные успешно сохранены/изменены на нулевом этапе", "Ошибка запроса"