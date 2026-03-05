# **📦 \[Project Name]**

**MVP Status:** \[e.g., v1.0-Production]

**Group Members:** Aubane JOSEPH, Anfel BOUSSOURA, Delhia KEDDAR, Joan ATTAL


## **🎯 Project Overview**

Provide a concise (2-3 sentence) description of what your application does and the specific problem it solves. Why did you build this?

This is a Tic-Tac-Toe game with three modes: Player vs Player, Player vs AI, and AI vs AI. The AI uses the Minimax algorithm to choose the best moves. The game was made to show how an AI can make smart decisions in a fun and easy-to-use interface with PyQt5.


## **🚀 Quick Start (Architect Level: < 60s Setup)**

Instructions on how to get this project running on a fresh machine.

1. **Clone the repo:**\
   git clone \[your-repo-link]\
   cd \[project-folder]

2. **Setup Virtual Environment:**\
   python -m venv .venv\
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3. **Install Dependencies:**\
   pip install -r requirements.txt

4. **Run Application:**\
   python main.py


## **🛠️ Technical Architecture**

Explain how your code is organized. An "Architect-level" README should describe the separation of concerns.

- **main.py**: Entry point of the application.

- **logic/**: Contains core algorithms and data processing.

- **ui/**: Handles user interactions (CLI/GUI).

- **utils/**: Helper functions and shared constants.


## **🧪 Testing & Validation**

How can a user verify the code works?

- List any test scripts included (e.g., pytest tests/).

- Describe the "Happy Path" inputs for the demo.


## **📦 Dependencies**

List the main third-party libraries used and _why_ they were chosen:

- library\_name: \[Reason for use]

- PyQt5: For building the GUI interface.

math: For Minimax algorithm calculations and infinite value representation.


## **🔮 Future Roadmap (v2.0)**

What features would you add if you had more time or a larger budget?

_Generated as part of the \[Course Name] Production Deliverables._

Add alpha-beta pruning for faster AI decisions.

Visualize Minimax evaluation scores per move for educational purposes.

Implement online multiplayer mode or a web version.

Add custom themes, sounds, and animations to improve UX.
__
