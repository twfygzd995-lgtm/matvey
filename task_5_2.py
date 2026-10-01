# ============ Шаг 1: конфликт в ОДНОМ окружении ============
$ pip install "packaging==24.0"
$ pip install "packaging==21.0"
$ python -c "import packaging; print(packaging.__version__)"

# ============ Шаг 2: изоляция в ДВУХ окружениях ============
$ mkdir project_a project_b
$ python3 -m venv project_a/.venv
$ python3 -m venv project_b/.venv

$ source project_a/.venv/bin/activate
(project_a) $ pip install -q "packaging==21.0"
(project_a) $ python -c "import packaging; print('A:', packaging.__version__)"
(project_a) $ deactivate

$ source project_b/.venv/bin/activate
(project_b) $ pip install -q "packaging==24.0"
(project_b) $ python -c "import packaging; print('B:', packaging.__version__)"
(project_b) $ deactivate

# ============ Шаг 3: сравнение ============
$ diff <(project_a/.venv/bin/pip freeze) <(project_b/.venv/bin/pip freeze)
