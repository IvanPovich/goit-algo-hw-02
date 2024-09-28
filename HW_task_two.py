from collections import deque

def is_palindrome(input_str: str) -> bool:
  normalize_str = ''

  for char in input_str:
    if char != ' ':
      normalize_str += char.lower()

  dq = deque(normalize_str)

  while len(dq) > 1:
    if dq.popleft() != dq.pop():
      return False

  return True


#Вкажіть рядок для перевірки
input = "Ваш рядок"
if is_palindrome(input):
    print(f"'{input}' є паліндромом")
else:
    print(f"'{input}' не є паліндромом")
