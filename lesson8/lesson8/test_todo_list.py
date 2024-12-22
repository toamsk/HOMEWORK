import requests
base_url = "https://todo-app-sky.herokuapp.com/"


def test_create():            # создание задания
    new_task = {
        'title': 'готовиться к собеседованию',
        'completed': False
    }

    resp = requests.post(base_url, json=new_task)
    global task_id
    task_id = resp.json()


def test_rename():            # редактирование задания
    rename_task = {
        # 'title': task_id['title'] + 'ghghghghgh'
        'title': 'готовить еду'
    }

    resp = requests.patch(base_url + str(task_id['id']), json=rename_task)
    assert resp.status_code == 200


def test_get_task():         # Получение конкретной задачи из списка
    resp = requests.get(base_url + str(task_id['id']))
    assert resp.status_code == 200


def test_get_task():         # Получение списка
    resp = requests.get(base_url)
    assert resp.status_code == 200


def test_mark_complet():     # Отметка задачи «Выполнена»
    mark_comp = {
        'completed': True
    }

    resp = requests.patch(base_url + str(task_id['id']), json=mark_comp)
    assert resp.status_code == 200


def test_unmarking_completed():  # Снятие отметки «Выполнена»
    unmarking_comp = {
        'completed': False
    }

    resp = requests.patch(base_url + str(task_id['id']), json=unmarking_comp)
    assert resp.status_code == 200


def test_del_task():    # Удаление
    resp = requests.delete(base_url + str(task_id['id']))
    assert resp.status_code == 200
