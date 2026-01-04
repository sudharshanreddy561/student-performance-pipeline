import joblib

model = joblib.load("student_model.pkl")

# New student data
new_student = [[6, 70]]
predicted_marks = model.predict(new_student)

print("Predicted Marks:", round(predicted_marks[0], 2))
