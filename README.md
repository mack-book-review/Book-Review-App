# Book Review App

![App Preview](/screenshot.png "user interface")

![App Preview](/screenshot2.png "user interface")


A sample website where users can log in, view a book catalog, and write reviews for different books.  Three tiers of permissions exist for authenticated users.  Admins are authorized to CRUD the book catalog itself.  Registered users are authorized to write reviews for a book in the catalog.  Regular visitors are allowed to view the catalog and read the reviews left by other users.

## Admin Permissions

Allowed to perform CRUD operations on the Book Catalog (i.e. create, read, update, and delete) books in the catalog as well as write reviews.

## Authenticated User Permissions

Allowed to leave book reviews for any book in the catalog.

## Non-Authenticated Users

Allowed to view informaiton for books and authors in the database as well as to read reviews left by registered users.

*** 

## Models

Two models are used for storing data: *BookReview* and *Book*.  A Book simply stores a title, author name, and description for a book in the catalog.  A BookReview, by contrast, stores the title, text, book (foreign key), and user (foreign key) for book review left by a specific user for a specific book.

## Views

View a catalog showcasing all books in the app.  Click on an individual book item to see book detail information along with user reviews for that specific book.  In addition, an authenticated user can see all of their reviews on their homapage, which functions as a user profile dashboard.

