# Lab 3 - Foreign Keys and Simple SQL

Introduction to Database Systems, Alexandria National University, Fall 2026.

## Contents
| File | Purpose |
|---|---|
| `problem1_DDL.sql` | COMPANY database: tables, primary keys, foreign keys |
| `problem1_DML.sql` | Sample rows (4 employees, 3 departments, 3 projects) |
| `problem1_Answers.txt` | SQL and output/error for Q1.1 - Q1.3 |
| `problem2_DDL.sql` | LIBRARY database (AUTHOR, BOOK, `ON DELETE CASCADE`) |
| `problem2_DML.sql` | Seed data: 3 authors, 6 books |
| `website/` | Flask website (Lab 2 website + the new CRUD pages) |

## Requirements
- Python 3.9+
- MySQL 8.0.16+ (needed for `CHECK` constraints) and the `mysql` client

## How to run

### Problem 1
```bash
mysql -u root -p < problem1_DDL.sql
mysql -u root -p < problem1_DML.sql
mysql -u root -p company        # type the queries of problem1_Answers.txt by hand
```

### Problem 2 (database + website)
1. Build the database (DDL first, then DML):
   ```bash
   mysql -u root -p < problem2_DDL.sql
   mysql -u root -p < problem2_DML.sql
   ```
2. Install the dependencies:
   ```bash
   cd website
   pip install -r requirements.txt
   ```
3. Set your MySQL password as an environment variable (it is never stored in the code):
   - Windows PowerShell: `$env:DB_PASSWORD="your_password"`
   - Windows CMD: `set DB_PASSWORD=your_password`
   - Linux / macOS: `export DB_PASSWORD="your_password"`

   Optional variables: `DB_HOST` (default `localhost`), `DB_USER` (default `root`), `DB_NAME` (default `library`).
4. Start the website:
   ```bash
   python app.py
   ```
5. Open http://127.0.0.1:5000

## Website features
- **F2.1** Show the authors table and the books table (with `author_id`)
- **F2.2** Add an author / add a book
- **F2.3** Edit an author / edit a book (inline, press Save)
- **F2.4** Remove a book
- **F2.5** Remove an author (their books are deleted too, by `ON DELETE CASCADE`)
- **Bonus** Upload a photo for each author and a cover for each book (png, jpg, gif, webp; max 2 MB).
  Images are stored in `website/static/uploads/` (created automatically); the database keeps only the file name.
