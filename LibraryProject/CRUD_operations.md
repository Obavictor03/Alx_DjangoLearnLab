# Django Shell CRUD Operations Documentation

This document summarizes all CRUD operations performed on the Book model using the Django shell.

---

## CREATE
Created a Book instance with:
- Title: "1984"
- Author: "George Orwell"
- Publication Year: 1949  
The book was successfully saved in the database.

---

## RETRIEVE
Retrieved the book instance just created.  
All attributes (title, author, publication year) were successfully displayed.

---

## UPDATE
Updated the title of the book from "1984" to "Nineteen Eighty-Four".  
The changes were successfully saved in the database.

---

## DELETE
Deleted the book instance.  
Confirmed deletion by retrieving all books — the database returned an empty set.
