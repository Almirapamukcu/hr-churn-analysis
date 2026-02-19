"""
IBM HR Analytics Veri Seti Oluşturucu
Bu script, IBM HR Analytics benzeri sentetik bir veri seti oluşturur.
"""

import pandas as pd
import numpy as np

# Tekrarlanabilirlik için seed
np.random.seed(42)

# Çalışan sayısı
n_employees = 1470

# Veri seti oluşturma
data = {
    'EmployeeID': range(1, n_employees + 1),
    'Age': np.random.randint(18, 60, n_employees),
    'Gender': np.random.choice(['Male', 'Female'], n_employees),
    'MaritalStatus': np.random.choice(['Single', 'Married', 'Divorced'], n_employees, p=[0.3, 0.55, 0.15]),
    'Education': np.random.randint(1, 6, n_employees),  # 1: Lise, 2: Ön Lisans, 3: Lisans, 4: Yüksek Lisans, 5: Doktora
    'EducationField': np.random.choice(['Life Sciences', 'Medical', 'Marketing', 'Technical Degree', 'Human Resources', 'Other'], n_employees),
    'Department': np.random.choice(['Sales', 'Research & Development', 'Human Resources'], n_employees, p=[0.3, 0.6, 0.1]),
    'JobRole': np.random.choice([
        'Sales Executive', 'Research Scientist', 'Laboratory Technician', 
        'Manufacturing Director', 'Healthcare Representative', 'Manager',
        'Sales Representative', 'Research Director', 'Human Resources'
    ], n_employees),
    'JobLevel': np.random.randint(1, 6, n_employees),
    'YearsAtCompany': np.random.randint(0, 40, n_employees),
    'YearsInCurrentRole': np.random.randint(0, 18, n_employees),
    'YearsSinceLastPromotion': np.random.randint(0, 15, n_employees),
    'YearsWithCurrManager': np.random.randint(0, 17, n_employees),
    'TotalWorkingYears': np.random.randint(0, 40, n_employees),
    'NumCompaniesWorked': np.random.randint(0, 10, n_employees),
    'TrainingTimesLastYear': np.random.randint(0, 7, n_employees),
    'MonthlyIncome': np.random.randint(1000, 20000, n_employees),
    'PercentSalaryHike': np.random.randint(11, 25, n_employees),
    'StockOptionLevel': np.random.randint(0, 4, n_employees),
    'DistanceFromHome': np.random.randint(1, 30, n_employees),
    'BusinessTravel': np.random.choice(['Non-Travel', 'Travel_Rarely', 'Travel_Frequently'], n_employees, p=[0.15, 0.7, 0.15]),
    'OverTime': np.random.choice(['Yes', 'No'], n_employees, p=[0.3, 0.7]),
    'EnvironmentSatisfaction': np.random.randint(1, 5, n_employees),  # 1-4 scale
    'JobSatisfaction': np.random.randint(1, 5, n_employees),  # 1-4 scale
    'RelationshipSatisfaction': np.random.randint(1, 5, n_employees),  # 1-4 scale
    'WorkLifeBalance': np.random.randint(1, 5, n_employees),  # 1-4 scale
    'JobInvolvement': np.random.randint(1, 5, n_employees),  # 1-4 scale
    'PerformanceRating': np.random.choice([3, 4], n_employees, p=[0.85, 0.15]),  # 3: Meets Expectations, 4: Exceeds
}

df = pd.DataFrame(data)

# Mantıklı ilişkiler oluşturma
# YearsAtCompany, TotalWorkingYears'dan büyük olamaz
df['YearsAtCompany'] = df.apply(lambda x: min(x['YearsAtCompany'], x['TotalWorkingYears']), axis=1)
df['YearsInCurrentRole'] = df.apply(lambda x: min(x['YearsInCurrentRole'], x['YearsAtCompany']), axis=1)
df['YearsWithCurrManager'] = df.apply(lambda x: min(x['YearsWithCurrManager'], x['YearsAtCompany']), axis=1)
df['YearsSinceLastPromotion'] = df.apply(lambda x: min(x['YearsSinceLastPromotion'], x['YearsAtCompany']), axis=1)

# JobLevel'a göre maaş ayarlama
df['MonthlyIncome'] = df['JobLevel'] * 2000 + np.random.randint(1000, 5000, n_employees)

# Attrition (Ayrılma) - Belirli faktörlere dayalı
attrition_prob = (
    (df['JobSatisfaction'] < 3).astype(int) * 0.15 +
    (df['EnvironmentSatisfaction'] < 3).astype(int) * 0.1 +
    (df['WorkLifeBalance'] < 3).astype(int) * 0.1 +
    (df['OverTime'] == 'Yes').astype(int) * 0.15 +
    (df['YearsAtCompany'] < 2).astype(int) * 0.1 +
    (df['MonthlyIncome'] < 5000).astype(int) * 0.1 +
    (df['DistanceFromHome'] > 20).astype(int) * 0.05 +
    (df['YearsSinceLastPromotion'] > 5).astype(int) * 0.1 +
    np.random.uniform(0, 0.15, n_employees)
)

df['Attrition'] = np.where(attrition_prob > 0.35, 'Yes', 'No')

# Veri setini kaydet
df.to_csv('data/hr_employee_attrition.csv', index=False)
print(f"Veri seti oluşturuldu: {len(df)} çalışan")
print(f"Ayrılan çalışan sayısı: {(df['Attrition'] == 'Yes').sum()} ({(df['Attrition'] == 'Yes').mean()*100:.1f}%)")
print(f"\nVeri seti sütunları: {len(df.columns)}")
print(df.head())
