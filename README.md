# Bone-Fracture-Detection-using-Machine-Learning

The project aims to develop a machine learning-based system for automated bone fracture detection using advanced image preprocessing and feature extraction techniques to improve diagnostic accuracy in X-ray imaging.

![image](https://github.com/user-attachments/assets/4b67186c-f0be-468f-bf77-092f1936ca0d)

## Dataset Information

The dataset has been split into training and testing sets to facilitate the development and evaluation of the predictive models. Specifically, 80% of the data, equivalent to approximately 7,570 images, has been designated as the training set. This large training set is crucial for effectively training the machine learning algorithms by allowing them to learn from a wide range of examples, including both fractured and non-fractured X-rays. The remaining 20% of the data, about 1,893 images, constitutes the test set. This separation ensures that the model’s performance is evaluated on new, unseen images, providing an unbiased assessment of its diagnostic accuracy.

This dataset not only supports the model training phase but also ensures that the evaluation phase is rigorous and reflective of real-world scenarios. The balanced nature of the dataset, with nearly equal numbers of fractured and non-fractured images, is particularly beneficial for reducing model bias towards any one class.

**Dataset link:** https://drive.google.com/drive/folders/1bMFk7jmarRsduj_beAgRjawmKP04quv4


## Evaluation Metrics

To identify all relevant cases, particularly those with fractures, the following metrics were used:

- **F1 Score**: The F1 Score provides a balance between precision and recall, making it a vital metric in scenarios where class distribution is uneven or where both false positives and false negatives carry significant consequences. The F1 Score is particularly valuable in medical imaging tasks where both the correct identification of fractures and the avoidance of false alarms are critical.

- **Accuracy**: While accuracy is a straightforward measure of the proportion of correctly identified instances out of the total cases, it is not always the most informative metric in medical imaging, especially when the classes (fracture vs. no fracture) are imbalanced. However, it remains a useful overall indicator of model performance.

- **AUC-ROC**: The Area Under the Receiver Operating Characteristic curve (AUC-ROC) is a performance measurement for classification problems at various threshold settings. It provides an aggregate measure of model performance across all classification thresholds, making it an excellent metric for assessing the ability of a model to distinguish between classes.

## Results and Discussion

Upon completion of the testing phase, the results from each model were analyzed and compared to determine the best-performing algorithm. The analysis focused on how well each model balanced the trade-offs between precision and recall, with a particular emphasis on ensuring high recall rates to minimize the risk of missed fractures. The models were also evaluated based on their ability to generalize to new data, as evidenced by their performance on the unseen test set.

![image](https://github.com/user-attachments/assets/36c102f8-6095-4bc8-8d83-3414469ed491)

The Random Forest model emerged as the most robust and reliable algorithm, achieving the highest F1 Score and AUC-ROC values. Its ensemble nature allowed it to handle the complexity and variability of the X-ray images effectively, making it particularly well-suited for this application. The Support Vector Machine (SVM) also performed well, especially in terms of precision, but was slightly less effective in maintaining a high recall rate. The Decision Tree and K-Nearest Neighbors (KNN) algorithms showed lower performance, particularly in handling the high-dimensional feature space, while the Logistic Regression and Naïve Bayes models, although useful, did not match the performance of the more sophisticated models like Random Forest.

![image](https://github.com/user-attachments/assets/56ae477f-0a57-40c5-a810-de731bbb8e88)

## Conclusion

The project successfully demonstrated the potential of machine learning techniques, particularly the Random Forest algorithm, in enhancing the diagnostic accuracy of bone fractures from X-ray images. By addressing the challenges of blurry vision, noisy data, and decision dilemmas inherent in traditional X-ray imaging, the proposed system offers a significant improvement in the quality of medical diagnostics. The integration of this system into a clinical setting through a user-friendly interface ensures that medical professionals can make faster, more informed decisions, ultimately leading to better patient outcomes and reduced healthcare costs.

## Future Work

Looking ahead, there are several avenues for further research and development. One potential direction is the exploration of deep learning models, such as convolutional neural networks (CNNs), which may offer even greater accuracy and robustness in fracture detection by automatically learning the most relevant features from the data. Additionally, expanding the dataset to include a broader range of fracture types and incorporating multi-modal imaging data could further improve the system's generalizability and diagnostic capabilities. Finally, ongoing collaboration with medical professionals will be essential to refine the system's usability and ensure its successful integration into real-world clinical workflows.
