---
date: 2026-08-30
time: "19:34:11+05:30"
---
# Topics 

- Multiple Language Projects
- Mechanism
- Game Engines
- ML Implementations

_____________


# MultiLang Projects 

Python is slow for heavy computation. C is fast but painful to write. So the real world does this:

```
Write the easy logic in Python
Write the performance critical parts in C/C++
Make them talk to each other
```

- This is exactly what **numpy, tensorflow, opencv** do. The Python API you use is just a thin wrapper. The actual math happening underneath is C/C++.

## MECHANISM 1 : FFI (Foreign Function Interface)

The most fundamental concept. A way for one language to call functions written in another language.

The key insight is:

```
At the end of the day EVERYTHING becomes machine code.
Machine code has no idea what language wrote it.
If you know WHERE a function lives in memory
and WHAT arguments it expects
you can call it from anywhere.
```


______

## MECHANISM 2 : Python C Extensions

Python is written in C. So Python has a built in way to call C code directly.


```
Python calls fast_add(5, 10)
      |
      | Python passes PyObject* pointers
      |
   C function receives them
   PyArg_ParseTuple extracts raw C integers from PyObjects
   C does the math (pure machine code speed)
   PyLong_FromLong wraps result back into PyObject
      |
      | returns PyObject* back to Python
      |
   Python receives it normally
```

- The conversion at the boundary (PyObject <-> C types) has a small cost. But if C is doing heavy work, this cost is negligible.

---

## MECHANISM 3 : ==ctypes== (Calling ANY compiled library)

You do not even need to write Python-aware C. You can call ANY compiled `.so` or `.dll` file.

Say you have this C code compiled into a shared library:

c

```c
// math_lib.c
int multiply(int a, int b) {
    return a * b;
}

double square_root(double x) {
    return x * x;  // simplified
}
```

Compile it:

bash

```bash
gcc -shared -fPIC -o math_lib.so math_lib.c
```

Call it from Python with zero changes:

python

```python
import ctypes

# load the compiled library
lib = ctypes.CDLL("./math_lib.so")

# tell Python what types the function expects and returns
lib.multiply.argtypes = [ctypes.c_int, ctypes.c_int]
lib.multiply.restype  = ctypes.c_int

# call it -- this is running compiled C machine code
result = lib.multiply(6, 7)
print(result)   # 42
```

The OS loads the `.so` into memory. ctypes finds the function by name in that memory. Calls it directly. Pure C speed.

---

### HOW NUMPY USES THIS

This is the real example that matters.

python

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
result = np.sum(arr)
```

What actually happens:

```
np.sum(arr)
    |
    Python layer -- just finds the right C function
    |
    calls _multiarray_umath.so  (compiled C/Fortran library)
    |
    C code iterates over raw memory directly
    no PyObject overhead per element
    SIMD CPU instructions (processes multiple numbers simultaneously)
    |
    returns result as PyObject back to Python
```

==The array data itself is stored as **raw C memory**==, not as Python objects:

python

```python
import numpy as np
import sys

# Python list -- each element is a full PyObject (28 bytes each)
python_list = [1, 2, 3, 4, 5]
print(sys.getsizeof(python_list[0]))   # 28 bytes per int

# Numpy array -- raw C memory, 4 bytes per int
numpy_arr = np.array([1, 2, 3, 4, 5], dtype=np.int32)
print(numpy_arr.itemsize)              # 4 bytes per int
```

Numpy bypasses Python's object system entirely for the data. That is its entire secret.


_______

## MECHANISM 4 : ==SUBPROCESS (Completely Separate Processes)==

Sometimes languages do not share memory at all. They run as separate processes and communicate.

python

```python
import subprocess

# Run a compiled C++ binary from Python
result = subprocess.run(
    ["./my_cpp_program", "arg1", "arg2"],
    capture_output=True,
    text=True
)

output = result.stdout
print(output)
```

```
Python Process              C++ Process
--------------              -----------
runs normally               compiled binary
calls subprocess.run()  --> OS spawns new process
waits...                    C++ does heavy work
receives stdout  <--------- C++ prints result
continues                   process exits
```

No shared memory. Communication via ==stdin/stdout/files/sockets.== Clean separation. Used a lot in data pipelines.

_____

## MECHANISM 5 : ==SHARED MEMORY (Processes sharing RAM directly)==

Two processes, different languages, looking at the same memory block:

python

```python
# Python side
import mmap
import struct

# create shared memory block
shm = mmap.mmap(-1, 1024)

# write data into it
shm.write(struct.pack('ii', 42, 100))   # two integers
shm.seek(0)
```

c

```c
// C side reads the same memory block
int* data = (int*)shared_memory_pointer;
int a = data[0];   // 42
int b = data[1];   // 100
```

Both processes see the same RAM. No serialization needed. Very fast.

_______


## Boundaries 

Every time data crosses the language boundary there is a cost:

```
Python int (PyObject, 28 bytes)
    |
    | -- conversion cost --
    |
C int (4 bytes)
    |
    | -- conversion cost --
    |
Python int (PyObject, 28 bytes)
```

This is called ==**marshalling** or **serialization**.== The trick is:

```
Make the C side do enough work that the
boundary crossing cost is worth it.

Crossing boundary to add 2 numbers = NOT worth it
Crossing boundary to process 1 million numbers = absolutely worth it
```

This is why numpy works on whole arrays, not element by element.


_______

# Game Engines 

>Que : i heard a thing where it fits : the pyhthon acts a a programming layer but when it interpreats it has a kwy value map that is exposed from where it retrieves use values that values are modiefiwd or done my compiled languages and changed up hter or caluclated and used ; second is the compiled can also read form this and they read form there and the pyhton interface can act as flexible pannel or like external file or storage source but programmable , used in game engins to avoid recompilation at each chage

```
Python as a SCRIPTING LAYER
on top of a compiled ENGINE\

C++ Engine                    Python Layer
----------                    ------------
Does heavy work               Controls WHAT the engine does
Rendering, Physics            Game logic, Rules, Configs
Memory management             Easy to change, no recompile
Fixed, compiled               Flexible, interpreted at runtime
```

- The key-value map you are describing is essentially the ==**shared state / binding layer**== between Python and the compiled world.

### The Key Value Tables

This is real. It is called the **scripting context** or **binding table**.

The compiled engine exposes a table. Python reads and writes to it. The engine reads from it too.

Conceptually:

```
Shared State Table
------------------
"player_health"   ->  100
"player_speed"    ->  5.5
"enemy_count"     ->  12
"gravity"         ->  9.8
"level_name"      ->  "dungeon_01"
```

Python can modify this:

python

```python
# Python script -- game designer writes this
state["player_speed"] = 8.0       # player got a powerup
state["gravity"] = 4.9            # low gravity zone
state["enemy_count"] = 0          # all enemies defeated
```

C++ engine reads this every frame:

cpp

```cpp
// C++ engine -- runs at 60fps
float speed   = state["player_speed"];   // reads 8.0
float gravity = state["gravity"];        // reads 4.9
int   enemies = state["enemy_count"];    // reads 0

// uses these values in physics, rendering, AI
player.velocity = speed * direction;
rigidbody.gravity = gravity;
```

Neither side needs to know HOW the other side works. They just share the table.

______
Without scripting layer:

```
Game Designer wants to change player speed
      |
      | edit C++ source code
      | wait for compilation (can take minutes to hours)
      | restart game
      | test
      | wrong value, repeat
      |
      -> 1 change = 10 minutes lost
```

With Python scripting layer:

```
Game Designer wants to change player speed
      |
      | edit player_speed = 8.0 in Python script
      | save file
      | game reloads the script INSTANTLY (no recompile)
      | test
      |
      -> 1 change = 5 seconds
```

The C++ engine never changed. It just reads different values from the shared state.

_______
### PYTHON AS EXTERNAL CONFIG

You also described Python as an **external programmable config file**. This is also real and has a name:

==**Python as a configuration language** or **DSL (Domain Specific Language)**.==

Instead of a static config file like JSON:

json

```json
{
    "player_speed": 5.5,
    "gravity": 9.8,
    "enemies": ["goblin", "troll"]
}
```

You use a Python file that IS the config ==but can also have logic:==

python

```python
# config.py -- this is executable, not just data
player_speed = 5.5
gravity = 9.8

# JSON cannot do this -- logic in config
if DIFFICULTY == "hard":
    player_speed = 3.0
    enemy_count  = 50
else:
    player_speed = 5.5
    enemy_count  = 20

# JSON cannot do this either -- computed values
jump_force = player_speed * 2.2
```

C++ reads this at startup or reload:

cpp

```cpp
// load and execute the Python config
PyRun_SimpleFile("config.py");

// read values out
float speed = get_python_float("player_speed");
float grav  = get_python_float("gravity");
```

Change the config, restart or hot-reload, new behavior. Zero recompilation.

---

### FULL ARCHITECTURE 

```
+--------------------------------------------------+
|              Python Scripting Layer              |
|                                                  |
|  game_logic.py    config.py    ai_behavior.py    |
|       |                |            |            |
|  game rules       settings      enemy AI         |
|  easy to edit     no recompile  designers write  |
+--------------------|----|------------------------+
                      |    |
              get/set |    | read/write
                      |    |
+--------------------|----|------------------------+
|         Shared State / Binding Table             |
|                                                  |
|   "player_speed"  ->  5.5                        |
|   "gravity"       ->  9.8                        |
|   "level"         ->  "dungeon_01"               |
|   "enemy_health"  ->  100                        |
+--------------------------------------------------+
                      |    |
              read     |    |  read + heavy compute
                      |    |
+--------------------------------------------------+
|              C++ Engine Layer                    |
|                                                  |
|   Physics     Renderer     Audio     Networking  |
|   60fps       GPU calls    Fast IO   Low latency |
|                                                  |
|   compiled, fast, never changes often            |
+--------------------------------------------------+
```



COMPILED calling INTERPRETED
-----------------------------
Mechanism: EMBED the interpreter
The compiled code includes the interpreter as a library
Compiled code drives the interpreter
Example: Godot engine embeds GDScript interpreter
         Neovim embeds Lua interpreter
         Your game engine embeds Python


INTERPRETED calling COMPILED
-----------------------------
Mechanism: FFI (Foreign Function Interface)
You do NOT embed a compiler (compiler translates, does not run)
Instead: create a function structure the interpreter understands
Insert it into the interpreter's function table
Interpreter calls it like any native function
Example: Python calling C via ctypes or C extensions
         numpy calling C/Fortran routines


## ML Implementation

### AI/ML ARCHITECTURE

```
Library         Python Layer        Compiled Layer
-------         ------------        --------------
NumPy           np.sum()            C + Fortran (BLAS)
TensorFlow      tf.matmul()         C++ + CUDA (GPU code)
PyTorch         torch.mm()          C++ + CUDA
OpenCV          cv2.resize()        C++ optimized routines
Pandas          df.groupby()        C + Cython
scikit-learn    model.fit()         C + Cython + Fortran
```

When you call `torch.mm(a, b)` to multiply two matrices:

```
Python: torch.mm(a, b)
   |
   crosses the boundary
   |
C++: launches optimized matrix multiply
   |
CUDA (if GPU): runs thousands of parallel threads on GPU
   |
result wrapped back as PyObject (torch.Tensor)
   |
Python receives it
```

You are writing Python. The actual computation is C++ and CUDA assembly. This is not an implementation detail. This is the entire reason these libraries exist.

### Py vs C

```c
# YOUR loop -- pure Python
total = 0
for i in range(1_000_000):
    total += i
# Every iteration: PyObject creation, refcount, type lookup
# 1 million * ~100 C operations = slow

# NUMPY -- crosses the boundary once
import numpy as np
arr = np.arange(1_000_000)
total = np.sum(arr)
# ONE boundary crossing
# C iterates over raw contiguous memory
# No PyObjects per element
# SIMD instructions (CPU processes 4-8 numbers simultaneously)
# fast
```


> =="every interpreted language project is already a multi-language project. We just don't notice the compiled part because it comes pre-compiled"==

In ML this is literally your entire stack:

```
You think you are writing Python.
You are actually orchestrating:
   - C routines (numpy, scipy)
   - C++ routines (pytorch core)
   - CUDA kernels (GPU computation)
   - Fortran routines (BLAS linear algebra)
   - Sometimes assembly (hand-optimized SIMD)

Python is the conductor.
Everything else is the orchestra.
```

Understanding this tells you:

```
- Why profiling Python code misses the real bottlenecks
- Why memory layout affects training speed
- Why moving data between CPU and GPU is expensive
- Why writing Python loops inside training is catastrophic
- Why frameworks push you toward their ops instead of raw Python
```
______
_______
____


# Summary

> From [[Python-LowLevelExecution]] & [[Python-MultilangIntegration]]

---

Python is an ==interpreted language==, meaning unlike compiled languages such as C and C++ which go through a multi-stage pipeline -- preprocessor, compiler, assembler, linker -- converting your source code all the way down to native machine code that the CPU executes directly, Python never becomes machine code in the traditional sense. Instead, when you run `python3 script.py`, you are not running your script at all. You are running CPython, a compiled C binary sitting on your disk, and handing your `.py` file to it as data -- exactly like handing an `.mp4` to VLC or an `.xlsx` to Excel. Your script is not a program. It is data that another program processes on your behalf.

CPython, being a C program, first reads your `.py` file as raw text -- just a stream of characters -- and passes it through a ==lexer== which breaks that text into labeled tokens like ==NAME, EQUAL, PLUS, NUMBER==. These tokens still have no meaning or structure, just categories. The ==parser== then takes those tokens and builds an AST, an ==Abstract Syntax Tree==, which is a tree data structure that encodes the structure and relationships of your code. The tree is critical because flat text cannot express things like operator precedence -- the tree's nesting IS the precedence. `z = x + y * 2` becomes a tree where `y * 2` is a deeper subtree that must be evaluated before the addition, and this structure is what makes ==ambiguity impossible==. Everything in Python is a tree -- every expression, every if statement, every function call -- one giant tree with a root node at the top.

The compiler then walks this AST in post-order traversal, meaning leaves first and root last, and emits bytecode -- a flat serialized sequence of simple numbered instructions called ==opcodes== meant not for the CPU but for the ==Python Virtual Machine==. Bytecode is the middle layer. It is not human code and not machine code. It sits in between, architecture-neutral, portable across any OS or CPU as long as a PVM exists there. You can see this bytecode yourself using `dis.dis()` and you will see instructions like `LOAD_FAST`, `BINARY_OP`, `STORE_FAST` -- each one is just a number like 124 or 122, and the `dis` module translates those numbers into readable names. This bytecode gets cached in `__pycache__` as `.pyc` files so Python skips recompilation if the source has not changed.

Now the PVM runs. The Python Virtual Machine is not a separate program -- it is a C function inside CPython called `_PyEval_EvalFrameDefault()` which runs a giant while loop, reads each opcode number one by one, and does a switch-case to find the corresponding C function that handles that opcode. This C function runs on CPython's own C stack -- the real OS stack. But here is the critical separation: your Python code never touches the C stack. Everything belonging to your code lives on the C heap. CPython has its own memory allocator called ==pymalloc== sitting on top of the C heap, managing memory in arenas divided into pools divided into blocks, and every single thing in your Python world is allocated from there.

The most fundamental thing in this heap-world is the ==PyObject== -- a C struct that is the universal wrapper for every value in Python. When you write `x = 10` in C, that is 4 bytes on the stack holding the raw integer. When you write `x = 10` in Python, that creates a PyObject struct on the heap containing a reference count, a pointer to the type object, and the actual value -- ==roughly 28 bytes minimum.== Every integer, string, list, function, class -- ==everything is a PyObject== on the heap. Variables in Python are not memory boxes like in C. They are names bound to pointers that point at these PyObjects. When you write `y = x`, both names point to the same PyObject. When you mutate a mutable object through one name, the other name sees the change because they both point to the same heap struct.

Python's call stack -- what you think of as function calls -- is also not the real OS stack. Each function call creates a ==PyFrameObject== on the heap containing the local variables, a pointer to the bytecode, a pointer back to the calling frame, and crucially an evaluation stack which is just an array of PyObject pointers inside the frame. When the PVM executes bytecode, it pushes and pops PyObject pointers on this eval stack to handle intermediate values. So when you compute `z = (x + y) * (a + b)`, the intermediate result of ==`x + y` is a brand new PyObject allocated on the heap,== pushed onto the eval stack, sitting there while `a + b` is computed as another new PyObject, and then both are popped when the multiplication runs, both their reference counts drop to zero, and CPython immediately frees them. This is reference counting -- every PyObject tracks how many names or containers point to it, and the moment that count hits zero the memory is freed instantly without waiting for a garbage collector. For circular references that reference counting cannot handle, Python has a separate cyclic garbage collector.

PyFrameObjects form a ==linked list on the heap== -- each frame's `f_back` pointer points to the calling frame -- so Python's call stack is a chain of heap objects, not the OS stack. This is why Python can do things C cannot: you can inspect live frames at runtime with `inspect.currentframe()`, you can suspend frames mid-execution for generators with `yield`, you can resume them later -- none of which is possible with real OS stack frames that are raw memory the program cannot introspect.

The execution of bytecode maps directly to the AST's post-order traversal. Leaves of the expression tree become the first `LOAD` instructions, internal nodes become operation instructions, and the root becomes the final store. The tree structure is preserved in the bytecode's ordering -- the bytecode IS the tree serialized into a flat instruction list. This is different from C where the AST exists only at compile time, is used to emit machine code, and is then discarded completely. At C runtime there is no tree, no type information, no variable names -- just raw CPU instructions operating on registers and stack memory directly. In Python the tree's ghost lives on in the bytecode and the PVM knows variable names, line numbers, and types at runtime.

This brings the fundamental performance difference: a ==C addition is 3 CPU instructions== operating on registers inside the chip. A Python addition is roughly a hundred or more C operations -- loading PyObjects from heap memory, doing a type lookup on `ob_type`, finding the `__add__` method in a method table, calling it, checking the argument's type compatibility, extracting the raw numbers, doing the C-level addition, allocating a new PyObject for the result on the heap, updating reference counts, and returning the new PyObject. The heap allocation, cache misses from scattered PyObjects, and dynamic type dispatch at every single operation is why ==Python is 30 to 100 times slower== than C for raw computation.

But this is where the architecture becomes intelligent rather than just a limitation. Because CPython is itself a compiled C program, it can be extended by more compiled C code. CPython deliberately exposes a public API through `Python.h` that defines how external C code must structure functions and values to be callable from Python. The key insight the video by George confirms is that the interpreter stores everything -- variables, functions, types -- in internal data structures, primarily hashmaps. Variables live in a hashmap keyed by name. Functions live in a function table. Since the interpreter is written in C and C code can access these same hashmaps, compiled C code can read values Python defined, write new values Python can then see, and register C functions into Python's function table so Python calls them as if they were native. You do not mix Python with C -- you mix C with the interpreter. You compile your C code as a ==dynamic shared library `.so` or `.dll`,== and when Python does `import yourmodule`, CPython asks the OS to load that library into its memory space at runtime, making those C functions available in Python's namespace without recompiling CPython itself.

This is the entire secret of ==NumPy, PyTorch, TensorFlow, OpenCV, Pandas,== and every high-performance Python library. The Python API you call -- `np.sum()`, `torch.mm()`, `cv2.resize()` -- is a thin wrapper that crosses the language boundary once, hands data to ==compiled C, C++, Fortran, or CUDA code==, which operates on raw contiguous memory with no PyObject overhead per element, often using SIMD CPU instructions that process multiple numbers simultaneously or launching thousands of parallel threads on a GPU, and then wraps the result back as a PyObject to return to Python. A Python loop over a million elements creates a million PyObjects, does a million type lookups, a million heap allocations. NumPy's `sum` crosses the boundary once and runs a tight C loop over raw 4-byte integers in contiguous memory that the CPU cache loves. The difference is not a constant factor -- it is architectural.

The opposite direction -- compiled code embedding an interpreter rather than extending one -- is how game engines work, exactly as George's video demonstrates. The C++ engine handles rendering, physics, audio -- performance critical work compiled to machine code running at full CPU speed. Embedded inside is a Python or Lua interpreter, and game logic, enemy behavior, gravity values, player speed, color configurations -- everything a designer changes frequently -- lives in interpreted scripts. Those scripts read from and write to the interpreter's variable hashmap. The compiled engine reads those same values every frame. Change the script, restart, see the change. No recompilation of the engine. ==This is the exact architecture of Godot with GDScript, Neovim with Lua, Civilization IV with Python, and Blender with Python==. The scripting layer is not a toy addition -- it is a deliberate architectural decision to separate what must be fast from what must be flexible.

The GIL -- ==Global Interpreter Lock== -- is a consequence of this entire architecture. Because every PyObject has a reference count that multiple threads could modify simultaneously, and because corrupting that count would silently destroy memory safety, CPython uses a mutex ensuring only one thread executes Python bytecode at a time. Real OS threads are used but only one runs Python at any moment. This makes Python threads ==useless for CPU-bound parallelism== -- for that you use multiprocessing which spawns separate processes each with their own CPython instance, their own heap, their own GIL, communicating via IPC. For IO-bound work -- waiting for network or disk -- threads work fine because the GIL is released during IO waits.

Everything connects back to one architectural truth: ==Python is a C progra==m that treats your code as data, builds a tree from it, serializes that tree into bytecode, and interprets that bytecode through a software stack and heap that live entirely inside the C heap, separate from the OS stack the PVM machinery runs on. The compiled world and the interpreted world coexist through a shared hashmap and a public API, the compiled side doing computation at machine speed and the interpreted side doing orchestration at human speed. For AI and ML this is not background knowledge -- it is the explanation for every performance decision, every vectorization requirement, every GPU transfer cost, and every reason you never write Python loops over data when a library op exists. You are always writing Python but you are always running C.