1. Клонировать репозиторий 
git clone https://github.com/IlyaPodlesnyj/pjtx4.git
cd pjtx4

2. Создать и активировать виртуальное окружение
python3 -m venv myenv
source myenv/bin/activate

3. Установить зависимости
pip install -r requirements.txt

4. Установить и настроить PostgreSQL
sudo -u postgres psql

Внутри psql выполнить:

CREATE DATABASE testdb;
CREATE USER testuser WITH PASSWORD 'testpassword';
GRANT ALL PRIVILEGES ON DATABASE testdb TO testuser;
\c testdb
ALTER SCHEMA public OWNER TO testuser;
GRANT ALL PRIVILEGES ON SCHEMA public TO testuser;
ALTER USER testuser SET search_path TO public;
\q

5. Запускаем сервер 
python manage.py migrate
python manage.py runserver

   Открыть в браузере:

   http://127.0.0.1:8000/
