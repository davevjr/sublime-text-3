#*=============================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	Remove Migrations Folder
#*=============================== #
import os, os.path
import sys
import shutil


base = "/sys/centerstack/projects/cave/site"
apps = [
	"classes",
	"files",
	"inventory",
	"members",
	"pos",
	"preferences",
	"reservations",
]

for app in apps:
	migrations = os.path.join(base,"apps", app, "migrations")
	if os.path.exists(migrations):
		shutil.rmtree(migrations)
		print "Migrations Removed: %s" % app

		
db = os.path.join(base, "db.sqlite3")
if os.path.exists(db):
		os.remove(db)
		print "SQLite3 Database Removed\n\n"


