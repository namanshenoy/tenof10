# READ THIS:<br />
=============

So here is a basic starter project for tenof10 with csv file included.

If you would like to edit this i can make you a contributor but you HAVE TO MAKE YOUR OWN BRANCH.

You also would need to setup a postresql server with psycopg2, you can modify database server settings in tenof10/settings.py

If you want to learn more / get started playing around with this then either contact me or checkout some sources such as [thenewboston Django Tutorial Series](https://youtu.be/qgGIqRFvFFk?list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK) or this online all you ever need [Djangobook](http://djangobook.com/)

All html files go into Templates folder. All other files (IMGS, FONTS, CSS, JS, ...) will go into a Static folder

There is a database file for default sqlite called db.sqlite3, the use of this is commented out in tenof10/settings.py

The script for parsing the CSV and pushing to server is located at scripy.py

Functions for running the server, creating a new webapp (which we shouldn't need anytime soon), creating a new superuser for admin panel, and using the python interpreter within django can all be accessed with manage.py

Happy Coding :)
-- Corey
