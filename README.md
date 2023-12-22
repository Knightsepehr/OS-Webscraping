Title: Scraping and Storing Images from StockSnap

Documentation:

Overview
The purpose of this Python Project is to scrape image data ( using main module ) and images from the website StockSnap.io and store the information in a local mysql database ( Using db module ) and show the scraped data using flask ( using webapp module ).

Structure of main.py
Imports: Necessary modules like BeautifulSoup, requests, threading, and cloudscraper are imported.

Global Variables: The global variables such as database_name, proxies, and headers are defined.

Functions: The functions in this script include req(), get_cats(), get_image_links(), getSearchLinks(), get_image_data(), download_image(), do_job(), and get_all_images().

Job Class: The Job class is defined to represent each scraped image. It has attributes such as title, description, url, img_url, author, views, downloads, img_id, res, lic, and cat.

category Class: The category class is defined to represent each category. It has attributes such as name and page_link.

Database Functions: Functions like create_database(), connection(), try_sql_query(), and close_connection() are used to manage the SQLite database.

Main Function: The get_all_images() function is the main function that is executed when the script is run. It calls the necessary functions to scrape image data and images from the StockSnap website and store them in the SQLite database.

Steps
The get_cats() function is called to fetch all the categories from the StockSnap website.

The getSearchLinks() function is called to create search links for each category.

The get_image_links() function is called to fetch all the image links from each category.

The get_image_data() function is called to fetch detailed data about each image from the StockSnap website.

The download_image() function is called to download each image and save it in a local folder named "static".

The do_job() function is called to perform the database operations, including inserting the image data and downloading the image.

Finally, the get_all_images() function is called to execute the entire process.

Additional Information
This script uses cloudscraper, which is a Python module used to scrape websites bypassing their Cloudflare protection.

It also utilizes the BeautifulSoup module to parse the HTML content and extract the necessary data.

To improve performance, the script uses threading to scrape and download images simultaneously.


Structure of db.py:
This code provides a Python module that interacts with a MySQL database to create tables, execute SQL queries, and perform CRUD operations on the data. The module defines the following functions:

connection(database_name): This function establishes a connection to the MySQL database. It takes a string database_name as input, which represents the name of the database to connect to.

close_connection(connection): This function closes the MySQL database connection. It takes a connection object as input.

try_execute(connection,sql_query): This function executes a given SQL query. It takes a connection object and a string sql_query as inputs. If an error occurs while executing the query, the error message is printed.

create_database(database_name): This function creates a new MySQL database. It takes a string database_name as input. If the database already exists, the function does nothing.

try_sql_query(connection, title, description, url, img_url, author, views, downloads, license, resolution, category, img_id): This function inserts a new record into the MySQL database. It takes a connection object and 13 other parameters as inputs. If an error occurs while executing the SQL query, the error message is printed.

To use this module, you need to import it in your Python script or interactive shell.


Structure of webapp.py

In this code, a Flask application is created. The Flask application serves as the backend of the web application. It establishes a connection to the database using the connection function from the db module.

The query function is defined to interact with the database. It fetches all the rows from the image2 table and returns them.

The jobs variable stores the result of the query function, which are the rows fetched from the image2 table.

The Flask application's main route (/) is defined by the index function. When a user accesses the main route, the index function is executed. It renders the index.html template and passes three arguments to it: the title of the webpage, which is set to "Home"; and the jobs data fetched from the database.

Finally, the app.run() function is called to start the Flask application. The application runs on the local machine and can be accessed by opening a web browser and navigating to http://127.0.0.1:5000/.

In the index.html template, the jobs data is used to generate a list of jobs. The title variable is used to set the title of the webpage.