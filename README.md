
# [Linear Cryptanalysis of SPN Cipher](https://github.com/vikrant-vikram/AES)

### Explore the linear cryptanalysis of the SPN cipher in this project. Learn how we can analyze the weaknesses of cryptographic systems and improve their security.

For supplementary material, check out this [guide](https://ioactive.com/wp-content/uploads/2015/07/ldc_tutorial.pdf).

---

<div align="center">
  <img src="https://preview.redd.it/91gi221gxtc81.png?width=712&format=png&auto=webp&s=1a67c63376b7c5cdca1e9ef6fd7c2820ffd0ba89" height="500" />
</div>

---

## Instructions

### To run the linear cryptanalysis of the SPN Cipher:
```bash
python3 linear_analysis_test.py
```

### To see the output of the SPN cipher:
```bash
python3 spn_test.py
```

---

## SPN Encryption:

**Input:**
- X : `{0, 1}^lm`
- Kr : `{0, 1}^lm`

**Output:**
- Y : `{0, 1}^lm`

### Key Schedule:
1. Generates key values: `(K0, ..., KNr)`
2. Set `W0 = X`
3. For each round `r` (from 1 to `Nr-1`):
   - `Ur = Wr-1 Kr-1`
   - For each value of `i` (from 1 to `Mr`):
     - `Vri = S(Uri)`
   - Update `Wr = Vrp(1), Vrp(2), ..., Vrp(lm)`
4. For final round (`Nr`):
   - `UNr = VNr-1 KNr-1`
   - For each value of `i` (from 1 to `m`):
     - `VNri = S(UNri)`

---

## Constructing Linear Approximations

Linear approximations describe high-probability relationships between plaintext, ciphertext, and intermediate states. These approximations are derived by analyzing the S-box for biases.

### Linear Approximation of an S-box:
- **Input Tuples**: `(x1, x2, ..., xm)` where `xi` represents the values that the random variable `Xi` takes.
- **Output Tuples**: `(y1, y2, ..., ym)` where `yi` represents the values that the random variable `Yi` takes.
- The values of both inputs and outputs are `{0, 1}`.

### Computing the Probability of Linear Approximation:
The probability can be computed as follows:

- If the output tuple `(y1, ..., yn)` equals the S-box output `S(x1, ..., xm)`, then:
  ```
  Pr[X1 = x1, ..., Xm = xm, Y1 = y1, ..., Yn = yn] = 2^(-m)
  ```
- Otherwise, if the output tuple doesn't match the S-box output:
  ```
  Pr[X1 = x1, ..., Xm = xm, Y1 = y1, ..., Yn = yn] = 0
  ```

### Representing the Approximations:
Any approximation can be written as a product of the form:
```
(4i = 1 aixi) (4i = 1 biyi)
```
where `ai, bi ∈ {0, 1}`. These values can be represented using hexadecimal numbers from `0` to `F` and stored in a table known as the **Linear Approximation Table (LAT)**.

---

## Piling-Up Lemma

The Piling-Up Lemma provides a method to compute the bias of linear approximations. Here's how it works:

Consider independent random variables `X1, X2, ..., Xn`. For each random variable:
- `Pr[X1 = 0] = P1` and `Pr[X1 = 1] = 1 - P1`
- `Pr[X2 = 0] = P2` and `Pr[X2 = 1] = 1 - P2`

The bias of `X1 ^ X2` (XOR operation) is given by:
```
Pr[X1 ^ X2 = 0] = P1P2 + (1 - P1)(1 - P2)
```

We define bias values as:
```
1 = P1 - ½, 2 = P2 - ½
```

The general formula for `n` independent linear approximations is:
```
Pr[X1 ^ X2 ^ ... ^ Xn = 0] = ½ + 2^(n-1) Σ (from i=1 to n) Ci
```

The Piling-Up Lemma is valid only when the random variables are independent.

---
