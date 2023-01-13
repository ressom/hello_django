## Purpose
* To explore and learn about python / Django framework
* To build some functionality
* To help land a job

## Dependencies
- See [requirements.txt](./requirements.txt)
- NodeJS >=12 (for [django-tailwind](https://django-tailwind.readthedocs.io))

## HowTo Run
 - Check out the project
 - At a command prompt run `make superuser`
   - This will install dependencies into `./.venv`, create an empty local dB, run migrations, and prompt to create the `admin` user
 - At a command prompt run `make run`
   - This will start server processes
 - Login as Superuser - [http://127.0.0.1:8000/admin/login/](http://127.0.0.1:8000/admin/login/)
 - Create a application User then log out of `admin` account
 - Login as application User - [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Project Task Checklist
- [X] Initial GIT/GH project setup
- [X] Initial Python/Django setup
- [X] Admin portal bootstrapped
- [ ] Make something useful

### Useful Links
- Django Crash Course - Caleb Curry - https://www.youtube.com/watch?v=EuBQU_miReM
- Django Docs - https://docs.djangoproject.com/
- Django Tutorials - https://learndjango.com/
- MDN Django Docs - https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django
- Project structure - https://docs.python-guide.org/writing/structure/
- Environments - https://code.visualstudio.com/docs/python/environments
- Dependency management
  - https://www.mend.io/free-developer-tools/blog/python-dependency-management/
  - https://learnpython.com/blog/python-requirements-file/
- Tailwind for Django - https://django-tailwind.readthedocs.io/en/latest/installation.html
- Tailwind Docs - https://tailwindcss.com/docs/utility-first
- Makefile - https://earthly.dev/blog/python-makefile/#using-make-with-python