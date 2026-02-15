TASK 1

Q1: Find an example command injection that prints the content of /etc/passwd file, by just providing input for the sample program.
Answer: one example i concocted using the example docs is. python ping_service.py "1.1.1.1; cat /etc/passwd"

Q2: It has potentially two issues which have led injection to be possible. What are they?
Answer: there is no sanitization or neutralization in the code. The code does check the validity of the request, but it only cheks if its valid for the shell, not if its proper for the use case.

Q3: How can you fix them?
Answer: we can introduce sanitization inside the code. Also, by removing the shell parameter from subprocess.check_output()

Q4: How would you implement either input validation or input sanitisation for this context? What could be better?
Answer: without major alteration to the code we can add a subprocess.run function to the first line of the try block. this way we can check that only proper function calls are made.

Q5: How can you be sure that injection is not possible anymore?
Answer: as we sanitize the input values and only allow ip addresses in this should eliminate command injections in this file


TASK 2

A)
the final SQL string i used was "test@test.com ' OR '1'='1';". Where test email is just as filler the first semicolon stops the first part of the sql string. After that we can input sql logic into the email field. Here we use OR, so the serverside tries both of our queries separately. Last is the logic '1'='1'; this sentence is always true so the serverside automatically returns a user from its database. The password doesn't even matter in this case. that is how we get access to this account {"typ":"JWT","alg":"RS256"}.{"status":"success","data":{"id":1,"username":"","email":"admin@juice-sh.op","password":"0192023a7bbd73250516f069df18b500","role":"admin","deluxeToken":"","lastLoginIp":"","profileImage":"assets/public/images/uploads/defaultAdmin.png","totpSecret":"","isActive":true,"createdAt":"2026-02-15 18:20:20.502 +00:00","updatedAt":"2026-02-15 18:20:20.502 +00:00","deletedAt":null},"iat":1771181149}

B)
First I needed to find the search get request. Then through some googling I found out about the following SQL query GET "/rest/products/search?q='))"-- Here the "'))--" Modifies the internal search thus that it returns all the items inside the datatable. I will put the JSON as a separate file not to clog this one.
