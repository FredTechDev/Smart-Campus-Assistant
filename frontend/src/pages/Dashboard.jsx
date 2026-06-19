import React, { useEffect, useState } from 'react'
import { studentAPI } from '../services/api'
import '../styles/Dashboard.css'

function Dashboard() {
  const [students, setStudents] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    const fetchStudents = async () => {
      try {
        setLoading(true)
        const response = await studentAPI.list()
        setStudents(response.data)
        setError(null)
      } catch (err) {
        setError('Failed to fetch students')
        console.error(err)
      } finally {
        setLoading(false)
      }
    }

    fetchStudents()
  }, [])

  return (
    <div className="dashboard">
      <h1>Dashboard</h1>

      {loading && <p>Loading...</p>}
      {error && <p className="error">{error}</p>}

      <section className="stats-section">
        <h2>Overview</h2>
        <div className="stats-grid">
          <div className="stat-card">
            <h3>Total Students</h3>
            <p className="stat-value">{students.length}</p>
          </div>
          <div className="stat-card">
            <h3>Average GPA</h3>
            <p className="stat-value">3.5</p>
          </div>
          <div className="stat-card">
            <h3>At Risk</h3>
            <p className="stat-value">5</p>
          </div>
        </div>
      </section>

      <section className="students-section">
        <h2>Students</h2>
        {students.length > 0 ? (
          <table className="students-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Email</th>
                <th>Major</th>
                <th>GPA</th>
              </tr>
            </thead>
            <tbody>
              {students.map((student) => (
                <tr key={student.id}>
                  <td>{student.student_id}</td>
                  <td>
                    {student.first_name} {student.last_name}
                  </td>
                  <td>{student.email}</td>
                  <td>{student.major}</td>
                  <td>{student.gpa}</td>
                </tr>
              ))}
            </tbody>
          </table>
        ) : (
          <p>No students found</p>
        )}
      </section>
    </div>
  )
}

export default Dashboard
