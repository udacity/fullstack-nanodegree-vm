from app import app

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument(
    '-c', '--clean', help='Use this to clean up the database.', action="store_true")
parser.add_argument(
    '--with-data', help='Use this to initialize the app with data.', action="store_true")
parser.add_argument(
    '--with-no-data', help='Use this to create database tables for the app with no items data.', action="store_true")
parser.add_argument(
    '-p', '--port', help='Provide a port to launch the app.', type=int, default=80)

args = parser.parse_args()

if args.clean:
    os.system("rm udacity_catalog.db")

if args.with_data:
    from app import create_catalog_with_tems_db
elif args.with_no_data:
    from app import create_catalog_no_items_db

if args.with_data is not True and args.with_no_data is not True and args.clean is not True:
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=args.port)
        app.run(debug=True)
