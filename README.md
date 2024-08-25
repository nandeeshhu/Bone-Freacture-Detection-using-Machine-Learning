# Bone Fracture Detection using Machine Learning

## Project Overview
This project aims to develop a machine learning-based system for automated bone fracture detection, utilizing advanced image preprocessing and feature extraction techniques to improve diagnostic accuracy in X-ray imaging.

![Bone Fracture Detection](https://github.com/user-attachments/assets/4b67186c-f0be-468f-bf77-092f1936ca0d)

## Objective
The primary goal is to identify all relevant cases, particularly those involving fractures. In medical imaging, missing a fracture can lead to severe health consequences. Therefore, achieving a high recall rate is crucial to ensure that all potential fractures are detected and examined further.

## Model Evaluation Metrics
To evaluate the performance of the machine learning models, the following metrics were employed:

- **F1 Score:** Balances precision and recall, making it an essential metric in scenarios with uneven class distribution or where both false positives and false negatives carry significant consequences. This score is particularly valuable in medical imaging tasks where the correct identification of fractures and the avoidance of false alarms are critical.
  
- **Accuracy:** A straightforward measure of the proportion of correctly identified instances out of the total cases. Although accuracy is not always the most informative metric in medical imaging, especially with imbalanced classes (fracture vs. no fracture), it remains a useful overall indicator of model performance.

- **AUC-ROC:** The Area Under the Receiver Operating Characteristic curve (AUC-ROC) provides an aggregate measure of model performance across various classification thresholds. It is an excellent metric for assessing a model's ability to distinguish between classes.

## Results and Discussion
Upon completing the testing phase, the results from each model were analyzed and compared to determine the best-performing algorithm. The analysis focused on how well each model balanced the trade-offs between precision and recall, with particular emphasis on ensuring high recall rates to minimize the risk of missed fractures. The models were also evaluated based on their ability to generalize to new data, as evidenced by their performance on the unseen test set.

![Model Comparison](https://github.com/user-attachments/assets/36c102f8-6095-4bc8-8d83-3414469ed491)

The Random Forest model emerged as the most robust and reliable algorithm, achieving the highest F1 Score and AUC-ROC values. Its ensemble nature enabled it to handle the complexity and variability of the X-ray images effectively, making it particularly well-suited for this application. The Support Vector Machine (SVM) also performed well, especially in terms of precision, though it was slightly less effective in maintaining a high recall rate. The Decision Tree and K-Nearest Neighbors (KNN) algorithms showed lower performance, particularly in handling the high-dimensional feature space, while the Logistic Regression and Naïve Bayes models, although useful, did not match the performance of the more sophisticated models like Random Forest.

![Random Forest](https://github.com/user-attachments/assets/56ae477f-0a57-40c5-a810-de731bbb8e88)

## Conclusion
This project successfully demonstrated the potential of machine learning techniques, particularly the Random Forest algorithm, in enhancing the diagnostic accuracy of bone fractures from X-ray images. By addressing the challenges of blurry vision, noisy data, and decision dilemmas inherent in traditional X-ray imaging, the proposed system offers significant improvements in medical diagnostics. The integration of this system into clinical settings through a user-friendly interface ensures that medical professionals can make faster, more informed decisions, ultimately leading to better patient outcomes and reduced healthcare costs.

## Future Work
Looking ahead, several avenues for further research and development are proposed:

- **Deep Learning Models:** Exploration of deep learning techniques, such as convolutional neural networks (CNNs), may offer even greater accuracy and robustness in fracture detection by automatically learning the most relevant features from the data.
  
- **Dataset Expansion:** Expanding the dataset to include a broader range of fracture types and incorporating multi-modal imaging data could further improve the system's generalizability and diagnostic capabilities.
  
- **Clinical Integration:** Ongoing collaboration with medical professionals will be essential to refine the system's usability and ensure its successful integration into real-world clinical workflows.
