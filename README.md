# another-pid
Just Another PID controller.


# Usage
Initialize the PID controller.
```python
from another_pid import PID

pid = PID(0.5, 0.8, 1.2, time_interval=0.5, set_point=10)
```

Use the PID controller in a system.
```python
# initial value.
value = 0

while True:
  # use the value in a system.
  value = a_system(value)
  
  value = pid.next_value(value)
```
