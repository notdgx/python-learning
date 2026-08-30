---
date: 2026-08-30
time: "19:34:11+05:30"
---
# Topics 
- Python Introduction  
- Python vs CPP
- Python Under the hood 
- Python Step by Step Parts and executioon 
 
_________

# 00 -> Python

> Python is a ==high-level, interpreted, dynamically typed, garbage-collected, general-purpose programming language==. Created by ==Guido van Rossum in 1991.==

- The philosophy: code should be readable like English. You trade raw speed for developer speed and simplicity
- Scripting Language 


```
              PYTHON vs C vs C++ -- THE REAL DIFFERENCES


FEATURE             C               C++             PYTHON
-----------         --------        --------        --------
Type System         Static          Static          Dynamic
Typing              Manual          Manual          Inferred at runtime
Memory Mgmt         Manual(malloc)  Manual/RAII     Automatic (GC)
Compilation         Compiled        Compiled        Interpreted
Execution           Machine code    Machine code    Bytecode -> CPython VM
Speed               Fastest         Very Fast       Slow (10x-100x slower)
Paradigm            Procedural      OOP+Procedural  Multi-paradigm
Primitive Types     YES             YES             NO (everything = object)
Pointers            YES             YES             NO (abstracted away)
Header Files        YES             YES             NO
Memory Layout       Direct          Direct          Hidden behind VM
```

## Low Level structure 

### CPP 

- It has primitive datatypes like `int a = 4` will take 4 bytes in memory cpu directly talks zero overhead 
- The machine code produced upto the linker is 

```
.c source
   |
   v
[Preprocessor]
   |
   v
[Compiler] -- checks types, optimizes, catches errors HERE
   |
   v
[Assembler]
   |
   v
[Linker]
   |
   v
.exe / ELF binary  <-- THIS is what runs, not your source code
   |
   v
CPU executes directly
```

```
MANUAL (C, C++)
- You call malloc() and free()
- Full control, full responsibility
- Bug: forget to free = memory leak
- Bug: free twice = crash
- Bug: use after free = security vulnerability

GARBAGE COLLECTION (Python, Java, Go)
- Runtime tracks what is alive
- Automatically frees dead objects
- Safe, easy
- Pause times, overhead, less control

OWNERSHIP SYSTEM (Rust)
- Compiler tracks who OWNS each piece of memory
- Owner goes out of scope = memory freed automatically
- No GC, no manual free, no bugs
- Steep learning curve
```
### Python

- The C/CPP stores primitive data types directly like the int takes 4 bytes and the size is determined and fixed but every thing in python is a Object the size is not fixed it can be variable
- It can store extremely large integers and performs calcualtions at start it is 28bytes ie the PyObject , it stores data in chunks of 30bit and it can increases it 
- the float however is standard same as C/CPP IEEE 554 8 bytes which is fixed slow and has a lot of precision and some disadvantages in equlity checking
- In Cpp the 

```c
int x = 10;
int y = x ;
x = 20 ;
```

> here the copy of x ie 10 is created and stored in seperate place with 4 byte size in y any chnage in x dont affects the y

- but in pyhton for the same thing if we even canges the x then the y will  be same because before both keys x,y pointing to the pyobject int 10 but when the x is made x = 20 then the x key will point to a new pyobject created with digit 20 and y is still pointing there so no change here
- but if we had mutable datatypes then they will be changed

```python
a = [1, 2, 3]    # a points to a list PyObject
b = a            # b points to the SAME list PyObject
a.append(4)      # mutates the PyObject in-place

print(b)         # [1, 2, 3, 4] -- b sees the change!
```

- the cpp program compiled executable is a machine coded instruction with no immedate translation it is one time compiled
- But the python is a interpreated langauge there is no single binary output it directly gives cpu the instructions to execute
- Every Process has a stack heap given by the OS the heap is growable on demand of chunks from OS but the stack is fixed 
- The CPP compiled or any other language that compiles to binary use Stack and Heap given by OS the executable binary has zero dependecies with copiler once it is compiled it may depenf on for what artitecture it was compiled to run 
- But in Python the python's interpreater ie PVM itself is a C compiled binary CPyhton under the hood it is written in CPP and uses the C structs, when interpreater is called the pyhton file act as a input or argunment which has to be runned in it like a mp4 fiel needed to be played in VLC 
- That PVM Process gets its own stack which is purely used by python  interal functions and definations and working and actull python file code executes from the heap all the fucntions variables, datatypes objects stays in heap and the process is carried out there
- It has its own virtual stack in heap called eval stack That helds the fucntions executrions etc
- In Cpp 

```
.c source
   |
   v
[Preprocessor]
hello.c  ->  [Preprocessor]  ->  hello.i  (expanded source)
   |
   v
[Compiler] -- checks types, optimizes, catches errors HERE
hello.i  ->  [Compiler]  ->  hello.s  (assembly)
   |
   v
[Assembler]
hello.s  ->  [Assembler]  ->  hello.o  (object file, binary)
   |
   v
[Linker]
hello.o + libc.o  ->  [Linker]  ->  hello (final executable)
   |
   v
.exe / ELF binary  <-- THIS is what runs, not your source code
   |
   v
CPU executes directly
```

- After the Compiler the CPP program becomes artitecture dependent for what machine it is made
- But in Pyhton

```
              LOW-LEVEL STRUCTURE OF PYTHON (CPython)


  Your Python Code (.py)
         |
         v
  [ Lexer / Tokenizer ]         -- breaks code into tokens
         |
         v
  [ Parser ]                    -- builds Abstract Syntax Tree (AST)
         |
         v
  [ Compiler ]                  -- converts AST to bytecode (.pyc)
         |
         v
  [ CPython Virtual Machine ]   -- executes bytecode line by line
         |
         v
  [ C Runtime / OS ]            -- actual machine interaction

* CPython itself is written in C.
* The VM is a STACK-based interpreter, not register-based.
* .pyc files are stored in __pycache__/
```

### Python Program Running


1. The python code is source file jsut a normal text file 
2. the file goes through the lexer and Tokenizer That breats the source fiel in tokens like `1` `+` `7` `=` `8`
3. from that it makes a Abstract Tree of the file content every fnction , if else, caluclations etc is made into a tree for the predefined rules to find errors optimize it 

#### ==ByteCode== 

4. Then the ATS code is compiled into ==BYTECODE it is not machine code it .pyc extension== upto here everything is machine independent the user can share and then inteerpreat it using PVM in different machine huge helpful
	- It is made automatically in `__pycache__` Folder for chaching and reducing workload
	- the folder may contains File with different timestamps python versions
	- It anything in code from where it is derieved from cahnges it will re compiled and use as for further cache hits
	- These are the Instructions for the PVM according to defined c functions for run python 


In Python, ==**`dis`** is a built-in module that stands for **disassembler**.== It lets you inspect the **Python bytecode** generated from your code.

Bytecode is the low-level instruction set that Python's virtual machine executes.


```python

import dis

def add():
    x = 5
    y = 10
    z = x + y
    print(z)

dis.dis(add)
```

> ByteCode 

```
3           0 RESUME                   0

  4           2 LOAD_CONST               1 (5)       ; push 5 onto stack
              4 STORE_FAST               0 (x)       ; store as x

  5           6 LOAD_CONST               2 (10)      ; push 10 onto stack
              8 STORE_FAST               1 (y)       ; store as y

  6          10 LOAD_FAST                0 (x)       ; push x onto stack
             12 LOAD_FAST                1 (y)       ; push y onto stack
             14 BINARY_OP               0 (+)        ; pop both, add, push result
             18 STORE_FAST               2 (z)       ; store as z

  7          20 PUSH_NULL
             22 LOAD_GLOBAL              1 (print)   ; find print function
             32 LOAD_FAST                2 (z)       ; push z
             34 CALL                     1           ; call print(z)
             42 RETURN_CONST             0 (None)
```

#### PVM 

5. The python virtual machine executes the Bytecode
	- It is a giant loop written in C to execute bytecode step by step
	- It reads the opcode run it under the hood like c moves to next 
	- CPU runs PVM, PVM runs your code
	- The types are checked at runtiem unlike C which are checked at compiled time

__________

## Properites

- The ==types are checked at runtiem== unlike C which are checked at compiled time
- The intermediate data lives in eval stack in pyhton and i c it lives in stack or regesters 
- 
```python
z = (x + y) * (a + b)
```

- `(x + y)` is intermediate -- it exists temporarily to compute the final result.
- Python's PVM has its own software stack called the **evaluation stack** or **value stack**. It lives in **heap memory** as part of the frame object.
- The entire program has ONE root node (the If statement). Everything hangs off it. Execution always starts at the root and recurses into children, but evaluates children BEFORE parents.
- The python is 50x to 100x slower then C because of the internal C fucntions required for python to be a language 
- C addition:     3 CPU instructions
- Python addition: ~100+ C function calls inside PVM
                 + PyObject allocation on heap
                 + reference count update
                 + type lookup
                 + method dispatch
                 + actual addition
                 + another PyObject for the result

### ATS 

```
z = x + y
```

- This to the program arrieve as raw string characters
- they are tokenized into small parts like 
- The job is to giving the raw characters structure and meaning 

```
'z', ' ', '=', ' ', 'x', ' ', '+', ' ', 'y', '\n'
```

#### STEP 1  : ==LEXING==  

- It is breaking down raw string into tokens like 
```c
z = x + y


NAME    'z'
EQUAL   '='
NAME    'x'
PLUS    '+'
NAME    'y'
NEWLINE
```

- Each token has a **type** and a **value**. The lexer does not care about meaning yet. It just categorizes chunks of text
#### STEP 2 : ==PARSING== 

- Now the parser takes those tokens and figures out the **structure and relationships** between them.

```c
z = x + y


Assign
  |
  +-- target: Name('z')
  |
  +-- value: BinOp
               |
               +-- left:  Name('x')
               |
               +-- op:    Add (+)
               |
               +-- right: Name('y')
```

- This is an **assignment**
- The **target** of the assignment is `z`
- The **value** being assigned is the **result of a binary operation**
- That operation is **addition**
- The **left operand** is `x`, the **right operand** is `y`

#### Properties

- It helps to decide precedence. `y * 2` is a subtree that must be evaluated first before its result feeds into the addition. No ambiguity. No need to re-check rules later.
- What should be evaluated first 
- ==Independent of== 
	- ==What CPU you are targeting==
	- ==What bytecode format you use==
	- ==What optimizations you want to apply==

- You can take the SAME AST and:
	- Compile it to CPython bytecode
	- ==Compile it to JavaScript== (tools like Transcrypt do this)
	- Analyze it for bugs (linters use the AST)
	- Format your code (Black, autopep8 use the AST)
	- Generate documentation

- Helps to ptimize the small calcualtions patterns 
- `x = 2 * 3 * 10`
```
Before optimization:
BinOp(BinOp(Const(2), Mult, Const(3)), Mult, Const(10))

After optimization:
Const(60)
```
- Your bytecode just loads 60 directly. No multiplication at runtime. This is called ==**constant folding**== and it is trivially easy to do on a tree by walking nodes.
- The parser can catch structural errors with precise location info:
```python
z = x +          # SyntaxError: incomplete expression
```

- The ==parser knows exactly which node is incomplete==, which line, which column. It can give you a useful error message because it understands the STRUCTURE, not just the characters.

**Peephole optimization** is a broader concept.

The compiler looks at a **small sequence of instructions**—as if looking through a tiny "peephole"—and tries to replace it with a more efficient equivalent.

Historically, Python used peephole optimization for things such as:

- ==Constant folding==
- Simplifying jumps
- Removing unreachable instructions in certain situations
- Optimizing some constant sequences

```
Optimization
│
├── Peephole optimization
│   ├── Constant folding
│   ├── Jump optimization
│   └── Other small local optimizations
│
└── Other optimizations
    ├── Dead code elimination
    ├── Constant propagation
    └── ...
```

```
Source code  "z = x + y"
     |
  [Lexer]
     |
  Tokens:  NAME EQUAL NAME PLUS NAME
     |
  [Parser]
     |
  AST:  Assign(Name(z), BinOp(Name(x), Add, Name(y)))
     |
  [Compiler]  -- walks the AST node by node
     |
  Bytecode:
     LOAD_FAST  x
     LOAD_FAST  y
     BINARY_OP  +
     STORE_FAST z
     |
  [PVM]
     |
  Actual execution
```

- The compiler **walks the tree** depth-first. For a `BinOp` node it recursively compiles the left side, then the right side, then emits the operation. The tree structure directly determines the order bytecode is emitted.
- The C and CPP also makes it for optimization but after the compiling it goes away
- ALso in pyhton after the Bytecode Compilation it goes away they both in cases becomes a step by step instruction to cpu and PVM resp.

#### T==he Peephole Optimizer==

Between AST and final bytecode, Python runs an optimizer that simplifies bytecode before it ever runs:

python

```python
import dis

def foo():
    x = 1 + 2        # you wrote addition
    
dis.dis(foo)
# LOAD_CONST 3       <- Python already computed 1+2 at compile time
                     # not at runtime
                     # this is constant folding
```

Python does this silently. Knowing it exists means you understand why some "slow" code is actually already optimized.

_________
________
__________

### ==ByteCode==

>Bytecode is a sequence of **simple instructions** for a **Virtual Machine**. Not for your CPU. For a ==fake/virtual== CPU that Python implements in C.

- Each instruction is called an ==**opcode**== (operation code). Each opcode is just a **number** (1 byte originally, hence "byte"-code).
```
LOAD_FAST  =  124   (the number 124 in binary)
BINARY_OP  =  122
STORE_FAST =  125
RETURN     =  83
```

- The PVM reads these numbers one by one and executes ==corresponding C code== for each.
- `dis` shows you the human-readable version. The ACTUAL bytecode stored in the `.pyc` file is raw bytes.


```python
import dis

def add(x, y):
    z = x + y
    return z

# get the raw bytes
raw = add.__code__.co_code
print(list(raw))
```

Output:

```
[151, 0, 124, 0, 124, 1, 122, 0, 0, 0, 125, 2, 124, 2, 83, 0]
```

- Just numbers. That is the actual bytecode. The `dis` module translates these numbers into readable names like `LOAD_FAST` so humans can understand it.

```
151  =  RESUME
124  =  LOAD_FAST    (next byte: 0 = first argument, x)
124  =  LOAD_FAST    (next byte: 1 = second argument, y)
122  =  BINARY_OP    (next byte: 0 = addition)
125  =  STORE_FAST   (next byte: 2 = third local, z)
124  =  LOAD_FAST    (next byte: 2 = z)
83   =  RETURN_VALUE
```

- The PVM runs a loop in C upon this bytecode 

```
Python Bytecode              C Machine Code
---------------              --------------
Instructions for PVM         Instructions for CPU
PVM is a C program           CPU is physical hardware
Stack based                  Register based
Each opcode -> C function    Each opcode -> 1 CPU cycle (roughly)
~100+ C ops per bytecode     1-3 CPU ops per instruction
Portable (any OS, any CPU)   Specific to x86 / ARM / etc
Stored in .pyc file          Stored in .exe / ELF binary
```


________
- C compiled code is tied to the CPU architecture.

```
Compile on x86 Linux  ->  runs on x86 Linux ONLY
Want to run on ARM?   ->  recompile from scratch
Want to run on Mac?   ->  recompile from scratch
```

Python bytecode is portable:

```
Compile once to bytecode
   |
   +-- Run on Windows  (PVM is installed there)
   +-- Run on Linux    (PVM is installed there)
   +-- Run on Mac      (PVM is installed there)
   +-- Run on ARM      (PVM is installed there)
```

- The bytecode does not change. The PVM is what is different on each platform. Your `.pyc` file works everywhere Python is installed.

After Python runs this file, check your folder:

```
your_file.py
__pycache__/
    your_file.cpython-311.pyc    <-- bytecode cached here
```

The `.pyc` file contains:

```
[magic number]        -- which Python version created this
[timestamp]           -- when source was last modified
[source size]         -- to detect changes
[marshalled bytecode] -- the actual raw bytes
```

- Next time you run the file, Python checks: has the source changed? If no -> skip compilation, use cached `.pyc` directly. Saves time.
- The PVM is the **translator** that knows how to take neutral bytecode and speak the language of whatever hardware it is running on.
- 
__________

```
your_code.py
     |
  [Lexer]  -> tokens
     |
  [Parser] -> AST
     |
  [Compiler] -> bytecode (raw numbers)
     |
  __pycache__/your_code.pyc  (cached)
     |
  [PVM - eval loop in C]
     |
  reads opcode by opcode
  uses a stack
  calls C functions for each opcode
     |
  actual computation happens in C
     |
  result
```


```
Q1 -- Intermediates:
      Python stores them as PyObjects on the heap via eval stack.
      C stores them in CPU registers. Heap vs register = Python slower.

Q2 -- Tree execution:
      Yes. Post-order traversal. Leaves first, root last.
      Bytecode is just the tree serialized into a flat instruction list.

Q3 -- Different from others:
      C:    tree dies at compile time, registers at runtime.
      Python: tree becomes bytecode, heap at runtime, no JIT.
      Java/JS: bytecode + JIT eventually becomes machine code.
      Rust:   most compile time work, zero runtime overhead.
```

______

_______

### Memory 

- The Python's stack and heap are NOT the OS stack and heap. They are **data structures living inside the C heap**.

```
+--------------------------------------------------+
|              OS / HARDWARE LEVEL                 |
+--------------------------------------------------+
|                                                  |
|   CPython Process (this is just a C program)     |
|   |                                              |
|   +-- C Stack (conventional stack)               |
|   |      PVM's own C function calls live here    |
|   |      eval loop, opcode handlers etc          |
|   |                                              |
|   +-- C Heap (conventional heap)                 |
|          |                                       |
|          +-- Python's ENTIRE world lives here    |
|                 |                                |
|                 +-- PyObjects (all variables)    |
|                 +-- PyFrameObjects (call frames) |
|                 +-- Eval Stack (inside frames)   |
|                 +-- Python's memory allocator    |
|                                                  |
+--------------------------------------------------+
```

#### THE PVM Stack

- It is the process's stack by the OS 
- When CPython runs, it is just a C program. It has a normal C call stack.

```
C Stack (OS managed)
+----------------------+
|  main()              |  <- CPython entry point
+----------------------+
|  Py_RunMain()        |
+----------------------+
|  PyEval_EvalCode()   |
+----------------------+
|  _PyEval_EvalFrameDefault()  |  <- THE PVM LOOP lives here
+----------------------+
|  ... opcode handlers |
+----------------------+
```

This is the REAL stack. But YOUR Python code never touches it directly. This is the PVM's internal machinery.

#### THE FAKE STACK : EVAL STACK

- This is what Python uses instead of the C stack for YOUR code.
- It is just an **array of pointers** allocated on the C heap inside a PyFrameObject:

```c
// Simplified PyFrameObject in CPython source
struct PyFrameObject {
    PyObject_HEAD
    PyFrameObject  *f_back;        // previous frame (linked list)
    PyCodeObject   *f_code;        // bytecode
    PyObject      **f_valuestack;  // BOTTOM of eval stack
    PyObject      **f_stacktop;    // CURRENT TOP of eval stack
    PyObject       *f_localsplus[]; // locals + eval stack space
};
```

- The eval stack is literally an array inside the frame. PUSH = increment pointer. POP = decrement pointer. That is it.

```
PyFrameObject on heap:
+---------------------------+
|  f_back -> prev frame     |
|  f_code -> bytecode       |
|  f_valuestack -> [0]      |
|  f_stacktop   -> [2]      |  <- top is here currently
|                           |
|  f_localsplus:            |
|  [0] local var x          |
|  [1] local var y          |
|  [2] local var z          |
|  [3] <- eval stack starts |
|  [4]    here              |
|  [5]                      |
+---------------------------+
```

#### THE PROCESS HEAP

Python does NOT use malloc/free directly for every object. It has its own **memory allocator** sitting on top of the C heap.

```
C Heap
+------------------------------------------------+
|  Python's Memory Allocator                     |
|  (pymalloc)                                    |
|                                                |
|  Manages memory in ARENAS -> POOLS -> BLOCKS   |
|                                                |
|  +----------+  +----------+  +----------+     |
|  | Arena 1  |  | Arena 2  |  | Arena 3  |     |
|  | 256 KB   |  | 256 KB   |  | 256 KB   |     |
|  |          |  |          |  |          |     |
|  | Pool Pool|  | Pool Pool|  |          |     |
|  | 4KB  4KB |  | 4KB  4KB |  |          |     |
|  |          |  |          |  |          |     |
|  | Blk Blk  |  |          |  |          |     |
|  | 32B 32B  |  |          |  |          |     |
|  +----------+  +----------+  +----------+     |
|                                                |
|  PyObjects allocated from blocks               |
+------------------------------------------------+
```

- Python pre-allocates large chunks (arenas) and carves them up internally. Much faster than calling malloc for every single PyObject.
- It can request the OS to give it the heap chunks 



```
C:      your variables on OS stack, intermediates in CPU registers.
        OS manages everything.

Python: NOTHING of yours touches the OS stack directly.
        ALL of it lives in the C heap.
        Frames are heap objects linked together.
        Eval stack is an array inside those heap objects.
        Python has its own allocator (pymalloc) on top of the C heap.
        The C stack only holds the PVM's own machinery.
```


#### Interpreater

```
CPython = a compiled C program (binary executable)
.py file = DATA that CPython takes as input
```

Exactly like:

```
VLC Player  = compiled C program
.mp4 file   = data VLC takes as input and processes

CPython     = compiled C program  
.py file    = data CPython takes as input and processes
```

Your `.py` file is not a program running on the CPU. It is **data being processed** by a program (CPython) that IS running on the CPU.

##### Flow 

```
1. You run:  python3 script.py

2. OS loads CPython binary into memory
   CPython is now a running process
   CPython has its C stack and C heap ready

3. CPython opens script.py
   Reads it as a STRING -- just text data

4. Lexer runs (C code on C stack)
   Tokenizes the string
   Tokens stored in C heap

5. Parser runs (C code on C stack)
   Builds AST from tokens
   AST stored in C heap

6. Compiler runs (C code on C stack)
   Walks AST
   Emits bytecode
   Bytecode stored in PyCodeObject on C heap

7. PVM starts (C code on C stack)
   _PyEval_EvalFrameDefault() runs on C stack
   Creates PyFrameObject on C HEAP for your code
   Reads bytecode instruction by instruction
   All YOUR variables, frames, intermediates
   created and managed on C HEAP

8. YOUR code never touches C stack
   It lives entirely in heap objects
   PVM on C stack manipulates those heap objects
```


_____
