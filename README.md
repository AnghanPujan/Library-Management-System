# 📚 Django Library Management System  

## 🎯 Objective  
A web-based Library Management System built with **Django** (without DRF).  
This project manages **Books, Authors, Members, and Borrow/Return functionality** with dashboards and reports.  

---

## 🚀 Features  

### ✅ Book & Author Management  
- CRUD for Books (Add, Update, Delete).  
- Fields: `title`, `id` (pk,unique), `category`, `is_available`, `author_if`(fk) ,`member_id`(fk), `issue_date` , `due_date` , `return_Date`.  
- Each Book → One Author; Author → Many Books.    

### ✅ Member Management  
- Manage members with: `id`(pk),`name`, `email` (unique), `join_date`.  
- Each member can borrow multiple books(Max=5).  
- A book can only be borrowed by **one member at a time**.  

### ✅ Borrow & Return  
- Borrow Book:  
  - Set `is_available = False`.  
  - Store `issue_date` and `due_date` (`issue_date + 14 days`).  
  - Limit: Max **5 books per member**.  
- Return Book:  
  - Set `is_available = True`.  
  - Calculate fine = ₹10/day after `due_date`.  
  - Display fine on confirmation.  

### ✅ Filters    
- Show overdue books (past `due_date`, not returned).  

### ✅ Reports & Dashboard  
- Dashboard (`/`) shows:  
  - Total Books  
  - Total Members  
  - Borrowed Books  
  - Overdue Books  

## 🛠 Tech Stack  

- **Django** (ORM, no DRF)  
- **SQLite** (default DB)  
- **Bootstrap / Minimal CSS**   

---

## 🗂 Data Model  

- **Author** → `name`  
- **Book** → `title`, `id`, `category`, `is_available`,`member_id`(FK), `author_id (FK)`,`issue_date` , `due_date` , `return_date`  
- **Member** →`id`, `name`, `email`, `join_date`   

---

## 📌 URLs  

| URL | Page | Description |
|-----|------|-------------|
| `/` | Dashboard | Overview page |
| `/books/` | Book List | Browse & search books |
| `/books/add/` | Add Book | Create new book |
| `/books/<id>/edit/` | Edit Book | Update book info |
| `/books/<id>/delete/` | Delete Book | Remove book |
| `/members/` | Members | Member list |
| `/members/add/` | Add Member | Create member |
| `/borrow/` | Borrow | Borrow book form |
| `/return/` | Return | Return borrowed book |
| `/reports/overdue/` | Overdue | List overdue books |

---

## ⚙️ Setup Guide  

1. Clone repo:  
   ```bash
   git clone https://github.com/your-username/library-management-django.git
   cd library-management-django

2. Create virtual environment & install dependencies:
    ```bash
    python -m venv env
    source env/bin/activate  
    pip install -r requirements.txt

3. Run migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate

4. Create superuser:
    ```bash
    python manage.py createsuperuser

5. Start server:
    ```bash
    python manage.py runserver

6. Access:
    ```bash
    App → http://127.0.0.1:8000/
    Admin → http://127.0.0.1:8000/admin/








