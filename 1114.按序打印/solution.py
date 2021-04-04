# !/usr/bin/python
# -*- coding: utf-8 -*-

# author      : Tao Qitian
# email       : taoqt@mail2.sysu.edu.cn
# datetime    : 2021/4/4 17:36
# filename    : solution.py
# description : LC 1114 按序打印

import queue
import threading
import time


class Foo:
    """ While 循环 """

    def __init__(self):
        self.first_done = False
        self.second_done = False

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.first_done = True

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # 正常情况下，while 循环会跑满 CPU，影响 GIL 线程上下文切换的判定，导致超时
        # time.sleep 会把 CPU 交还给 GIL，可以让 GIL 及时切换线程，即使 sleep 很短的时间
        while not self.first_done:
            time.sleep(1e-5)
        printSecond()
        self.second_done = True

    def third(self, printThird: 'Callable[[], None]') -> None:
        while not self.second_done:
            time.sleep(1e-5)
        printThird()


class Foo2:
    """ threading.Condition """

    def __init__(self):
        self.first_done = False
        self.second_done = False
        self.condition = threading.Condition()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        with self.condition:
            printFirst()
            self.first_done = True
            self.condition.notify_all()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.condition:
            self.condition.wait_for(lambda: self.first_done)
            printSecond()
            self.second_done = True
            self.condition.notify_all()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.condition:
            self.condition.wait_for(lambda: self.second_done)
            printThird()
            self.condition.notify_all()


class Foo3:
    """
    threading.Lock
    添加阻塞，然后释放线程，只是类初始化的时候不能包含有参数，
    所以要写一句 acquire 进行阻塞，调用其他函数的时候按顺序 release 释放
    """

    def __init__(self):
        self.first_lock = threading.Lock()
        self.first_lock.acquire()
        self.second_lock = threading.Lock()
        self.second_lock.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.first_lock.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.first_lock.acquire()
        printSecond()
        self.second_lock.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.second_lock.acquire()
        printThird()


class Foo4:
    """ threading.Semaphore """

    def __init__(self):
        self.first_semaphore = threading.Semaphore(0)
        self.second_semaphore = threading.Semaphore(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.first_semaphore.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.first_semaphore.acquire()
        printSecond()
        self.second_semaphore.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.second_semaphore.acquire()
        printThird()


class Foo5:
    """ threading.Event 用 wait 方法作为阻塞，用 set 来释放线程，默认类赋值就是阻塞的 """

    def __init__(self):
        self.first_event = threading.Event()
        self.second_event = threading.Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.first_event.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.first_event.wait()
        printSecond()
        self.second_event.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.second_event.wait()
        printThird()


class Foo6:
    """
    threading.Barrier
    Barrier 初始化的时候定义了 parties = 2 个等待线程，调用完了 parties 个 wait 就会释放线程
    """

    def __init__(self):
        self.first_barrier = threading.Barrier(2)
        self.second_barrier = threading.Barrier(2)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.first_barrier.wait()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.first_barrier.wait()
        printSecond()
        self.second_barrier.wait()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.second_barrier.wait()
        printThird()


class Foo7:
    """
    queue.Queue()
    直接使用多线程专用的阻塞队列，对于队列为空时，get方法就会自动阻塞，直到put使之非空才会释放进程
    """

    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.q1.put(0)

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.q1.get()
        printSecond()
        self.q2.put(0)

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.q2.get()
        printThird()


class Foo8:
    """
    对于定容队列来说，如果队列满了，put 方法也是阻塞。
    """

    def __init__(self):
        self.q1 = queue.Queue(1)
        self.q1.put(0)
        self.q2 = queue.Queue(1)
        self.q2.put(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.q1.get()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.q1.put(0)
        printSecond()
        self.q2.get()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.q2.put(0)
        printThird()
