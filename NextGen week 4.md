# NextGenLearners Internship Selection Prediction

A machine learning project that explores factors associated with internship selection outcomes using applicant data from the NextGenLearners programme.

## 1. Objective

The objective of this project was to build a basic prediction model to explore whether applicant information and selected application features could help predict internship selection outcomes.

## 2. Dataset Description

The project uses applicant data containing information such as:

- Applicant's name
- Domain applied for
- University
- Application date
- Selection status

Additional features were created for this exercise:

- Number of skills listed
- Whether the applicant has a portfolio
- Previous hackathon participation
- Statement quality score

**Note:** These additional features were simulated for the project and were not collected from actual historical applications. Therefore, the model's findings should be treated as illustrative rather than as evidence of actual selection criteria.

## 3. Method

The project followed these main steps:

1. **Data cleaning:** Prepared the applicant dataset for analysis.
2. **Feature preparation:** Converted relevant information into a format suitable for machine learning and created the target variable for selection outcomes.
3. **Model training:** Used Logistic Regression to identify patterns between applicant features and selection outcomes.
4. **Model evaluation:** Tested the model using a separate test group and assessed its performance using accuracy, precision, recall and a confusion matrix.
5. **Interpretation:** Examined which features were positively or negatively associated with the model's predictions.

## 4. Key Results

The model produced the following results on the test group:

| Evaluation measure | Result |
|---|---:|
| Accuracy | 60% |
| Precision | 50% |
| Recall | 75% |

In simple terms:
- **Accuracy:** The model correctly predicted 6 out of 10 applicants.
- **Precision:** Half of the applicants predicted as Selected were actually selected.
- **Recall:** The model identified 3 out of the 4 applicants who were actually selected.

Previous hackathon participation and the number of skills listed had positive associations with predicted selection. However, the results should be interpreted cautiously because of the small dataset and simulated features.

## 5. How to Run the Notebook

1. Open the notebook in Google Colab.
2. Upload or make the required cleaned dataset available.
3. Run all cells from top to bottom.
4. Review the model evaluation results and final interpretations.

## 6. Recorded Walkthrough

[Insert link to recorded project walkthrough here]
