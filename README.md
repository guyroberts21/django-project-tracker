## Steps to create new project

### 1. Create Virtual Environment in Python
`virtualenv venv`

### 2. Save project workspace on VSCode
- This stores any configurations you might want to have persistent when working across multiple machines or with other developers. 

### 3. Install project packages via requirements

`python -m pip install -r src/requirements.txt`

### 4. Create a src/ directory and add any files accordingly here

### 5. Use Django to start the project
`django-admin startproject <projectName> .`

### 6. Add the folders local-cdn/static to the main directory

### 7. Edit settings.py to include
```python
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

STATIC_ROOT = BASE_DIR.parent / "local-cdn" / "static"
```

### 8. Edit urls.py to reflect:
```python
from django.conf import settings
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    # do not do this in prod
    from django.conf.urls.static import static
    # Try Django
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

### 9. Run the following admin command
- First add the static folder to the src/ directory 

`python manage.py collectstatic`

### 10. Add some basic templates in src/templates 
- Check that everything is working as expected ...

### 11. Install Tailwind CSS

`npm install -D tailwindcss`

### 12. Edit the package.json file to include a script 
Eg. 
```json
{
  "scripts": {
    "dev": "tailwindcss -i src/static/tw/tailwind-input.css -o src/static/css/home-ui.css --watch"
  },
  "devDependencies": {
    "tailwindcss": "^3.4.16"
  }
}

```

### 13. Add folders 

src/static/css

src/static/tw AND src/static/tw/tailwind-input.css

### 14. Run command 

`npx tailwindcss init`
`npm run dev`

AND edit config of tailwind.config.js

`content: ["./src/**/*.{html,js}"],`