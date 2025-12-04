# Advanced Concepts

Advanced Python programming paradigms and patterns. This section covers object-oriented programming, functional programming, concurrency, and advanced Python features.

## 📂 Contents

### [Object-Oriented Programming (OOP)](./OOP/)
Master classes, objects, and object-oriented design.

#### Core OOP Concepts
- **class_definition.py** - Class vs instance attributes, __init__, methods
- **class_and_function_example.py** - Combining classes with functions
- **creating_class_example.py** - Step-by-step class creation
- **another_class_example.py** - Additional class examples
- **objects_and_classes.py** - Fundamental OOP concepts

#### Inheritance
- **class_inheritance.py** - Before inheritance (code duplication problem)
- **class_hierarchy.py** - Refactored with inheritance
- **class_inheritance_example.py** - Inheritance basics
- **class_inheritance_example2.py** - Advanced inheritance
- **python_class_inheritance.py** - Python-specific inheritance
- **python_class_inheritance2.py** - More inheritance patterns
- **implicit_class_ineritance.py** - Implicit inheritance from object
- **complex_class_inheritance.py** - Multi-level inheritance
- **multiple_inheritance.py** - Multiple parent classes
- **class_inheritance_overriden.py** - Method overriding

#### Advanced OOP
- **abstract_base_classes.py** - ABC module for abstract classes
- **abstract_classes_and_interfaces.py** - Interfaces in Python
- **class_interface_example.py** - Interface implementation
- **python_dataclass.py** - Modern dataclasses (@dataclass decorator)
- **dataclasses_default_values.py** - Default values in dataclasses
- **immutable_dataclasses.py** - Frozen dataclasses
- **python_postinit.py** - __post_init__ in dataclasses
- **class_level_and_static_methods.py** - @classmethod and @staticmethod
- **class_methods_example.py** - Class methods usage
- **properties_and_methods.py** - @property decorator

#### Special Methods
- **magic_methods.py** - Dunder methods (__str__, __repr__, etc.)
- **magic_attributes.py** - Special attributes
- **magic_calls.py** - __call__ method
- **equality_and_comparison.py** - __eq__, __lt__, etc.

#### Design Patterns
- **object_composition.py** - Composition over inheritance
- **flight_booking_system.py** - Real-world OOP example

**Projects:**
- **coffee_machine/** - Coffee machine simulation
- **pong_game/** - Classic Pong game
- **quiz_game/** - Interactive quiz application
- **snake_game/** - Snake game implementation
- **turtle_crossing_game/** - Road crossing game
- **turtle_race/** - Turtle racing game

---

### [Decorator Functions](./decorators/)
Function decorators and metaprogramming.

#### Core Decorator Concepts
**Basic Patterns:**

#### More Examples:
- **decorator_func_blueprint.py** - Blueprint for conditional decorators, guard patterns
- **decorator_classes.py** - Class-based decorators, __call__, state management
- **decorators_with_classes.py** - Decorators using classes, call counting, statistics
- **classmethod_decorator.py** - Using @classmethod as a decorator
- **static_method_decorator.py** - Using @staticmethod as a decorator
- **property_decorator.py** - Using @property for managed attributes
- **python_decorators.py** - General decorator examples
- **python_decorators2.py** - Additional decorator patterns

#### Practical Decorators

#### More Practical Examples:
- **decorator_munching.py** - Parameterized decorators, decorator factories
- **decorators_usecases.py** - Real-world patterns: authentication, logging, configuration

#### Advanced Patterns

#### Other Examples:
- **decorator_munching.py** - Parameterized decorators, decorator factories
- **decorator_metadata.py** - Metadata preservation with functools.wraps
- **decorator_timing_func.py** - Timing function execution
- **html_decorator_styling.py** - HTML output styling with decorators

**Common Decorators:**

---

### [Generator Functions](./generator_func/)
Lazy evaluation with generators.

- **generator_function.py** - Countdown generator with yield
- **generator_function2.py** - Additional generator examples
- **generator_function3.py** - Advanced generator patterns
- **generator_function_example.py** - Practical generator use cases

**Key Concepts:** yield, next(), generator expressions, memory efficiency

---

### [Lambda Functions](./lambda_func/)
Anonymous functions and functional programming.

- Lambda syntax and usage
- Using lambda with map(), filter(), reduce()
- When to use lambda vs def
- Functional programming patterns

---

### [Dunder Methods](./dunder_methods/)
Magic methods for operator overloading.

- Special method implementations
- Operator overloading
- Custom object behavior
- String representation methods

---

### [Async Programming](./asyncio/)
Asynchronous programming with asyncio.

- **asyncio_coroutines.py** - Async/await basics with detailed docstrings
- **asyncio_tasks_1.py** - Creating and managing tasks
- **asyncio_tasks_2.py** - Advanced task patterns
- **asyncio_taskgroups.py** - Task groups (Python 3.11+)
- **synchronization_primer_1.py** - Locks and synchronization
- **synchronization_primer_2.py** - Events and coordination
- **semaphore_primers.py** - Semaphore usage
- **bounded_semaphore_primer.py** - Bounded semaphores
- **future_primer.py** - Futures and promises

**Key Concepts:** async/await, coroutines, tasks, event loop, concurrency

---

### [Multiprocessing](./multiprocessing/)
Parallel processing with multiple CPU cores.

- **main.py** - Multiprocessing basics
- Process pools
- Inter-process communication
- Shared memory

**Key Concepts:** Process, Pool, Queue, parallel execution

---

### [Multithreading](./multithreading/)
Concurrent execution with threads.

- **multithreading_demo.py** - Threading basics
- Thread synchronization
- Locks and semaphores
- Thread-safe code

**Key Concepts:** Thread, Lock, threading module, GIL limitations

---

### [Exception Handling](./exception_handling/)
Error handling and custom exceptions.

- **exception_handling_examples.py** - try/except/finally patterns
- Custom exception classes
- Exception hierarchy
- Best practices for error handling

**Key Concepts:** try/except/else/finally, raise, custom exceptions

---

### [Call Stack](./call_stack/)
Understanding the call stack and recursion.

- **abcd_callstack_example.py** - Call stack visualization
- **stack_example.py** - Stack data structure
- **deque.py** - Double-ended queue

**Key Concepts:** Stack frames, recursion depth, stack overflow

---

### [Pattern Matching](./pattern_matching/)
Structural pattern matching (Python 3.10+).

- **pattern_matching.py** - match/case syntax
- Matching sequences, mappings, classes
- Guards and wildcards

**Key Concepts:** match statement, case patterns, structural matching

---

## 🎯 Learning Path

### Beginner to Intermediate
1. **OOP basics** - Classes, objects, inheritance
2. **Decorators** - Start with simple decorators
3. **Generators** - Understand yield and lazy evaluation
4. **Exception Handling** - Robust error handling

### Intermediate to Advanced
5. **Advanced OOP** - Dataclasses, abstract classes, composition
6. **Async Programming** - Coroutines and concurrent code
7. **Multithreading/Multiprocessing** - Parallel execution
8. **Pattern Matching** - Modern Python syntax

## 💡 Tips

- **OOP**: Favor composition over inheritance
- **Decorators**: Use @wraps to preserve metadata
- **Generators**: Great for large datasets or infinite sequences
- **Async**: Use for I/O-bound operations
- **Multiprocessing**: Use for CPU-bound operations
- **Multithreading**: Be aware of GIL limitations in Python

## ⚡ Performance

- Generators use less memory than lists
- Async is faster than threading for I/O
- Multiprocessing bypasses the GIL
- Decorators add minimal overhead
- Dataclasses are faster than regular classes
