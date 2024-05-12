# Automatic Spelling Correction

This project was inspired by a repository found at: [Spelling Correction by oliverguhr](https://github.com/oliverguhr/spelling).

## Usage Guide:

### 1. Dataset Generation:
- Prepare a dataset suitable for your task in a directory named `data` as a TXT file.
- Run two scripts for dataset preparation:
  - `convert_leipzig_data.sh`
  - `generate_dataset.py`

### 2. Fine-Tuning:
- Utilize the fine-tuning script for training your model.
  - Refer to `fine-tuning_script.py`.

### 3. Environment Setup:
- All steps can be executed within a Colab notebook.
  - Refer to `spelling_correction.ipynb`.

### 4. Model Deployment:
- The final models have been uploaded to the Hugging Face Model Hub [here](https://huggingface.co/Elalimy/english_spelling_correction).
- For deployment, consider using the provided Flask application:
  - Refer to `app.py`.

### Testing Deployment:
- Test deployment using the provided link: [Spelling Correction Deployment](https://huggingface.co/spaces/Elalimy/autocorrect_english_spelling_sentence).
