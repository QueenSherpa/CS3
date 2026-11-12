# Makefile for the sorting algorithms
#
# Usage:
#   make            run every sort
#   make insert     run just insertion sort (also: bubble, merge, quick)
#   make list       print the generated random list
#   make clean      delete Python cache files
#
# Change the file names below to match your files.
 
PYTHON = python3
 
LIST_FILE   = randList.py
INSERT_FILE = InsertSort.py
BUBBLE_FILE = BubbleSort.py
MERGE_FILE  = MergeSort.py
QUICK_FILE  = QuickSort.py
 
.PHONY: all insert bubble merge quick list clean
 
all: insert bubble merge quick
 
insert:
	@echo "=== Insertion Sort ==="
	@$(PYTHON) $(INSERT_FILE)
	@echo
 
bubble:
	@echo "=== Bubble Sort ==="
	@$(PYTHON) $(BUBBLE_FILE)
	@echo
 
merge:
	@echo "=== Merge Sort ==="
	@$(PYTHON) $(MERGE_FILE)
	@echo
 
quick:
	@echo "=== Quick Sort ==="
	@$(PYTHON) $(QUICK_FILE)
	@echo
 
list:
	@$(PYTHON) $(LIST_FILE)
 
clean:
	rm -rf __pycache__ *.pyc
 