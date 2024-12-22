import requests
base_url = "http://5.101.50.27:8000/"


def get_token(user='hermione', password='leviosa'):     # авторизация, получение токена
    creds = {
        'username': user,
        'password': password
    }

    resp = requests.post(base_url + 'auth/login', json=creds)
    return resp.json()["user_token"]


def test_new_company(name='НоваяКомпания', description='чем-то занимается'):    # создание компании
    new_company = {
        'name': name,
        'description': description
    }
    resp = requests.post(base_url + 'company/create', json=new_company)
    return resp.json()


def test_get_list(params_add=None):             # получение списка активных компаний
    list_company = requests.get(base_url + 'company', params=params_add)
    return list_company.json()


def test_new_employee(first_name='Лео', last_name='Петрович', middle_name='ДиКаприо', company_id=12, email='user@example.com'):    # создание сотрудника
    employee = {
        'first_name': first_name,
        'last_name': last_name,
        'middle_name': middle_name,
        'company_id': company_id,
        'email': email,
        'phone': 'string',
        'birthdate': '2024-12-10',
        'is_active': True
    }

    resp = requests.post(base_url + 'employee/create', json=employee)
    return resp.json()


def test_list_employees():             # получение списка сотрудников
    all_employee = requests.get(base_url + 'employee/list/12')
    assert all_employee.status_code == 200


def test_get_employee():               # получение данных о сотруднике по ID
    resp = requests.get(base_url + 'employee/info/11')
    assert resp.status_code == 200


# изменение информации о сотруднике
def test_edit_employee(last_name='Маша', email='gosy@example.com', phone=895959595):
    employee_edit = {
        "last_name": last_name,
        "email": email,
        "phone": phone,
        "is_active": True
    }

    my_headers = {}
    my_headers["user_token"] = get_token()
    resp = requests.patch(base_url + 'employee/change/14',
                          json=employee_edit, headers=my_headers)
    return resp.json()


def test_get_employee_id():
    get_employee_id = requests.get(base_url + 'employee/info/11')
    return get_employee_id.json()
