# Wagtail v4111_richtext_mark_demo

Trying out the first section of the [Extending the Draftail Editor](https://docs.wagtail.org/en/stable/extending/extending_draftail.html) Wagtail documentation, on a brand new project generated with `wagtail start`.

Screenshot of how the mark feature appears in the page editor:

![Screenshot of the Wagtail page editor UI with the mark feature displayedin the rich text toolbar](/screenshot.png)

---

## How to run this demo

```sh
pip install wagtail==4.1.1
./manage.py runserver 0:8001
```

Then visit <http://localhost:8001/admin/pages/3/edit/> and log in with the username `admin` and password `changeme`.
