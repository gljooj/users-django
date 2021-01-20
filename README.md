# users-django
Pequeno crud de super usuarios django

# Instruções

```python
pip3 install virtualenv
pip3 virtualenv venv
pip install -r requirements.txt
source venv/bin/activate
-----------------------
python manage.py migrate
python manage.py runserver
or
python3 manage.py migrate
python3 manage.py runserver

```
# How to run
Após o migrate e com o runserver.
Vá para o localhost em seu navegador, lá se encontrará o crud, onde você pode cadastrar, editar e excluir os usuarios ou também acessar o admin,
mas para acessar o admin é necessário que o usuario tenha uma senha, o crud foi pensado apenas na listagem e edição dos superusuarios. 

Para acessar o admin é necessário criar um usuario através do terminal usando o comando python.

```
python manage.py createsuperuser
or
python3 manage.py createsuperuser

```

![alt text](https://github.com/gljooj/users-django/blob/master/images_readme/1.jpeg?raw=true)

![alt text](https://github.com/gljooj/users-django/blob/master/images_readme/2.jpeg?raw=true)

![alt text](https://github.com/gljooj/users-django/blob/master/images_readme/3.jpeg?raw=true)
