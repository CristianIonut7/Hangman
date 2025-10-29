# Hangman – UNSTPB – ACS | IS – 1AC, 2024

Gamified **HANGMAN** project featuring terms from the field of **circular and sustainable economy** — module developed within the European project:  
**"Gender, Digitalization, Green: Ensuring a Sustainable Future for All in Europe"**

---

## UPLOAD DETAILS

A) Clone the repository locally:  
```bash
git clone https://github.com/andrewen11/Hangman.git
```
Add the newly created files in the corresponding folders:
```bash
git add FILE_NAME
```
Commit with a descriptive message:
```bash
git commit -m "Descriptive upload/update message"
```
Push your changes to the branch:
```bash
git push
```
Create a merge / pull request at the end, when everything is finalized and validated.

## TASK DISTRIBUTION
### FILES – COORDINATOR: Ionescu Raul
Description:

Two main types of files will be added here:

CSV file – multiple columns:
Question, Answer A, Answer B, Answer C, Correct answer(s)
→ Used for quiz-like questions when the player loses all lives and doesn’t want to restart the game.

TXT file – list of expressions / words, one per line.
→ These are the actual words used in the core Hangman game.

Requirements:

a) 20 multiple-choice questions (CSV file) — import 6–7 from Quiz 3 and add new ones from the Module 3 presentation (see links below).  
b) 100 words / expressions (TXT file), each on a separate line — no delimiters!  
c) Files must be uploaded to the FISIERE folder on the branch andrewen11-patch1-DEMO:  

### GRAPHICS – COORDINATORS: Cîrcioroabă Radu, Lică Ștefan & Pleșeanu Cristian
Description:

This section contains graphic assets and C–Python integration files.

Category 1 – JPEG/PNG files for art style, UI, and layout prototypes (handled by Radu Cîrcioroabă).

Category 2 – Python files managing C–Python integration, configuration, and linking visual modules to the core code (handled by Ștefan Lică and Cristian Pleșeanu).

Requirements:

1. Implement functions / APIs to connect C source code with the graphic interface  
2. Create a fixed-size window including:
  - Main menu (title, new game, etc.)
  - In-game interface
  - End screens (lose / win) with:
  - Quiz window for one extra life
  - Input field for letters or words
3. Files go to the GRAPHICS folder:

### SOURCE CODE – COORDINATORS: Bălălău Andrei & Șipanu Eduard
Description:
This section includes the core source code, responsible for:
Reading data from files
Processing and managing game logic
Implementing singly linked lists and other dynamic data structures

Part 1: File handling (reading CSV/TXT, random selection of questions or words).  
Part 2: Linked list implementation (letter-by-letter handling, push/pop functions).  
Part 3: Post-demo phase — integration of additional modules (audio, effects, etc.).

