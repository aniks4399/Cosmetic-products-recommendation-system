**🧴 Cosmetics Recommendation System**

**AI-Driven Ingredient Analysis for Personalized Skincare**



**📌 Project Overview**

    Choosing the right skincare product is challenging due to complex ingredient lists and varying skin requirements. This project builds a content-based recommendation system that analyzes cosmetic ingredient compositions and recommends similar products based on ingredient similarity rather than brand or price.
    
    The system uses Natural Language Processing (NLP) and machine learning techniques to analyze 1,472 cosmetic products and visually explore similarities using dimensionality reduction and interactive dashboards.

**🎯 Objectives**

    Analyze cosmetic ingredient lists using NLP techniques
    
    Identify similarities between products based on ingredient composition
    
    Visualize ingredient-based clusters using dimensionality reduction
    
    Recommend similar skincare products using cosine similarity
    
    Provide an interactive, user-friendly exploration of cosmetic data

**🧠 Key Concepts & Techniques**

    Content-Based Recommendation Systems
    
    Natural Language Processing (NLP)
    
    Feature Engineering (Bag-of-Words, One-Hot Encoding)
    
    Dimensionality Reduction (t-SNE)
    
    Interactive Data Visualization

**🛠️ Tech Stack**

Programming Language

**Python**

    Libraries & Tools
    
    Pandas – data manipulation & preprocessing
    
    NumPy – numerical computations
    
    Scikit-learn – t-SNE, cosine similarity
    
    Bokeh – interactive visualization
    
    Matplotlib – exploratory plots
    
    Regex – text cleaning

**📂 Dataset**

    Source: Sephora cosmetic product dataset
    
    Records: 1,472 products

**Key attributes:**

Product name

    Brand
    
    Ingredients
    
    Price
    
    Rating
    
    Skin-type suitability

**🔍 Methodology**

    Data Collection & Filtering
    
    Imported dataset using Pandas
    
    Filtered moisturizers suitable for dry skin
    
    Text Preprocessing
    
    Converted text to lowercase
    
    Removed special characters using regex
    
    Tokenized ingredient lists
    
    Removed common, non-informative ingredients
    
    Feature Extraction
    
    Built a Bag-of-Words model
    
    Created a document-term matrix using One-Hot Encoding
    
    Dimensionality Reduction
    
    Applied t-SNE to reduce high-dimensional ingredient space to 2D
    
    Visualization
    
    Created interactive scatter plots using Bokeh
    
    Added hover tools to display product details
    
    Recommendation Engine
    
    Used cosine similarity to recommend top similar products
    
    Returned ingredient-based alternatives to selected products

    ## 📁 Code Structure & Responsibilities

The project is organized into modular components to ensure clarity, reusability, and maintainability.

- **data/**
  - Contains raw and processed datasets (not included in the repository due to size and licensing).
  - Includes a README explaining data sources and structure.

- **notebooks/**
  - Used for exploratory data analysis (EDA), experimentation, and validation of ideas.
  - Demonstrates step-by-step reasoning behind preprocessing, feature engineering, and visualization.

- **src/**
  - Contains production-style Python modules implementing the core logic of the system:
    - `preprocessing.py`: Text cleaning and ingredient tokenization
    - `encoder.py`: One-hot encoding and document-term matrix construction
    - `recommender.py`: Similarity computation and recommendation logic
    - `visualization.py`: Interactive visualization using Bokeh

- **outputs/**
  - Stores generated artifacts such as interactive HTML visualizations.

This structure mirrors real-world analytics and data science projects and separates experimentation from reusable logic.


**📊 Results & Insights**

    Identified clusters of similar skincare formulations (gel-based vs cream-based)
    
    Found that many premium products share similar ingredient profiles with budget alternatives
    
    Observed that price does not necessarily reflect ingredient complexity
    
    Highlighted common irritants such as fragrances in products marketed as “gentle”

**🚀 How to Run the Project**
    # Clone the repository
    git clone https://github.com/your-username/cosmetics-recommendation-system.git
    
    # Navigate to the project directory
    cd cosmetics-recommendation-system
    
    # Install dependencies
    pip install -r requirements.txt
    
    # Run the notebook or script
    python main.py

**📁 Repository Structure**
cosmetics-recommendation-system/
│
├── data/
│   └── cosmetics.csv
│
├── notebooks/
│   └── analysis.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── encoder.py
│   ├── visualization.py
│   └── recommender.py
│
├── outputs/
│   └── interactive_plot.html
│
├── requirements.txt
├── README.md
└── report/
    └── Project_Report.pdf

**🔮 Future Enhancements**

    Add TF-IDF or word embeddings for richer similarity detection
    
    Incorporate user preferences (skin sensitivity, allergies)
    
    Deploy as a web application using Streamlit or Flask
    
    Integrate Power BI or dashboarding for business users


    

**👤 Author**

**Anirudha K S**  
Data Analyst | SQL | Python | Power BI  
Bengaluru, India  

