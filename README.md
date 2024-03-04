# Uzdevums: Fibonači Skaitļi

## Apraksts

Jūsu uzdevums ir izveidot funkciju `fib` *fib.py* failā, kas aprēķina Fibonači skaitli, izmantojot rekursiju vai iterāciju. Fibonači secība sākas ar pirmajiem diviem skaitļiem 0 un 1, un katrs nākamais skaitlis secībā ir divu iepriekšējo skaitļu summa. Piemēram, pirmie desmit Fibonači skaitļi ir:
- 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

Funkcijai `fib` jāpieņem viens arguments:
- `n` (int): indekss Fibonači secībā, kur `n` ir naturāls skaitlis. Pieņemsim, ka pirmā Fibonači skaitļa indekss ir 0.

Funkcijai jāatgriež `n`-tais Fibonači skaitlis.

## Piemērs

```python
print(fib(0))  # Izvadīs 0
print(fib(1))  # Izvadīs 1
print(fib(2))  # Izvadīs 1
print(fib(10)) # Izvadīs 55
