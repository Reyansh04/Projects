Run script.bat (if on windows) else (script.sh) to run the code, it takes input commands, until "END" command & performs the operations, for wrong commands, we output invalid output.

in ROLLBACK, we set version = -1 if no version_id is provided & if version_id happens to not be a string then a error pops up as well.

these are some edge cases:
CREATE research_paper.tex
File 'research_paper.tex' already exists 

READ non_existent.file
File 'non_existent.file' not found (... same goes for INSERT, SNAPSHOT, HISTORY, etc.)

ROLLBACK research_paper.tex 100
Invalid version ID.

ROLLBACK
File '' not found (... similarly for others)

ROLLBACK research_paper.tex
No parent to rollback to.

ROLLBACK main.py not_int
Invalid version ID.



