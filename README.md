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

