# **📦 \[Project Name]**

**MVP Status:** \[e.g., v1.0-Production]
 
Group Members: Attal Joan , Joseph Aubane, Keddar Delhia , Boussoura Anfel 


## **🎯 Project Overview**

Provide a concise (2-3 sentence) description of what your application does and the specific problem it solves. Why did you build this?


## **🚀 Quick Start (Architect Level: < 60s Setup)**

Instructions on how to get this project running on a fresh machine.

1. **Clone the repo:**\
   git clone \https://github.com/anfelboussoura-cloud/pbl2\
   cd \pbl2

2. **Setup Virtual Environment:**\
   python -m venv .venv\
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3. **Install Dependencies:**\
   pip install -r requirements.txt

4. **Run Application:**\
    To check it works we have to run the app, load lowbid_manche_demo.csv with the Load CSV button, the bids should show up in the table with unique prices highlighted in green. Then we hit Find Winner and it gives you the winning player. For successor/predecessor we just type a price that exists in the tree and click.


## **🛠️ Technical Architecture**

Explain how your code is organized. An "Architect-level" README should describe the separation of concerns.

- **main.py**: Entry point of the application.
  
This is the file that launches the program.
It simply creates the application window, starts the graphical interface (Tkinter) and connects everything together.
Think of it as the on/off button of the project.

- **logic/**: Contains core algorithms and data processing.
  
It contains all the important calculations and rules of the auction.
It includes :


1)    Binary Search Tree (BST)
This structure stores all bids in a smart way so the program can sort prices automatically, quickly find the lowest unique bid and find the next higher or lower price (successor / predecessor).
This makes the app fast even with many bids.


2)    Auction calculations
This part handles the cost of each bid, the total revenue earned by the seller and the winner detection. 


3)    Strategies and simulations
The app can simulate hundreds of auction rounds using different player behaviors :
-     Random bids 
-     Low bids 
-     Mid-range bids 
The simulation calculates the win rate of each strategy, the average cost per bid and the average seller revenue.
This allows us to compare strategies and see which one performs best.



- **ui/**: Handles user interactions (CLI/GUI).
  
This part is everything the user sees and interacts with.
Built with Tkinter, it provides : adding bids manually, loading bids from a CSV file, viewing the bid tree in real time, finding the winner of the auction, running large simulations, displaying results in tables.
The interface only displays information and collects user input. All calculations are done in the logic part.


- **utils/**: Helper functions and shared constants.

It contains small reusable elements such as : default parameters (base cost, alpha), shared helper functions, strategy list. This keeps the main code cleaner and avoids repetition.


## **🧪 Testing & Validation**

How can a user verify the code works?

- List any test scripts included (e.g., pytest tests/).

- Describe the "Happy Path" inputs for the demo.

To check it works we have to run the app, load a csv with the Load CSV button, the bids should show up in the table with unique prices highlighted in green. Then we hit Find Winner and it gives you the winning player. For successor/predecessor we just type a price that exists in the tree and click.

We kept everything in one file since the project isn't that big. The code is split into 4 main parts :

-Node / BST : the heart of the project, it's the binary search tree we built from scratch to store and sort the bids

-bid_cost / vendor_revenue / run_simulation : all the math and game logic, calculates costs and runs the simulations

-Strategies : the 3 bot behaviors (random, low, mid) that we use in the simulation tab

-LowBidApp : the whole interface, buttons, tables, the two tabs, everything the user sees and clicks



## **📦 Dependencies**

List the main third-party libraries used and _why_ they were chosen:

tkinter : for the interface
csv : to load the data files
random : to generate the bots' bids


## **🔮 Future Roadmap (v2.0)**

What features would you add if you had more time or a larger budget?
 If we had more time we would have loved to actually draw the Binary search tree as a real tree with nodes and branches instead of just a table, since that's kind of the whole point of the project. We also thought about adding charts to see how the strategies compare over time but we ran out of time.
