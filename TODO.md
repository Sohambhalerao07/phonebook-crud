# TODO: Add UI for Contacts Project

- [x] Update core/settings.py to include templates directory in TEMPLATES['DIRS']
- [x] Create templates directory structure: templates/contacts/
- [x] Add function-based views in contacts/views.py for web UI: contact_list, contact_create, contact_update, contact_delete
- [x] Update core/urls.py to include paths for web views (e.g., '', 'add/', '<int:pk>/edit/', '<int:pk>/delete/')
- [x] Create base.html template with Bootstrap CDN
- [x] Create contact_list.html template for listing contacts with links to add/edit/delete
- [x] Create contact_form.html template for add/edit forms
- [x] Test the UI by running the server and checking the pages
