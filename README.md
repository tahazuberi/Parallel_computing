# Parallel Computing Repository

This repository provides examples and tutorials on various parallel computing concepts and techniques, implemented in Python. It covers threading, multiprocessing, asynchronous programming, and inter-process communication (IPC).

## Table of Contents

1. [Basics](#1-basics)
2. [Chapter 2: Threading and Process Management](#2-chapter-2-threading-and-process-management)
3. [Chapter 3: Advanced Process Management](#3-chapter-3-advanced-process-management)
4. [Chapter 4: Message Passing Interface (MPI)](#4-chapter-4-message-passing-interface-mpi)
5. [Chapter 5: Asynchronous Programming](#5-chapter-5-asynchronous-programming)

## 1. Basics

**Files**:

- `basics.py`: Introduction to basic Python programming.
- `calculator.py`: A simple calculator program.
- `greeting.py`: Demonstrates basic input/output in Python.
- `object.py`: Basic object-oriented programming concepts.

## 2. Chapter 2: Threading and Process Management

This chapter focuses on threading, synchronization primitives, and process management.

**Files**:

- `MyThreadClass.py`, `MyThreadClassLock.py`: Threading with and without locks.
- `ProcessCreationAndManagement.py`: Managing processes in Python.
- `SynchronizationPrimitive.py`: Demonstrates various synchronization techniques.
- Other files cover topics such as semaphores, barriers, events, and threading queues.

**Required Libraries**:

- `threading`
- `multiprocessing`
- `queue`

## 3. Chapter 3: Advanced Process Management

Focuses on managing processes and inter-process communication (IPC).

**Files**:

- `spawningProcess.py`: Demonstrates how to spawn new processes.
- `communicatingwithQueue.py`, `communicatingwithPipe.py`: IPC mechanisms.
- `killingProcesses.py`: Safely terminating processes.

**Required Libraries**:

- `multiprocessing`

## 4. Chapter 4: Message Passing Interface (MPI)

Explains how to use MPI for distributed computing tasks.

**Files**:

- `scatter.py`, `gather.py`, `broadcast.py`: Basic MPI operations.
- `pointToPointCommunication.py`: Demonstrates direct communication between processes.
- `deadLockProblems.py`: Examples of common pitfalls in MPI programming.

**Required Libraries**:

- `mpi4py`

## 5. Chapter 5: Asynchronous Programming

Covers asynchronous programming using Python's `asyncio` module.

**Files**:

- `asyncioCoRoutine.py`, `asyncioAndFuture.py`: Basics of coroutines and futures.
- `asyncioEventLoop.py`: Working with the asyncio event loop.
- `asyncioTaskManipulation.py`: Managing asyncio tasks.
- `concurrent_Futures_pooling.py`: Pooling tasks with `concurrent.futures`.

**Required Libraries**:

- `asyncio`
- `concurrent.futures`

## How to Use

1. Install the required libraries:
   ```bash
   pip install mpi4py
   ```
2. Navigate to the desired chapter directory.
3. Run the scripts using Python:
   ```bash
   python <script_name>.py
   ```

## Contributions

Feel free to contribute by submitting issues or pull requests to improve the examples or add new content.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
