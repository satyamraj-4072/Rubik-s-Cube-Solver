# 🧩 Rubik's Cube Solver

A Python-based Rubik's Cube Solver that accepts cube colors as user input, validates the cube configuration, converts the input into the standard cube notation, and generates the optimal solution using the **Kociemba Algorithm**.

## 📌 Features

- 🎨 Accepts cube input using standard colors:
  - White (W)
  - Yellow (Y)
  - Green (G)
  - Blue (B)
  - Red (R)
  - Orange (O)
- 🔄 Automatically converts color notation to solver notation (U, R, F, D, L, B)
- ✅ Validates cube before solving
  - Ensures exactly 54 stickers
  - Checks each color appears exactly 9 times
  - Verifies unique center colors
- ⚡ Solves the cube using the Kociemba two-phase algorithm
- 📝 Displays the optimal sequence of moves

---

## 🛠️ Technologies Used

- Python 3.x
- Kociemba Solver
- Collections (Counter)

---

## 📂 Project Structure

```
Rubiks-Cube-Solver/
│
├── Rubik's_Cube_Solver.ipynb
├── README.md
└── requirements.txt (optional)
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Rubiks-Cube-Solver.git
```

Move into the project directory:

```bash
cd Rubiks-Cube-Solver
```

Install the required package:

```bash
pip install kociemba
```

---

## ▶️ Usage

Run the notebook or Python script.

Enter each face of the cube in the following order:

1. Up (White)
2. Right (Red)
3. Front (Green)
4. Down (Yellow)
5. Left (Orange)
6. Back (Blue)

Each face should be entered as **3 rows**, with **3 colors per row**.

Example:

```
Row 1: W W W
Row 2: W W W
Row 3: W W W
```

After entering all six faces, the program:

1. Converts colors into cube notation.
2. Validates the cube configuration.
3. Computes the solution.
4. Prints the solving sequence.

---

## 🎯 Color Mapping

| Color | Face |
|-------|------|
| White | U |
| Red | R |
| Green | F |
| Yellow | D |
| Orange | L |
| Blue | B |

---

## 📋 Validation Checks

The program verifies:

- Total stickers = 54
- Each face color appears exactly 9 times
- All six center pieces are unique

If validation fails, an appropriate error message is displayed.

---

## 📖 Algorithm

This project uses the **Kociemba Two-Phase Algorithm**, which efficiently computes near-optimal solutions for a Rubik's Cube.

---

## 💡 Future Improvements

- Graphical User Interface (GUI)
- 3D Cube Visualization
- Webcam/Image-based cube scanning
- Animated solution playback
- Move-by-move visualization

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

**Satyam Raj**

- GitHub: https://github.com/satyamraj-4072
