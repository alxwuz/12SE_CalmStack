# SOFTWARE ENGINEERING PROJECT DOCUMENTATION TEMPLATE {#software-engineering-project-documentation-template}

---

## RATIONALE {#rationale}

This documentation template is designed to help you complete **Component A – Project Documentation** of your Software Engineering Year 12 Personal Project.

**The template supports the four required stages from the syllabus:**

* Identifying and Defining

* Research and Planning

* Producing and Implementing

* Testing and Evaluating

**It also includes essential modelling tools (which are EXAMINABLE in the HSC\!):**

* Context Diagram

* Data Flow Diagrams (DFDs)

* Structure Chart

* IPO Chart

* Data Dictionary

* UML Class Diagram (if OOP)

---

## TITLE PAGE {#title-page}

**Project Title:** CalmStack  
**Student Name:** Alex Wu  
**Course:** Software Engineering Stage 6  
**GitHub URL (if applicable):** [GitHub](https://github.com/alxwuz/12SE_CalmStack)	

Table of Contents

[SOFTWARE ENGINEERING PROJECT DOCUMENTATION TEMPLATE	1](#software-engineering-project-documentation-template)

[RATIONALE	1](#rationale)

[TITLE PAGE	2](#title-page)

[Syllabus Requirements	5](#syllabus-requirements)

[1\. Identifying and Defining	7](#1.-identifying-and-defining)

[1.1 Problem Statement	7](#1.1-problem-statement)

[1.2 Project Purpose and Boundaries	7](#1.2-project-purpose-and-boundaries)

[1.3 Stakeholder Requirements	7](#1.3-stakeholder-requirements)

[1.4 Functional Requirements	7](#1.4-functional-requirements)

[1.5 Non-Functional Requirements	7](#1.5-non-functional-requirements)

[1.6 Constraints	7](#1.6-constraints)

[1.7 Requirements Analysis and Prioritisation	8](#1.7-requirements-analysis-and-prioritisation)

[2\. Research and Planning	9](#2.-research-and-planning)

[2.1 Development Methodology	9](#2.1-development-methodology)

[2.2 Tools and Technologies	9](#2.2-tools-and-technologies)

[2.3 Gantt Chart / Timeline	9](#2.3-gantt-chart-/-timeline)

[2.4 Communication Plan	9](#2.4-communication-plan)

[2.5 Resource Allocation Justification	9](#2.5-resource-allocation-justification)

[3\. System Design	10](#3.-system-design)

[3.1 Context Diagram	10](#3.1-context-diagram)

[3.2 Data Flow Diagrams (Level 0 and Level 1\)	10](#3.2-data-flow-diagrams-\(level-1\))

[3.3 Structure Chart	10](#3.3-structure-chart)

[3.4 IPO Chart	10](#3.4-ipo-chart)

[3.5 Data Dictionary	10](#3.5-data-dictionary)

[3.6 UML Class Diagram (if OOP)	10](#3.6-uml-class-diagram-\(if-oop\))

[4\. Producing and Implementing	11](#4.-producing-and-implementing)

[4.1 Development Process	11](#4.1-development-process)

[4.2 Key Features Developed	11](#4.2-key-features-developed)

[4.2.1 Back-End Engineering Contribution	11](#4.2.1-back-end-engineering-contribution)

[4.3 Screenshots of Interface	11](#4.3-screenshots-of-interface)

[4.4 Version Control Summary (Optional)	11](#4.4-version-control-summary-\(optional\))

[5\. Testing and Evaluation	12](#5.-testing-and-evaluation)

[5.1 Testing Methods Used	12](#5.1-testing-methods-used)

[5.2 Test Cases and Results	12](#5.2-test-cases-and-results)

[5.3 Evaluation Against Requirements	12](#5.3-evaluation-against-requirements)

[5.4 Improvements and Future Development	12](#5.4-improvements-and-future-development)

[6\. Feedback, Security and Reflection	13](#6.-feedback,-security-and-reflection)

[6.1 Summary of Client or Peer Feedback	13](#6.1-summary-of-client-or-peer-feedback)

[6.2 Secure Software Design and Data Handling	13](#6.2-secure-software-design-and-data-handling)

[6.3 Personal Reflection	13](#6.3-personal-reflection)

[7\. Appendices	14](#7.-appendices)

## Syllabus Requirements {#syllabus-requirements}

| Syllabus Requirement | Template Section |
| :---- | :---- |
| Identifying problem, feasibility, and requirements | Section 1.1 – 1.6 |
| Stakeholder and client expectations and feedback | Section 1.3, Section 6.1 |
| Functional and non-functional requirements | Section 1.4, 1.5 |
| Project constraints | Section 1.6 |
| Planning methodology and Gantt chart | Section 2.1 – 2.3 |
| Tools and language justification | Section 2.2 |
| Communication with clients and feedback loops | Section 2.4, 6.1 |
| Context Diagram and DFDs | Section 3.1, 3.2 |
| Structure Chart and IPO | Section 3.3, 3.4 |
| Data Dictionary | Section 3.5 |
| UML Class Diagram (if applicable) | Section 3.6 |
| Code implementation and key features | Section 4.1 – 4.2 |
| UI screenshots and explanation | Section 4.3 |
| Version control and iterations (optional) | Section 4.4 |
| Testing methods and test cases | Section 5.1 – 5.2 |
| Evaluation of requirements and software effectiveness | Section 5.3 |
| Suggestions for improvement and future development | Section 6.1 \- 6.3 |
| Analyse and respond to feedback,  evaluate the effectiveness of a software solution | Section 6.2 |

# 

# 1\. Identifying and Defining {#1.-identifying-and-defining}

## 1.1 Problem Statement {#1.1-problem-statement}

**Outline** the problem or opportunity that the project addresses. Consider who is affected by this issue.

The game addresses the problem of individuals in a variety of age groups who do not have access to a quick and accessible minigame to pass time, relieve stress, and build their cognitive skills. For instance, a Year 11 student can use the game during study breaks to reset focus, while a younger users might use it to improve their cognitive function

**Explain** why this problem or opportunity is significant. 

This problem is significant because many people do not have a solution to the three major problems (passing time, relieving stress, and building cognitive skills) that this game solves. These three benefits of playing the game can impact long-term mental and physical health, preventing burnout, maintaining brain efficiency, and improving quality of life. For example, a student playing the game on after school.

**Justify** the development of a software solution as an appropriate response.

This project addresses the need for a more interactive and enjoyable way to improve their health, as well as encouraging thinking skills while doing so.

---

## 1.2 Project Purpose and Boundaries {#1.2-project-purpose-and-boundaries}

**Outline** what the project is trying to achieve. 

The goal of this project is to create a 8x8 2D game similar to that of Tetris, except there are no time limits of the falling blocks. It aims to create a comfortable environment where the user can relax and play the game without any stressful or competitive mechanics.

---

## 1.3 Stakeholder Requirements {#1.3-stakeholder-requirements}

**Identify** stakeholders (client, users, teacher, peers). 

Users of all ages (children, students, adults, the elderly).

**Describe** their needs, expectations, and how these influenced the project direction.

Because the goal of the project was to create a simple but effective game for all age groups, there would need to be a lot of factors to consider. Children and elderly people would need the program to be simple enough to understand, hence why it is a more ‘simplified’ version of Tetris. For students and workers, the game needs to be engaging and fun to play. Overall accessibility such as offline access also needs to be considered.

---

## 1.4 Functional Requirements {#1.4-functional-requirements}

**List** and **describe** what the system must do.

- Have a set list of blocks and colours that can randomly generate  
- Use algorithms to check for completed lines and to add score  
- Recognise user input in the game and respond to it  
- Ability to save logins and user data

---

## 1.5 Non-Functional Requirements {#1.5-non-functional-requirements}

**List** and **describe** system qualities such as: 

* Performance

* Usability

* Security

* Reliability

1. Optimized for all types of devices (consistent FPS, no frame drops, good and fast code)  
2. Easy to use and navigate (accessibility)  
3. Stores all data securely (encryption)  
4. Works offline (portability)

---

## 1.6 Constraints {#1.6-constraints}

**Identify** limitations affecting the project, such as: 

* Time 

* Technical knowledge

* Hardware/software access

The project is limited to approximately a three-month period. However, not all of this will be spent on the project due to external factors. There also will be no paid assets or tools used in the game, and the program will be completed in Python, with videos to help with the development.

---

## 1.7 Requirements Analysis and Prioritisation {#1.7-requirements-analysis-and-prioritisation}

**Analyse** the functional and non-functional requirements. In your analysis, consider: 

* which requirements were prioritised and why, 

* trade-offs made due to constraints, 

* how requirements align with the identified problem or opportunity

The functional and non-functional requirements are both equally important, however the priority of the project is to ensure the core mechanics of the game are able to work well without any game-breaking mechanics, ensuring a good user experience. Because of this, some other minor requirements such as UI might not be as polished, but will still achieve the project’s main functional requirement.

---

# 2\. Research and Planning {#2.-research-and-planning}

## 2.1 Development Methodology {#2.1-development-methodology}

**Describe** the development approach used (e.g. Agile, Waterfall, WAgile).

**Justify** the suitability of this methodology. You could consider… 

* Project size and complexity 

* Time constraints 

* Feedback and iteration requirements

The project will be using the Agile approach, which breaks down the project into different sprints (four in this case). It is ideal for this project as it allows for an iterative development allowing requirements such as the mechanics to be refined as the game progresses.

---

## 2.2 Tools and Technologies {#2.2-tools-and-technologies}

**Justify** the selection of software applications, engines, developer tools, programming languages, IDEs, frameworks, libraries and/or hardware components.

**Language:** Python 3, a developed language with many libraries which is easy to use.

**IDE:** Visual Studio Code. It is the most widely used code editor, with lots of support and beginner friendly tools that make programming easier.

**Libraries:** customtkinter (more improved version of tkinter), json, os, hashlib. These libraries provide the core functionality of the game, allowing for the GUI and encryption.

**Assets:** None

**Explain** how these tools supported efficient and effective development.

These tools help development by giving access to create the game which allows for meeting all functional requirements. Without these tools, many core mechanics of the game would not be able to work.

---

## 2.3 Gantt Chart / Timeline {#2.3-gantt-chart-/-timeline}

Include a timeline showing key project milestones.

[Copy of GANTT CHART TEMPLATE](https://docs.google.com/spreadsheets/d/11NN39W13s-LcuDlV0wZMKY1laYH0ABrM6YrEe3ulm2w/edit?usp=sharing)

**Explain** how time was allocated to planning, development, testing, and evaluation.

Because the project is using an agile methodology, some sprints will be more focused on compared to others. Sprint 2 is going to be the longest in terms of development, as it is targeted towards the core mechanics of the game which will need extra time. Sprint 4 will have the longest review and launch, as it is the final “check” before releasing the program.

---

## 2.4 Communication Plan {#2.4-communication-plan}

**Explain** how client or peer feedback was obtained and incorporated.

Development builds of the game will be sent to peers for feedback. When the user notices an improvement or a bug, it can be submitted and incorporated for the next sprint. For example, if a user encountered a bug where the high scores did not save, the function that does that action will be analysed.

---

## 2.5 Resource Allocation Justification {#2.5-resource-allocation-justification}

**Justify** the resource allocation for the project, including:

* Time

* Software and hardware tools

* Human input (client, peers, teacher feedback)

A lot of time will be spent developing the project, ensuring that everything is functional, as well as planning and testing the build under test cases so there aren’t any unexpected problems that come up which may not be good for the users. Another resource for the project needed is Visual Studio Code and GitHub Desktop, which allows the program to be created and documented as well as saved and kept track of. 

---

# 3\. System Design {#3.-system-design}

This section justifies the use of modelling tools to represent system structure, data flow, and processing logic prior to implementation.

---

## 3.1 Context Diagram {#3.1-context-diagram}

Include a context diagram showing system boundaries and external entities.

![][image1]

---

## 3.2 Data Flow Diagrams (Level 1\) {#3.2-data-flow-diagrams-(level-1)}

Illustrate how data moves through the system.

![][image2]

---

## 3.3 Structure Chart {#3.3-structure-chart}

Show the modular structure of the system and relationships between modules.

![][image3]

---

## 3.4 IPO Chart {#3.4-ipo-chart}

| Input | Process | Output |
| :---- | :---- | :---- |
| username | reads user database from file | updates status on screen (account created or login successful) |
| password | hashes the password/checks the password is valid | when successful, closes login window and opens game UI (or incorrect login) |
| mouse click on sign in | validates credentials or creates a new login | writes the user credentials to users.json |
| mouse click on piece | finds shape from dictionary | selects the piece and waits for user input |
| mouse click on game board (after piece) | converts coordinates from click into the grid positions (gx, gy) checks placement rules for boundary limits and overlapping modifies board on successful move checks for filled horizontal and vertical lines calculates the score (no. of cells \+ cells cleared) checks grid status to see if there are any more moves | visual update of block placed on board removes the piece selected from the generation of blocks randomises 3 more blocks if list is empty clear lines that are filled updates score triggers game over status if no legal moves |
| mouse click on restart button | resets all variables  (score, board,  available pieces, index) saves high score | clears canvas resets score counter new block generation |

---

## 3.5 Data Dictionary {#3.5-data-dictionary}

## 

| Variable | Data Type | Format for Display | Size in bytes | Size for display | Description | Example | Validation |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| username | string | XX..XX | 32 | 20 | name for profile of user | ProGamerShawnyBoi | cannot match an existing user in users.json  |
| password | string | XX..XX | 64 | 20 | user password entered during login or registration | Secret123123123\! | can’t be empty |
| is\_register\_mode | boolean | X | 1 bit | 1 | indicates | Y | Y or N |
| score | integer | NNN | 2 | 3 | total score of game (number of cells placed \+ cleared) | 283 | greater or equal to 0 |
| selected\_piece\_index | integer | N | 2 | 1 | Index of the currently selected piece in the preview row | 2 | integer between 0 and 2, or None |
| board | list | 8x8 coloured matrix  | 8\*8\*7 (grid size and colour) | N/A | 2D grid with hex colour tracking | \#000000 | 8x8 array matrix with elements |
| piece\_colours | list | list of 7 hex colour strings | 10\*7 | N/A | list of different hex colours for block generation | \#000000 | elements must match the hex colour |
| gx | integer | N | 2 | 1 | click coordinates converted to column number | 4 | integer between 0 and 7 |
| gy | integer | N | 2 | 1 | click coordinates converted to row number | 0 | integer between 0 and 7 |

## ---

## 3.6 UML Class Diagram (if OOP) {#3.6-uml-class-diagram-(if-oop)}

Include a class diagram if your project uses an OOP approach.

**Explain** the class structure and relationships.

Game: acts as the blueprint for the game, with generate\_pieces and clear\_lines being abstract methods (other methods like clear\_lines don’t have to be necessary), and also includes the variables needed.

CalmStack: Inherits from the game class, has all the game logic needed.

GameUI: Handles all the GUI needs in the game such as score\_label and board\_canvas, containing methods to draw the board and previews.

LoginUI: Another UI before the GameUI used to authenticate user login. Contains a toggle between both modes and pulls methods from [auth.py](http://auth.py) to hash and create accounts.

CalmStackGame: Connects the logic and visuals, contains handlers like on\_board\_click and more.

CalmStack inherits from Game, while CalmStackGame manages CalmStack. CalmStackGame also starts the LoginUI, and it controls the GameUI, essentially being the main application.

---

# 4\. Producing and Implementing {#4.-producing-and-implementing}

## 4.1 Development Process {#4.1-development-process}

**Describe** how the solution was built and implemented.

The application was developed with an iterative approach in Python, in four different sprints. By planning and developing the project, the core mechanics of the game were built efficiently, ensuring that the program was working.

**Justify** the engineering techniques used, such as:

* Modular design

The project was divided into four different sprints, which serves to reduce the code complexity and system errors, increasing maintainability at the same time. It allowed for the focus of only a few specific features/bug fixes at once, making the project much easier to manage.

* Object-oriented principles 

In the project, many different object-oriented principles were included within the game. This included abstraction, inheritance, etc, which allow for scalability and provides a much more coherent and efficient program.

* Reuse of code 

The reuse of code allowed for the project to be more efficient by allowing pre-existing modules and code blocks to be used in other parts of the program rather than rewriting the same logic. This can minimise human error and increase development efficiency, as shown in load\_users and save\_users.

* Validation and error handling

Validation and error handling are extremely important in this specific scenario, as without it, there would be many mechanics that would not work at all. By implementing boundary checks and input logic, the game was much more stable as there wouldn’t be anything that could break the game, as it is able to handle it, similarly in the can\_place\_piece method, checking if the block is able to be placed onto the grid.

---

## 4.2 Key Features Developed {#4.2-key-features-developed}

**Describe** the core features of the system.

**Justify** their inclusion.

The main feature of the program was the piece placement. It allowed for three randomly generated pieces to be selected and transferred onto the 8x8 grid, the critical mechanic to fulfill the functional requirements. By mapping the click coordinates from the user into the grid column and row, it allowed the blocks to be placed onto the grid, with placement checks included.

Another important feature in the system was the line clearing and score addition, which allowed the game to be infinite if played well enough, with the users’ skill tracked by the scoring system.

---

## 4.2.1 Back-End Engineering Contribution {#4.2.1-back-end-engineering-contribution}

**Explain** how back-end engineering contributed to the success and ease of use of the software, including

* Data processing

* Validation and logic

* Storage and retrieval

* Authentication (if applicable)

Back-end engineering was the most important part of the projects’ success and usability. It included the main validation and logic of the block placements, and included data processing for the user logins and scores. For example, in [auth.py](http://auth.py), hashing was used to ensure that the program was secure and could protect the user logins.

import json

import os

import hashlib

user\_file \= "users.json" \# file for user and password data

def hash\_password(password):

   return hashlib.sha256(password.encode()).hexdigest()

def load\_users():

   if not os.path.exists(user\_file) or os.path.getsize(user\_file) \== 0: \# if file isn't there give an empty list

       return {}

   with open(user\_file, "r") as f: \# read mode

       return json.load(f)

def save\_users(users):

   with open(user\_file, "w") as f:

       json.dump(users, f, indent\=2)

def register\_user(username, password):

   users \= load\_users()

   if username in users:

       return False, "Username already taken."

   users\[username\] \= hash\_password(password)

   save\_users(users)

   return True, "Account created\!"

def verify\_user(username, password):

   users \= load\_users()

   if username not in users:

       return False, "No account with that username."

   if hash\_password(password) \== users\[username\]:

       return True, "Login successful\!"

   else:

       return False, "Incorrect password."

---

## 4.3 Screenshots of Interface {#4.3-screenshots-of-interface}

Include annotated screenshots explaining how the user interacts with the system.

see [calmstack annotation](https://docs.google.com/document/d/1rJmE56UA8VWlNptpFANngUceHZ2FQFwBQDLk9iQLIEE/edit?usp=sharing)

---

## 4.4 Version Control Summary (Optional) {#4.4-version-control-summary-(optional)}

**Summarise** commits, iterations, or sprints if version control was used.

Sprint 1: Initial repository setup, creation of main window, multiple file scaffolding  
Sprint 2: Implementation of game logic, piece generation, placement mechanics, line-clearing  
Sprint 3: Login and registration page, password hashing, high score saving  
Sprint 4:  Bug fixes \+ addition of extra blocks, documentation added  
---

# 5\. Testing and Evaluation {#5.-testing-and-evaluation}

## 5.1 Testing Methods Used {#5.1-testing-methods-used}

Describe testing approaches, such as:

* Unit testing

* Integration testing 

* User testing

**Explain** how testing results were used to improve performance, efficiency, or reliability.

In the project, the most used testing approaches were unit testing and user testing, which improved the program’s performance greatly by allowing for the discovery of bugs and the fixes of programs. Unit testing allowed for the specific modules and methods to be tested, such as the authentication and grid placement check, as well as user testing the overall functionality of the system and making sure that the experience is well-defined. Integration testing was mainly just making sure that the different files could communicate correctly, other than that it was all great.

---

## 5.2 Test Cases and Results {#5.2-test-cases-and-results}

| Test ID | Description | Expected Result | Actual Result | Pass/Fail |
| :---- | :---- | :---- | :---- | :---- |
| TC01 | Valid login with correct credentials | Success message, transition to game UI | Success message and game loads | Pass |
| TC02 | Invalid login with incorrect password | Error message and stay on login screen | Error message, login screen stay | Pass |
| TC03 | Register new account with unique username | Account created and success message, going to game UI | Success, game UI | Pass |
| TC04 | Register with existing username | Error message saying username taken | Error message | Pass |
| TC05 | Place piece on empty grid cell | Piece appears on board \+ score | Placed correctly, score updated | Pass |
| TC06 | Place piece on occupied cell | Unable to place, status update   | Handled error correctly | Pass |
| TC07 | Complete full row | Line clear, added score | Line clear, updated score | Pass |
| TC08 | Complete full column | Line clear, added score | Column cleared, score update | Pass |
| TC09 | Game over (no pieces can be played) | Game over status | Shows game over status | Pass |
| TC10 | High score loading correctly | Previous high score loads after restarting/login | When logged in with existing account, saved high score is there | Pass |
| TC11 | Password hashing | Stored password is hashed with SHA-256, not plain text | Hash stored, verification works | Pass |
| TC12 | Register new account with weak password | Password rejected, status claiming it is too weak | Login succeeds anyway, no validation errors | Fail |

---

## 5.3 Evaluation Against Requirements {#5.3-evaluation-against-requirements}

**Evaluate** how effectively the solution meets the identified functional and non-functional requirements. Consider your ongoing quality assurance processes.

The final solution of the project met all the functional requirements stated at the beginning of the documentation, as well as having all required non-functional features. The project had a set list of blocks and colours that randomly generated, could use algorithms to check for completed lines and add score, recognise user input (clicking the piece) and place the block, as well as the ability to save logins and user data. For the non-functional requirements, it was optimised for all devices (Python is a universal language, working on any OS), had a simple GUI that was easy to use and navigate, and stored all data securely (however, instead of encryption, a hashing method was used without salt, making the same passwords have the same hashes, not as secure).

**Evaluate** your project in terms of how effectively you addressed compliance and legislative requirements (consider privacy, use of data, etc). 

The project definitely addressed compliance and legislative requirements very effectively, including privacy, data minimisation, and secure handling features. User data such as usernames and passwords are stored locally in users.json, and is not transmitted externally. In addition, only the essential data needed in the project (username, password hash, high score), are collected and stored, as well as the passwords having secure handling, never being stored in plaintext.

---

## 5.4 Improvements and Future Development {#5.4-improvements-and-future-development}

**Outline** your project’s limitations. 

The project does not have any drag and drop functionality, no animations or visual effects for line clears, no input validation, no sound effects or music, as well as only being singleplayer.

**Explain** realistic future enhancements.

To make the user experience better, adding enhancements such as drag and drop placement will allow users to interact directly with the block for a more satisfying mechanic, as well as animations such as smooth transitions for better visual appeal. In addition, adding input validation is also a good enhancement, which all of these can improve the game’s functionality.

---

## 5.5 Evaluation of Social, Ethical and Legal Issues

**Evaluate** your project in terms of social, ethical, and communication issues.

Social:

The game promotes lots of cognitive engagement across all age groups, by removing time pressure and making it accessible to players who find Tetris too stressful. 

Ethical:

The project handles all ethical aspects well, with respect to user data privacy. It is also fair to all players, with no hidden biases or pay-to-win mechanics, only the random piece generation. It is also accessible, with a clear UI, but there are some issues regarding more accessibility features such as language support or colourblind modes.

Legal:

CalmStack’s idea of a timeless tetris game is similar to the already existing Block Blast, so if this game was to be published commercially, there may be some issues regarding legal troubles with copyright. However, this game is not intended to make money but uses no license file on GitHub, meaning all rights are reserved on default. Adding an MIT license would allow others the contribute and use the code.

# 6\. Feedback, Security and Reflection {#6.-feedback,-security-and-reflection}

## 6.1 Summary of Client or Peer Feedback {#6.1-summary-of-client-or-peer-feedback}

**Summarise** feedback received and explain how it influenced development. 

You could collect a **‘PMI’ (Plus, Minus, Implication)** table from **at least three** different people after testing, or **record and summarise an interview** with **at least three** three people who test the software. 

**Evaluate** your use of feedback to improve your project:

* Consider your individual workflow and how well you responded to peer / stakeholder feedback

* Consider how well you involved, empowered or negotiated with a peer/client throughout the process. 

|  | Plus | Minus | Implication |
| :---- | :---- | :---- | :---- |
| Shawn | Nice UI Cool login page (switch between login and register is clean) Features work well with no issues Application UI spaces well | can’t drag blocks no animations no input validation | Very nice app overall, with good features, just needs some polishing regarding user experience, and security |
| Victor | Easy on the eyes: The interface is very pleasing The features work extremely well, with no issues The application uses screen space well, not too little, not to much | No/limited password validation (except hashing)  | Overall, a well made application. However, I do wish that you could drag the blocks, though I do understand that this is extremely difficult to make.  |
| Ronen | Nicely configured interface, features work well and there are not any issues | Could benefit from password strength validation, and a drag-and-drop functionality for ease of use | An aesthetically pleasing application, however I would wish for drag and drop blocks for increasing functionality and strength validations to ensure a higher extent of confidentiality and security |

---

## 6.2 Secure Software Design and Data Handling {#6.2-secure-software-design-and-data-handling}

**Evaluate** the approach undertaken to safely and securely collect, use, and store data.

Your evaluation should address: 

* Secure coding practices applied during development

* Input validation and error handling 

* Data storage and protection methods 

* The impact of secure software design on user trust, data integrity, and system reliability

The approach taken to safely and securely collect, use, and store data was met with precaution. Password hashing (hashlib) was used to secure passwords before the storage, meaning no plain passwords were ever written, as well as error handling in [auth.py](http://auth.py) and score\_manager.py to prevent crashing in the application. Input validation was also used for the game logic, making sure the blocks were placed correctly. However, other aspects of input validation and error handling weren’t as polished, as there were no username or password checks. Passwords were kept secure with hashing, but adding a salt (random data on password) would prevent rainbow table attacks and improve security further. Ultimately, the overall approach to safely and securely collect, use, and store data was met with precaution to ensure all user data is safe.

---

## 6.3 Personal Reflection {#6.3-personal-reflection}

**Reflect** on what you learned during the project, including

* Software engineering skills developed

* Challenges encountered and how they were overcome

The object-oriented program deepened my understanding of the OOP principles, allowing me to implement inheritance, abstraction, and more. I also learnt more about lists, hashing, and customtkinter. However, there were many challenges I was met with and had to workaround. Initially, my project was in pygame but after spending hours trying to fix bugs regarding the mechanics and logic, I ultimately gave up and switched to customtkinter, which was much better, paired with guidance from a youtube tutorial. This set me up to keep improving the project by converting it into OOP and adding more features such as hashing. This definitely changed my perspective on time management and correctly planning things, as the rework definitely took up my time, the lesson being to always make sure what you are doing is final, and make sure you do it consistently.

---

# 7\. Appendices {#7.-appendices}

* Full Gantt Chart

* Complete Data Dictionary 

* Full Test Logs

* Raw Feedback Notes

* Exemplar Code Snippets

[image1]: <data:image/png;base64,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CwcURdxPlwEA+oMA1wEf4oAy02f7AQD6jwDXAel1swGOa+EAAEAvEOA6RC8cAADoNQJch+iFAwAAvUaAywC9cAAAoJcIcBnwv86A6li1alVYAADoFQJcRuR3PbXIM8VQHYR3AECvEeCADtEDCwDoNQIckAEb4nioMwCg2whwQIboiQMA9AIBDsgYIQ4A0G0EOCBj/tmAAABkjQAHdIE80JkQBwDoFgIcGpIfMP/22299dSFIcDp06JCv7hkb4viFDgBAlghwaKioPUjXrl0Llvvxxx/3o3rK9sIR4gAAWSHApdCNENONeXZDUZbTW79+fbDco0aN8qN6zoY4AACyQIBLoRsH327MsxuKspyeLvf48eP9qL6wNzbwnDgAQKcIcCl0I8R0Y57dUJTl9HS5n3nmGT+qbwhxAICsEOCaePjwYXjQ9WXEiBG+eSrdmGe3yDINHDjQV+eers8NGzb4UX1lP2tCHACgXYUPcH/++aevSu3IkSN1Acry42wZMGBA8PNJrfLzyWKeavHixXXz7MTFixeDeYwbN86P6pnVq1fXtm7dGg4fP3689uDBA9Minr7/q1ev+lF9Zz8fQhwAoB1tBbizZ8/WFi1aVPv111/9qAg50H755ZdBL8h3333nR3dk8ODBkQPh7du3fZNE9+/frws6PvBcunSpbpyECek9a2bHjh21TZs2BQHRanWeO3furL311lu+Ophu7Nix4fCrr75aN1//ftqhv++5YMECPyrRyJEjw9eWQLpr1y7fJOLUqVO1Dz/8MFhncXReS5cujbyvSZMmRdrJuj18+HA4nMX77yb7XjoJ7QCAamo5wPngJL0jElTee++9SLvp06dH2iUdUG/cuBH8q6FKD8Ly/LGkaez8xowZk9guiZ1+7969fnTo+eefDx9HkWb+58+fj8xbioQYq5V5xrX55Zdf6urTvp9WrVmzJpinBEQJ4wcOHKh9+umntZMnT/qmtX//+991790W786dO3Vt4tr58Y888kht+PDhkXDs28g6T5pfXmg41kKIAwC0oqUAZw840gMiB0rpOfEHy2HDhoV1c+fOrR08eDAMZNevXw/bzZ8/P5xu9uzZkfnY11q7dm04jVyPJXX2uqznnnsu8vrN2HlLz00z+poXLlzwo0Jyak/n+dprr9W+//778CA9evRo3zzVPO36UDNnzqyrb/X9pDVn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>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnAAAAFcCAYAAABIlYNzAACAAElEQVR4Xuy9h7sUxda+/ftL3nMMCHiMGAAzgogkEVFEFAVBBBQRUMxiAFRURBBFDCiIGQOoiIhgBJGMKCJmEUVB9Jg99vfd9b6rT03tmdmz957p6Zl57uuqa7qre6bjVD+9atVa/y8SQgghhBAVxf8LK4QQQgghRLqRgBNCCCGEqDAk4IQQQgghKgwJOCGEKDN///139Pvvv0dLliyJy8SJE6PFixdHv/zyS/Tbb79Ff/75Z/g1IUQNIwEnhBAJsX379mjevHlRhw4dov/5n/9pchk6dGi0bNmycDNCiBpAAk4IIUrIihUrojZt2tQRX5QjjzwymjlzZrRp06bwazGsd+WVV0aXX355dMwxx9T5DStt27aNrr766ug///lP+BNCiCpEAk4IIYrMNddcE+23334ZAmvPPfeMmjVrFu3atStcPS9899dffw2ro2+++caJw9GjR9cRc2wH0SeEqF4k4IQQool88MEH0R577JEhok466STn14Z/G7z77rvR22+/HXyzuPz111/R7bffnrEf//jHP6I5c+aEqwohKhwJOCGEaCB0eYZWr+uuuy5cLTX06tUr3s8hQ4ZEn3/+ebiKEKLCkIATQogCGTBgQIZou/DCCytKDG3evDnDUnjZZZeFqwghKgQJOCGEqIf+/ftnCLdnn302XKWioMvXP57BgweHqwghUo4EnBBC5OChhx6KRc5uu+0W/fTTT+EqFQ0+er6QO//888NVhBApRQJOCCECevfu7QRNq1atoh07doSLq5JBgwZliLnvv/8+XEUIkSIk4IQQ4v9Yt25dLGBmz54dLq568JFr2bJlfA7uuuuucBUhREqQgBNCiP+fRx55xImWkSNHhotqjptuuikWcUcccYTrahVCpAsJOCFETWMO/S1atAgX1Twnn3xyLOSOP/74cLEQooxIwAkhapaNGzc6cUJOUZGdl19+2QUDNiH3xx9/hKsIIcqABJwQoiZZtGiREyTLly8PF4ksmICjlDqjhBCifiTghBA1h424nDt3brhI5ODnn3+O2rdvH4s4CV8hyosEnBCipiCe2+677x5WiwJ54403YhG37777houFEAkhAdcISBhd7CKEKD2HHnpotNdee4XVohH4XapCiOSpCAFH9POdO3e68umn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/xwuFkKUGAm4GoFgkRYpnPP5/vvvu88uXboEawpRnTC6kHv+4IMPDheJBmIxyihY4YQQySMBVyP459AEXK9eveJh70LUCvgUUSQ8GgepoWhDFPFfiPIiAVcD4AibTcCZ87EQtYa1K5WYZL1cYMHEYq82WYh0IAFXAxA76NVXX43nOZ9btmyJpwkUKUStYblTjznmmHCRCFi6dGncFg8bNixcLIQoAxJwNQDnz0+dxbxF6+7UqVN0+eWXx8uEqCWIhWhtDIJO1KVbt27xOaq09FhCVDMScFUOefLC8+cLOHNGFqJWsdydFN9SXetYIGS1wUKkEwm4KodkyPfcc0+duu+++y5j3pIwC1GrtGzZMm5vCLdTy4wePTo+F61atYrzgxoEASdv57Zt2zLqhRDJIQEnhBD/x5133plhdfroo4/CVaqadu3aZRx/mLqJl8H9998/OumkkzLWoyjvrBDJIgEnhBAeWKfJn2ptT9euXcNVqo6rrroqQ4xddNFF4SoxRx55ZMa63bt3z5gn20uY8F0IUXwk4IQQIgt0EfrCpBpjJuIL6x8jpZBk9IMGDcr4znXXXee6WSdOnBjXESdOgx6EKB0ScBXK33//HVaVDAKejhgxIqwWourZtGlTtNdee2WIFUZtE0OxkrnvvvsyjolE9Lfddlu4Wl4IT8R3R44c6T5POeWUjOXHH398/PuLFi3KWCaEaDoScBVIx44do0MPPTSsLhn4vXANkhSNQqSNHj16ZIgeullnz54drpZKEJw333xzxv5T6O5sihg1S9ysWbOiE0880U0TJDxkwIABbtlLL70ULhJCNBIJuArkqKOOisaNGxdWlwyLAyVErbN69eo6IohCruE0gsAk92u4v/ynCSFUDOw3O3fuHD399NNueufOneFqQogiIwFXgTCsf8WKFWF1yaB7RddAiP9i6enC0qxZs+jss88OV08UMiX4gzD8wgCEYlvSX3zxxfj3CcVisSVXrlwZriqEKCIScBVIviTSDPt/6KGHoieffLJO7Cb4+eefo59++ime37FjR3TllVdG69atc+eZ8ADGL7/84j6pb968eVwvhMgES9dBBx1URzBZefPNN6Nvvvkm/FqD4T/J7yCS+vXrV2c7YWndunW0bNmy8GeKzm677eZiw02YMMFtl3aFT142f//993B1IUQRkICrQOyBQNwl4lbt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>

[image3]: <data:image/png;base64,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>