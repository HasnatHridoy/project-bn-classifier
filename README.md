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

  - **Large Scale Data:** Scraped **47,000+** news articles from *Bangladesh Pratidin*.
  - **Synthetic Labeling:** Leveraged **Gemma 3 27B** to assign and re-evaluate labels across a taxonomy of 45 categories.
  - **Model Benchmarking:** Comparative study between **Bangla BERT**, **Bangla T5**, and **Gemma 270m**.
  - **Production Ready:** Deployed via **Flask** on **Render**, utilizing the **Hugging Face Inference API** for the backend.

-----

## Benchmarking & Performance

We conducted extensive experiments on Kaggle to find the most efficient model for deployment. While Gemma 270m showed promise, **Bangla BERT** provided the most stable and balanced performance for multi-label classification.

| Model | F1-Micro | F1-Macro | Accuracy |
| :--- | :---: | :---: | :---: |
| **Bangla BERT** | 0.814 | 0.631 | 0.361 |
| **Bangla T5** | **0.861** | **0.716** | **0.443** |
| **Gemma 3 270m** | 0.763 | 0.612 | 0.417 |

*Note: - Although Bangla T5 led in metrics, Bangla BERT was selected for the current deployment phase due to its optimized inference speed for the news classifier architecture. -All fine tuned models are available on Hugging Face.*


-----

## The Pipeline

1.  **Scraping:** 47k articles collected from Bangladesh Pratidin via custom Kaggle scripts.
2.  **Preprocessing:** Text cleaning, noise removal, and normalization.
3.  **Synthetic Annotation:** - Defined a set of 45 labels.
      - Used **Gemma 3 27B** to pair news text with correct labels.
      - Implemented a "Re-evaluation" step where the model checked its own labeling logic for consistency.
4.  **Training:** Fine-tuned models on the synthetically labeled dataset using Kaggle's GPU environment.
5.  **Deployment:** Integrated the best-performing weights into a Hugging Face Space, served through a Flask Web UI.

-----

## Project Structure

```text
├── notebooks/
│   ├── 01_link_scraper.ipynb            # Discovering article URLs
│   ├── 02_news_scraping.ipynb           # Extracting full text from links
│   ├── 03_data_cleaning.ipynb           # Preprocessing & noise removal
│   ├── 04_dataset_creation.ipynb        # Finalizing the 47k article pool
│   ├── 05_data_annotation_gemma.ipynb   # Synthetic labeling with Gemma 3 27B
│   ├── 06_bert_model_training.ipynb     # Bangla BERT training (deployed)
│   ├── 07_bangla_t5_training.ipynb      # T5 benchmarking
│   └── 08_gemma_3_training.ipynb        # Gemma 270m benchmarking
├── templates/
│   └── home.html                        # Web UI
├── app.py                               # Flask Backend
├── requirements.txt                     # Dependencies
└── README.md                            # Documentation
```

-----

## 💻 Local Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/YourUsername/BNMLNC.git
    cd BNMLNC
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

## Acknowledgments

  - **Bangladesh Pratidin** for the data source.
  - **Kaggle** for providing the compute resources for training and labeling.
  - **Hugging Face** and **Google (Gemma)** for the model architectures.

-----

*This project is part of an ongoing effort to improve Bangla NLP tools for edge devices.*