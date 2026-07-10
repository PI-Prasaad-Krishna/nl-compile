export const syntaxSections = [
  {
    id: "installation",
    title: "0. Installation",
    description: "NL is built on top of Python. You can install the interpreter globally on any Operating System (Windows, macOS, Linux) directly via pip. Once installed, simply type `nl <filename>.nl` in your terminal to run a script, or just `nl` to start the interactive REPL!",
    code: `pip install git+https://github.com/PI-Prasaad-Krishna/nl-compile.git`
  },
  {
    id: "variables",
    title: "1. Variables",
    description: "Variables are dynamically typed and can be created or updated using the `set` and `to` keywords. You can optionally use `create variable <name> and set it to <value>` for a more verbose sentence.",
    code: `create variable x and set it to 10\nset y to 20`
  },
  {
    id: "math",
    title: "2. Mathematics and Arithmetic",
    description: "Math is done using English words (`plus`, `minus`, `times`, `divided by`) rather than symbols (`+`, `-`, `*`, `/`). Standard order of operations (PEMDAS) applies automatically.",
    code: `set result to 5 times 10\nset z to x plus y`
  },
  {
    id: "strings",
    title: "3. Strings & Concatenation",
    description: "Text is enclosed in quotes. You can combine strings together, or combine strings with variables, using the `plus` keyword.",
    code: `set greeting to "Hello " plus "World"\nprint greeting`
  },
  {
    id: "printing",
    title: "4. Printing",
    description: "To output a value to the terminal, simply use the `print` keyword. You can string multiple expressions together by placing them next to each other.",
    code: `print "Execution completed!"\nset name to "Prasaad"\nprint "Hello" name`
  },
  {
    id: "logic",
    title: "5. Conditionals (If Statements)",
    description: "NL supports boolean logic using conversational comparators: `is greater than`, `is less than`, `is equal to`, `contains`. Chain conditions using `and` and `or`.",
    code: `set age to 18\nif age is greater than 10 then do\n    print "You are old enough!"\nend`
  },
  {
    id: "loops",
    title: "6. Loops",
    description: "Execute valid statements repeatedly using `loop till`, `while`, or `for each` for lists.",
    code: `set count to 0\nwhile count is less than 5 do\n    set count to count plus 1\n    print count\nend`
  },
  {
    id: "actions",
    title: "7. Actions (Functions)",
    description: "You can define reusable blocks of code called `actions`. Actions create their own local scope (memory environment).",
    code: `define action double with x and do\n    return x times 2\nend\n\nset result to run double with 10\nprint result`
  },
  {
    id: "data-structures",
    title: "8. Data Structures",
    description: "Group items together into Lists or Key-Value Objects using a highly conversational syntax.",
    code: `create list colors containing "red", "blue", "green"\nprint item 1 of colors\n\ncreate object user containing "name" as "Prasaad"`
  },
  {
    id: "string-manipulation",
    title: "9. String Manipulation",
    description: "Perform complex text operations using natural conversational expressions.",
    code: `print length of "Hello"\nprint uppercase "hello"\nprint replace "bad" with "good" in "this is a bad idea"\nset words to split "a,b" by ","`
  },
  {
    id: "file-io",
    title: "10. File I/O",
    description: "Read and write directly to your local file system natively.",
    code: `write "Hello File System" into file "data.txt"\nset file_content to read file "data.txt"\nprint file_content`
  },
  {
    id: "interactive",
    title: "11. User Input",
    description: "You can pause the script, prompt the user for input, and save the result dynamically.",
    code: `ask "What is your name? " and set it to name\nprint "Welcome, " plus name`
  },
  {
    id: "errors",
    title: "12. Error Catching",
    description: "Prevent your scripts from crashing by catching runtime errors.",
    code: `try to do\n    print 10 divided by 0\nend but if it fails do\n    print "Caught a math error!"\nend`
  },
  {
    id: "time",
    title: "13. Time & Flow Control",
    description: "You can pause your scripts or fetch timestamps dynamically.",
    code: `set start to get current time\nwait for 5 seconds\nprint "Waited"`
  },
  {
    id: "shell",
    title: "14. Shell Execution",
    description: "You can run shell commands natively and capture their output directly into a variable!",
    code: `set output to execute command "dir" in terminal\nprint output`
  },
  {
    id: "web",
    title: "15. Web & API Requests",
    description: "You can fetch data directly from the internet natively without importing any libraries!",
    code: `set data to fetch from "https://api.example.com/data"\nprint data`
  },
  {
    id: "modules",
    title: "16. Modules & Multi-File Projects",
    description: "You can import other `.nl` files to use their predefined variables and actions.",
    code: `include "math_helpers.nl"\nrun double_number with 10`
  },
  {
    id: "type-conversions",
    title: "17. Type Conversions & JSON",
    description: "Dynamically cast data between text, numbers, and JSON objects!",
    code: `set num to convert "100" to number\nset person to parse json from '{"name": "Alice"}'\nset text to convert person to json`
  },
  {
    id: "ui",
    title: "18. Native UI Graphical Dialogs",
    description: "You can spawn native OS alert boxes and input prompts!",
    code: `show alert "Your script has finished running!"\nprompt user with "Enter password:" and set it to pass`
  },
  {
    id: "secrets",
    title: "19. System Secrets",
    description: "Securely read environment variables from your OS.",
    code: `set api_key to get secret "GITHUB_TOKEN"`
  },
  {
    id: "string-matching",
    title: "20. Advanced String Matching",
    description: "Check prefixes, suffixes, or use wildcards to match patterns!",
    code: `if email matches pattern "*@*.com" then print "Valid!"\nif name starts with "Mr." then print "Hello"`
  },
  {
    id: "oop",
    title: "21. Object-Oriented Templates",
    description: "Enforce rigid blueprints for the objects you create.",
    code: `define template Car with "make", "model", "year"\ncreate Car ride with "Toyota", "Corolla", 2015`
  },
  {
    id: "concurrency",
    title: "22. Concurrency (Background Tasks)",
    description: "Run heavy logic in the background so your main script doesn't freeze.",
    code: `run in background do\n    wait for 5 seconds\n    print "Done in background!"\nend`
  },
  {
    id: "filesystem",
    title: "23. File System Management",
    description: "Create folders, read folder directories, and delete files automatically.",
    code: `create folder "images"\nset files to get files in folder "images"\ndelete file "temp.txt"`
  },
  {
    id: "math-adv",
    title: "24. Math and Randomness",
    description: "You can quickly generate random variables and round decimals natively.",
    code: `set num to get random number between 1 and 10\nset clean to round 3.14 to nearest integer`
  }
];
