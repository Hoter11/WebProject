
[![Website](https://img.shields.io/website?url=https%3A%2F%2Fhoter11.eu.pythonanywhere.com%2F)](https://hoter11.eu.pythonanywhere.com/)
[![License: MIT](https://img.shields.io/badge/license-MIT%20License-blue.svg)](https://github.com/Hoter11/WebProject/blob/master/LICENSE)

# About
I started this blog for practise after the [Udacity](https://www.udacity.com/) course [Intro to HTML and CSS](https://www.udacity.com/course/intro-to-html-and-css--ud001) while I was in university.

With time, it has evolved, and I switch from a completely static blog, to a dynamic one using [Django](https://www.djangoproject.com/) and [Bootstrap](https://getbootstrap.com). Currently the site is hosted on [Python Anywhere](https://eu.pythonanywhere.com).

Dependency management is done using [Pipenv](https://pipenv.pypa.io). 

# Disclaimer
This is a personal blog. The opinions expressed here represent my own and not those of my employer.

# Deploy
In order to add a new blog entry, add it to the file /blog/fixtures/data.json and run:
```
python manage.py loaddata data.json
```

For updates and deletes, modify the file /blog/fixtures/data.json and run:
```
rm db.sqlite3
python manage.py migrate
python manage.py loaddata data.json
```

# Todo
- Add testing
- Improve header

# License
[MIT License](LICENSE)