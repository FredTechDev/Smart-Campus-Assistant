"""Generate sample student data for testing and development"""

import random
from datetime import datetime, timedelta
from typing import List

import numpy as np
import pandas as pd

from ml.src.utils import log_info


class SampleDataGenerator:
    """Generate realistic sample data for the Smart Campus Assistant"""

    MAJORS = [
        "Computer Science",
        "Engineering",
        "Business",
        "Biology",
        "Chemistry",
        "Physics",
        "Mathematics",
        "Psychology",
        "Economics",
        "History",
    ]

    COURSES = [
        ("CS101", "Introduction to Programming", 3),
        ("CS201", "Data Structures", 4),
        ("CS301", "Algorithms", 4),
        ("MATH101", "Calculus I", 4),
        ("MATH201", "Linear Algebra", 3),
        ("ENG101", "Technical Writing", 3),
        ("BUS101", "Business Fundamentals", 3),
        ("PHY101", "Physics I", 4),
        ("CHEM101", "Chemistry I", 4),
        ("BIO101", "Biology I", 4),
    ]

    @staticmethod
    def generate_students(num_students: int = 100, seed: int = 42) -> pd.DataFrame:
        """
        Generate sample student data
        
        Args:
            num_students: Number of students to generate
            seed: Random seed
            
        Returns:
            DataFrame with student data
        """
        random.seed(seed)
        np.random.seed(seed)

        students = []
        for i in range(num_students):
            student = {
                "student_id": f"STU{100000 + i}",
                "first_name": f"Student{i}",
                "last_name": f"Last{i}",
                "email": f"student{i}@university.edu",
                "major": random.choice(SampleDataGenerator.MAJORS),
                "year": random.randint(1, 4),
                "gpa": round(random.uniform(1.5, 4.0), 2),
                "enrollment_date": (datetime.now() - timedelta(days=random.randint(365, 1460))).strftime(
                    "%Y-%m-%d"
                ),
            }
            students.append(student)

        df = pd.DataFrame(students)
        log_info(f"Generated {len(df)} sample students")
        return df

    @staticmethod
    def generate_attendance(num_records: int = 500, seed: int = 42) -> pd.DataFrame:
        """
        Generate sample attendance data
        
        Args:
            num_records: Number of attendance records
            seed: Random seed
            
        Returns:
            DataFrame with attendance records
        """
        random.seed(seed)
        np.random.seed(seed)

        attendance_records = []
        for _ in range(num_records):
            record = {
                "student_id": f"STU{random.randint(100000, 100099)}",
                "course_id": random.choice([c[0] for c in SampleDataGenerator.COURSES]),
                "date": (datetime.now() - timedelta(days=random.randint(1, 180))).strftime("%Y-%m-%d"),
                "present": random.choices([True, False], weights=[0.8, 0.2])[0],
            }
            attendance_records.append(record)

        df = pd.DataFrame(attendance_records)
        log_info(f"Generated {len(df)} sample attendance records")
        return df

    @staticmethod
    def generate_grades(num_students: int = 100, seed: int = 42) -> pd.DataFrame:
        """
        Generate sample grade data
        
        Args:
            num_students: Number of students
            seed: Random seed
            
        Returns:
            DataFrame with grade records
        """
        random.seed(seed)
        np.random.seed(seed)

        grades = []
        courses = [c[0] for c in SampleDataGenerator.COURSES]
        
        for i in range(num_students):
            num_courses = random.randint(3, 6)
            selected_courses = random.sample(courses, min(num_courses, len(courses)))
            
            for course in selected_courses:
                grade = {
                    "student_id": f"STU{100000 + i}",
                    "course_id": course,
                    "semester": random.choice(["Fall 2023", "Spring 2024", "Summer 2024"]),
                    "grade": random.choice(["A", "B", "C", "D", "F"]),
                    "score": round(random.uniform(0, 100), 1),
                }
                grades.append(grade)

        df = pd.DataFrame(grades)
        log_info(f"Generated {len(df)} sample grade records")
        return df

    @staticmethod
    def generate_course_performance_features(df_students: pd.DataFrame) -> pd.DataFrame:
        """
        Generate performance-related features
        
        Args:
            df_students: Student DataFrame
            
        Returns:
            DataFrame with performance features
        """
        random.seed(42)
        np.random.seed(42)

        features = []
        for _, student in df_students.iterrows():
            gpa = student["gpa"]
            year = student["year"]
            
            feature = {
                "student_id": student["student_id"],
                "gpa": gpa,
                "study_hours_per_week": round(random.uniform(5, 40), 1),
                "homework_completion_rate": round(random.uniform(0.5, 1.0), 2),
                "class_participation": random.randint(1, 10),
                "exam_average": round(random.uniform(50 + gpa * 10, 90 + gpa * 5), 1),
                "assignment_average": round(random.uniform(60 + gpa * 8, 95), 1),
                "year": year,
                "major": student["major"],
            }
            features.append(feature)

        df = pd.DataFrame(features)
        log_info(f"Generated performance features for {len(df)} students")
        return df

    @staticmethod
    def generate_complete_dataset(
        num_students: int = 100,
        output_dir: str = "ml/data/raw",
        seed: int = 42,
    ) -> None:
        """
        Generate complete dataset with multiple tables
        
        Args:
            num_students: Number of students
            output_dir: Output directory for CSV files
            seed: Random seed
        """
        from ml.src.data_loader import DataLoader

        # Generate all datasets
        students = SampleDataGenerator.generate_students(num_students, seed)
        attendance = SampleDataGenerator.generate_attendance(num_students * 5, seed)
        grades = SampleDataGenerator.generate_grades(num_students, seed)
        performance = SampleDataGenerator.generate_course_performance_features(students)

        # Save to CSV
        DataLoader.save_csv(students, f"{output_dir}/students.csv")
        DataLoader.save_csv(attendance, f"{output_dir}/attendance.csv")
        DataLoader.save_csv(grades, f"{output_dir}/grades.csv")
        DataLoader.save_csv(performance, f"{output_dir}/performance_features.csv")

        log_info(f"Generated complete dataset with {num_students} students")
