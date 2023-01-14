# worksheet1-ASP
Click on the following to the each task:-  
[Task 1](#task-1)<br />
[Task 2](#task-2)<br />
[Task 3](#task-3)<br />

## Task 1




```
template <typename T>
    T* alloc (int num) {

        if (head + sizeof(T)*num <= base + Size) {
            head = head +sizeof(T)*num;

            return (T*)head;
        }
        return nullptr;
    }
    void *realloc(void *ptr, size_t size);
};
```

![taskone](images/sc.png)
![taskone](images/foonyeecust.png)
