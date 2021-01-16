
# About
I started this blog for practise after the [Udacity](https://www.udacity.com/) course [Intro to HTML and CSS](https://www.udacity.com/course/intro-to-html-and-css--ud001) while I was in university.

With time, it has evolved, and I switch from a completely static blog, to a dynamic one using [Django](https://www.djangoproject.com/) and [Bootstrap](http://getbootstrap.com).

Dependency management is done using [Pipenv](https://pipenv.pypa.io). 

# Disclaimer
This is a personal blog. The opinions expressed here represent my own and not those of my employer.

# Deploy
In order to add a new blog entry, add it to the file /blog/fixtures/data.json and run:
```
python manage.py loaddata data.json
```

If an entry has to be deleted, remove it from the previously mentioned file, delete the *db.sqlite3* file, run a migrate and run the previous command again.

# Todo
- Add testing
- Upload page on server
- Improve header

# License
[MIT License](LICENSE)