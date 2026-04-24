# BN-MultiLabel: Synthetic Data Pipeline & Benchmark for Bangla News Classification

[](https://www.python.org/)
[](https://flask.palletsprojects.com/)
[](https://huggingface.co/)
[](https://render.com/)

An experiment to find the best model for multi-label news classifier designed to categorize Bangla news articles into various distinct labels. This project utilizes a  synthetic labeling pipeline and benchmarks multiple transformer architectures to achieve high-performance inference.

-----

## Project Overview

The mission of this project is to develop a lightweight yet highly accurate news classifier for the Bangla language that can eventually run in edge environments.

### Key Highlights:

  - **The Dataset:** Scraped **47,000+** news articles from *Bangladesh Pratidin*.
  - **Synthetic Labeling:** Leveraged **Gemma 3 27B** to assign and re-evaluate labels across a taxonomy of 45 categories.
  - **Model Benchmarking:** Comparative study between **Bangla BERT**, **Bangla T5**, and **Gemma 270m**.
  - **Production Ready:** Deployed via **Flask** on **Render**, utilizing the **Hugging Face Inference API** for the backend.

-----

## Benchmarking & Performance

We conducted extensive experiments on Kaggle to find the most efficient model for deployment. While Gemma 270m showed promise, **Bangla BERT** provided the most stable and balanced performance for multi-label classification.

<img width="1188" height="590" alt="download" src="https://github.com/user-attachments/assets/d31bb36f-da42-4686-8890-5c869a5081b6" />

<br>



| Model | F1-Micro | F1-Macro | Accuracy |
| :--- | :---: | :---: | :---: |
| **Bangla BERT** | 0.814 | 0.631 | 0.361 |
| **Bangla T5** | **0.861** | **0.716** | **0.443** |
| **Gemma 3 270m** | 0.763 | 0.612 | 0.417 |

*Note:* 
- Although Bangla T5 led in metrics, Bangla BERT was selected for the current deployment phase due to its optimized inference speed for the news classifier architecture. 
- All fine tuned models are available on Hugging Face.


-----

## The Pipeline

1.  **Scraping:** 47k articles collected from Bangladesh Pratidin via custom Kaggle scripts.
2.  **Preprocessing:** Text cleaning, noise removal, and normalization.
3.  **Synthetic Annotation:** - Defined a set of 45 labels.
      - Used **Gemma 3 27B** to pair news text with correct labels.
      - Implemented a "Re-evaluation" step where the model checked its own labeling logic for consistency.
4.  **Training:** Fine-tuned models on the synthetically labeled dataset using Kaggle's GPU environment.
5.  **Deployment:** Integrated the best-performing weights into a Hugging Face Space, served through a Flask Web UI.

*Note: All notebooks are available in the notebooks folder of the repo.*

-----

## Project Structure

```text
├── notebooks/
│   ├── link-scraper-part-1.ipynb          # Article URL discovery
│   ├── news-scraping-part-1.ipynb        # Content extraction from Bangladesh Pratidin
│   ├── data-cleaning-part-2.ipynb        # Preprocessing and text normalization
│   ├── dataset-creation.ipynb            # Final 47k article compilation
│   ├── data-annot-part-1.ipynb           # Synthetic labeling via Gemma 3 27B
│   ├── bert_model_training.ipynb         # Bangla BERT training (deployed)
│   ├── bangla_t5_model_training.ipynb    # T5 benchmarking
│   └── gemma_3_model_training.ipynb      # Gemma 270m benchmarking
├── templates/
│   └── home.html                        # Main Web Interface
├── app.py                               # Flask Application Logic
├── LICENSE                              # Project License
├── requirements.txt                     # Production Dependencies
└── README.md                            # Documentation
```

-----

## 💻 Local Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/YourUsername/BNMLNC](https://github.com/HasnatHridoy/project-bn-classifier.git
    cd project-bn-classifier
    ```

2.  **Create a Virtual Environment:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the App:**

    ```bash
    python app.py
    ```

-----

## Deployment

This project is configured for **Render**.

  - **Build Command:** `pip install -r requirements.txt`
  - **Start Command:** `gunicorn --timeout 120 app:app`

-----

## Limitation 

The currently deployed model has a limited context window. Our experiment is ongoing for a better model with a larger context size.

-----

## Acknowledgment

  - **Bangladesh Pratidin** for the data source.

-----

<p align='center'> <i>Contributors are warmly welcome to contribute to this project. </i> </p>
