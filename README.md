# MovieRex---Movie-Recommendation-System
MovieReX is a hybrid recommendation system that combines collaborative filtering and content-based filtering to provide personalized movie recommendations. Built using Python and the TMDB 5000 dataset, it utilizes Scikit-learn features to run Cosine similarity for both content and collaborative filtering.
How to get this running:
### 1: Go to Kaggle 
### 2: search up "TMDB 5000" and download or use the API to get the files in your instance
### 3: Do the same for "The Movies Dataset"
### 4: Upload the files to Colab or use the path to read the csv files

Important Notes:
- This project is heavily dependent on libraries, which are constantly changing. Any errors along the lines of " 'X' has no attribute 'Y' ", check online if the library still supports that method and if not, what the alternative is.
- The project may not work as intended with other datasets. If you are going to use a different dataset, some things to note are that the TMDB dataset requires us to combine 2 datasets into one. You may want to ignore this step depending on what your files look like. Make sure you keep track of which dataset the code is dealing with so that your new dataset works properly.
